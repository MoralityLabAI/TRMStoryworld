# TRM Mechanistic Interpretability Toolkit

This directory contains a preparedness-grade instrumentation stack for recurrent-latent reasoning models (TRM/HRM/RRM style).

Scope is intentionally limited to tracing, analysis, causal intervention, and evaluation. It does not implement capability-improving training.

## Structure

- `src/trm_trace/trace.py`
  - `TraceWriter` for incremental trace logging (`jsonl` or `npz`)
  - `TraceReader` and schema validation
- `src/trm_trace/hooks.py`
  - step wrappers and capture config
- `src/trm_trace/interventions.py`
  - activation patching, directional edits, auxiliary ablations
- `src/runner/run_tasks.py`
  - deterministic synthetic benchmark runner with trace output
- `src/runner/patch_run.py`
  - single-episode patching CLI
- `src/analysis/dynamics.py`
  - convergence, cycle, divergence analysis
- `src/analysis/embedding.py`
  - low-dimensional trajectory projection (PCA)
- `src/analysis/causality.py`
  - patching experiments and step causal contribution
- `src/analysis/monitors.py`
  - early-failure predictor from first `k` steps
- `src/mechinterp_cli.py`
  - unified CLI with `run`, `trace`, `analyze`, `patch`

## Reproducibility

- All run/analyze commands take explicit seeds.
- Randomness is fixed via Python, NumPy, and Torch seed setting.
- Trace JSON uses canonical serialization (`sort_keys=True`, compact separators, ASCII-safe output).
- Each step is recorded with explicit integer timestep `t`.

## Usage

Set module path:

```powershell
$env:PYTHONPATH = "src"
```

Run synthetic tasks and emit traces:

```powershell
python -m runner.run_tasks --out-dir tools/bench/out/traces --num-tasks 12 --steps 6 --seed 7 --fmt jsonl
```

Dynamics analysis:

```powershell
python -m analysis.dynamics --summary-json tools/bench/out/traces/run_summary_seed7.json
```

Causality analysis (activation patching):

```powershell
python -m analysis.causality --summary-json tools/bench/out/traces/run_summary_seed7.json --seed 7 --steps 6
```

Early-failure monitor:

```powershell
python -m analysis.monitors --summary-json tools/bench/out/traces/run_summary_seed7.json --k 3
```

Patch one target task with a donor trace state:

```powershell
python -m runner.patch_run --donor-trace tools/bench/out/traces/task_0_seed7.jsonl --target-task-id task_4 --seed 7 --steps 6 --patch-step 2
```

Unified CLI:

```powershell
python -m mechinterp_cli run --seed 7
python -m mechinterp_cli analyze --summary-json tools/bench/out/traces/run_summary_seed7.json --seed 7 --steps 6
```

## Tests

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```
