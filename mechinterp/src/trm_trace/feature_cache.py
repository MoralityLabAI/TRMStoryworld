from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

from analysis.common import write_json
from analysis.sae import SAEModel
from trm_trace.trace import TraceReader


def _to_array(h: Any) -> np.ndarray:
    return np.asarray(h, dtype=np.float32)


def compute_feature_cache(trace_path: Path, sae: SAEModel, top_n: int = 6) -> Dict[str, Any]:
    steps = list(TraceReader(trace_path).iter_steps())
    acts: List[np.ndarray] = []
    events: List[Dict[str, Any]] = []
    prev = None
    for step in steps:
        a = sae.encode(_to_array(step["h"]))
        acts.append(a.astype(np.float32))
        top_idx = np.argsort(np.abs(a))[-min(top_n, a.shape[0]) :][::-1]
        row = {"t": int(step["t"]), "top_features": [int(i) for i in top_idx.tolist()]}
        if prev is not None:
            delta = np.abs(a - prev)
            burst_idx = np.argsort(delta)[-min(top_n, delta.shape[0]) :][::-1]
            row["burst_features"] = [int(i) for i in burst_idx.tolist()]
        events.append(row)
        prev = a

    act_arr = np.stack(acts, axis=0) if acts else np.zeros((0, sae.feature_dim), dtype=np.float32)
    return {
        "trace_path": str(trace_path),
        "num_steps": int(len(steps)),
        "feature_dim": int(sae.feature_dim),
        "k": int(sae.k),
        "activations": act_arr.tolist(),
        "events": events,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cache per-step SAE features for a trace.")
    parser.add_argument("--trace", type=Path, required=True)
    parser.add_argument("--sae-model-json", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--top-n", type=int, default=6)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model_payload: Dict[str, Any]
    with open(args.sae_model_json, "r", encoding="utf-8") as fh:
        import json

        model_payload = json.load(fh)
    sae = SAEModel.from_dict(model_payload)
    cache = compute_feature_cache(args.trace, sae=sae, top_n=int(args.top_n))
    write_json(args.out_json, cache)
    print(f"Wrote feature cache: {args.out_json}")


if __name__ == "__main__":
    main()
