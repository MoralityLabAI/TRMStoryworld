#!/usr/bin/env python3
"""Build TRM controller SFT rows directly from SWMD-0-MIN markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ENC_RE = re.compile(r"^ENC\s+(\S+)\s+turn=([^\s]+)\s*$")
ORX_RE = re.compile(r"^ORX\s+([^/]+)/([^\s]+)\s+->\s+([^|]+)\|(.+)$")
CONST_RE = re.compile(r"C\((-?\d+(?:\.\d+)?)\)")
EFFECT_RE = re.compile(r"SET\s+([^.]+)\.([^\s]+)\s+\+=\s+(-?\d+(?:\.\d+)?)")


@dataclass
class Reaction:
    rxn_id: str
    consequence: str
    effects_blob: str
    desirability_blob: str


@dataclass
class OptionBucket:
    opt_id: str
    text: str
    reactions: List[Reaction] = field(default_factory=list)


@dataclass
class Encounter:
    enc_id: str
    turn_span: str
    options: Dict[str, OptionBucket] = field(default_factory=dict)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--swmd-min", type=str, required=True, help="Path to SWMD-0-MIN markdown file.")
    parser.add_argument("--out", type=str, default="negotiation-storyworld/logs/swmd_controller_sft.jsonl")
    parser.add_argument("--summary-out", type=str, default="negotiation-storyworld/logs/swmd_controller_summary.json")
    parser.add_argument("--include-k", action="store_true", help="Append K label to target.")
    parser.add_argument(
        "--k-margin",
        type=float,
        default=0.2,
        help="If top score margin >= k-margin then K=1 else K=2.",
    )
    return parser.parse_args()


def canonical_hash(text: str) -> str:
    normalized = "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n")).strip() + "\n"
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def parse_swmd_min(path: Path) -> Tuple[str, str, Dict[str, Encounter]]:
    raw = path.read_text(encoding="utf-8")
    world_hash = canonical_hash(raw)
    world_id = "unknown"
    encounters: Dict[str, Encounter] = {}
    current_enc_id: Optional[str] = None

    for line in raw.splitlines():
        row = line.strip()
        if not row:
            continue
        if row.startswith("id:"):
            world_id = row.split(":", 1)[1].strip()
            continue
        m_enc = ENC_RE.match(row)
        if m_enc:
            enc_id, turn_span = m_enc.group(1), m_enc.group(2)
            encounters[enc_id] = Encounter(enc_id=enc_id, turn_span=turn_span)
            current_enc_id = enc_id
            continue
        m_orx = ORX_RE.match(row)
        if m_orx and current_enc_id:
            opt_id = m_orx.group(1).strip()
            rxn_id = m_orx.group(2).strip()
            consequence = m_orx.group(3).strip()
            rest = m_orx.group(4).strip()
            parts = [p.strip() for p in rest.split("|")]
            payload = {}
            for p in parts:
                if ":" in p:
                    k, v = p.split(":", 1)
                    payload[k.strip()] = v.strip()
            opt_text = payload.get("O", "")
            effects_blob = payload.get("E", "")
            desirability_blob = payload.get("D", "C(0)")
            bucket = encounters[current_enc_id].options.setdefault(opt_id, OptionBucket(opt_id=opt_id, text=opt_text))
            bucket.reactions.append(
                Reaction(
                    rxn_id=rxn_id,
                    consequence=consequence,
                    effects_blob=effects_blob,
                    desirability_blob=desirability_blob,
                )
            )
    return world_id, world_hash, encounters


def parse_effect_deltas(effects_blob: str) -> Tuple[float, float]:
    trust = 0.0
    threat = 0.0
    for part in effects_blob.split(";"):
        m = EFFECT_RE.search(part.strip())
        if not m:
            continue
        prop_path = m.group(2)
        val = float(m.group(3))
        if prop_path.endswith("Trust") or ".Trust" in prop_path or prop_path.startswith("Trust"):
            trust += val
        if prop_path.endswith("Threat") or ".Threat" in prop_path or prop_path.startswith("Threat"):
            threat += val
    return trust, threat


def desirability_prior(expr: str) -> float:
    consts = [float(x) for x in CONST_RE.findall(expr or "")]
    if not consts:
        return 0.0
    return sum(consts)


def option_score(bucket: OptionBucket) -> Tuple[float, float, float, List[str]]:
    if not bucket.reactions:
        return 0.0, 0.0, 0.0, []
    trust_vals: List[float] = []
    threat_vals: List[float] = []
    d_vals: List[float] = []
    next_nodes: List[str] = []
    for rxn in bucket.reactions:
        t, h = parse_effect_deltas(rxn.effects_blob)
        trust_vals.append(t)
        threat_vals.append(h)
        d_vals.append(desirability_prior(rxn.desirability_blob))
        next_nodes.append(rxn.consequence)
    n = float(len(bucket.reactions))
    return sum(trust_vals) / n, sum(threat_vals) / n, sum(d_vals) / n, sorted(set(next_nodes))


def fmt_signed(x: float) -> str:
    return f"+{x:.2f}" if x >= 0 else f"{x:.2f}"


def build_prompt(enc: Encounter, ranked: List[Tuple[str, OptionBucket, float, float, float, List[str]]]) -> str:
    lines = ["<SWMD-CTRL>", f"E {enc.enc_id} turn={enc.turn_span}"]
    for idx, (_opt_id, bucket, trust, threat, dscore, next_nodes) in enumerate(ranked):
        nxt = ",".join(next_nodes) if next_nodes else "none"
        lines.append(
            f"C{idx} {bucket.opt_id} -> {nxt} | O:{bucket.text} | DT:{fmt_signed(trust)} | DH:{fmt_signed(threat)} | D0:{dscore:.3f}"
        )
    lines.append("</SWMD-CTRL>")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    swmd_path = Path(args.swmd_min)
    out_path = Path(args.out)
    summary_path = Path(args.summary_out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    world_id, swmd_hash, encounters = parse_swmd_min(swmd_path)
    rows = 0
    k1_count = 0
    k2_count = 0
    encounter_count = 0

    with out_path.open("w", encoding="utf-8") as handle:
        for enc_id in sorted(encounters.keys()):
            enc = encounters[enc_id]
            if not enc.options:
                continue
            scored: List[Tuple[str, OptionBucket, float, float, float, List[str]]] = []
            for opt_id in sorted(enc.options.keys()):
                bucket = enc.options[opt_id]
                trust, threat, dscore, next_nodes = option_score(bucket)
                scored.append((opt_id, bucket, trust, threat, dscore, next_nodes))
            ranked = sorted(scored, key=lambda x: (-x[4], x[0]))
            prompt = build_prompt(enc, ranked)
            top = ranked[0]
            label = "PICK 0"
            margin = top[4] - ranked[1][4] if len(ranked) > 1 else top[4]
            k = 1 if margin >= float(args.k_margin) else 2
            if k == 1:
                k1_count += 1
            else:
                k2_count += 1
            target = label if not args.include_k else f"{label}\nK {k}"
            out_row = {
                "input": prompt,
                "target": target,
                "meta": {
                    "world_id": world_id,
                    "swmd_hash": swmd_hash,
                    "encounter_id": enc.enc_id,
                    "turn_span": enc.turn_span,
                    "option_count": len(ranked),
                    "margin": margin,
                    "k_budget": k,
                },
            }
            handle.write(json.dumps(out_row, ensure_ascii=False) + "\n")
            rows += 1
            encounter_count += 1

    summary = {
        "mission": "trm-controller-dataset-from-swmd-min",
        "target": str(swmd_path),
        "result": "ok",
        "rows": rows,
        "encounters": encounter_count,
        "swmd_hash": swmd_hash,
        "k_budget_counts": {"k1": k1_count, "k2": k2_count},
        "out": str(out_path),
    }
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
