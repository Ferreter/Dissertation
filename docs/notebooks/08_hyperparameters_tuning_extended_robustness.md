# Tuned-Model Robustness Analysis

**Executable:** `notebooks/08_hyperparameters_tuning_extended_robustness.ipynb`
**Status:** I use this in the main dissertation workflow.

## Purpose

After tuning, I wanted to check whether the chosen models still looked believable from a few different angles. This notebook covers matched benchmarks, regimes, feature stability and the idea of only acting on higher-confidence days.

## Workflow

```mermaid
flowchart LR
    A["Selected tuned configurations"] --> B["Fold-matched, regime and feature-stability checks"]
    B --> C["Robustness tables, figures and canonical models"]
    C --> D["Economic interpretation"]
```

## Inputs

- Strict and relaxed split datasets
- Frozen tuned configurations

## Processing and rationale

- I rebuild each chosen model inside the same outer folds as its benchmark.
- I calculate feature importance and market-regime cut-offs using training information only.
- For RQ1, I gradually keep fewer, more confident sessions and check what happens to accuracy and coverage.

## Outputs

- `outputs/hyperparameter_tuning/tables/selected_winner_outer_fold_predictions.csv`
- `outputs/hyperparameter_tuning/tables/fold_matched_benchmark_summary.csv`
- Feature-stability, regime and selective-prediction tables

## Representative outputs

![RQ1 selective-prediction coverage](../../outputs/hyperparameter_tuning/figures/rq1_selective_prediction_coverage.png)

*This plot shows the trade-off between acting on fewer high-confidence sessions and retaining usable coverage.*

![RQ1 permutation importance](../../outputs/hyperparameter_tuning/figures/rq1_outer_fold_permutation_importance.png)

*This plot shows the stability of feature contributions across chronological outer folds.*

## Findings and decisions

- RQ1 did improve at some of the lower-coverage confidence levels, but the pattern wasn't consistent all the way through.
- The regime results moved around as well, which fits with the fairly weak overall direction result.
- I use these saved predictions as the link between the modelling work and the RQ4 economic analysis.

## Limitations

- These are still development-period checks carried out after choosing the model families.
- Once I split the data into regimes or confidence groups, some of the groups become very small.

## Next steps

- The next step is to freeze the setup for a future holdout and see whether the signals concentrate useful opportunities in RQ4.
