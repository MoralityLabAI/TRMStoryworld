#!/usr/bin/env python3
"""Determinism verifier for SWMD controller datasets and receipts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from identity_utils import git_commit, make_run_identity
from swmd_utils import canonical_swmd_hash, merkle_root_hex, sha256_hex, stable_json


def iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = line.strip()
            if not row:
                continue
            yield json.loads(row)


def canonical_row_bytes(row: Dict[str, Any]) -> str:
    return stable_json(row)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--swmd-min", type=str, required=True)
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--summary", type=str, default="")
    parser.add_argument("--out", type=str, default="tools/bench/out/verify_swmd_dataset.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    swmd_path = Path(args.swmd_min)
    dataset_path = Path(args.dataset)
    summary_path = Path(args.summary) if args.summary else None
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    swmd_hash = canonical_swmd_hash(swmd_path)
    rows = list(iter_jsonl(dataset_path))
    row_hashes: List[str] = []
    canonical_lines: List[str] = []
    for i, row in enumerate(rows):
        line = canonical_row_bytes(row)
        canonical_lines.append(line)
        leaf = sha256_hex(f"SFT1|{i}|{sha256_hex(str(row.get('input', '')))}|{sha256_hex(str(row.get('target', '')))}")
        row_hashes.append(leaf)
    dataset_canon = "\n".join(canonical_lines) + ("\n" if canonical_lines else "")
    dataset_hash = sha256_hex(dataset_canon)
    rows_merkle_root = merkle_root_hex(row_hashes)

    checks: List[Dict[str, Any]] = []
    ok = True
    if summary_path and summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        expected_swmd = summary.get("swmd_hash")
        expected_rows = summary.get("rows")
        if expected_swmd is not None:
            passed = expected_swmd == swmd_hash
            checks.append({"check": "swmd_hash_matches_summary", "passed": passed, "expected": expected_swmd, "actual": swmd_hash})
            ok = ok and passed
        if expected_rows is not None:
            passed = int(expected_rows) == len(rows)
            checks.append({"check": "row_count_matches_summary", "passed": passed, "expected": int(expected_rows), "actual": len(rows)})
            ok = ok and passed

    result = {
        "result": "ok" if ok else "mismatch",
        "schema_version": 1,
        "newline_mode": "LF",
        "normalized_bytes_spec": "stable_json(sort_keys=True,separators=',:') + LF",
        "swmd_hash": swmd_hash,
        "dataset_hash": dataset_hash,
        "rows_merkle_root": rows_merkle_root,
        "rows": len(rows),
        "checks": checks,
    }
    repo_root = Path(__file__).resolve().parents[2]
    result["run_identity"] = make_run_identity(
        swmd_hash=swmd_hash,
        dataset_hash=dataset_hash,
        rows_merkle_root=rows_merkle_root,
        builder_git_commit="",
        trainer_git_commit=git_commit(repo_root),
        base_model_id="",
        adapter_config={},
    )
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
