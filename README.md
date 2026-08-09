# Dissertation Trading Project

This repository contains the reproducible artefact for my dissertation on whether intraday SPX, SPY and VIX information can predict final-hour SPX movements and support an economically meaningful 0DTE options strategy.

## Repository structure

```text
data/                    Raw and derived data used by the main analysis
data_extended_2023_2026/ Isolated extended-history dataset
notebooks/               Main executable research notebooks
notebooks/legacy/        Earlier exploratory notebooks kept for provenance
scripts/                 Reusable Python code
scripts/legacy/          Earlier browser-automation experiments
models/                  Saved trained models, when a workflow exports them
outputs/                 Tables, plots, manifests and dissertation drafts
docs/notebooks/          A companion guide for every notebook
docs/scripts/            A companion guide for every Python script
docs/workflow.md          End-to-end artefact workflow and evidence map
config.yaml              Stable project paths and research timing settings
requirements.txt         Python dependencies
```

The notebooks find the repository root by looking for `config.yaml`, then run from that root. As a result, paths such as `data/...` and `outputs/...` resolve consistently whether Jupyter starts in the repository root or inside `notebooks/`.

## Setup

1. Create and activate a Python environment.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run `playwright install chromium` only if the legacy browser-automation scripts are needed.
4. Copy `main.env.example` to `main.env` and add the local API credentials. The real `main.env` file must not be committed.
5. Start Jupyter from the repository root or from `notebooks/`.

The large market datasets are intentionally kept outside package installation. Existing data and research outputs remain in `data/`, `data_extended_2023_2026/` and `outputs/`.

## Main workflow

The linked [workflow guide](docs/workflow.md) provides an end-to-end diagram, the companion documentation for every maintained stage and representative existing evidence.

The core analysis is designed to run in this order:

1. `notebooks/massive_database_starter.ipynb` - confirm API access and storage behaviour.
2. `notebooks/massive_database_raw_retrieve.ipynb` - retrieve the underlying and options data incrementally.
3. `notebooks/aligned_eda.ipynb` - align SPY, SPX and VIX without look-ahead and perform EDA.
4. `notebooks/cleaning_modellingprep.ipynb` - clean sessions and prepare chronological modelling splits.
5. `notebooks/dataset_Splitting.ipynb` - build strict and relaxed dataset variants on common dates.
6. `notebooks/modeling_baseline.ipynb` - compare rule, dummy and machine-learning baselines for RQ1-RQ3.
7. `notebooks/hyperparameters_tuning.ipynb` - tune the selected families with nested time-aware validation.
8. `notebooks/hyperparameters_tuning_extended_robustness.ipynb` - add fold-matched benchmarks, regimes, feature stability and selective-prediction checks.
9. `notebooks/extended_2023_2026_full_pipeline.ipynb` - repeat the underlying-market pipeline on isolated 2023-2026 data.
10. `notebooks/lstm_intraday_sequence_extension.ipynb` - test a small exploratory LSTM on minute sequences.
11. `notebooks/rq4_economic_meaningfulness.ipynb` - assess whether the predictive signals identify economically larger opportunities.
12. `notebooks/rq4_economic_meaningfulness_extended.ipynb` - repeat RQ4 using the extended-history outputs.
13. `notebooks/rq5_options_data_retrieval.ipynb` - retrieve and audit the option contracts required for RQ5.
14. `notebooks/rq5_options_backtest.ipynb` - run the frozen ATM strategy and required mean-reversion comparator.
15. `notebooks/rq5_exit_strategy_sensitivity.ipynb` - test pre-specified exit and risk-management rules.
16. `notebooks/rq5_strategy_robustness_and_multi_contract.ipynb` - test concentration, path dependence and multi-contract scaling.

`notebooks/probe_massive_2021_2022_underlying_access.ipynb` is a non-destructive entitlement check and can be run before any historical expansion. The notebooks under `notebooks/legacy/` are exploratory records rather than dependencies of the final pipeline.

## Reproducibility and leakage controls

- Feature values use information available before the 15:00 ET decision point.
- SPX and VIX alignment is backward-looking only.
- Train, validation and test blocks are chronological.
- Imputation, clipping, scaling, regime thresholds and model selection are fitted on training data within the relevant fold.
- Previously viewed test results are not described as fresh confirmatory evidence.
- RQ5 trading rules and execution assumptions are frozen before any future holdout evaluation.

## Documentation and outputs

Every executable has a matching file under `docs/notebooks/` or `docs/scripts/`. Each guide records its purpose, workflow, inputs, processing, outputs, representative evidence, findings or decisions, limitations and next steps. Generated evidence remains under `outputs/`; the canonical model filenames and metadata contract are documented in [models/README.md](models/README.md).

The tuning notebooks expose a `SAVE_MODEL_ARTIFACTS` switch for the selected RQ1-RQ3 classical models. The LSTM notebook uses the same switch for exploratory development refits and matching scalers. No model binaries are included by this refactor; they are generated only when those notebook cells are run.

The main limitations are the relatively small daily sample, changing market regimes, incomplete historical quote information for options, synthetic execution-cost assumptions and the absence of a genuinely fresh post-selection holdout in the current results.
