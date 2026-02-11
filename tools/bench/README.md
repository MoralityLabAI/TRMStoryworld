# TRM Bench Harness

## Collect
```powershell
python tools/bench/collect_trm_runs.py --logs-root D:\Research_Engine\Llama_Storyworld\logs --pattern "*summary.json"
```

## Guarded long run (single instance + memory watchdog + live logs)
```powershell
pip install psutil
python tools/bench/run_guarded.py `
  --cwd D:\Research_Engine\Llama_Storyworld `
  --log-dir D:\Research_Engine\Llama_Storyworld\logs `
  --run-id hrm_trm-run-safe-001 `
  --max-ram-pct 85 `
  --heartbeat-seconds 30 `
  --authorize I_UNDERSTAND_THIS_STARTS_TRAINING `
  --command "python train.py --config configs\trm_4608.yaml"
```

Notes:
- Prevents concurrent starts via lock file (`trm_training.lock` under `--log-dir`).
- Streams stdout/stderr in real time to console and `<run-id>.log`.
- Writes heartbeat JSONL (`<run-id>_heartbeat.jsonl`) with timestamp/pid/rss.
- If RSS crosses `--max-ram-pct`, it logs the event and cleanly terminates.

## Plot
```powershell
python tools/bench/plot_trm_runs.py --agg-json tools/bench/out/trm_runs_agg.json
```

## Verify dataset determinism
```powershell
python tools/bench/verify_swmd_dataset.py --swmd-min <story.swmd.min.md> --dataset <controller_sft.jsonl> --summary <summary.json>
```

## Eval controller
```powershell
python tools/bench/eval_trm_controller.py --dataset <controller_sft.jsonl> --model-path <base_model> --adapter-path <adapter> --device cpu
```

## Rollout eval
```powershell
python tools/bench/eval_storyworld_rollout.py --swmd <story.swmd.min.md> --episodes 16 --max-steps 12 --base-model <base_model> --adapter-path <adapter> --device cpu
```

## Parallel TRM + HRM codec benchmark
```powershell
python tools/bench/parallel_trm_hrm_codec_bench.py `
  --codec D:\Download\codec.txt `
  --hrm-dry-run `
  --max-swmd 10 `
  --trm-workers 4 `
  --hrm-runs 2 `
  --hrm-workers 2
```

Writes one consolidated manifest:
- `tools/bench/out/parallel_codec_bench/parallel_manifest.json`
