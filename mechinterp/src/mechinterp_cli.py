from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from runner.run_tasks import run_tasks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TRM mechanistic interpretability toolkit CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name in ("run", "trace"):
        p = sub.add_parser(name, help="Run synthetic tasks and collect traces")
        p.add_argument("--out-dir", type=Path, default=Path("tools/bench/out/traces"))
        p.add_argument("--num-tasks", type=int, default=12)
        p.add_argument("--steps", type=int, default=6)
        p.add_argument("--seed", type=int, default=7)
        p.add_argument("--fmt", choices=["jsonl", "npz"], default="jsonl")
        p.add_argument("--compress", action="store_true")

    p = sub.add_parser("analyze", help="Run dynamics, embedding, causality, and monitor analyses")
    p.add_argument("--summary-json", type=Path, required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--steps", type=int, default=6)

    p = sub.add_parser("patch", help="Patch one episode with donor state")
    p.add_argument("--donor-trace", type=Path, required=True)
    p.add_argument("--target-task-id", required=True)
    p.add_argument("--num-tasks", type=int, default=12)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--steps", type=int, default=6)
    p.add_argument("--patch-step", type=int, default=2)
    p.add_argument("--out-json", type=Path, default=Path("tools/bench/out/patch_result.json"))

    return parser.parse_args()


def _run_module(args: list[str]) -> None:
    subprocess.run([sys.executable, "-m", *args], check=True)


def main() -> None:
    args = parse_args()
    if args.cmd in {"run", "trace"}:
        summary = run_tasks(args.out_dir, args.num_tasks, args.steps, args.seed, args.fmt, args.compress)
        print(f"Summary: {summary}")
        return

    if args.cmd == "analyze":
        _run_module(["analysis.dynamics", "--summary-json", str(args.summary_json)])
        _run_module(["analysis.embedding", "--summary-json", str(args.summary_json)])
        _run_module(["analysis.sae", "--summary-json", str(args.summary_json)])
        _run_module(["analysis.causality", "--summary-json", str(args.summary_json), "--seed", str(args.seed), "--steps", str(args.steps)])
        _run_module(["analysis.monitors", "--summary-json", str(args.summary_json)])
        return

    if args.cmd == "patch":
        _run_module(
            [
                "runner.patch_run",
                "--donor-trace",
                str(args.donor_trace),
                "--target-task-id",
                str(args.target_task_id),
                "--num-tasks",
                str(args.num_tasks),
                "--seed",
                str(args.seed),
                "--steps",
                str(args.steps),
                "--patch-step",
                str(args.patch_step),
                "--out-json",
                str(args.out_json),
            ]
        )
        return


if __name__ == "__main__":
    main()
