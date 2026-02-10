#!/usr/bin/env python3
"""Run deterministic rollouts on SWMD/SWMD-min with base and adapter controllers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from model_utils import controller_from_args, parse_pick
from swmd_utils import SwmdEncounter, SwmdOption, merkle_root_hex, parse_swmd, sha256_hex, stable_json


def mk_leaf(mode: str, episode: int, turn: int, state_hash: str, pick: int, out_hash: str) -> str:
    payload = f"SWMDR|{mode}|{episode}|{turn}|{state_hash}|{pick}|{out_hash}"
    return sha256_hex(payload)


def choose_reaction(option: SwmdOption) -> Optional[str]:
    if not option.reactions:
        return None
    rxn = sorted(option.reactions, key=lambda r: r.rxn_id)[0]
    return rxn.consequence


def build_prompt(enc: SwmdEncounter) -> str:
    lines = ["<SWMD-CTRL>", f"E {enc.enc_id} turn={enc.turn_span}", f"T {enc.title}"]
    options = sorted(enc.options, key=lambda o: o.opt_id)
    for i, opt in enumerate(options):
        nexts = sorted({r.consequence for r in opt.reactions if r.consequence})
        lines.append(f"C{i} {opt.opt_id} -> {','.join(nexts) if nexts else 'none'} | O:{opt.text}")
    lines.append("</SWMD-CTRL>")
    return "\n".join(lines)


def run_episode(
    mode: str,
    encounters: Dict[str, SwmdEncounter],
    start_id: str,
    controller,
    episode_idx: int,
    max_steps: int,
) -> Dict[str, Any]:
    cur = start_id
    leaves: List[str] = []
    steps: List[Dict[str, Any]] = []
    for turn in range(max_steps):
        enc = encounters.get(cur)
        if enc is None:
            break
        if not enc.options:
            break
        opts = sorted(enc.options, key=lambda o: o.opt_id)
        prompt = build_prompt(enc)
        state_hash = sha256_hex(stable_json({"encounter": enc.enc_id, "turn": turn}))
        pred = controller.predict(prompt, max_new_tokens=8)
        pick = parse_pick(pred.text)
        if pick is None or pick < 0 or pick >= len(opts):
            pick = 0
        selected = opts[pick]
        next_id = choose_reaction(selected)
        out_hash = sha256_hex(stable_json({"next": next_id or "END"}))
        leaf = mk_leaf(mode, episode_idx, turn, state_hash, pick, out_hash)
        leaves.append(leaf)
        steps.append(
            {
                "episode": episode_idx,
                "turn": turn,
                "mode": mode,
                "encounter_id": enc.enc_id,
                "prompt": prompt,
                "label": f"PICK {pick}",
                "state_hash": state_hash,
                "receipt_leaf": leaf,
                "next_encounter": next_id,
            }
        )
        if not next_id:
            break
        cur = next_id
    trace_root = merkle_root_hex(leaves)
    output_commitment = sha256_hex(
        stable_json(
            {
                "episode": episode_idx,
                "mode": mode,
                "trace_root": trace_root,
                "labels": [s["label"] for s in steps],
                "final_node": (steps[-1]["next_encounter"] if steps else start_id),
            }
        )
    )
    return {
        "episode": episode_idx,
        "mode": mode,
        "trace_root": trace_root,
        "output_commitment": output_commitment,
        "steps": steps,
        "final_node": (steps[-1]["next_encounter"] if steps else start_id),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--swmd", type=str, required=True)
    parser.add_argument("--episodes", type=int, default=8)
    parser.add_argument("--max-steps", type=int, default=8)
    parser.add_argument("--base-model", type=str, default="")
    parser.add_argument("--adapter-path", type=str, default="")
    parser.add_argument("--device", type=str, default="auto")
    parser.add_argument("--dtype", type=str, default="auto", choices=["auto", "float16", "bfloat16", "float32"])
    parser.add_argument("--out-dir", type=str, default="tools/bench/out")
    return parser.parse_args()


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def summarize(episodes: List[Dict[str, Any]]) -> Dict[str, Any]:
    outcomes: Dict[str, int] = {}
    total_steps = 0
    for ep in episodes:
        total_steps += len(ep.get("steps", []))
        final_node = ep.get("final_node") or "none"
        outcomes[final_node] = outcomes.get(final_node, 0) + 1
    return {
        "episodes": len(episodes),
        "steps": total_steps,
        "outcomes": outcomes,
    }


def main() -> int:
    args = parse_args()
    world = parse_swmd(Path(args.swmd))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    encounters = {e.enc_id: e for e in world.encounters}
    if not encounters:
        raise ValueError("no encounters found in SWMD")
    start_id = sorted(world.encounters, key=lambda e: (e.turn_span, e.enc_id))[0].enc_id

    base_controller = controller_from_args(
        model_path=(args.base_model or None),
        adapter_path=None,
        device=args.device,
        dtype=args.dtype,
    )
    adapter_controller = controller_from_args(
        model_path=(args.base_model or None),
        adapter_path=(args.adapter_path or None),
        device=args.device,
        dtype=args.dtype,
    )

    base_eps: List[Dict[str, Any]] = []
    adapter_eps: List[Dict[str, Any]] = []
    base_steps: List[Dict[str, Any]] = []
    adapter_steps: List[Dict[str, Any]] = []
    for i in range(args.episodes):
        b = run_episode("base", encounters, start_id, base_controller, i, args.max_steps)
        a = run_episode("adapter", encounters, start_id, adapter_controller, i, args.max_steps)
        base_eps.append(b)
        adapter_eps.append(a)
        base_steps.extend(b["steps"])
        adapter_steps.extend(a["steps"])

    base_trace_path = out_dir / "rollout_base_traces.jsonl"
    adapter_trace_path = out_dir / "rollout_adapter_traces.jsonl"
    base_ep_path = out_dir / "rollout_base_episodes.jsonl"
    adapter_ep_path = out_dir / "rollout_adapter_episodes.jsonl"
    write_jsonl(base_trace_path, base_steps)
    write_jsonl(adapter_trace_path, adapter_steps)
    write_jsonl(base_ep_path, base_eps)
    write_jsonl(adapter_ep_path, adapter_eps)

    summary = {
        "mission": "swmd-rollout-eval",
        "target": args.swmd,
        "swmd_hash": world.hash_sha256,
        "result": "ok",
        "base": summarize(base_eps),
        "adapter": summarize(adapter_eps),
        "evidence_paths": {
            "base_trace": str(base_trace_path),
            "adapter_trace": str(adapter_trace_path),
            "base_episodes": str(base_ep_path),
            "adapter_episodes": str(adapter_ep_path),
        },
    }
    summary_path = out_dir / "rollout_eval_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
