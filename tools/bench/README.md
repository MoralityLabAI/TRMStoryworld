# TRM Bench Harness

## Collect
```powershell
python tools/bench/collect_trm_runs.py --logs-root D:\Research_Engine\Llama_Storyworld\logs --pattern "*summary.json"
```

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
