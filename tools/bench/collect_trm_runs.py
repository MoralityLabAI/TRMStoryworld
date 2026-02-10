#!/usr/bin/env python3
"""Collect TRM run artifacts into an aggregated table."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = line.strip()
            if not row:
                continue
            try:
                yield json.loads(row)
            except json.JSONDecodeError:
                continue


def safe_num(value: Any) -> Optional[float]:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    return None


def read_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def epoch_to_iso(ts: Optional[float]) -> str:
    if ts is None:
        return ""
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.isoformat()


def find_trainer_state(summary_path: Path) -> Optional[Path]:
    parent = summary_path.parent
    stem = summary_path.name.replace("_summary.json", "")
    candidates = [
        parent / f"{stem}_trainer_state.json",
        parent / "trainer_state.json",
    ]
    for c in candidates:
        if c.exists():
            return c
    nearby = sorted(parent.glob("*trainer*state*.json"))
    return nearby[0] if nearby else None


def find_events_path(summary_path: Path) -> Optional[Path]:
    parent = summary_path.parent
    stem = summary_path.name.replace("_summary.json", "")
    candidates = [
        parent / f"{stem}_events.jsonl",
        parent / f"{stem}_traces.jsonl",
        parent / f"{stem}.events.jsonl",
    ]
    for c in candidates:
        if c.exists():
            return c
    nearby = sorted(parent.glob("*events*.jsonl")) + sorted(parent.glob("*traces*.jsonl"))
    return nearby[0] if nearby else None


def extract_loss_curve_from_trainer(trainer_state: Dict[str, Any]) -> List[Tuple[int, float]]:
    curve: List[Tuple[int, float]] = []
    for row in trainer_state.get("log_history", []) or []:
        step = row.get("step")
        loss = row.get("loss")
        if isinstance(step, int) and isinstance(loss, (int, float)):
            curve.append((step, float(loss)))
    curve.sort(key=lambda x: x[0])
    return curve


def extract_metrics_from_events(events_path: Optional[Path]) -> Dict[str, Any]:
    if events_path is None or not events_path.exists():
        return {
            "steps": None,
            "peak_ram": None,
            "avg_ram": None,
            "steps_per_sec": None,
            "tokens_per_sec": None,
            "loss_curve": [],
        }
    ram_vals: List[float] = []
    steps_per_sec: List[float] = []
    tokens_per_sec: List[float] = []
    losses: List[Tuple[int, float]] = []
    max_step = -1
    for row in iter_jsonl(events_path):
        step = row.get("step")
        if isinstance(step, int):
            max_step = max(max_step, step)
        for key in ("ram_gb", "ram", "memory_gb", "peak_ram_gb"):
            v = safe_num(row.get(key))
            if v is not None:
                ram_vals.append(v)
                break
        sps = safe_num(row.get("steps_per_sec") or row.get("steps/s"))
        if sps is not None:
            steps_per_sec.append(sps)
        tps = safe_num(row.get("tokens_per_sec") or row.get("tokens/s"))
        if tps is not None:
            tokens_per_sec.append(tps)
        loss = safe_num(row.get("loss"))
        if isinstance(step, int) and loss is not None:
            losses.append((step, loss))
    losses.sort(key=lambda x: x[0])
    return {
        "steps": (max_step + 1) if max_step >= 0 else None,
        "peak_ram": (max(ram_vals) if ram_vals else None),
        "avg_ram": (sum(ram_vals) / len(ram_vals) if ram_vals else None),
        "steps_per_sec": (sum(steps_per_sec) / len(steps_per_sec) if steps_per_sec else None),
        "tokens_per_sec": (sum(tokens_per_sec) / len(tokens_per_sec) if tokens_per_sec else None),
        "loss_curve": losses,
    }


def aggregate_one(summary_path: Path) -> Dict[str, Any]:
    summary = read_json(summary_path)
    events_path = find_events_path(summary_path)
    trainer_path = find_trainer_state(summary_path)
    trainer_state = read_json(trainer_path) if trainer_path else {}

    run_id = str(summary.get("run_id") or summary_path.name.replace("_summary.json", ""))
    dt = summary.get("datetime") or summary.get("started_at") or summary.get("timestamp") or ""
    if not dt:
        dt = epoch_to_iso(summary_path.stat().st_mtime)

    metrics = extract_metrics_from_events(events_path)
    trainer_curve = extract_loss_curve_from_trainer(trainer_state)
    curve = metrics["loss_curve"] or trainer_curve

    steps = summary.get("steps")
    if not isinstance(steps, int):
        steps = metrics["steps"] or trainer_state.get("global_step")

    peak_ram = safe_num(summary.get("peak_ram") or summary.get("peak_ram_gb")) or metrics["peak_ram"]
    avg_ram = safe_num(summary.get("avg_ram") or summary.get("avg_ram_gb")) or metrics["avg_ram"]
    loss_start = curve[0][1] if curve else safe_num(summary.get("loss_start"))
    loss_end = curve[-1][1] if curve else safe_num(summary.get("loss_end"))
    dataset_id = (
        summary.get("dataset_id")
        or summary.get("swmd_hash")
        or summary.get("meta", {}).get("swmd_hash")
        or ""
    )
    git_commit = summary.get("git_commit") or summary.get("commit") or ""
    row = {
        "run_id": run_id,
        "datetime": dt,
        "summary_path": str(summary_path),
        "events_path": "" if events_path is None else str(events_path),
        "trainer_state_path": "" if trainer_path is None else str(trainer_path),
        "steps": steps,
        "peak_ram": peak_ram,
        "avg_ram": avg_ram,
        "loss_start": loss_start,
        "loss_end": loss_end,
        "dataset_id": dataset_id,
        "git_commit": git_commit,
        "steps_per_sec": metrics["steps_per_sec"],
        "tokens_per_sec": metrics["tokens_per_sec"],
        "loss_curve": curve,
    }
    return row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--logs-root", type=str, required=True)
    parser.add_argument("--out-json", type=str, default="tools/bench/out/trm_runs_agg.json")
    parser.add_argument("--out-csv", type=str, default="tools/bench/out/trm_runs_agg.csv")
    parser.add_argument(
        "--pattern",
        type=str,
        default="*summary.json",
        help="Glob pattern under logs-root (default includes hrm_trm-*_summary.json and others).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.logs_root)
    out_json = Path(args.out_json)
    out_csv = Path(args.out_csv)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    summaries = sorted(root.rglob(args.pattern))
    runs = [aggregate_one(path) for path in summaries]
    runs.sort(key=lambda r: (r.get("datetime") or "", r.get("run_id") or ""))

    out_json.write_text(json.dumps({"runs": runs}, indent=2), encoding="utf-8")

    fields = [
        "run_id",
        "datetime",
        "steps",
        "peak_ram",
        "avg_ram",
        "loss_start",
        "loss_end",
        "steps_per_sec",
        "tokens_per_sec",
        "dataset_id",
        "git_commit",
        "summary_path",
        "events_path",
        "trainer_state_path",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in runs:
            writer.writerow({k: row.get(k, "") for k in fields})

    print(json.dumps({"runs": len(runs), "out_json": str(out_json), "out_csv": str(out_csv)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
