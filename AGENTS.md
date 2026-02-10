# AGENTS.md

## Purpose
TRMStoryworld is the benchmark/eval side for controller training over storyworld IR.
This repo consumes SWMD/SWMD-min artifacts and produces:
- consolidated run metrics,
- benchmark plots,
- controller eval summaries,
- deterministic rollout traces/commitments.

## Active Harness Surface
- `tools/bench/collect_trm_runs.py`
- `tools/bench/plot_trm_runs.py`
- `tools/bench/eval_trm_controller.py`
- `tools/bench/eval_storyworld_rollout.py`
- `tools/bench/verify_swmd_dataset.py`
- shared helpers:
  - `tools/bench/swmd_utils.py`
  - `tools/bench/model_utils.py`

## Data Contracts
- Input IR:
  - `SWMD-0`
  - `SWMD-0-MIN`
- Controller dataset rows:
  - `input` (prompt)
  - `target` (`PICK k`, optional `K n`)
  - `meta` (`swmd_hash`, `encounter_id`, etc.)
- Eval outputs:
  - `eval_summary.json`
  - rollout traces and episode logs with `receipt_leaf`, `trace_root`, `output_commitment`

## Determinism Rules
- Normalize newlines to LF before hashing.
- Stable sort by IDs (encounter/option/reaction).
- Canonical JSON for hashes:
  - `json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=True)`
- Receipt hash payloads must be versioned (`SWMDR|...`, `SFT1|...`) and immutable once published.

## Security Rules (Mandatory)
- Do not commit live secrets in logs or artifacts.
- Scan before commit for:
  - `sk-...`, `sk-proj-...`, `Bearer ...`, `OPENAI_API_KEY=...`
- If detected, redact in-place (replace token value with `REDACTED`) while keeping event context.

## Run/Artifact Hygiene
- Keep generated benchmark outputs under `tools/bench/out/` or `negotiation-storyworld/logs/`.
- Do not commit generated logs/plots by default unless explicitly requested.
- Keep code changes separate from generated artifacts.

## Minimal Execution Flow
1. Aggregate runs:
   - `python tools/bench/collect_trm_runs.py --logs-root negotiation-storyworld/logs`
2. Plot:
   - `python tools/bench/plot_trm_runs.py --agg-json tools/bench/out/trm_runs_agg.json`
3. Controller eval:
   - `python tools/bench/eval_trm_controller.py --dataset <controller_sft.jsonl>`
4. Rollout eval:
   - `python tools/bench/eval_storyworld_rollout.py --swmd <story.swmd.min.md>`
5. Determinism verify:
   - `python tools/bench/verify_swmd_dataset.py --swmd-min <story.swmd.min.md> --dataset <controller_sft.jsonl> --summary <summary.json>`

## Editing Guidance
- Prefer additive scripts in `tools/bench/`.
- Avoid refactoring core env/training code unless required for harness compatibility.
- Keep parser behavior explicit and testable with small fixtures.
