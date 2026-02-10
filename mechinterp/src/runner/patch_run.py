from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import torch

from runner.synthetic import ToyTRM, build_synthetic_tasks, run_episode, set_global_seed
from trm_trace.interventions import patch_state
from trm_trace.trace import TraceReader


def _read_trace(path: Path) -> Dict[str, Any]:
    record = TraceReader(path).read()
    return {"task_id": record.task_id, "seed": record.seed, "steps": record.steps}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one patched episode with donor state at selected step.")
    parser.add_argument("--donor-trace", type=Path, required=True)
    parser.add_argument("--target-task-id", type=str, required=True)
    parser.add_argument("--num-tasks", type=int, default=12)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--patch-step", type=int, default=2)
    parser.add_argument("--out-json", type=Path, default=Path("tools/bench/out/patch_result.json"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    set_global_seed(args.seed)
    model = ToyTRM()
    tasks = build_synthetic_tasks(num_tasks=args.num_tasks, seed=args.seed)
    by_id = {task["task_id"]: task for task in tasks}
    if args.target_task_id not in by_id:
        raise ValueError(f"Unknown target task_id: {args.target_task_id}")

    donor = _read_trace(args.donor_trace)

    def intervention(t: int, state: torch.Tensor, aux: Dict[str, torch.Tensor]):
        if t != args.patch_step:
            return state, aux, {}
        patched, log = patch_state(
            {"steps": [{"h": state.detach().cpu().numpy()}]},
            {"steps": [{"h": donor["steps"][args.patch_step]["h"]}]},
            t=0,
        )
        return torch.tensor(patched, dtype=state.dtype), aux, log

    target_task = by_id[args.target_task_id]
    baseline = run_episode(model, target_task, steps=args.steps)
    patched = run_episode(model, target_task, steps=args.steps, intervention=intervention)

    result = {
        "target_task_id": args.target_task_id,
        "patch_step": int(args.patch_step),
        "baseline_final_correct": int(baseline["final_correct"]),
        "patched_final_correct": int(patched["final_correct"]),
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out_json, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, indent=2, sort_keys=True, ensure_ascii=True)

    print(f"Wrote patch result: {args.out_json}")


if __name__ == "__main__":
    main()
