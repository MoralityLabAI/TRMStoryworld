from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List

import numpy as np

from trm_trace.trace import TraceReader


def load_trace_paths(summary_json: Path) -> List[Path]:
    with open(summary_json, "r", encoding="utf-8") as fh:
        rows = json.load(fh)
    return [Path(row["trace_path"]) for row in rows]


def load_trace_states(path: Path) -> np.ndarray:
    reader = TraceReader(path)
    states = []
    for step in reader.iter_steps():
        states.append(np.asarray(step["h"], dtype=np.float32))
    if not states:
        raise ValueError(f"Empty trace: {path}")
    return np.stack(states, axis=0)


def write_json(path: Path, payload: Dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True, ensure_ascii=True)


def trajectory_deltas(states: np.ndarray) -> np.ndarray:
    if states.shape[0] < 2:
        return np.zeros((0,), dtype=np.float32)
    return np.linalg.norm(states[1:] - states[:-1], axis=1)


def flatten_prefix(states: np.ndarray, k: int) -> np.ndarray:
    k = max(1, min(k, states.shape[0]))
    return states[:k].reshape(-1)


def safe_auc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    pos = y_true == 1
    neg = y_true == 0
    n_pos = int(pos.sum())
    n_neg = int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        return 0.5
    order = np.argsort(y_score)
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(y_score) + 1)
    pos_rank_sum = ranks[pos].sum()
    auc = (pos_rank_sum - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)
    return float(auc)
