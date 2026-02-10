#!/usr/bin/env python3
"""Evaluate controller prompts (PICK k) on SFT JSONL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from identity_utils import git_commit, make_run_identity, sha256_hex, stable_json
from model_utils import controller_from_args, memory_snapshot, parse_pick, parse_target_pick


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
    parser.add_argument("--device", type=str, default="cpu", help='Transformers device_map, e.g. "auto" or "cpu".')
    parser.add_argument("--dtype", type=str, default="auto", choices=["auto", "float16", "bfloat16", "float32"])
    parser.add_argument("--max-new-tokens", type=int, default=8)
    parser.add_argument("--max-rows", type=int, default=0, help="Optional cap for quick eval (0 = all rows).")
    parser.add_argument("--heartbeat-rows", type=int, default=250, help="Emit memory heartbeat every N evaluated rows (0=off).")
    parser.add_argument("--out", type=str, default="tools/bench/out/eval_summary.json")
    parser.add_argument("--swmd-hash", type=str, default="")
    parser.add_argument("--builder-git-commit", type=str, default="")
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
    import hashlib

    dataset_hasher = hashlib.sha256()
    leaf_hashes: List[str] = []
    for idx, row in enumerate(iter_jsonl(dataset)):
        if args.max_rows and total >= args.max_rows:
            break
        prompt = row.get("input")
        target = row.get("target")
        if not isinstance(prompt, str) or not isinstance(target, str):
            continue
        total += 1
        canon = stable_json(row)
        dataset_hasher.update(canon.encode("utf-8"))
        dataset_hasher.update(b"\n")
        leaf_hex = sha256_hex(f"SFT1|{idx}|{sha256_hex(str(prompt))}|{sha256_hex(str(target))}")
        leaf_hashes.append(leaf_hex)
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
        if args.heartbeat_rows > 0 and total % args.heartbeat_rows == 0:
            mem = memory_snapshot()
            print(
                "[heartbeat] "
                f"rows={total} "
                f"rss_mb={mem['rss_mb']:.1f} "
                f"cuda_allocated_mb={mem['cuda_allocated_mb']:.1f} "
                f"cuda_reserved_mb={mem['cuda_reserved_mb']:.1f}"
            )

    dataset_hash = dataset_hasher.hexdigest()
    if leaf_hashes:
        level = [bytes.fromhex(x) for x in leaf_hashes]
        while len(level) > 1:
            if len(level) % 2 == 1:
                level.append(level[-1])
            nxt = []
            for i in range(0, len(level), 2):
                nxt.append(hashlib.sha256(level[i] + level[i + 1]).digest())
            level = nxt
        rows_merkle_root = level[0].hex()
    else:
        rows_merkle_root = sha256_hex("EMPTY")

    repo_root = Path(__file__).resolve().parents[2]
    base_model_id = args.model_path or "heuristic"
    adapter_cfg = {
        "adapter_path": args.adapter_path or "",
        "dtype": args.dtype,
        "device": args.device,
        "max_new_tokens": args.max_new_tokens,
    }
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
        "runtime": {
            **memory_snapshot(),
            "heartbeat_rows": args.heartbeat_rows,
        },
    }
    summary["run_identity"] = make_run_identity(
        swmd_hash=args.swmd_hash,
        dataset_hash=dataset_hash,
        rows_merkle_root=rows_merkle_root,
        builder_git_commit=args.builder_git_commit,
        trainer_git_commit=git_commit(repo_root),
        base_model_id=base_model_id,
        adapter_config=adapter_cfg,
    )
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
