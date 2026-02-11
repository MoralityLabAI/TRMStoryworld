#!/usr/bin/env python3
"""Export rollout traces into a QuantumBlot-ready corpus JSONL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from identity_utils import sha256_hex


def iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = line.strip()
            if not row:
                continue
            try:
                obj = json.loads(row)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                yield obj


def read_json(path: Path) -> Dict[str, Any]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return obj if isinstance(obj, dict) else {}


def _as_int(value: Any, default: int = 0) -> int:
    return int(value) if isinstance(value, int) else default


def _as_str(value: Any, default: str = "") -> str:
    return value if isinstance(value, str) else default


def _episode_map(path: Path) -> Dict[Tuple[str, int], Dict[str, Any]]:
    out: Dict[Tuple[str, int], Dict[str, Any]] = {}
    if not path.exists():
        return out
    for row in iter_jsonl(path):
        mode = _as_str(row.get("mode"), "")
        ep = _as_int(row.get("episode"), -1)
        if mode and ep >= 0:
            out[(mode, ep)] = row
    return out


def _world_id(summary: Dict[str, Any], summary_path: Path) -> str:
    target = _as_str(summary.get("target"), "")
    if target:
        return Path(target).stem
    return summary_path.parent.name


def _text_from_step(world_id: str, run_mode: str, step: Dict[str, Any]) -> str:
    episode = _as_int(step.get("episode"), 0)
    turn = _as_int(step.get("turn"), 0)
    encounter = _as_str(step.get("encounter_id"), "unknown")
    label = _as_str(step.get("label"), "PICK 0")
    nxt = _as_str(step.get("next_encounter"), "END")
    prompt = _as_str(step.get("prompt"), "")
    base = (
        f"world={world_id} mode={run_mode} episode={episode} turn={turn} "
        f"encounter={encounter} action={label} next={nxt}"
    )
    if prompt:
        # Keep optional prompt context compact for embedding pipelines.
        compact = " ".join(prompt.split())
        if len(compact) > 600:
            compact = compact[:600]
        return f"{base} prompt={compact}"
    return base


def _row_from_step(
    summary: Dict[str, Any],
    summary_path: Path,
    run_mode: str,
    step: Dict[str, Any],
    ep_row: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    world_id = _world_id(summary, summary_path)
    episode = _as_int(step.get("episode"), 0)
    turn = _as_int(step.get("turn"), 0)
    encounter = _as_str(step.get("encounter_id"), "unknown")
    label = _as_str(step.get("label"), "PICK 0")
    rid = sha256_hex(
        json.dumps(
            {
                "summary_path": str(summary_path),
                "mode": run_mode,
                "episode": episode,
                "turn": turn,
                "encounter_id": encounter,
                "label": label,
                "receipt_leaf": _as_str(step.get("receipt_leaf"), ""),
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        )
    )
    row = {
        "id": rid,
        "text": _text_from_step(world_id, run_mode, step),
        "meta": {
            "world_id": world_id,
            "target": _as_str(summary.get("target"), ""),
            "swmd_hash": _as_str(summary.get("swmd_hash"), ""),
            "summary_path": str(summary_path),
            "run_modes": _as_str(summary.get("run_modes"), ""),
            "mode": run_mode,
            "episode": episode,
            "turn": turn,
            "encounter_id": encounter,
            "label": label,
            "next_encounter": _as_str(step.get("next_encounter"), ""),
            "state_hash": _as_str(step.get("state_hash"), ""),
            "receipt_leaf": _as_str(step.get("receipt_leaf"), ""),
            "trace_root": _as_str((ep_row or {}).get("trace_root"), ""),
            "output_commitment": _as_str((ep_row or {}).get("output_commitment"), ""),
            "final_node": _as_str((ep_row or {}).get("final_node"), ""),
        },
    }
    return row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rollout-root", type=str, default="tools/bench/out")
    parser.add_argument("--summary-glob", type=str, default="**/rollout_eval_summary.json")
    parser.add_argument("--out-jsonl", type=str, default="tools/bench/out/qblot/trm_rollout_corpus.jsonl")
    parser.add_argument("--out-manifest", type=str, default="tools/bench/out/qblot/trm_rollout_corpus_manifest.json")
    parser.add_argument("--max-summaries", type=int, default=0, help="Optional cap for quick export (0=all).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.rollout_root)
    out_jsonl = Path(args.out_jsonl)
    out_manifest = Path(args.out_manifest)
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    out_manifest.parent.mkdir(parents=True, exist_ok=True)

    summaries = sorted(root.glob(args.summary_glob))
    if args.max_summaries > 0:
        summaries = summaries[: args.max_summaries]

    rows_written = 0
    summary_count = 0
    mode_counts: Dict[str, int] = {}
    trace_counts: Dict[str, int] = {}

    with out_jsonl.open("w", encoding="utf-8") as out:
        for summary_path in summaries:
            summary = read_json(summary_path)
            if not summary:
                continue
            evidence = summary.get("evidence_paths") or {}
            if not isinstance(evidence, dict):
                evidence = {}
            summary_count += 1

            pairs: List[Tuple[str, Path, Path]] = []
            base_trace = _as_str(evidence.get("base_trace"), "")
            base_eps = _as_str(evidence.get("base_episodes"), "")
            adapter_trace = _as_str(evidence.get("adapter_trace"), "")
            adapter_eps = _as_str(evidence.get("adapter_episodes"), "")
            if base_trace:
                pairs.append(("base", Path(base_trace), Path(base_eps) if base_eps else Path("")))
            if adapter_trace:
                pairs.append(("adapter", Path(adapter_trace), Path(adapter_eps) if adapter_eps else Path("")))

            for run_mode, trace_path, eps_path in pairs:
                if not trace_path.exists():
                    continue
                ep_map = _episode_map(eps_path) if eps_path and str(eps_path) else {}
                local_count = 0
                for step in iter_jsonl(trace_path):
                    episode = _as_int(step.get("episode"), -1)
                    ep_row = ep_map.get((run_mode, episode))
                    row = _row_from_step(summary, summary_path, run_mode, step, ep_row)
                    out.write(json.dumps(row, ensure_ascii=False) + "\n")
                    rows_written += 1
                    local_count += 1
                mode_counts[run_mode] = mode_counts.get(run_mode, 0) + local_count
                trace_counts[str(trace_path)] = local_count

    manifest = {
        "rollout_root": str(root),
        "summary_glob": args.summary_glob,
        "summaries_scanned": summary_count,
        "rows_written": rows_written,
        "mode_counts": mode_counts,
        "trace_counts": trace_counts,
        "out_jsonl": str(out_jsonl),
        "out_manifest": str(out_manifest),
    }
    out_manifest.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
