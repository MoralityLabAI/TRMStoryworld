from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
import torch


Task = Dict[str, Any]


def set_global_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


@dataclass
class ToyTRM:
    obs_dim: int = 8
    state_dim: int = 16
    hidden_dim: int = 32

    def __post_init__(self) -> None:
        self.w_in = torch.nn.Linear(self.obs_dim, self.hidden_dim)
        self.w_state = torch.nn.Linear(self.state_dim, self.hidden_dim)
        self.w_gate = torch.nn.Linear(self.hidden_dim, self.state_dim)
        self.w_out = torch.nn.Linear(self.state_dim, 1)

    def init_state(self) -> torch.Tensor:
        return torch.zeros(self.state_dim, dtype=torch.float32)

    def step(self, state: torch.Tensor, obs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, Dict[str, torch.Tensor]]:
        x = torch.tanh(self.w_in(obs) + self.w_state(state))
        gate = torch.sigmoid(self.w_gate(x))
        proposal = torch.tanh(gate)
        new_state = 0.85 * state + 0.15 * proposal
        logit = self.w_out(new_state)
        output = torch.sigmoid(logit)
        aux = {
            "gate": gate.detach(),
            "proposal": proposal.detach(),
            "logit": logit.detach(),
        }
        return new_state, output.squeeze(), aux


def task_to_obs(task: Task, t: int, obs_dim: int) -> torch.Tensor:
    obs = np.zeros(obs_dim, dtype=np.float32)
    payload = task["payload"]
    if task["type"] == "parity":
        obs[: len(payload)] = payload
        obs[-2] = float(t)
    elif task["type"] == "sum_mod":
        obs[: len(payload)] = payload
        obs[-1] = float(t)
    else:  # constraints
        obs[: min(len(payload), obs_dim)] = payload[:obs_dim]
        obs[-1] = float(t)
    return torch.tensor(obs, dtype=torch.float32)


def build_synthetic_tasks(num_tasks: int, seed: int) -> List[Task]:
    rng = np.random.default_rng(seed)
    tasks: List[Task] = []
    for i in range(num_tasks):
        kind = ["parity", "sum_mod", "constraints"][i % 3]
        if kind == "parity":
            payload = rng.integers(0, 2, size=6).astype(np.float32)
            target = int(payload.sum() % 2)
        elif kind == "sum_mod":
            payload = rng.integers(0, 5, size=5).astype(np.float32)
            target = int(payload.sum() % 3)
        else:
            payload = rng.normal(size=8).astype(np.float32)
            target = int((payload[:4].sum() - payload[4:].sum()) > 0)
        tasks.append({"task_id": f"task_{i}", "type": kind, "payload": payload, "target": target})
    return tasks


def evaluate_output(task: Task, output: torch.Tensor) -> int:
    val = float(output.item())
    if task["type"] == "sum_mod":
        pred = int(np.floor(val * 3.0)) % 3
    else:
        pred = int(val > 0.5)
    return pred


def run_episode(
    model: ToyTRM,
    task: Task,
    steps: int,
    intervention: Optional[Callable[[int, torch.Tensor, Dict[str, torch.Tensor]], Tuple[torch.Tensor, Dict[str, torch.Tensor], Dict[str, Any]]]] = None,
) -> Dict[str, Any]:
    state = model.init_state()
    trace_steps: List[Dict[str, Any]] = []
    history = []

    for t in range(steps):
        obs = task_to_obs(task, t=t, obs_dim=model.obs_dim)
        state, output, aux = model.step(state, obs)
        intervention_log = {}
        if intervention is not None:
            state, aux, intervention_log = intervention(t, state, aux)

        pred = evaluate_output(task, output)
        correct = int(pred == task["target"])
        entropy_proxy = float(-(output * torch.log(output + 1e-6) + (1 - output) * torch.log(1 - output + 1e-6)).item())
        metrics = {
            "pred": pred,
            "target": int(task["target"]),
            "correct": correct,
            "uncertainty": entropy_proxy,
            "state_norm": float(state.norm().item()),
        }
        if intervention_log:
            metrics["intervention"] = intervention_log

        trace_steps.append(
            {
                "t": t,
                "h": state.detach().cpu().numpy().astype(np.float32),
                "aux": {k: v.detach().cpu().numpy().astype(np.float32) for k, v in aux.items()},
                "y": float(output.item()),
                "metrics": metrics,
            }
        )
        history.append(correct)

    final_correct = int(history[-1]) if history else 0
    return {"task_id": task["task_id"], "seed": None, "steps": trace_steps, "final_correct": final_correct}
