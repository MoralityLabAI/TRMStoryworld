#!/usr/bin/env python3
"""Verify SW1 trace leaf hashes and episode Merkle roots."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


def iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = line.strip()
            if not row:
                continue
            yield json.loads(row)


def stable_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def h_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def h_bytes(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(left + right).digest()


def merkle_root_hex(leaves_hex: List[str]) -> str:
    if not leaves_hex:
        return h_hex("EMPTY")
    level = [bytes.fromhex(x) for x in leaves_hex]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        nxt = []
        for i in range(0, len(level), 2):
            nxt.append(h_bytes(level[i], level[i + 1]))
        level = nxt
    return level[0].hex()


def parse_pick(label: str) -> int:
    parts = label.split()
    if len(parts) != 2 or parts[0] != "PICK":
        raise ValueError(f"invalid PICK label: {label}")
    return int(parts[1])


def parse_k(k_label: str) -> int:
    parts = k_label.split()
    if len(parts) != 2 or parts[0] != "K":
        raise ValueError(f"invalid K label: {k_label}")
    return int(parts[1])


def mk_leaf(
    episode_idx: int,
    turn: int,
    state_hash: str,
    pick_idx: int,
    k_budget: int,
    out_hash: str,
) -> str:
    payload = f"SW1D|{episode_idx}|{turn}|{state_hash}|{pick_idx}|{k_budget}|{out_hash}"
    return h_hex(payload)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace-log", type=str, required=True)
    parser.add_argument("--episode-log", type=str, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    trace_rows = list(iter_jsonl(Path(args.trace_log)))
    episode_rows = list(iter_jsonl(Path(args.episode_log)))

    leaf_mismatches: List[Tuple[int, int]] = []
    leaves_by_episode: Dict[int, List[Tuple[int, str]]] = {}

    for row in trace_rows:
        episode = int(row.get("episode"))
        turn = int(row.get("turn"))
        state_hash = str(row.get("state_hash"))
        event = row.get("event", {})
        out_hash = h_hex(stable_json(event.get("outcome")))
        pick_idx = parse_pick(str(row.get("label", "")))
        k_budget = parse_k(str(row.get("k_label", "")))
        expected = mk_leaf(episode, turn, state_hash, pick_idx, k_budget, out_hash)
        actual = str(row.get("receipt_leaf"))
        if actual != expected:
            leaf_mismatches.append((episode, turn))
        leaves_by_episode.setdefault(episode, []).append((turn, actual))

    root_mismatches: List[int] = []
    episode_map = {int(row.get("episode")): row for row in episode_rows}
    for episode, leaves in leaves_by_episode.items():
        ordered = [leaf for _turn, leaf in sorted(leaves, key=lambda x: x[0])]
        computed_root = merkle_root_hex(ordered)
        expected_root = str(episode_map.get(episode, {}).get("trace_root"))
        if computed_root != expected_root:
            root_mismatches.append(episode)

    result = {
        "trace_rows": len(trace_rows),
        "episode_rows": len(episode_rows),
        "leaf_mismatch_count": len(leaf_mismatches),
        "root_mismatch_count": len(root_mismatches),
        "leaf_mismatches": leaf_mismatches[:20],
        "root_mismatches": root_mismatches[:20],
    }
    print(json.dumps(result, indent=2))
    return 0 if not leaf_mismatches and not root_mismatches else 2


if __name__ == "__main__":
    raise SystemExit(main())
