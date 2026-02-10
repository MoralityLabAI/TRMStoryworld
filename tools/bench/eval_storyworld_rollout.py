#!/usr/bin/env python3
"""Run deterministic rollouts on SWMD/SWMD-min with base and adapter controllers."""

from __future__ import annotations

import argparse
import gc
import json
import math
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from identity_utils import git_commit, make_run_identity, sha256_hex as h_hex
from model_utils import controller_from_args, memory_snapshot, parse_pick
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
    include_prompt_in_trace: bool = False,
    include_steps_in_episode: bool = False,
    emit_step: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    cur = start_id
    leaves: List[str] = []
    labels: List[str] = []
    episode_steps: List[Dict[str, Any]] = []
    final_node = start_id
    step_count = 0
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
        label = f"PICK {pick}"
        labels.append(label)
        step_row: Dict[str, Any] = {
            "episode": episode_idx,
            "turn": turn,
            "mode": mode,
            "encounter_id": enc.enc_id,
            "label": label,
            "state_hash": state_hash,
            "receipt_leaf": leaf,
            "next_encounter": next_id,
        }
        if include_prompt_in_trace:
            step_row["prompt"] = prompt
        if emit_step is not None:
            emit_step(step_row)
        if include_steps_in_episode:
            episode_steps.append(step_row)
        step_count += 1
        final_node = next_id or final_node
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
                "labels": labels,
                "final_node": final_node,
            }
        )
    )
    return {
        "episode": episode_idx,
        "mode": mode,
        "trace_root": trace_root,
        "output_commitment": output_commitment,
        "steps": episode_steps if include_steps_in_episode else [],
        "step_count": step_count,
        "final_node": final_node,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--swmd", type=str, required=True)
    parser.add_argument("--episodes", type=int, default=8)
    parser.add_argument("--max-steps", type=int, default=8)
    parser.add_argument("--base-model", type=str, default="")
    parser.add_argument("--adapter-path", type=str, default="")
    parser.add_argument("--device", type=str, default="cpu")
    parser.add_argument("--dtype", type=str, default="auto", choices=["auto", "float16", "bfloat16", "float32"])
    parser.add_argument("--require-gpu", action="store_true", help="Fail if CUDA is unavailable or model is not on GPU.")
    parser.add_argument("--allow-large-model", action="store_true", help="Allow models above the size cap.")
    parser.add_argument("--max-model-params-millions", type=float, default=200.0, help="Reject larger models unless --allow-large-model.")
    parser.add_argument("--out-dir", type=str, default="tools/bench/out")
    parser.add_argument("--dataset-hash", type=str, default="")
    parser.add_argument("--rows-merkle-root", type=str, default="")
    parser.add_argument("--builder-git-commit", type=str, default="")
    parser.add_argument(
        "--run-modes",
        type=str,
        default="both",
        choices=["both", "adapter-only", "base-only"],
        help="Select which controllers to evaluate. adapter-only avoids loading a second model.",
    )
    parser.add_argument(
        "--heartbeat-seconds",
        type=int,
        default=30,
        help="Emit periodic progress lines with episode index and RSS memory.",
    )
    parser.add_argument(
        "--include-prompt-in-trace",
        action="store_true",
        help="Store full prompt text in trace rows (disabled by default to reduce memory/disk pressure).",
    )
    parser.add_argument(
        "--include-steps-in-episodes",
        action="store_true",
        help="Store per-step arrays inside episode rows (disabled by default to avoid duplicate payloads).",
    )
    parser.add_argument("--emit-fft", action="store_true", help="Emit FFT summary JSON from rollout signals.")
    parser.add_argument("--fft-top-k", type=int, default=5, help="Top FFT peaks to retain.")
    parser.add_argument("--fft-max-points", type=int, default=256, help="Max point count for FFT padding/truncation.")
    return parser.parse_args()


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path: Path, obj: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def pick_series_from_steps(steps: List[Dict[str, Any]]) -> List[float]:
    out: List[float] = []
    for row in steps:
        label = str(row.get("label", ""))
        pick = parse_pick(label)
        if pick is not None:
            out.append(float(pick))
    return out


def _rfft_magnitude(series: List[float], fft_n: int) -> List[float]:
    try:
        import numpy as np

        arr = np.asarray(series, dtype=float)
        if arr.size < fft_n:
            arr = np.pad(arr, (0, fft_n - arr.size), mode="constant")
        else:
            arr = arr[:fft_n]
        arr = arr - float(arr.mean())
        mags = np.abs(np.fft.rfft(arr))
        return [float(x) for x in mags.tolist()]
    except Exception:
        vals = list(series[:fft_n]) + [0.0] * max(0, fft_n - len(series))
        mean = sum(vals) / float(len(vals) or 1)
        vals = [v - mean for v in vals]
        out: List[float] = []
        half = fft_n // 2
        for k in range(half + 1):
            re = 0.0
            im = 0.0
            for n, x in enumerate(vals):
                ang = 2.0 * math.pi * float(k) * float(n) / float(fft_n)
                re += x * math.cos(ang)
                im -= x * math.sin(ang)
            out.append(math.sqrt(re * re + im * im))
        return out


def compute_fft_report(
    series_by_episode: Dict[int, List[float]],
    top_k: int = 5,
    max_points: int = 256,
) -> Dict[str, Any]:
    episodes = sorted(series_by_episode.keys())
    aggregate: List[float] = []
    per_episode: List[Dict[str, Any]] = []
    for ep in episodes:
        series = series_by_episode.get(ep, [])
        aggregate.extend(series)
        per_episode.append(
            {
                "episode": ep,
                "length": len(series),
                "mean": (sum(series) / len(series) if series else 0.0),
            }
        )

    n = len(aggregate)
    if n == 0:
        return {
            "signal": "pick_index",
            "episodes": len(episodes),
            "aggregate_length": 0,
            "fft_n": 0,
            "top_peaks": [],
            "per_episode": per_episode,
        }

    fft_n = 1 << (n - 1).bit_length()
    fft_n = min(max_points, max(2, fft_n))
    mags = _rfft_magnitude(aggregate, fft_n=fft_n)
    peaks: List[Dict[str, Any]] = []
    for i, mag in enumerate(mags):
        if i == 0:
            continue
        peaks.append({"bin": i, "freq": float(i) / float(fft_n), "magnitude": float(mag)})
    peaks.sort(key=lambda x: (-x["magnitude"], x["bin"]))
    return {
        "signal": "pick_index",
        "episodes": len(episodes),
        "aggregate_length": n,
        "fft_n": fft_n,
        "top_peaks": peaks[: max(1, top_k)],
        "per_episode": per_episode,
    }


def summarize(episodes: List[Dict[str, Any]]) -> Dict[str, Any]:
    outcomes: Dict[str, int] = {}
    total_steps = 0
    for ep in episodes:
        total_steps += int(ep.get("step_count", len(ep.get("steps", []))))
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

    need_base = args.run_modes in ("both", "base-only")
    need_adapter = args.run_modes in ("both", "adapter-only")

    if need_adapter and not args.base_model:
        raise ValueError("--base-model is required when run mode includes adapter")
    if need_adapter and not args.adapter_path:
        raise ValueError("--adapter-path is required in adapter-only/both modes")

    base_trace_path = out_dir / "rollout_base_traces.jsonl"
    adapter_trace_path = out_dir / "rollout_adapter_traces.jsonl"
    base_ep_path = out_dir / "rollout_base_episodes.jsonl"
    adapter_ep_path = out_dir / "rollout_adapter_episodes.jsonl"
    if need_base:
        write_jsonl(base_trace_path, [])
        write_jsonl(base_ep_path, [])
    if need_adapter:
        write_jsonl(adapter_trace_path, [])
        write_jsonl(adapter_ep_path, [])

    base_eps: List[Dict[str, Any]] = []
    adapter_eps: List[Dict[str, Any]] = []
    base_pick_series: Dict[int, List[float]] = {}
    adapter_pick_series: Dict[int, List[float]] = {}
    base_trace_rows = 0
    adapter_trace_rows = 0
    last_hb = 0.0
    def maybe_heartbeat(mode: str, episode_idx: int) -> None:
        nonlocal last_hb
        now = time.time()
        if args.heartbeat_seconds <= 0 or (now - last_hb) < args.heartbeat_seconds:
            return
        mem = memory_snapshot()
        print(
            "[heartbeat] "
            f"mode={mode} "
            f"episode={episode_idx + 1}/{args.episodes} "
            f"rss_mb={mem['rss_mb']:.1f} "
            f"cuda_allocated_mb={mem['cuda_allocated_mb']:.1f} "
            f"cuda_reserved_mb={mem['cuda_reserved_mb']:.1f} "
            f"base_trace_rows={base_trace_rows} "
            f"adapter_trace_rows={adapter_trace_rows}"
        )
        last_hb = now

    if need_base:
        base_controller = controller_from_args(
            model_path=(args.base_model or None),
            adapter_path=None,
            device=args.device,
            dtype=args.dtype,
            require_gpu=args.require_gpu,
            allow_large_model=args.allow_large_model,
            max_model_params_millions=args.max_model_params_millions,
        )
        for i in range(args.episodes):
            b_steps: List[Dict[str, Any]] = []
            b = run_episode(
                "base",
                encounters,
                start_id,
                base_controller,
                i,
                args.max_steps,
                include_prompt_in_trace=args.include_prompt_in_trace,
                include_steps_in_episode=args.include_steps_in_episodes,
                emit_step=b_steps.append,
            )
            step_count = int(b["step_count"])
            append_jsonl(base_trace_path, b_steps)
            append_jsonl(base_ep_path, [b])
            base_trace_rows += step_count
            if args.emit_fft:
                base_pick_series[i] = pick_series_from_steps(b_steps)
            base_eps.append(b)
            maybe_heartbeat("base", i)
        del base_controller
        gc.collect()
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except Exception:
            pass

    if need_adapter:
        adapter_controller = controller_from_args(
            model_path=(args.base_model or None),
            adapter_path=(args.adapter_path or None),
            device=args.device,
            dtype=args.dtype,
            require_gpu=args.require_gpu,
            allow_large_model=args.allow_large_model,
            max_model_params_millions=args.max_model_params_millions,
        )
        for i in range(args.episodes):
            a_steps: List[Dict[str, Any]] = []
            a = run_episode(
                "adapter",
                encounters,
                start_id,
                adapter_controller,
                i,
                args.max_steps,
                include_prompt_in_trace=args.include_prompt_in_trace,
                include_steps_in_episode=args.include_steps_in_episodes,
                emit_step=a_steps.append,
            )
            step_count = int(a["step_count"])
            append_jsonl(adapter_trace_path, a_steps)
            append_jsonl(adapter_ep_path, [a])
            adapter_trace_rows += step_count
            if args.emit_fft:
                adapter_pick_series[i] = pick_series_from_steps(a_steps)
            adapter_eps.append(a)
            maybe_heartbeat("adapter", i)
        del adapter_controller
        gc.collect()
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except Exception:
            pass

    base_fft_path = out_dir / "rollout_base_fft.json"
    adapter_fft_path = out_dir / "rollout_adapter_fft.json"
    if args.emit_fft and need_base:
        write_json(
            base_fft_path,
            compute_fft_report(
                base_pick_series,
                top_k=max(1, int(args.fft_top_k)),
                max_points=max(2, int(args.fft_max_points)),
            ),
        )
    if args.emit_fft and need_adapter:
        write_json(
            adapter_fft_path,
            compute_fft_report(
                adapter_pick_series,
                top_k=max(1, int(args.fft_top_k)),
                max_points=max(2, int(args.fft_max_points)),
            ),
        )

    summary = {
        "mission": "swmd-rollout-eval",
        "target": args.swmd,
        "swmd_hash": world.hash_sha256,
        "result": "ok",
        "base": summarize(base_eps) if need_base else None,
        "adapter": summarize(adapter_eps) if need_adapter else None,
        "run_modes": args.run_modes,
        "runtime": {
            **memory_snapshot(),
            "base_trace_rows": base_trace_rows,
            "adapter_trace_rows": adapter_trace_rows,
            "episodes": args.episodes,
            "max_steps": args.max_steps,
            "include_prompt_in_trace": bool(args.include_prompt_in_trace),
            "include_steps_in_episodes": bool(args.include_steps_in_episodes),
            "require_gpu": bool(args.require_gpu),
            "allow_large_model": bool(args.allow_large_model),
            "max_model_params_millions": float(args.max_model_params_millions),
            "emit_fft": bool(args.emit_fft),
            "fft_top_k": int(args.fft_top_k),
            "fft_max_points": int(args.fft_max_points),
        },
        "evidence_paths": {
            "base_trace": str(base_trace_path) if need_base else "",
            "adapter_trace": str(adapter_trace_path) if need_adapter else "",
            "base_episodes": str(base_ep_path) if need_base else "",
            "adapter_episodes": str(adapter_ep_path) if need_adapter else "",
            "base_fft": str(base_fft_path) if (need_base and args.emit_fft) else "",
            "adapter_fft": str(adapter_fft_path) if (need_adapter and args.emit_fft) else "",
        },
    }
    repo_root = Path(__file__).resolve().parents[2]
    summary["run_identity"] = make_run_identity(
        swmd_hash=world.hash_sha256,
        dataset_hash=args.dataset_hash,
        rows_merkle_root=args.rows_merkle_root,
        builder_git_commit=args.builder_git_commit,
        trainer_git_commit=git_commit(repo_root),
        base_model_id=args.base_model or "heuristic",
        adapter_config={
            "adapter_path": args.adapter_path or "",
            "dtype": args.dtype,
            "device": args.device,
            "episodes": args.episodes,
            "max_steps": args.max_steps,
            "require_gpu": bool(args.require_gpu),
            "allow_large_model": bool(args.allow_large_model),
            "max_model_params_millions": float(args.max_model_params_millions),
            "emit_fft": bool(args.emit_fft),
            "fft_top_k": int(args.fft_top_k),
            "fft_max_points": int(args.fft_max_points),
        },
    )
    summary["run_identity_hash"] = h_hex(stable_json(summary["run_identity"]))
    summary_path = out_dir / "rollout_eval_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
