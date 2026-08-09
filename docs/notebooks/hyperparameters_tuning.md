# Hyperparameter Tuning and Threshold Optimisation

**Executable:** `notebooks/hyperparameters_tuning.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I tune the selected RQ1-RQ3 model families while keeping the previously viewed test block disabled.

## Inputs

- Strict and relaxed split datasets
- Baseline model and feature-set decisions

## Processing and rationale

- Run nested expanding-window searches for classification and regression.
- Select classification thresholds inside development folds.
- Freeze the final parameter manifests without using a fresh holdout.

## Outputs

- `outputs/hyperparameter_tuning/tables/`
- `outputs/hyperparameter_tuning/figures/`
- `outputs/hyperparameter_tuning/final_tuned_configuration_manifest.json`
- `outputs/hyperparameter_tuning/nested_tuning_dissertation_draft.md`

## Findings and decisions

- The selected specifications were relaxed Histogram Gradient Boosting for RQ1, relaxed RBF SVR for RQ2 and strict RBF SVC for RQ3.
- Mean outer-fold RQ1 balanced accuracy was about 0.544, indicating limited and unstable directional evidence.
- I treat nested development performance, not the previously viewed test block, as the primary evidence.

## Limitations

- Only three outer and three inner time splits are available.
- Hyperparameter search cannot compensate for a small sample or missing options-derived information.

## Next steps

- Add fold-matched benchmarks, feature stability, regime checks and selective-prediction analysis.
