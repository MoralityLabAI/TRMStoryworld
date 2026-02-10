from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List

from trm_trace.trace import TraceWriter

from .synthetic import ToyTRM, build_synthetic_tasks, run_episode, set_global_seed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run synthetic TRM tasks and emit traces.")
    parser.add_argument("--out-dir", type=Path, default=Path("tools/bench/out/traces"))
    parser.add_argument("--num-tasks", type=int, default=12)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--fmt", choices=["jsonl", "npz"], default="jsonl")
    parser.add_argument("--compress", action="store_true")
    return parser.parse_args()


def run_tasks(out_dir: Path, num_tasks: int, steps: int, seed: int, fmt: str, compress: bool) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    set_global_seed(seed)
    model = ToyTRM()
    tasks = build_synthetic_tasks(num_tasks=num_tasks, seed=seed)

    summary: List[dict] = []

    for i, task in enumerate(tasks):
        trace_suffix = ".jsonl.gz" if (fmt == "jsonl" and compress) else (".jsonl" if fmt == "jsonl" else ".npz")
        path = out_dir / f"{task['task_id']}_seed{seed}{trace_suffix}"
        result = run_episode(model=model, task=task, steps=steps)

        with TraceWriter(path=path, task_id=task["task_id"], seed=seed, fmt=fmt, compress=compress) as writer:
            for step in result["steps"]:
                writer.add_step(t=step["t"], h=step["h"], aux=step["aux"], y=step["y"], metrics=step["metrics"])

        summary.append(
            {
                "task_id": task["task_id"],
                "type": task["type"],
                "target": int(task["target"]),
                "final_correct": int(result["final_correct"]),
                "trace_path": str(path),
            }
        )

    summary_path = out_dir / f"run_summary_seed{seed}.json"
    with open(summary_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(summary, fh, indent=2, sort_keys=True, ensure_ascii=True)
    return summary_path


def main() -> None:
    args = parse_args()
    summary_path = run_tasks(
        out_dir=args.out_dir,
        num_tasks=args.num_tasks,
        steps=args.steps,
        seed=args.seed,
        fmt=args.fmt,
        compress=args.compress,
    )
    print(f"Wrote summary: {summary_path}")


if __name__ == "__main__":
    main()
