from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

import numpy as np

from .common import load_trace_paths, load_trace_states, write_json


def pca_project(x: np.ndarray, n_components: int = 2) -> np.ndarray:
    x_centered = x - x.mean(axis=0, keepdims=True)
    u, s, _vt = np.linalg.svd(x_centered, full_matrices=False)
    comps = u[:, :n_components] * s[:n_components]
    return comps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute low-dim embeddings for trajectory states.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, default=Path("tools/bench/out/embedding.json"))
    parser.add_argument("--components", type=int, default=2)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    trace_paths = load_trace_paths(args.summary_json)

    rows: List[np.ndarray] = []
    metadata: List[Dict] = []
    for path in trace_paths:
        states = load_trace_states(path)
        for t, state in enumerate(states):
            rows.append(state)
            metadata.append({"trace_path": str(path), "t": int(t)})

    x = np.stack(rows, axis=0)
    z = pca_project(x, n_components=args.components)

    output = []
    for i, point in enumerate(z):
        row = metadata[i].copy()
        row["embedding"] = [float(v) for v in point]
        output.append(row)

    write_json(args.out_json, {"components": args.components, "points": output})
    print(f"Wrote embeddings: {args.out_json}")


if __name__ == "__main__":
    main()
