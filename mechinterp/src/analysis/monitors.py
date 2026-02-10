from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

from .common import flatten_prefix, load_trace_states, safe_auc, write_json


def _load_summary(path: Path) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def fit_logreg(x: np.ndarray, y: np.ndarray, lr: float = 0.1, epochs: int = 400) -> np.ndarray:
    w = np.zeros(x.shape[1], dtype=np.float64)
    for _ in range(epochs):
        pred = _sigmoid(x @ w)
        grad = x.T @ (pred - y) / len(y)
        w -= lr * grad
    return w


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train early-failure monitor from first k steps.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, default=Path("tools/bench/out/monitor.json"))
    parser.add_argument("--k", type=int, default=3)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = _load_summary(args.summary_json)

    x_rows = []
    y_rows = []
    for row in rows:
        states = load_trace_states(Path(row["trace_path"]))
        x_rows.append(flatten_prefix(states, args.k))
        y_rows.append(1 - int(row["final_correct"]))  # 1=failure

    x = np.stack(x_rows, axis=0).astype(np.float64)
    y = np.asarray(y_rows, dtype=np.float64)

    perm = np.arange(len(y))
    rng = np.random.default_rng(123)
    rng.shuffle(perm)
    split = max(1, int(0.7 * len(y)))
    train_idx = perm[:split]
    test_idx = perm[split:]
    if len(test_idx) == 0:
        test_idx = train_idx

    mu = x[train_idx].mean(axis=0, keepdims=True)
    sigma = x[train_idx].std(axis=0, keepdims=True) + 1e-6
    x_norm = (x - mu) / sigma

    w = fit_logreg(x_norm[train_idx], y[train_idx])
    test_scores = _sigmoid(x_norm[test_idx] @ w)
    test_pred = (test_scores >= 0.5).astype(np.int64)
    test_true = y[test_idx].astype(np.int64)

    acc = float((test_pred == test_true).mean())
    auc = safe_auc(test_true, test_scores)

    payload = {
        "k": int(args.k),
        "num_samples": int(len(y)),
        "accuracy": acc,
        "auc": auc,
    }
    write_json(args.out_json, payload)
    print(f"Wrote monitor analysis: {args.out_json}")


if __name__ == "__main__":
    main()
