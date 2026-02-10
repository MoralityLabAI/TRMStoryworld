#!/usr/bin/env python3
"""Batch rollout evaluator for multiple SWMD-min files with a single controller load."""

from __future__ import annotations

import argparse
import gc
import json
import time
from pathlib import Path
from typing import Any, Dict, List

from eval_storyworld_rollout import append_jsonl, run_episode, summarize, write_jsonl
from identity_utils import git_commit, make_run_identity, sha256_hex as h_hex
from model_utils import controller_from_args, memory_snapshot
from swmd_utils import parse_swmd, stable_json


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--swmd-root", type=str, required=True)
    p.add_argument("--glob", type=str, default="*.swmd.min.md")
    p.add_argument("--episodes", type=int, default=1)
    p.add_argument("--max-steps", type=int, default=8)
    p.add_argument("--base-model", type=str, default="")
    p.add_argument("--adapter-path", type=str, default="")
    p.add_argument("--device", type=str, default="cpu")
    p.add_argument("--dtype", type=str, default="auto", choices=["auto", "float16", "bfloat16", "float32"])
    p.add_argument("--out-dir", type=str, default="tools/bench/out/rollout_batch")
    p.add_argument("--run-modes", type=str, default="adapter-only", choices=["both", "adapter-only", "base-only"])
    p.add_argument("--heartbeat-seconds", type=int, default=30)
    p.add_argument("--max-rss-mb", type=int, default=0, help="Abort cleanly if RSS exceeds this threshold (0=disabled).")
    p.add_argument(
        "--include-prompt-in-trace",
        action="store_true",
        help="Store full prompt text in trace rows (disabled by default to reduce memory/disk pressure).",
    )
    p.add_argument(
        "--include-steps-in-episodes",
        action="store_true",
        help="Store per-step arrays inside episode rows (disabled by default to avoid duplicate payloads).",
    )
    return p.parse_args()


def _rss_mb() -> float:
    return float(memory_snapshot().get("rss_mb", -1.0))


def main() -> int:
    args = parse_args()
    swmd_root = Path(args.swmd_root)
    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    files = sorted(swmd_root.rglob(args.glob))
    if not files:
        raise ValueError(f"no files found under {swmd_root} matching {args.glob}")

    need_base = args.run_modes in ("both", "base-only")
    need_adapter = args.run_modes in ("both", "adapter-only")
    if need_adapter and not args.base_model:
        raise ValueError("--base-model required in adapter mode")
    if need_adapter and not args.adapter_path:
        raise ValueError("--adapter-path required in adapter mode")

    batch_rows: List[Dict[str, Any]] = []
    for idx, swmd in enumerate(files):
        world = parse_swmd(swmd)
        encounters = {e.enc_id: e for e in world.encounters}
        if not encounters:
            continue
        start_id = sorted(world.encounters, key=lambda e: (e.turn_span, e.enc_id))[0].enc_id

        world_id = swmd.stem
        out_dir = out_root / world_id
        out_dir.mkdir(parents=True, exist_ok=True)

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
        base_trace_rows = 0
        adapter_trace_rows = 0
        last_hb = 0.0
        def maybe_heartbeat(mode: str, episode_idx: int) -> None:
            nonlocal last_hb
            now = time.time()
            if args.heartbeat_seconds <= 0 or now - last_hb < args.heartbeat_seconds:
                return
            mem = memory_snapshot()
            print(
                "[heartbeat] "
                f"mode={mode} "
                f"world={idx + 1}/{len(files)} "
                f"episode={episode_idx + 1}/{args.episodes} "
                f"rss_mb={mem['rss_mb']:.1f} "
                f"cuda_allocated_mb={mem['cuda_allocated_mb']:.1f} "
                f"cuda_reserved_mb={mem['cuda_reserved_mb']:.1f} "
                f"base_trace_rows={base_trace_rows} "
                f"adapter_trace_rows={adapter_trace_rows}"
            )
            last_hb = now

        def enforce_rss_cap() -> None:
            if args.max_rss_mb > 0 and _rss_mb() > args.max_rss_mb:
                raise SystemExit(f"rss limit exceeded: {_rss_mb():.1f}MB > {args.max_rss_mb}MB")

        if need_base:
            base_controller = controller_from_args(args.base_model or None, None, args.device, args.dtype)
            for ep in range(args.episodes):
                b_steps: List[Dict[str, Any]] = []
                b = run_episode(
                    "base",
                    encounters,
                    start_id,
                    base_controller,
                    ep,
                    args.max_steps,
                    include_prompt_in_trace=args.include_prompt_in_trace,
                    include_steps_in_episode=args.include_steps_in_episodes,
                    emit_step=b_steps.append,
                )
                step_count = int(b["step_count"])
                append_jsonl(base_trace_path, b_steps)
                append_jsonl(base_ep_path, [b])
                base_trace_rows += step_count
                base_eps.append(b)
                maybe_heartbeat("base", ep)
                enforce_rss_cap()
            del base_controller
            gc.collect()
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except Exception:
                pass

        if need_adapter:
            adapter_controller = controller_from_args(args.base_model or None, args.adapter_path or None, args.device, args.dtype)
            for ep in range(args.episodes):
                a_steps: List[Dict[str, Any]] = []
                a = run_episode(
                    "adapter",
                    encounters,
                    start_id,
                    adapter_controller,
                    ep,
                    args.max_steps,
                    include_prompt_in_trace=args.include_prompt_in_trace,
                    include_steps_in_episode=args.include_steps_in_episodes,
                    emit_step=a_steps.append,
                )
                step_count = int(a["step_count"])
                append_jsonl(adapter_trace_path, a_steps)
                append_jsonl(adapter_ep_path, [a])
                adapter_trace_rows += step_count
                adapter_eps.append(a)
                maybe_heartbeat("adapter", ep)
                enforce_rss_cap()
            del adapter_controller
            gc.collect()
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except Exception:
                pass

        summary: Dict[str, Any] = {
            "mission": "swmd-rollout-eval",
            "target": str(swmd),
            "swmd_hash": world.hash_sha256,
            "result": "ok",
            "base": summarize(base_eps) if need_base else None,
            "adapter": summarize(adapter_eps) if need_adapter else None,
            "run_modes": args.run_modes,
            "evidence_paths": {
                "base_trace": str(base_trace_path) if need_base else "",
                "adapter_trace": str(adapter_trace_path) if need_adapter else "",
                "base_episodes": str(base_ep_path) if need_base else "",
                "adapter_episodes": str(adapter_ep_path) if need_adapter else "",
            },
            "runtime": {
                "episodes": args.episodes,
                "max_steps": args.max_steps,
                **memory_snapshot(),
                "base_trace_rows": base_trace_rows,
                "adapter_trace_rows": adapter_trace_rows,
                "include_prompt_in_trace": bool(args.include_prompt_in_trace),
                "include_steps_in_episodes": bool(args.include_steps_in_episodes),
            },
        }
        repo_root = Path(__file__).resolve().parents[2]
        summary["run_identity"] = make_run_identity(
            swmd_hash=world.hash_sha256,
            dataset_hash="",
            rows_merkle_root="",
            builder_git_commit="",
            trainer_git_commit=git_commit(repo_root),
            base_model_id=args.base_model or "heuristic",
            adapter_config={
                "adapter_path": args.adapter_path or "",
                "dtype": args.dtype,
                "device": args.device,
                "episodes": args.episodes,
                "max_steps": args.max_steps,
            },
        )
        summary["run_identity_hash"] = h_hex(stable_json(summary["run_identity"]))
        (out_dir / "rollout_eval_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
        batch_rows.append(
            {
                "world_id": world_id,
                "target": str(swmd),
                "run_modes": args.run_modes,
                "adapter_steps": (summary["adapter"] or {}).get("steps", 0),
                "adapter_episodes": (summary["adapter"] or {}).get("episodes", 0),
                "rss_mb": summary["runtime"]["rss_mb"],
                "summary_path": str(out_dir / "rollout_eval_summary.json"),
            }
        )

    batch_summary = {"count": len(batch_rows), "rows": batch_rows}
    (out_root / "rollout_batch_summary.json").write_text(json.dumps(batch_summary, indent=2), encoding="utf-8")
    print(json.dumps(batch_summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
