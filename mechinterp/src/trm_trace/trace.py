from __future__ import annotations

import gzip
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional

import numpy as np

try:
    import torch
except Exception:  # pragma: no cover
    torch = None


REQUIRED_STEP_KEYS = {"t", "h", "aux", "y", "metrics"}


@dataclass
class TraceRecord:
    task_id: str
    seed: int
    steps: List[Dict[str, Any]]


def _to_serializable(value: Any) -> Any:
    if torch is not None and isinstance(value, torch.Tensor):
        return value.detach().cpu().tolist()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, dict):
        return {str(k): _to_serializable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_serializable(v) for v in value]
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    return value


class TraceWriter:
    """Incremental trace writer for JSONL or NPZ outputs."""

    def __init__(
        self,
        path: str | Path,
        task_id: str,
        seed: int,
        fmt: str = "jsonl",
        compress: bool = False,
    ) -> None:
        self.path = Path(path)
        self.task_id = task_id
        self.seed = int(seed)
        self.fmt = fmt
        self.compress = compress
        self._steps: List[Dict[str, Any]] = []
        self._fh = None
        self._closed = False

        if self.fmt not in {"jsonl", "npz"}:
            raise ValueError("fmt must be jsonl or npz")

        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.fmt == "jsonl":
            if self.compress:
                self._fh = gzip.open(self.path, "at", encoding="utf-8")
            else:
                self._fh = open(self.path, "a", encoding="utf-8")

    def add_step(
        self,
        t: int,
        h: Any,
        aux: Dict[str, Any],
        y: Any,
        metrics: Dict[str, Any],
    ) -> None:
        if self._closed:
            raise RuntimeError("TraceWriter is closed")
        step = {
            "t": int(t),
            "h": _to_serializable(h),
            "aux": _to_serializable(aux),
            "y": _to_serializable(y),
            "metrics": _to_serializable(metrics),
        }
        validate_step_schema(step)

        if self.fmt == "jsonl":
            payload = {
                "task_id": self.task_id,
                "seed": self.seed,
                "step": step,
            }
            assert self._fh is not None
            self._fh.write(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n")
            self._fh.flush()
        else:
            self._steps.append(step)

    def close(self) -> None:
        if self._closed:
            return
        if self.fmt == "npz":
            steps_json = [json.dumps(step, sort_keys=True, separators=(",", ":"), ensure_ascii=True) for step in self._steps]
            arr = np.array(steps_json, dtype=object)
            if self.compress:
                np.savez_compressed(self.path, task_id=self.task_id, seed=self.seed, steps=arr)
            else:
                np.savez(self.path, task_id=self.task_id, seed=self.seed, steps=arr)
        elif self._fh is not None:
            self._fh.close()
        self._closed = True

    def __enter__(self) -> "TraceWriter":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


class TraceReader:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        suffixes = "".join(self.path.suffixes)
        if suffixes.endswith(".jsonl") or suffixes.endswith(".jsonl.gz"):
            self.fmt = "jsonl"
        elif suffixes.endswith(".npz"):
            self.fmt = "npz"
        else:
            raise ValueError("Unsupported trace file format")

    def iter_steps(self) -> Iterator[Dict[str, Any]]:
        if self.fmt == "jsonl":
            opener = gzip.open if "".join(self.path.suffixes).endswith(".gz") else open
            with opener(self.path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    row = json.loads(line)
                    if "step" not in row:
                        raise ValueError("Missing step field")
                    step = row["step"]
                    validate_step_schema(step)
                    yield {"task_id": row.get("task_id"), "seed": row.get("seed"), **step}
        else:
            data = np.load(self.path, allow_pickle=True)
            task_id = str(data["task_id"])
            seed = int(data["seed"])
            for raw in data["steps"]:
                step = json.loads(str(raw))
                validate_step_schema(step)
                yield {"task_id": task_id, "seed": seed, **step}

    def read(self) -> TraceRecord:
        steps = []
        task_id: Optional[str] = None
        seed: Optional[int] = None
        for row in self.iter_steps():
            task_id = row["task_id"] if task_id is None else task_id
            seed = int(row["seed"]) if seed is None else seed
            steps.append({k: row[k] for k in ("t", "h", "aux", "y", "metrics")})
        if task_id is None or seed is None:
            raise ValueError("Trace has no steps")
        return TraceRecord(task_id=task_id, seed=seed, steps=steps)


def validate_step_schema(step: Dict[str, Any]) -> None:
    keys = set(step.keys())
    missing = REQUIRED_STEP_KEYS - keys
    if missing:
        raise ValueError(f"Missing required step keys: {sorted(missing)}")
    if not isinstance(step["t"], int):
        raise ValueError("t must be an int")
    if not isinstance(step["aux"], dict):
        raise ValueError("aux must be a dict")
    if not isinstance(step["metrics"], dict):
        raise ValueError("metrics must be a dict")


def group_steps_by_trace(rows: Iterable[Dict[str, Any]]) -> List[TraceRecord]:
    grouped: Dict[tuple[str, int], List[Dict[str, Any]]] = {}
    for row in rows:
        key = (str(row["task_id"]), int(row["seed"]))
        grouped.setdefault(key, []).append({k: row[k] for k in ("t", "h", "aux", "y", "metrics")})

    traces = []
    for (task_id, seed), steps in grouped.items():
        steps_sorted = sorted(steps, key=lambda s: s["t"])
        traces.append(TraceRecord(task_id=task_id, seed=seed, steps=steps_sorted))
    return traces
