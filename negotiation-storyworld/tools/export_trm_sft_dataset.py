#!/usr/bin/env python3
"""Export TRM SW1 traces into SFT-ready JSONL rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable


def iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = line.strip()
            if not row:
                continue
            yield json.loads(row)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace-log", type=str, required=True)
    parser.add_argument("--out", type=str, default="logs/trm_sw1_sft.jsonl")
    parser.add_argument("--include-k", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    trace_path = Path(args.trace_log)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows_out = 0
    with out_path.open("w", encoding="utf-8") as handle:
        for row in iter_jsonl(trace_path):
            prompt = row.get("prompt")
            label = row.get("label")
            k_label = row.get("k_label")
            if not isinstance(prompt, str) or not isinstance(label, str):
                continue
            target = label if not args.include_k or not isinstance(k_label, str) else f"{label}\n{k_label}"
            out_row = {
                "input": prompt,
                "target": target,
                "meta": {
                    "episode": row.get("episode"),
                    "turn": row.get("turn"),
                    "state_hash": row.get("state_hash"),
                    "receipt_leaf": row.get("receipt_leaf"),
                },
            }
            handle.write(json.dumps(out_row, ensure_ascii=False) + "\n")
            rows_out += 1

    print(json.dumps({"rows": rows_out, "out": str(out_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
