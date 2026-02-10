from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional

import numpy as np

try:
    import torch
except Exception:  # pragma: no cover
    torch = None

from .trace import TraceWriter


@dataclass
class HookConfig:
    capture_state: bool = True
    capture_aux: bool = True
    capture_output: bool = True
    capture_metrics: bool = True


class StepTracer:
    """Wraps a model with step(state, obs)->(new_state, output, aux)."""

    def __init__(self, model: Any, writer: TraceWriter, config: Optional[HookConfig] = None) -> None:
        self.model = model
        self.writer = writer
        self.config = config or HookConfig()

    def step(self, t: int, state: Any, obs: Any, metrics: Optional[Dict[str, Any]] = None):
        new_state, output, aux = self.model.step(state, obs)
        self.writer.add_step(
            t=t,
            h=new_state if self.config.capture_state else None,
            aux=aux if self.config.capture_aux else {},
            y=output if self.config.capture_output else None,
            metrics=metrics if (metrics and self.config.capture_metrics) else {},
        )
        return new_state, output, aux


def select_tensor_dict(data: Dict[str, Any], keys: Iterable[str]) -> Dict[str, Any]:
    selected: Dict[str, Any] = {}
    for key in keys:
        if key in data:
            selected[key] = data[key]
    return selected


def tensor_norm(value: Any) -> float:
    if torch is not None and isinstance(value, torch.Tensor):
        return float(value.detach().norm().item())
    arr = np.asarray(value)
    return float(np.linalg.norm(arr))
