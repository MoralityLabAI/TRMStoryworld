#!/usr/bin/env python3
"""Plot summary charts for rollout batch outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--batch-summary", type=str, required=True)
    p.add_argument("--out-dir", type=str, default="tools/bench/out")
    return p.parse_args()


def _top_outcome(summary_path: Path) -> Tuple[str, int]:
    data = json.loads(summary_path.read_text(encoding="utf-8"))
    adapter = data.get("adapter") or {}
    base = data.get("base") or {}
    outcomes: Dict[str, int] = (adapter.get("outcomes") or {}) if adapter else (base.get("outcomes") or {})
    if not outcomes:
        return ("none", 0)
    key, count = sorted(outcomes.items(), key=lambda kv: (-kv[1], kv[0]))[0]
    return (key, int(count))


def _fft_peak(summary_path: Path) -> Tuple[float, float]:
    data = json.loads(summary_path.read_text(encoding="utf-8"))
    evidence = data.get("evidence_paths") or {}
    fft_path = str(evidence.get("adapter_fft") or evidence.get("base_fft") or "")
    if not fft_path:
        return (0.0, 0.0)
    p = Path(fft_path)
    if not p.exists():
        return (0.0, 0.0)
    try:
        fft_obj = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return (0.0, 0.0)
    peaks = fft_obj.get("top_peaks") or []
    if not peaks:
        return (0.0, 0.0)
    top = peaks[0] if isinstance(peaks[0], dict) else {}
    freq = float(top.get("freq", 0.0) or 0.0)
    mag = float(top.get("magnitude", 0.0) or 0.0)
    return (freq, mag)


def main() -> int:
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    batch = json.loads(Path(args.batch_summary).read_text(encoding="utf-8"))
    rows: List[Dict] = batch.get("rows", [])
    if not rows:
        raise ValueError("batch summary has no rows")

    worlds = [r["world_id"] for r in rows]
    steps = [int(r.get("adapter_steps", 0)) for r in rows]
    rss = [float(r.get("rss_mb", 0.0)) for r in rows]
    top_labels: List[str] = []
    top_counts: List[int] = []
    fft_peak_freq: List[float] = []
    fft_peak_mag: List[float] = []
    for r in rows:
        summary_path = Path(r["summary_path"])
        outcome, count = _top_outcome(summary_path)
        top_labels.append(outcome)
        top_counts.append(count)
        freq, mag = _fft_peak(summary_path)
        fft_peak_freq.append(freq)
        fft_peak_mag.append(mag)

    if all(s == 0 for s in steps):
        # Base-only runs report 0 adapter steps; recover from per-world summaries.
        recovered: List[int] = []
        for r in rows:
            s = json.loads(Path(r["summary_path"]).read_text(encoding="utf-8"))
            base_steps = int(((s.get("base") or {}).get("steps", 0)) or 0)
            recovered.append(base_steps)
        steps = recovered

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(worlds, steps)
    ax.set_title("Steps per Storyworld")
    ax.set_xlabel("Storyworld")
    ax.set_ylabel("Steps")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(out_dir / "rollout_adapter_steps.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(worlds, rss)
    ax.set_title("RSS Memory (MB) by Storyworld")
    ax.set_xlabel("Storyworld")
    ax.set_ylabel("RSS MB")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(out_dir / "rollout_rss_mb.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(worlds, top_counts)
    ax.set_title("Top Outcome Frequency")
    ax.set_xlabel("Storyworld")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(out_dir / "rollout_top_outcome_count.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(worlds, fft_peak_freq)
    ax.set_title("FFT Peak Frequency by Storyworld")
    ax.set_xlabel("Storyworld")
    ax.set_ylabel("Peak Frequency")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(out_dir / "rollout_fft_peak_freq.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(worlds, fft_peak_mag)
    ax.set_title("FFT Peak Magnitude by Storyworld")
    ax.set_xlabel("Storyworld")
    ax.set_ylabel("Peak Magnitude")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(out_dir / "rollout_fft_peak_mag.png", dpi=150)
    plt.close(fig)

    print(json.dumps({"plots": [
        str(out_dir / "rollout_adapter_steps.png"),
        str(out_dir / "rollout_rss_mb.png"),
        str(out_dir / "rollout_top_outcome_count.png"),
        str(out_dir / "rollout_fft_peak_freq.png"),
        str(out_dir / "rollout_fft_peak_mag.png"),
    ]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
