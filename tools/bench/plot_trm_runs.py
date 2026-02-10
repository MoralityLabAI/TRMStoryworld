#!/usr/bin/env python3
"""Plot aggregated TRM run metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agg-json", type=str, required=True)
    parser.add_argument("--out-dir", type=str, default="tools/bench/out")
    return parser.parse_args()


def load_runs(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    runs = data.get("runs", [])
    return runs if isinstance(runs, list) else []


def ensure_matplotlib():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return plt


def _curve_points(run: Dict[str, Any]) -> Tuple[List[int], List[float]]:
    xs: List[int] = []
    ys: List[float] = []
    for item in run.get("loss_curve", []) or []:
        if not isinstance(item, list) and not isinstance(item, tuple):
            continue
        if len(item) != 2:
            continue
        step, loss = item
        if isinstance(step, int) and isinstance(loss, (int, float)):
            xs.append(step)
            ys.append(float(loss))
    return xs, ys


def plot_loss_vs_step(plt, runs: List[Dict[str, Any]], out_path: Path) -> None:
    plt.figure(figsize=(10, 6))
    drawn = 0
    for run in runs:
        xs, ys = _curve_points(run)
        if not xs:
            continue
        label = str(run.get("run_id", f"run_{drawn}"))
        plt.plot(xs, ys, label=label, linewidth=1.5, alpha=0.9)
        drawn += 1
    plt.title("TRM Loss vs Step")
    plt.xlabel("Step")
    plt.ylabel("Loss")
    plt.grid(alpha=0.2)
    if drawn:
        plt.legend(fontsize=8, loc="best")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


def plot_peak_ram(plt, runs: List[Dict[str, Any]], out_path: Path) -> None:
    labels: List[str] = []
    vals: List[float] = []
    for run in runs:
        peak = run.get("peak_ram")
        if isinstance(peak, (int, float)):
            labels.append(str(run.get("run_id", "run")))
            vals.append(float(peak))
    plt.figure(figsize=(10, 6))
    if labels:
        plt.bar(labels, vals)
        plt.xticks(rotation=40, ha="right")
    plt.title("Peak RAM by Run")
    plt.ylabel("RAM (GB or reported units)")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


def plot_throughput(plt, runs: List[Dict[str, Any]], out_path: Path) -> None:
    labels: List[str] = []
    vals: List[float] = []
    ylab = "steps/sec"
    for run in runs:
        run_id = str(run.get("run_id", "run"))
        sps = run.get("steps_per_sec")
        tps = run.get("tokens_per_sec")
        if isinstance(tps, (int, float)):
            labels.append(run_id)
            vals.append(float(tps))
            ylab = "tokens/sec"
        elif isinstance(sps, (int, float)):
            labels.append(run_id)
            vals.append(float(sps))
    plt.figure(figsize=(10, 6))
    if labels:
        plt.bar(labels, vals)
        plt.xticks(rotation=40, ha="right")
    plt.title("Throughput by Run")
    plt.ylabel(ylab)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


def main() -> int:
    args = parse_args()
    runs = load_runs(Path(args.agg_json))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    plt = ensure_matplotlib()

    p1 = out_dir / "loss_vs_step.png"
    p2 = out_dir / "peak_ram_vs_run.png"
    p3 = out_dir / "throughput_vs_run.png"
    plot_loss_vs_step(plt, runs, p1)
    plot_peak_ram(plt, runs, p2)
    plot_throughput(plt, runs, p3)
    print(json.dumps({"plots": [str(p1), str(p2), str(p3)], "runs": len(runs)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
