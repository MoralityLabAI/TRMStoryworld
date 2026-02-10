#!/usr/bin/env python3
"""Model backends for controller-style PICK generation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

CHOICE_RE = re.compile(r"^C(\d+)\s+", re.MULTILINE)
PICK_RE = re.compile(r"PICK\s+(\d+)", re.IGNORECASE)
SIZE_HINT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*([bm])")


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
    def __init__(
        self,
        model_path: str,
        adapter_path: Optional[str],
        device: str,
        dtype: str,
        require_gpu: bool = False,
        allow_large_model: bool = False,
        max_model_params_millions: float = 200.0,
    ):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch

        if require_gpu:
            if not torch.cuda.is_available():
                raise RuntimeError("GPU required (--require-gpu) but CUDA is not available.")
            if str(device).lower().strip() == "cpu":
                raise RuntimeError("GPU required (--require-gpu) but device was set to cpu.")

        if not allow_large_model:
            hinted = model_size_hint_millions(model_path)
            if hinted is not None and hinted > max_model_params_millions:
                raise RuntimeError(
                    f"model path appears large (~{hinted:.1f}M params) > cap {max_model_params_millions:.1f}M. "
                    "Use --allow-large-model to override."
                )

        dtype_map = {
            "float16": torch.float16,
            "bfloat16": torch.bfloat16,
            "float32": torch.float32,
            "auto": None,
        }
        torch_dtype = dtype_map.get(dtype, None)
        load_device_map: Any = device
        if require_gpu:
            # Force single-GPU placement instead of auto CPU offload.
            load_device_map = {"": 0}
        tok = AutoTokenizer.from_pretrained(model_path, use_fast=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch_dtype,
            device_map=load_device_map,
            low_cpu_mem_usage=True,
        )
        if adapter_path:
            from peft import PeftModel
            offload_dir = Path(__file__).resolve().parent / "out" / "offload"
            offload_dir.mkdir(parents=True, exist_ok=True)
            # Some PEFT/transformers combinations fail when applying adapter weights with offload metadata.
            # Retry without offload so eval-only rollouts remain usable on local setups.
            try:
                model = PeftModel.from_pretrained(model, adapter_path, offload_folder=str(offload_dir))
            except KeyError:
                model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch_dtype, device_map=load_device_map)
                model = PeftModel.from_pretrained(model, adapter_path)
        if not allow_large_model:
            total_params_m = float(sum(p.numel() for p in model.parameters())) / 1_000_000.0
            if total_params_m > max_model_params_millions:
                raise RuntimeError(
                    f"loaded model is {total_params_m:.1f}M params, above cap {max_model_params_millions:.1f}M. "
                    "Use --allow-large-model to override."
                )
        if require_gpu:
            dev = str(getattr(model, "device", "")).lower()
            if "cuda" not in dev:
                raise RuntimeError(f"GPU required (--require-gpu) but model device is '{dev or 'unknown'}'.")
        model.eval()
        for param in model.parameters():
            param.requires_grad_(False)
        self.tokenizer = tok
        self.model = model

    def predict(self, prompt: str, max_new_tokens: int = 8) -> ModelResult:
        import torch

        tokenizer = self.tokenizer
        model = self.model
        inputs = tokenizer(prompt, return_tensors="pt")
        model_device = getattr(model, "device", None)
        if model_device is not None and str(model_device) != "meta":
            inputs = {k: v.to(model_device) for k, v in inputs.items()}
        with torch.inference_mode():
            out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=0.0,
                top_p=1.0,
                use_cache=False,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id,
            )
        gen = out[0][inputs["input_ids"].shape[1] :]
        gen_cpu = gen.detach().to("cpu")
        text = tokenizer.decode(gen_cpu, skip_special_tokens=True).strip()
        tokens = int(gen_cpu.numel())
        del gen_cpu
        del gen
        del out
        del inputs
        return ModelResult(text=text, tokens=tokens)


def memory_snapshot() -> Dict[str, Any]:
    snapshot: Dict[str, Any] = {
        "rss_mb": -1.0,
        "cuda_allocated_mb": 0.0,
        "cuda_reserved_mb": 0.0,
        "cuda_available": False,
    }
    try:
        import psutil

        snapshot["rss_mb"] = psutil.Process().memory_info().rss / (1024 * 1024)
    except Exception:
        pass
    try:
        import torch

        snapshot["cuda_available"] = bool(torch.cuda.is_available())
        if snapshot["cuda_available"]:
            snapshot["cuda_allocated_mb"] = torch.cuda.memory_allocated() / (1024 * 1024)
            snapshot["cuda_reserved_mb"] = torch.cuda.memory_reserved() / (1024 * 1024)
    except Exception:
        pass
    return snapshot


def parse_pick(text: str) -> Optional[int]:
    m = PICK_RE.search(text or "")
    return int(m.group(1)) if m else None


def parse_target_pick(target: str) -> Optional[int]:
    return parse_pick(target)


def model_size_hint_millions(model_path: str) -> Optional[float]:
    text = str(model_path).lower().replace("_", "").replace("-", "")
    match = SIZE_HINT_RE.search(text)
    if not match:
        return None
    value = float(match.group(1))
    unit = match.group(2)
    return value * 1000.0 if unit == "b" else value


def controller_from_args(
    model_path: Optional[str],
    adapter_path: Optional[str],
    device: str,
    dtype: str,
    require_gpu: bool = False,
    allow_large_model: bool = False,
    max_model_params_millions: float = 200.0,
):
    if not model_path:
        return HeuristicController()
    return HFController(
        model_path=model_path,
        adapter_path=adapter_path,
        device=device,
        dtype=dtype,
        require_gpu=require_gpu,
        allow_large_model=allow_large_model,
        max_model_params_millions=max_model_params_millions,
    )
