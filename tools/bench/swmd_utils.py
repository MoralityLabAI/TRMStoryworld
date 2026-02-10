#!/usr/bin/env python3
"""Shared SWMD parsing and hashing helpers for benchmark tools."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ENC_RE = re.compile(r"^ENC\s+(\S+)\s+turn=([^\s]+)\s*$")
ORX_RE = re.compile(r"^ORX\s+([^/]+)/([^\s]+)\s+->\s+([^|]+)\|(.+)$")
FULL_ENC_RE = re.compile(r"^##\s+ENC\s+(\S+)\s+\|\s+(.+?)\s+\|\s+turn=([^|]+)\|\s+spools=\[(.*?)\]\s*$")
FULL_OPT_RE = re.compile(r"^OPT\s+(\S+):\s*(.*)$")
FULL_RXN_RE = re.compile(r"^RXN\s+(\S+)\s+->\s+(\S+)\s*$")


@dataclass
class SwmdReaction:
    rxn_id: str
    consequence: str
    text: str = ""
    effects: List[str] = field(default_factory=list)
    desirability: str = "C(0)"


@dataclass
class SwmdOption:
    opt_id: str
    text: str
    reactions: List[SwmdReaction] = field(default_factory=list)


@dataclass
class SwmdEncounter:
    enc_id: str
    title: str
    turn_span: str
    spools: List[str] = field(default_factory=list)
    text: str = ""
    options: List[SwmdOption] = field(default_factory=list)


@dataclass
class SwmdWorld:
    world_id: str
    title: str
    mode: str
    hash_sha256: str
    encounters: List[SwmdEncounter]


def normalize_lf(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n")).strip() + "\n"


def stable_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_bytes(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(left + right).digest()


def merkle_root_hex(leaves_hex: List[str]) -> str:
    if not leaves_hex:
        return sha256_hex("EMPTY")
    level = [bytes.fromhex(x) for x in leaves_hex]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        nxt = []
        for i in range(0, len(level), 2):
            nxt.append(sha256_bytes(level[i], level[i + 1]))
        level = nxt
    return level[0].hex()


def canonical_swmd_hash(path: Path) -> str:
    return sha256_hex(normalize_lf(path.read_text(encoding="utf-8")))


def parse_swmd(path: Path) -> SwmdWorld:
    raw = normalize_lf(path.read_text(encoding="utf-8"))
    if raw.startswith("# SWMD-0-MIN"):
        world = _parse_swmd_min(raw)
    elif raw.startswith("# SWMD-0"):
        world = _parse_swmd_full(raw)
    else:
        raise ValueError(f"unsupported SWMD header in {path}")
    world.hash_sha256 = sha256_hex(raw)
    return world


def _parse_swmd_min(text: str) -> SwmdWorld:
    lines = [ln.strip() for ln in text.splitlines()]
    world_id = "unknown"
    title = "SWMD"
    encounters: Dict[str, SwmdEncounter] = {}
    current_enc: Optional[SwmdEncounter] = None

    for row in lines:
        if not row:
            continue
        if row.startswith("id:"):
            world_id = row.split(":", 1)[1].strip()
            continue
        if row.startswith("title:"):
            title = row.split(":", 1)[1].strip()
            continue
        m_enc = ENC_RE.match(row)
        if m_enc:
            enc_id, span = m_enc.group(1), m_enc.group(2)
            current_enc = SwmdEncounter(enc_id=enc_id, title=enc_id, turn_span=span)
            encounters[enc_id] = current_enc
            continue
        m_orx = ORX_RE.match(row)
        if m_orx and current_enc is not None:
            opt_id = m_orx.group(1).strip()
            rxn_id = m_orx.group(2).strip()
            consequence = m_orx.group(3).strip()
            payload_raw = m_orx.group(4).strip()
            payload: Dict[str, str] = {}
            for seg in payload_raw.split("|"):
                part = seg.strip()
                if ":" in part:
                    k, v = part.split(":", 1)
                    payload[k.strip()] = v.strip()
            opt = next((o for o in current_enc.options if o.opt_id == opt_id), None)
            if opt is None:
                opt = SwmdOption(opt_id=opt_id, text=payload.get("O", ""))
                current_enc.options.append(opt)
            reaction = SwmdReaction(
                rxn_id=rxn_id,
                consequence=consequence,
                text=payload.get("R", ""),
                effects=[x.strip() for x in payload.get("E", "").split(";") if x.strip()],
                desirability=payload.get("D", "C(0)"),
            )
            opt.reactions.append(reaction)

    ordered_encs = sorted(encounters.values(), key=lambda e: (e.turn_span, e.enc_id))
    for enc in ordered_encs:
        enc.options = sorted(enc.options, key=lambda o: o.opt_id)
        for opt in enc.options:
            opt.reactions = sorted(opt.reactions, key=lambda r: r.rxn_id)
    return SwmdWorld(world_id=world_id, title=title, mode="min", hash_sha256="", encounters=ordered_encs)


def _parse_swmd_full(text: str) -> SwmdWorld:
    lines = text.splitlines()
    world_id = "unknown"
    title = "SWMD"
    encounters: Dict[str, SwmdEncounter] = {}
    current_enc: Optional[SwmdEncounter] = None
    current_opt: Optional[SwmdOption] = None
    current_rxn: Optional[SwmdReaction] = None
    mode = ""

    for raw in lines:
        row = raw.rstrip()
        s = row.strip()
        if not s:
            continue
        if s.startswith("id:"):
            world_id = s.split(":", 1)[1].strip()
            continue
        if s.startswith("title:"):
            title = s.split(":", 1)[1].strip()
            continue
        if s.startswith("# SWMD-0"):
            mode = "full"
            continue
        m_enc = FULL_ENC_RE.match(s)
        if m_enc:
            enc_id = m_enc.group(1)
            enc_title = m_enc.group(2)
            turn_span = m_enc.group(3).strip()
            spools = [x.strip() for x in m_enc.group(4).split(",") if x.strip()]
            current_enc = SwmdEncounter(enc_id=enc_id, title=enc_title, turn_span=turn_span, spools=spools)
            encounters[enc_id] = current_enc
            current_opt = None
            current_rxn = None
            continue
        if current_enc is None:
            continue
        if s.startswith("T: ") and current_opt is None and current_rxn is None:
            current_enc.text = s[3:].strip()
            continue
        m_opt = FULL_OPT_RE.match(s)
        if m_opt:
            current_opt = SwmdOption(opt_id=m_opt.group(1), text=m_opt.group(2).strip())
            current_enc.options.append(current_opt)
            current_rxn = None
            continue
        m_rxn = FULL_RXN_RE.match(s)
        if m_rxn and current_opt is not None:
            current_rxn = SwmdReaction(rxn_id=m_rxn.group(1), consequence=m_rxn.group(2))
            current_opt.reactions.append(current_rxn)
            continue
        if s.startswith("T: ") and current_rxn is not None:
            current_rxn.text = s[3:].strip()
            continue
        if s.startswith("D: ") and current_rxn is not None:
            current_rxn.desirability = s[3:].strip()
            continue
        if s.startswith("SET ") and current_rxn is not None:
            current_rxn.effects.append(s)

    ordered_encs = sorted(encounters.values(), key=lambda e: (e.turn_span, e.enc_id))
    for enc in ordered_encs:
        enc.options = sorted(enc.options, key=lambda o: o.opt_id)
        for opt in enc.options:
            opt.reactions = sorted(opt.reactions, key=lambda r: r.rxn_id)
    return SwmdWorld(world_id=world_id, title=title, mode=(mode or "full"), hash_sha256="", encounters=ordered_encs)
