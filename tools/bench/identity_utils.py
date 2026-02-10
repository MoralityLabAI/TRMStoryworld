#!/usr/bin/env python3
"""Run identity helpers for deterministic benchmark receipts."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from pathlib import Path
from typing import Any, Dict


def stable_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_commit(repo_root: Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except Exception:
        return ""


def adapter_config_hash(config: Dict[str, Any]) -> str:
    return sha256_hex(stable_json(config))


def make_run_identity(
    *,
    swmd_hash: str,
    dataset_hash: str,
    rows_merkle_root: str,
    builder_git_commit: str,
    trainer_git_commit: str,
    base_model_id: str,
    adapter_config: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "schema_version": 1,
        "swmd_hash": swmd_hash,
        "dataset_hash": dataset_hash,
        "rows_merkle_root": rows_merkle_root,
        "builder_git_commit": builder_git_commit,
        "trainer_git_commit": trainer_git_commit,
        "base_model_id": base_model_id,
        "adapter_config_hash": adapter_config_hash(adapter_config),
        "adapter_config": adapter_config,
        "python_version": platform.python_version(),
        "normalized_bytes_spec": "stable_json(sort_keys=True,separators=',:') + LF",
    }
