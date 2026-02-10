# TRMInterp v0 Spec

## Commands

1. `trminterp trace`
2. `trminterp sae fit`
3. `trminterp intervene`

## Required Outputs

1. `trace.jsonl`
2. `report.json`

## Optional Outputs

1. `states.npy`
2. `sae.pt`
3. `sae_metrics.json`
4. `intervention_diffs.json`

## trace.jsonl Shape

Each line is one step payload with:

1. `t`
2. `obs`
3. `action`
4. `h`
5. `aux`
6. `y`
7. `metrics`

## report.json Shape

1. `baseline`
2. `intervened`
3. `delta`
4. `first_divergence_step`
5. `top_causal_features`

`delta` includes success-rate and loss changes.
