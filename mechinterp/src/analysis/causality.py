from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch

from runner.synthetic import ToyTRM, build_synthetic_tasks, run_episode, set_global_seed
from trm_trace.interventions import patch_features, patch_state

from .common import write_json
from .sae import fit_sae


def _load_summary(path: Path) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _make_state_patch_intervention(donor_trace: Dict[str, Any], t_patch: int):
    def intervention(t: int, state: torch.Tensor, aux: Dict[str, torch.Tensor]):
        if t != t_patch:
            return state, aux, {}
        # patch_state expects a step list indexed by t; wrapping as single-step traces keeps runtime hot-path simple.
        trace_a = {"steps": [{"h": state.detach().cpu().numpy()}]}
        trace_b = {"steps": [{"h": donor_trace["steps"][t_patch]["h"]}]}
        patched_np, patch_log = patch_state(trace_a, trace_b, t=0)
        patched_state = torch.tensor(patched_np, dtype=state.dtype)
        return patched_state, aux, patch_log

    return intervention


def _top_feature_ids(sae: Any, donor_h: np.ndarray, target_h: np.ndarray, k: int) -> np.ndarray:
    a_donor = np.asarray(sae.encode(donor_h), dtype=np.float32)
    a_target = np.asarray(sae.encode(target_h), dtype=np.float32)
    diff = np.abs(a_donor - a_target)
    n = int(min(max(k, 1), diff.shape[0]))
    return np.argsort(diff)[-n:]


def _make_feature_patch_intervention(
    sae: Any,
    donor_trace: Dict[str, Any],
    feature_ids: np.ndarray,
    t_patch: int,
):
    ids = [int(i) for i in feature_ids.tolist()]

    def intervention(t: int, state: torch.Tensor, aux: Dict[str, torch.Tensor]):
        if t != t_patch:
            return state, aux, {}
        donor_h = np.asarray(donor_trace["steps"][t_patch]["h"], dtype=np.float32)
        patched, log = patch_features(target_state=state, donor_state=donor_h, sae=sae, feature_ids=ids)
        return patched, aux, log

    return intervention


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Estimate causal effects from state and SAE feature patching.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, default=Path("tools/bench/out/causality.json"))
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--feature-dim", type=int, default=64)
    parser.add_argument("--sae-k", type=int, default=8)
    parser.add_argument("--feature-patch-k", type=int, default=6)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary_rows = _load_summary(args.summary_json)
    set_global_seed(args.seed)
    rng = np.random.default_rng(args.seed)

    model = ToyTRM()
    tasks = build_synthetic_tasks(num_tasks=len(summary_rows), seed=args.seed)
    by_task_id = {task["task_id"]: task for task in tasks}
    failures = [row for row in summary_rows if int(row["final_correct"]) == 0]
    corrects = [row for row in summary_rows if int(row["final_correct"]) == 1]

    if not failures or not corrects:
        payload = {
            "num_failures": len(failures),
            "num_correct": len(corrects),
            "step_effect_curves": {},
            "note": "Need at least one failed and one correct trajectory to run patching.",
        }
        write_json(args.out_json, payload)
        print(f"Wrote causality analysis: {args.out_json}")
        return

    donor_id = corrects[0]["task_id"]
    donor_task = by_task_id[donor_id]
    donor_trace = run_episode(model=model, task=donor_task, steps=args.steps)

    base_fail_traces: Dict[str, Dict[str, Any]] = {}
    all_states = []
    for row in failures + corrects:
        task = by_task_id[row["task_id"]]
        trace = run_episode(model=model, task=task, steps=args.steps)
        all_states.extend([np.asarray(s["h"], dtype=np.float32) for s in trace["steps"]])
        if row in failures:
            base_fail_traces[row["task_id"]] = trace

    sae = fit_sae(
        np.stack(all_states, axis=0),
        feature_dim=int(args.feature_dim),
        k=int(args.sae_k),
        seed=int(args.seed),
    )

    modes = ("full_state_patch", "topk_feature_patch", "random_feature_patch")
    flips_by_mode_step = {mode: {t: 0 for t in range(args.steps)} for mode in modes}
    corr_by_mode_step = {mode: {t: [] for t in range(args.steps)} for mode in modes}
    delta_by_mode_step = {mode: {t: [] for t in range(args.steps)} for mode in modes}

    for fail_row in failures:
        task = by_task_id[fail_row["task_id"]]
        base = base_fail_traces[fail_row["task_id"]]
        base_correct = int(base["final_correct"])
        for t in range(args.steps):
            full = run_episode(model=model, task=task, steps=args.steps, intervention=_make_state_patch_intervention(donor_trace, t))
            full_correct = int(full["final_correct"])
            if base_correct == 0 and full_correct == 1:
                flips_by_mode_step["full_state_patch"][t] += 1
            corr_by_mode_step["full_state_patch"][t].append(float(full_correct))
            delta_by_mode_step["full_state_patch"][t].append(
                float(full["steps"][t]["metrics"].get("intervention", {}).get("delta_l2", 0.0))
            )

            target_h = np.asarray(base["steps"][t]["h"], dtype=np.float32)
            donor_h = np.asarray(donor_trace["steps"][t]["h"], dtype=np.float32)
            feat_ids = _top_feature_ids(sae=sae, donor_h=donor_h, target_h=target_h, k=int(args.feature_patch_k))
            topk = run_episode(
                model=model,
                task=task,
                steps=args.steps,
                intervention=_make_feature_patch_intervention(sae=sae, donor_trace=donor_trace, feature_ids=feat_ids, t_patch=t),
            )
            topk_correct = int(topk["final_correct"])
            if base_correct == 0 and topk_correct == 1:
                flips_by_mode_step["topk_feature_patch"][t] += 1
            corr_by_mode_step["topk_feature_patch"][t].append(float(topk_correct))
            delta_by_mode_step["topk_feature_patch"][t].append(
                float(topk["steps"][t]["metrics"].get("intervention", {}).get("delta_l2", 0.0))
            )

            feat_count = int(feat_ids.shape[0])
            random_ids = rng.choice(sae.feature_dim, size=min(feat_count, sae.feature_dim), replace=False)
            rand = run_episode(
                model=model,
                task=task,
                steps=args.steps,
                intervention=_make_feature_patch_intervention(sae=sae, donor_trace=donor_trace, feature_ids=random_ids, t_patch=t),
            )
            rand_correct = int(rand["final_correct"])
            if base_correct == 0 and rand_correct == 1:
                flips_by_mode_step["random_feature_patch"][t] += 1
            corr_by_mode_step["random_feature_patch"][t].append(float(rand_correct))
            delta_by_mode_step["random_feature_patch"][t].append(
                float(rand["steps"][t]["metrics"].get("intervention", {}).get("delta_l2", 0.0))
            )

    num_failures = len(failures)
    curves: Dict[str, Dict[str, float]] = {}
    for mode in modes:
        curves[mode] = {str(t): float(flips_by_mode_step[mode][t] / num_failures) for t in range(args.steps)}

    effect_size: Dict[str, Dict[str, float]] = {}
    for mode in modes:
        effect_size[mode] = {
            str(t): float(np.mean(corr_by_mode_step[mode][t]) - 0.0) if corr_by_mode_step[mode][t] else 0.0 for t in range(args.steps)
        }

    mean_delta_full = np.mean([d for vals in delta_by_mode_step["full_state_patch"].values() for d in vals]) + 1e-6
    mean_flip_topk = np.mean(list(curves["topk_feature_patch"].values()))
    rsi_topk_vs_full = float(mean_flip_topk / mean_delta_full)

    payload = {
        "num_failures": num_failures,
        "num_correct": len(corrects),
        "donor_task_id": donor_id,
        "sae_config": {"feature_dim": int(args.feature_dim), "sae_k": int(args.sae_k), "feature_patch_k": int(args.feature_patch_k)},
        "step_effect_curves": curves,
        "step_effect_size_on_final_correct": effect_size,
        "rsi_topk_vs_full": rsi_topk_vs_full,
    }
    write_json(args.out_json, payload)
    print(f"Wrote causality analysis: {args.out_json}")


if __name__ == "__main__":
    main()
