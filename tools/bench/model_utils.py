#!/usr/bin/env python3
"""Model backends for controller-style PICK generation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional, Tuple

CHOICE_RE = re.compile(r"^C(\d+)\s+", re.MULTILINE)
PICK_RE = re.compile(r"PICK\s+(\d+)", re.IGNORECASE)


@dataclass
class ModelResult:
    text: str
    tokens: int


class HeuristicController:
    def predict(self, prompt: str, max_new_tokens: int = 8) -> ModelResult:
        _ = max_new_tokens
        picks = [int(x) for x in CHOICE_RE.findall(prompt)]
        choice = min(picks) if picks else 0
        text = f"PICK {choice}"
        return ModelResult(text=text, tokens=len(text.split()))


class HFController:
    def __init__(self, model_path: str, adapter_path: Optional[str], device: str, dtype: str):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch

        dtype_map = {
            "float16": torch.float16,
            "bfloat16": torch.bfloat16,
            "float32": torch.float32,
            "auto": None,
        }
        torch_dtype = dtype_map.get(dtype, None)
        tok = AutoTokenizer.from_pretrained(model_path, use_fast=True)
        model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch_dtype, device_map=device)
        if adapter_path:
            from peft import PeftModel

            model = PeftModel.from_pretrained(model, adapter_path)
        self.tokenizer = tok
        self.model = model

    def predict(self, prompt: str, max_new_tokens: int = 8) -> ModelResult:
        import torch

        tokenizer = self.tokenizer
        model = self.model
        inputs = tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=0.0,
                top_p=1.0,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id,
            )
        gen = out[0][inputs["input_ids"].shape[1] :]
        text = tokenizer.decode(gen, skip_special_tokens=True).strip()
        tokens = int(gen.numel())
        return ModelResult(text=text, tokens=tokens)


def parse_pick(text: str) -> Optional[int]:
    m = PICK_RE.search(text or "")
    return int(m.group(1)) if m else None


def parse_target_pick(target: str) -> Optional[int]:
    return parse_pick(target)


def controller_from_args(model_path: Optional[str], adapter_path: Optional[str], device: str, dtype: str):
    if not model_path:
        return HeuristicController()
    return HFController(model_path=model_path, adapter_path=adapter_path, device=device, dtype=dtype)
