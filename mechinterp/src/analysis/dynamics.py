from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

import numpy as np

from .common import load_trace_paths, load_trace_states, trajectory_deltas, write_json


def analyze_trajectory(states: np.ndarray, cycle_eps: float, diverge_threshold: float) -> Dict:
    deltas = trajectory_deltas(states)
    convergence_score = float(deltas[-1]) if len(deltas) else 0.0
    converged = bool(convergence_score < cycle_eps)

    cycle_detected = False
    cycle_len = 0
    for lag in range(1, min(5, states.shape[0] // 2 + 1)):
        shifted = states[lag:]
        base = states[:-lag]
        dist = np.linalg.norm(shifted - base, axis=1)
        if len(dist) > 1 and float(np.mean(dist)) < cycle_eps:
            cycle_detected = True
            cycle_len = lag
            break

    max_norm = float(np.max(np.linalg.norm(states, axis=1)))
    diverged = bool(max_norm > diverge_threshold)

    return {
        "converged": converged,
        "cycle_detected": cycle_detected,
        "cycle_len": cycle_len,
        "diverged": diverged,
        "final_delta": convergence_score,
        "max_state_norm": max_norm,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze convergence/cycles in TRM traces.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, default=Path("tools/bench/out/dynamics.json"))
    parser.add_argument("--cycle-eps", type=float, default=0.03)
    parser.add_argument("--diverge-threshold", type=float, default=25.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    per_trace = {}
    trace_paths = load_trace_paths(args.summary_json)
    for path in trace_paths:
        states = load_trace_states(path)
        per_trace[str(path)] = analyze_trajectory(states, cycle_eps=args.cycle_eps, diverge_threshold=args.diverge_threshold)

    payload = {
        "num_traces": len(per_trace),
        "results": per_trace,
    }
    write_json(args.out_json, payload)
    print(f"Wrote dynamics analysis: {args.out_json}")


if __name__ == "__main__":
    main()
