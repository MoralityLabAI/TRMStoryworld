#!/usr/bin/env python3
"""Evaluate controller prompts (PICK k) on SFT JSONL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from model_utils import controller_from_args, parse_pick, parse_target_pick


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, help="SFT JSONL with input/target.")
    parser.add_argument("--model-path", type=str, default="", help="HF base model path. Empty => heuristic.")
    parser.add_argument("--adapter-path", type=str, default="", help="Optional PEFT adapter path.")
    parser.add_argument("--device", type=str, default="auto", help='Transformers device_map, e.g. "auto" or "cpu".')
    parser.add_argument("--dtype", type=str, default="auto", choices=["auto", "float16", "bfloat16", "float32"])
    parser.add_argument("--max-new-tokens", type=int, default=8)
    parser.add_argument("--out", type=str, default="tools/bench/out/eval_summary.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dataset = Path(args.dataset)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    controller = controller_from_args(
        model_path=(args.model_path or None),
        adapter_path=(args.adapter_path or None),
        device=args.device,
        dtype=args.dtype,
    )

    total = 0
    valid = 0
    correct = 0
    invalid = 0
    token_sum = 0
    samples: List[Dict[str, Any]] = []
    for idx, row in enumerate(iter_jsonl(dataset)):
        prompt = row.get("input")
        target = row.get("target")
        if not isinstance(prompt, str) or not isinstance(target, str):
            continue
        total += 1
        truth = parse_target_pick(target)
        pred = controller.predict(prompt, max_new_tokens=args.max_new_tokens)
        token_sum += pred.tokens
        pick = parse_pick(pred.text)
        if pick is None:
            invalid += 1
        else:
            valid += 1
            if truth is not None and pick == truth:
                correct += 1
        if len(samples) < 10:
            samples.append(
                {
                    "row": idx,
                    "target": truth,
                    "pred_text": pred.text,
                    "pred_pick": pick,
                    "tokens": pred.tokens,
                }
            )

    summary = {
        "dataset": str(dataset),
        "rows_evaluated": total,
        "top1_accuracy": (correct / total if total else 0.0),
        "valid_output_rate": (valid / total if total else 0.0),
        "invalid_output_rate": (invalid / total if total else 0.0),
        "avg_tokens": (token_sum / total if total else 0.0),
        "model_path": args.model_path or "heuristic",
        "adapter_path": args.adapter_path or "",
        "samples": samples,
    }
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
