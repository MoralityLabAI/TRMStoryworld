from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch

from analysis.common import load_trace_states, write_json
from analysis.sae import SAEModel, fit_sae, sae_metrics
from runner.run_tasks import run_tasks
from runner.synthetic import ToyTRM, build_synthetic_tasks, run_episode, set_global_seed
from trm_trace.interventions import ablate_features, clamp_features, patch_features


def _load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True, ensure_ascii=True)


def _parse_csv_ints(raw: str | None) -> List[int]:
    if raw is None or raw.strip() == "":
        return []
    return [int(x.strip()) for x in raw.split(",") if x.strip() != ""]


def _parse_csv_floats(raw: str | None) -> List[float]:
    if raw is None or raw.strip() == "":
        return []
    return [float(x.strip()) for x in raw.split(",") if x.strip() != ""]


def _build_trace(args: argparse.Namespace) -> None:
    run_dir = args.run_dir
    traces_dir = run_dir / "traces"
    summary_path = run_tasks(
        out_dir=traces_dir,
        num_tasks=int(args.num_tasks),
        steps=int(args.steps),
        seed=int(args.seed),
        fmt="jsonl",
        compress=False,
    )
    rows = _load_json(summary_path)
    if not rows:
        raise ValueError("No traces were generated.")

    selected = rows[0]
    if args.task_id is not None:
        matches = [r for r in rows if r["task_id"] == args.task_id]
        if not matches:
            raise ValueError(f"task_id not found in summary: {args.task_id}")
        selected = matches[0]

    run_dir.mkdir(parents=True, exist_ok=True)
    out_summary = run_dir / "summary.json"
    shutil.copyfile(summary_path, out_summary)
    out_trace = run_dir / "trace.jsonl"
    shutil.copyfile(Path(selected["trace_path"]), out_trace)

    meta = {
        "seed": int(args.seed),
        "steps": int(args.steps),
        "num_tasks": int(args.num_tasks),
        "selected_task_id": selected["task_id"],
        "selected_trace_path": str(out_trace),
        "summary_path": str(out_summary),
    }
    write_json(run_dir / "trace_meta.json", meta)

    if args.states_npy:
        states = load_trace_states(out_trace)
        np.save(run_dir / "states.npy", states.astype(np.float32))

    print(f"Wrote trace: {out_trace}")
    print(f"Wrote summary: {out_summary}")


def _collect_states_from_summary(summary_json: Path) -> np.ndarray:
    rows = _load_json(summary_json)
    chunks = [load_trace_states(Path(row["trace_path"])) for row in rows]
    if not chunks:
        raise ValueError("No states found in summary.")
    return np.concatenate(chunks, axis=0).astype(np.float32)


def _sae_fit(args: argparse.Namespace) -> None:
    run_dir = args.run_dir
    if args.states_npy is not None:
        states = np.load(args.states_npy).astype(np.float32)
    else:
        summary_json = args.summary_json if args.summary_json is not None else (run_dir / "summary.json")
        states = _collect_states_from_summary(summary_json)

    sae = fit_sae(
        states,
        feature_dim=int(args.feature_dim),
        k=int(args.k),
        lr=float(args.lr),
        steps=int(args.train_steps),
        batch_size=int(args.batch_size),
        l1_coeff=float(args.l1),
        seed=int(args.seed),
    )

    run_dir.mkdir(parents=True, exist_ok=True)
    sae_payload = sae.to_dict()
    torch.save(sae_payload, run_dir / "sae.pt")
    metrics_payload = {
        "num_states": int(states.shape[0]),
        "state_dim": int(states.shape[1]),
        "metrics": sae_metrics(states, sae),
        "sae_config": {
            "feature_dim": int(args.feature_dim),
            "k": int(args.k),
            "lr": float(args.lr),
            "train_steps": int(args.train_steps),
            "batch_size": int(args.batch_size),
            "l1": float(args.l1),
            "seed": int(args.seed),
        },
    }
    write_json(run_dir / "sae_metrics.json", metrics_payload)
    print(f"Wrote SAE model: {run_dir / 'sae.pt'}")
    print(f"Wrote SAE metrics: {run_dir / 'sae_metrics.json'}")


def _topk_feature_ids(sae: SAEModel, donor_h: np.ndarray, target_h: np.ndarray, k: int) -> List[int]:
    a_donor = np.asarray(sae.encode(donor_h), dtype=np.float32)
    a_target = np.asarray(sae.encode(target_h), dtype=np.float32)
    diff = np.abs(a_donor - a_target)
    n = int(min(max(k, 1), diff.shape[0]))
    idx = np.argsort(diff)[-n:]
    return [int(i) for i in idx.tolist()]


def _load_sae(path: Path) -> SAEModel:
    payload = torch.load(path, map_location="cpu")
    if not isinstance(payload, dict):
        raise ValueError(f"Unexpected SAE payload in {path}")
    return SAEModel.from_dict(payload)


def _first_divergence_step(base_steps: List[Dict[str, Any]], new_steps: List[Dict[str, Any]]) -> int | None:
    max_len = min(len(base_steps), len(new_steps))
    for i in range(max_len):
        y_a = float(base_steps[i]["y"])
        y_b = float(new_steps[i]["y"])
        if abs(y_a - y_b) > 1e-6:
            return int(i)
    return None


def _intervene(args: argparse.Namespace) -> None:
    summary_json = args.summary_json if args.summary_json is not None else (args.run_dir / "summary.json")
    rows = _load_json(summary_json)
    if not rows:
        raise ValueError("summary.json has no rows")
    by_id = {row["task_id"]: row for row in rows}

    if args.task_id is None:
        task_id = rows[0]["task_id"]
    else:
        task_id = args.task_id
        if task_id not in by_id:
            raise ValueError(f"task_id not in summary: {task_id}")

    set_global_seed(int(args.seed))
    model = ToyTRM()
    tasks = build_synthetic_tasks(num_tasks=len(rows), seed=int(args.seed))
    task_map = {t["task_id"]: t for t in tasks}
    target_task = task_map[task_id]
    baseline = run_episode(model=model, task=target_task, steps=int(args.steps))

    donor_task_id = args.donor_task_id
    if donor_task_id is None:
        correct_rows = [r for r in rows if int(r["final_correct"]) == 1 and r["task_id"] != task_id]
        donor_task_id = correct_rows[0]["task_id"] if correct_rows else rows[0]["task_id"]
    donor_trace = run_episode(model=model, task=task_map[donor_task_id], steps=int(args.steps))

    sae_path = args.sae_pt if args.sae_pt is not None else (args.run_dir / "sae.pt")
    sae = _load_sae(sae_path)
    explicit_ids = _parse_csv_ints(args.feature_ids)
    explicit_values = _parse_csv_floats(args.values)
    t_patch = int(args.patch_step)
    donor_h = np.asarray(donor_trace["steps"][t_patch]["h"], dtype=np.float32)
    base_h = np.asarray(baseline["steps"][t_patch]["h"], dtype=np.float32)
    feature_ids = explicit_ids if explicit_ids else _topk_feature_ids(sae, donor_h=donor_h, target_h=base_h, k=int(args.top_k))

    def intervention(t: int, state: torch.Tensor, aux: Dict[str, torch.Tensor]):
        if t != t_patch:
            return state, aux, {}
        if args.policy == "ablate":
            patched, log = ablate_features(state=state, sae=sae, feature_ids=feature_ids)
            return patched, aux, log
        if args.policy == "clamp":
            values = explicit_values if explicit_values else [0.0 for _ in feature_ids]
            patched, log = clamp_features(state=state, sae=sae, feature_ids=feature_ids, values=values)
            return patched, aux, log
        patched, log = patch_features(state, donor_h, sae=sae, feature_ids=feature_ids)
        return patched, aux, log

    intervened = run_episode(model=model, task=target_task, steps=int(args.steps), intervention=intervention)

    diffs = []
    for i, (b, p) in enumerate(zip(baseline["steps"], intervened["steps"])):
        diffs.append(
            {
                "t": int(i),
                "y_delta": float(float(p["y"]) - float(b["y"])),
                "state_l2_delta": float(
                    np.linalg.norm(np.asarray(p["h"], dtype=np.float32) - np.asarray(b["h"], dtype=np.float32))
                ),
            }
        )

    report = {
        "baseline": {
            "task_id": task_id,
            "final_correct": int(baseline["final_correct"]),
            "final_y": float(baseline["steps"][-1]["y"]),
        },
        "intervened": {
            "task_id": task_id,
            "policy": args.policy,
            "donor_task_id": donor_task_id,
            "patch_step": t_patch,
            "feature_ids": feature_ids,
            "final_correct": int(intervened["final_correct"]),
            "final_y": float(intervened["steps"][-1]["y"]),
        },
        "delta": {
            "final_correct_delta": int(intervened["final_correct"]) - int(baseline["final_correct"]),
            "final_y_delta": float(float(intervened["steps"][-1]["y"]) - float(baseline["steps"][-1]["y"])),
        },
        "first_divergence_step": _first_divergence_step(baseline["steps"], intervened["steps"]),
        "top_causal_features": feature_ids,
    }

    args.run_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.run_dir / "report.json", report)
    write_json(args.run_dir / "intervention_diffs.json", {"diffs": diffs})
    print(f"Wrote report: {args.run_dir / 'report.json'}")
    print(f"Wrote intervention diffs: {args.run_dir / 'intervention_diffs.json'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TRMInterp wrapper: trace -> sae fit -> intervene")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_trace = sub.add_parser("trace", help="Run synthetic tasks and emit contract trace outputs.")
    p_trace.add_argument("--run-dir", type=Path, default=Path("tools/bench/out/trminterp"))
    p_trace.add_argument("--num-tasks", type=int, default=12)
    p_trace.add_argument("--steps", type=int, default=6)
    p_trace.add_argument("--seed", type=int, default=7)
    p_trace.add_argument("--task-id", type=str, default=None)
    p_trace.add_argument("--states-npy", action="store_true")

    p_sae = sub.add_parser("sae", help="SAE-related commands.")
    sub_sae = p_sae.add_subparsers(dest="sae_cmd", required=True)
    p_sae_fit = sub_sae.add_parser("fit", help="Fit SAE and emit sae.pt + sae_metrics.json.")
    p_sae_fit.add_argument("--run-dir", type=Path, default=Path("tools/bench/out/trminterp"))
    p_sae_fit.add_argument("--summary-json", type=Path, default=None)
    p_sae_fit.add_argument("--states-npy", type=Path, default=None)
    p_sae_fit.add_argument("--feature-dim", type=int, default=64)
    p_sae_fit.add_argument("--k", type=int, default=8)
    p_sae_fit.add_argument("--train-steps", type=int, default=600)
    p_sae_fit.add_argument("--batch-size", type=int, default=128)
    p_sae_fit.add_argument("--lr", type=float, default=1e-2)
    p_sae_fit.add_argument("--l1", type=float, default=1e-3)
    p_sae_fit.add_argument("--seed", type=int, default=0)

    p_int = sub.add_parser("intervene", help="Replay with feature interventions and emit report.")
    p_int.add_argument("--run-dir", type=Path, default=Path("tools/bench/out/trminterp"))
    p_int.add_argument("--summary-json", type=Path, default=None)
    p_int.add_argument("--sae-pt", type=Path, default=None)
    p_int.add_argument("--task-id", type=str, default=None)
    p_int.add_argument("--donor-task-id", type=str, default=None)
    p_int.add_argument("--seed", type=int, required=True)
    p_int.add_argument("--steps", type=int, default=6)
    p_int.add_argument("--patch-step", type=int, default=2)
    p_int.add_argument("--policy", choices=["patch", "ablate", "clamp"], default="patch")
    p_int.add_argument("--feature-ids", type=str, default=None, help="CSV feature ids. Defaults to top-k by donor-target activation gap.")
    p_int.add_argument("--values", type=str, default=None, help="CSV values for clamp policy.")
    p_int.add_argument("--top-k", type=int, default=6)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.cmd == "trace":
        _build_trace(args)
        return
    if args.cmd == "sae" and args.sae_cmd == "fit":
        _sae_fit(args)
        return
    if args.cmd == "intervene":
        _intervene(args)
        return
    raise ValueError("Unsupported command combination")


if __name__ == "__main__":
    main()
