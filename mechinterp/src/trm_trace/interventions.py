from __future__ import annotations

from typing import Any, Dict, Iterable, Tuple

import numpy as np

try:
    import torch
except Exception:  # pragma: no cover
    torch = None


def _clone(x: Any) -> Any:
    if torch is not None and isinstance(x, torch.Tensor):
        return x.clone()
    if isinstance(x, np.ndarray):
        return x.copy()
    if isinstance(x, list):
        return list(x)
    if isinstance(x, tuple):
        return tuple(x)
    if isinstance(x, dict):
        return {k: _clone(v) for k, v in x.items()}
    return x


def _to_array(x: Any) -> np.ndarray:
    if torch is not None and isinstance(x, torch.Tensor):
        return x.detach().cpu().numpy()
    return np.asarray(x, dtype=np.float32)


def _to_output(reference: Any, array: np.ndarray) -> Any:
    if torch is not None and isinstance(reference, torch.Tensor):
        return torch.tensor(array, dtype=reference.dtype, device=reference.device)
    return np.asarray(array, dtype=np.float32)


def patch_state(trace_a: Dict[str, Any], trace_b: Dict[str, Any], t: int) -> Tuple[Any, Dict[str, Any]]:
    """Return patched state from trace_b at step t with patch metadata."""
    step_a = trace_a["steps"][t]
    step_b = trace_b["steps"][t]
    patched = _clone(step_b["h"])
    delta = float(np.linalg.norm(_to_array(step_b["h"]) - _to_array(step_a["h"])))
    return patched, {"type": "patch_state", "t": int(t), "delta_l2": delta}


def add_direction(state: Any, v: Any, alpha: float) -> Tuple[Any, Dict[str, Any]]:
    if torch is not None and isinstance(state, torch.Tensor):
        direction = v if isinstance(v, torch.Tensor) else torch.tensor(v, dtype=state.dtype, device=state.device)
        out = state + float(alpha) * direction
        delta = float((out - state).norm().item())
        return out, {"type": "add_direction", "alpha": float(alpha), "delta_l2": delta}

    state_arr = _to_array(state)
    dir_arr = _to_array(v)
    out = state_arr + float(alpha) * dir_arr
    delta = float(np.linalg.norm(out - state_arr))
    return out, {"type": "add_direction", "alpha": float(alpha), "delta_l2": delta}


def ablate_aux(aux: Dict[str, Any], keys: Iterable[str]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    changed = []
    out = _clone(aux)
    for key in keys:
        if key in out:
            val = out[key]
            if torch is not None and isinstance(val, torch.Tensor):
                out[key] = torch.zeros_like(val)
            else:
                arr = _to_array(val)
                out[key] = np.zeros_like(arr)
            changed.append(key)
    return out, {"type": "ablate_aux", "keys": changed, "count": len(changed)}


def ablate_features(state: Any, sae: Any, feature_ids: Iterable[int]) -> Tuple[Any, Dict[str, Any]]:
    state_arr = _to_array(state)
    act = np.asarray(sae.encode(state_arr), dtype=np.float32).copy()
    ids = np.array(sorted({int(i) for i in feature_ids if int(i) >= 0}), dtype=np.int64)
    ids = ids[ids < act.shape[-1]]
    act_before = act.copy()
    if ids.size:
        act[..., ids] = 0.0
    patched = np.asarray(sae.decode(act), dtype=np.float32)
    delta = float(np.linalg.norm(patched - state_arr))
    changed = int(np.sum(np.abs(act_before - act) > 0.0))
    return _to_output(state, patched), {"type": "ablate_features", "count": changed, "delta_l2": delta}


def clamp_features(state: Any, sae: Any, feature_ids: Iterable[int], values: Iterable[float]) -> Tuple[Any, Dict[str, Any]]:
    state_arr = _to_array(state)
    act = np.asarray(sae.encode(state_arr), dtype=np.float32).copy()
    ids_list = [int(i) for i in feature_ids]
    vals_list = [float(v) for v in values]
    if len(ids_list) != len(vals_list):
        raise ValueError("feature_ids and values must have equal length")
    changed = 0
    for fid, val in zip(ids_list, vals_list):
        if 0 <= fid < act.shape[-1]:
            act[..., fid] = val
            changed += 1
    patched = np.asarray(sae.decode(act), dtype=np.float32)
    delta = float(np.linalg.norm(patched - state_arr))
    return _to_output(state, patched), {"type": "clamp_features", "count": changed, "delta_l2": delta}


def patch_features(target_state: Any, donor_state: Any, sae: Any, feature_ids: Iterable[int]) -> Tuple[Any, Dict[str, Any]]:
    tgt = _to_array(target_state)
    donor = _to_array(donor_state)
    a_tgt = np.asarray(sae.encode(tgt), dtype=np.float32).copy()
    a_donor = np.asarray(sae.encode(donor), dtype=np.float32)
    ids = np.array(sorted({int(i) for i in feature_ids if int(i) >= 0}), dtype=np.int64)
    ids = ids[ids < a_tgt.shape[-1]]
    changed = 0
    if ids.size:
        a_tgt[..., ids] = a_donor[..., ids]
        changed = int(ids.size)
    patched = np.asarray(sae.decode(a_tgt), dtype=np.float32)
    delta = float(np.linalg.norm(patched - tgt))
    return _to_output(target_state, patched), {"type": "patch_features", "count": changed, "delta_l2": delta}
