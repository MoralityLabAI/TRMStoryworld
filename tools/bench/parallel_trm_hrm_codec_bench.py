#!/usr/bin/env python3
"""Run TRM and HRM codec benchmarks in parallel and emit one consolidated manifest."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List


def _safe_name(path: Path) -> str:
    stem = "".join(path.suffixes)
    name = path.name[: -len(stem)] if stem else path.stem
    return "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in name)


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True, ensure_ascii=True)


def _run_cmd(cmd: List[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=None if cwd is None else str(cwd), capture_output=True, text=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parallel TRM/HRM codec benchmark runner")
    parser.add_argument("--codec", type=Path, required=True, help="Path to codec.txt")
    parser.add_argument(
        "--swmd-root",
        type=Path,
        default=Path("tools/bench/out/storyworlds_swmd_min_local"),
        help="Directory containing *.swmd.min.md files for TRM benchmarks.",
    )
    parser.add_argument(
        "--trm-script",
        type=Path,
        default=Path("negotiation-storyworld/tools/trm_trace_benchmark.py"),
        help="Path to TRM benchmark script.",
    )
    parser.add_argument("--episodes", type=int, default=4)
    parser.add_argument("--max-steps", type=int, default=6)
    parser.add_argument("--seed-base", type=int, default=101)
    parser.add_argument("--latent-dim", type=int, default=16)
    parser.add_argument("--latent-weight", type=float, default=0.15)
    parser.add_argument("--trm-workers", type=int, default=4)
    parser.add_argument("--max-swmd", type=int, default=0, help="Optional cap on number of SWMD files.")
    parser.add_argument("--hrm-repo", type=Path, default=Path(r"C:\projects\HRM-re"))
    parser.add_argument(
        "--hrm-codec-wrapper",
        type=Path,
        default=Path("experiments/trm_codec_frame/train_codec_frame.py"),
        help="Path inside HRM repo to codec training wrapper.",
    )
    parser.add_argument(
        "--hrm-config",
        type=Path,
        default=Path("experiments/hrm_trainer_template/trainer_config_safe.json"),
        help="Path inside HRM repo to base trainer config.",
    )
    parser.add_argument("--hrm-runs", type=int, default=2, help="How many HRM runs to launch.")
    parser.add_argument("--hrm-workers", type=int, default=2)
    parser.add_argument("--hrm-dry-run", action="store_true", help="Run HRM wrapper in dry-run mode.")
    parser.add_argument("--out-root", type=Path, default=Path("tools/bench/out/parallel_codec_bench"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    trm_script = (repo_root / args.trm_script).resolve()
    swmd_root = (repo_root / args.swmd_root).resolve()
    codec_path = args.codec.resolve()
    out_root = (repo_root / args.out_root).resolve()
    trm_out_root = out_root / "trm"
    hrm_out_root = out_root / "hrm"
    trm_out_root.mkdir(parents=True, exist_ok=True)
    hrm_out_root.mkdir(parents=True, exist_ok=True)

    swmd_files = sorted(swmd_root.rglob("*.swmd.min.md"))
    if args.max_swmd > 0:
        swmd_files = swmd_files[: args.max_swmd]

    trm_jobs = []
    for i, swmd in enumerate(swmd_files):
        safe = _safe_name(swmd)
        trm_jobs.append(
            {
                "idx": i,
                "swmd": swmd,
                "trace_out": trm_out_root / f"{safe}-codec_traces.jsonl",
                "episode_out": trm_out_root / f"{safe}-codec_episodes.jsonl",
                "latent_out": trm_out_root / f"{safe}-codec_latent_traces.jsonl",
                "summary_out": trm_out_root / f"{safe}-codec_summary.json",
            }
        )

    hrm_repo = args.hrm_repo.resolve()
    hrm_config = (hrm_repo / args.hrm_config).resolve()
    hrm_jobs = []
    for i in range(args.hrm_runs):
        run_name = f"codec_hrm_run_{i + 1:02d}"
        out_cfg = hrm_out_root / f"{run_name}_config.json"
        hrm_jobs.append({"idx": i, "run_name": run_name, "out_config": out_cfg})

    def run_trm(job: Dict[str, Any]) -> Dict[str, Any]:
        start = time.time()
        cmd = [
            "python",
            str(trm_script),
            "--world",
            str(job["swmd"]),
            "--episodes",
            str(args.episodes),
            "--max-steps",
            str(args.max_steps),
            "--seed",
            str(args.seed_base + job["idx"]),
            "--trace-out",
            str(job["trace_out"]),
            "--episode-out",
            str(job["episode_out"]),
            "--latent-trace-out",
            str(job["latent_out"]),
            "--summary-out",
            str(job["summary_out"]),
            "--latent-dim",
            str(args.latent_dim),
            "--latent-weight",
            str(args.latent_weight),
        ]
        proc = _run_cmd(cmd, cwd=repo_root)
        return {
            "kind": "trm",
            "world": str(job["swmd"]),
            "returncode": int(proc.returncode),
            "seconds": round(time.time() - start, 3),
            "summary_out": str(job["summary_out"]),
            "stdout_tail": (proc.stdout or "")[-1500:],
            "stderr_tail": (proc.stderr or "")[-1500:],
        }

    def run_hrm(job: Dict[str, Any]) -> Dict[str, Any]:
        start = time.time()
        cmd = [
            "python",
            "-m",
            "experiments.trm_codec_frame.train_codec_frame",
            "--config",
            str(hrm_config),
            "--codec",
            str(codec_path),
            "--out-config",
            str(job["out_config"]),
        ]
        if args.hrm_dry_run:
            cmd.append("--dry-run")
        proc = _run_cmd(cmd, cwd=hrm_repo)
        return {
            "kind": "hrm",
            "run_name": job["run_name"],
            "returncode": int(proc.returncode),
            "seconds": round(time.time() - start, 3),
            "config_out": str(job["out_config"]),
            "stdout_tail": (proc.stdout or "")[-1500:],
            "stderr_tail": (proc.stderr or "")[-1500:],
        }

    results: List[Dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.trm_workers + args.hrm_workers)) as pool:
        futures = []
        for job in trm_jobs:
            futures.append(pool.submit(run_trm, job))
        for job in hrm_jobs:
            futures.append(pool.submit(run_hrm, job))
        for fut in as_completed(futures):
            results.append(fut.result())

    trm_results = [r for r in results if r["kind"] == "trm"]
    hrm_results = [r for r in results if r["kind"] == "hrm"]
    payload = {
        "mission": "parallel_trm_hrm_codec_bench",
        "codec": str(codec_path),
        "config": {
            "episodes": int(args.episodes),
            "max_steps": int(args.max_steps),
            "seed_base": int(args.seed_base),
            "latent_dim": int(args.latent_dim),
            "latent_weight": float(args.latent_weight),
            "trm_workers": int(args.trm_workers),
            "hrm_workers": int(args.hrm_workers),
            "hrm_dry_run": bool(args.hrm_dry_run),
        },
        "counts": {
            "trm_jobs": len(trm_jobs),
            "hrm_jobs": len(hrm_jobs),
            "trm_ok": sum(1 for r in trm_results if r["returncode"] == 0),
            "hrm_ok": sum(1 for r in hrm_results if r["returncode"] == 0),
        },
        "trm_results": sorted(trm_results, key=lambda x: x["world"]),
        "hrm_results": sorted(hrm_results, key=lambda x: x["run_name"]),
    }
    manifest = out_root / "parallel_manifest.json"
    _write_json(manifest, payload)
    print(f"Wrote parallel manifest: {manifest}")
    return 0 if payload["counts"]["trm_ok"] == len(trm_jobs) and payload["counts"]["hrm_ok"] == len(hrm_jobs) else 2


if __name__ == "__main__":
    raise SystemExit(main())
