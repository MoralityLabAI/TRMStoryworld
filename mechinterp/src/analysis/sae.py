from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Tuple

import numpy as np
import torch

from .common import load_trace_paths, load_trace_states, write_json


@dataclass
class SAEModel:
    state_dim: int
    feature_dim: int
    k: int
    w_enc: np.ndarray
    b_enc: np.ndarray
    w_dec: np.ndarray
    b_dec: np.ndarray

    def encode(self, h: np.ndarray) -> np.ndarray:
        x = np.asarray(h, dtype=np.float32)
        if x.ndim == 1:
            x = x[None, :]
        pre = x @ self.w_enc + self.b_enc
        act = np.maximum(pre, 0.0)
        if self.k >= self.feature_dim:
            return act.squeeze(0) if np.asarray(h).ndim == 1 else act
        topk_idx = np.argpartition(act, kth=self.feature_dim - self.k, axis=1)[:, -self.k :]
        mask = np.zeros_like(act, dtype=np.float32)
        rows = np.arange(act.shape[0])[:, None]
        mask[rows, topk_idx] = 1.0
        out = act * mask
        return out.squeeze(0) if np.asarray(h).ndim == 1 else out

    def decode(self, a: np.ndarray) -> np.ndarray:
        x = np.asarray(a, dtype=np.float32)
        if x.ndim == 1:
            x = x[None, :]
        out = x @ self.w_dec + self.b_dec
        return out.squeeze(0) if np.asarray(a).ndim == 1 else out

    def to_dict(self) -> Dict[str, Any]:
        return {
            "state_dim": int(self.state_dim),
            "feature_dim": int(self.feature_dim),
            "k": int(self.k),
            "w_enc": self.w_enc.tolist(),
            "b_enc": self.b_enc.tolist(),
            "w_dec": self.w_dec.tolist(),
            "b_dec": self.b_dec.tolist(),
        }

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "SAEModel":
        return cls(
            state_dim=int(payload["state_dim"]),
            feature_dim=int(payload["feature_dim"]),
            k=int(payload["k"]),
            w_enc=np.asarray(payload["w_enc"], dtype=np.float32),
            b_enc=np.asarray(payload["b_enc"], dtype=np.float32),
            w_dec=np.asarray(payload["w_dec"], dtype=np.float32),
            b_dec=np.asarray(payload["b_dec"], dtype=np.float32),
        )


def _topk_mask(x: torch.Tensor, k: int) -> torch.Tensor:
    if k >= x.shape[-1]:
        return torch.ones_like(x)
    _, idx = torch.topk(x, k=k, dim=-1)
    mask = torch.zeros_like(x)
    mask.scatter_(dim=-1, index=idx, value=1.0)
    return mask


def _gini_nonneg(a: np.ndarray) -> float:
    x = np.asarray(a, dtype=np.float32).reshape(-1)
    x = np.abs(x)
    if x.size == 0 or float(x.sum()) == 0.0:
        return 0.0
    x = np.sort(x)
    n = x.size
    idx = np.arange(1, n + 1, dtype=np.float32)
    return float((np.sum((2 * idx - n - 1) * x)) / (n * np.sum(x)))


def _cosine_recon(h: np.ndarray, h_hat: np.ndarray) -> float:
    h = np.asarray(h, dtype=np.float32)
    h_hat = np.asarray(h_hat, dtype=np.float32)
    num = np.sum(h * h_hat, axis=1)
    den = np.linalg.norm(h, axis=1) * np.linalg.norm(h_hat, axis=1) + 1e-8
    return float(np.mean(num / den))


def _feature_correlation(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a_c = a - a.mean(axis=0, keepdims=True)
    b_c = b - b.mean(axis=0, keepdims=True)
    a_std = np.sqrt((a_c * a_c).mean(axis=0, keepdims=True) + 1e-8)
    b_std = np.sqrt((b_c * b_c).mean(axis=0, keepdims=True) + 1e-8)
    return (a_c / a_std).T @ (b_c / b_std) / a.shape[0]


def _greedy_match_score(corr: np.ndarray) -> float:
    mat = np.abs(corr).copy()
    n = min(mat.shape)
    score = 0.0
    for _ in range(n):
        flat_idx = int(np.argmax(mat))
        i, j = np.unravel_index(flat_idx, mat.shape)
        score += float(mat[i, j])
        mat[i, :] = -1.0
        mat[:, j] = -1.0
    return score / max(n, 1)


def fit_sae(
    states: np.ndarray,
    feature_dim: int = 64,
    k: int = 8,
    lr: float = 1e-2,
    steps: int = 600,
    batch_size: int = 128,
    l1_coeff: float = 1e-3,
    seed: int = 0,
) -> SAEModel:
    x = np.asarray(states, dtype=np.float32)
    if x.ndim != 2:
        raise ValueError("states must be [N, D]")
    n, d = x.shape
    if n < 2:
        raise ValueError("need at least 2 state rows")
    if feature_dim < 1:
        raise ValueError("feature_dim must be > 0")
    if k < 1:
        raise ValueError("k must be > 0")

    g = torch.Generator(device="cpu").manual_seed(int(seed))
    xt = torch.tensor(x, dtype=torch.float32)
    w_enc = torch.nn.Parameter(0.02 * torch.randn(d, feature_dim, generator=g))
    b_enc = torch.nn.Parameter(torch.zeros(feature_dim))
    w_dec = torch.nn.Parameter(0.02 * torch.randn(feature_dim, d, generator=g))
    b_dec = torch.nn.Parameter(torch.zeros(d))
    opt = torch.optim.Adam([w_enc, b_enc, w_dec, b_dec], lr=float(lr))

    for _ in range(int(steps)):
        idx = torch.randint(0, n, size=(min(batch_size, n),), generator=g)
        batch = xt[idx]
        pre = torch.relu(batch @ w_enc + b_enc)
        mask = _topk_mask(pre, k=int(min(k, feature_dim)))
        act = pre * mask
        recon = act @ w_dec + b_dec
        mse = torch.mean((recon - batch) ** 2)
        l1 = torch.mean(torch.abs(act))
        loss = mse + float(l1_coeff) * l1
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()

    return SAEModel(
        state_dim=d,
        feature_dim=feature_dim,
        k=int(min(k, feature_dim)),
        w_enc=w_enc.detach().cpu().numpy().astype(np.float32),
        b_enc=b_enc.detach().cpu().numpy().astype(np.float32),
        w_dec=w_dec.detach().cpu().numpy().astype(np.float32),
        b_dec=b_dec.detach().cpu().numpy().astype(np.float32),
    )


def sae_metrics(states: np.ndarray, sae: SAEModel, dead_eps: float = 1e-5) -> Dict[str, float]:
    h = np.asarray(states, dtype=np.float32)
    a = sae.encode(h)
    h_hat = sae.decode(a)
    nnz = np.sum(np.abs(a) > 0.0, axis=1)
    dead_rate = np.mean(np.mean(np.abs(a), axis=0) < dead_eps)
    return {
        "recon_mse": float(np.mean((h - h_hat) ** 2)),
        "recon_cosine": _cosine_recon(h, h_hat),
        "mean_nnz": float(np.mean(nnz)),
        "mean_abs_a": float(np.mean(np.abs(a))),
        "gini_abs_a": _gini_nonneg(a),
        "dead_feature_frac": float(dead_rate),
    }


def sae_stability(states: np.ndarray, config: Dict[str, Any], seed_a: int, seed_b: int) -> Dict[str, float]:
    sae_a = fit_sae(states, seed=seed_a, **config)
    sae_b = fit_sae(states, seed=seed_b, **config)
    a1 = sae_a.encode(states)
    a2 = sae_b.encode(states)
    corr = _feature_correlation(a1, a2)
    return {"mean_abs_feature_match_corr": float(_greedy_match_score(corr))}


def _load_all_states(summary_json: Path) -> np.ndarray:
    chunks = []
    for trace_path in load_trace_paths(summary_json):
        chunks.append(load_trace_states(trace_path))
    if not chunks:
        raise ValueError(f"No trace files listed in {summary_json}")
    return np.concatenate(chunks, axis=0).astype(np.float32)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fit a TopK SAE on TRM states and emit feature metrics.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, default=Path("tools/bench/out/sae_metrics.json"))
    parser.add_argument("--feature-dim", type=int, default=64)
    parser.add_argument("--k", type=int, default=8)
    parser.add_argument("--train-steps", type=int, default=600)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-2)
    parser.add_argument("--l1", type=float, default=1e-3)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--stability-seed-b", type=int, default=1)
    parser.add_argument("--save-model-json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    states = _load_all_states(args.summary_json)
    fit_cfg = {
        "feature_dim": int(args.feature_dim),
        "k": int(args.k),
        "lr": float(args.lr),
        "steps": int(args.train_steps),
        "batch_size": int(args.batch_size),
        "l1_coeff": float(args.l1),
    }
    sae = fit_sae(states, seed=int(args.seed), **fit_cfg)
    payload = {
        "num_states": int(states.shape[0]),
        "state_dim": int(states.shape[1]),
        "sae_config": {
            "feature_dim": int(args.feature_dim),
            "k": int(args.k),
            "train_steps": int(args.train_steps),
            "batch_size": int(args.batch_size),
            "lr": float(args.lr),
            "l1": float(args.l1),
            "seed": int(args.seed),
        },
        "metrics": sae_metrics(states, sae),
        "stability": sae_stability(states, fit_cfg, seed_a=int(args.seed), seed_b=int(args.stability_seed_b)),
    }
    write_json(args.out_json, payload)
    if args.save_model_json is not None:
        write_json(args.save_model_json, sae.to_dict())
    print(f"Wrote SAE metrics: {args.out_json}")


if __name__ == "__main__":
    main()
