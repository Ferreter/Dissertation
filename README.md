# Dissertation Trading Project

This repo is the practical side of my dissertation. I am looking at whether intraday SPX, SPY and VIX data can say anything useful about the final hour of SPX trading, and whether those signals still make sense once I apply them to 0DTE options.

## Repository structure

I split the project up like this:

```text
data/                    Raw and derived data used by the main analysis
data_extended_2023_2026/ Separate longer-history dataset
notebooks/               Main research notebooks
notebooks/legacy/        Older experiments kept to show how the work developed
scripts/                 Python helpers used by the notebooks
scripts/legacy/          Older browser-automation experiments
models/                  Saved models, once the model cells are run
outputs/                 Tables, plots, manifests and dissertation drafts
docs/notebooks/          One guide for each notebook
docs/scripts/            One guide for each Python script
docs/workflow.md          A map of the full workflow
config.yaml              Shared paths and timing settings
requirements.txt         Python packages used by the project
```

I made the notebooks look for `config.yaml` to find the project root. This means the `data/...` and `outputs/...` paths should still work whether Jupyter starts in the root folder or inside `notebooks/`.

## Setup

1. Create and activate a Python environment.
2. Install the packages with `pip install -r requirements.txt`.
3. Only run `playwright install chromium` if you want to try the old browser scripts.
4. Copy `main.env.example` to `main.env` and add the API details locally. The real `main.env` should never be committed.
5. Start Jupyter from the project root or the `notebooks/` folder.

The market data is large, so it stays in `data/`, `data_extended_2023_2026/` and `outputs/` rather than being installed as part of a Python package.

## Main workflow

The [workflow guide](docs/workflow.md) gives a diagram and links to the guide for every stage. If I need to rebuild the project, this is the order I follow:

1. `notebooks/massive_database_starter.ipynb` - check the API access and make sure the storage setup works.
2. `notebooks/massive_database_raw_retrieve.ipynb` - download the underlying and option data in restartable batches.
3. `notebooks/aligned_eda.ipynb` - line up SPY, SPX and VIX without looking forward.
4. `notebooks/cleaning_modellingprep.ipynb` - clean the sessions and make the chronological splits.
5. `notebooks/dataset_Splitting.ipynb` - create the strict and relaxed datasets on the same dates.
6. `notebooks/modeling_baseline.ipynb` - compare simple rules, dummy models and ML baselines for RQ1-RQ3.
7. `notebooks/hyperparameters_tuning.ipynb` - tune the shortlisted models with time-aware validation.
8. `notebooks/hyperparameters_tuning_extended_robustness.ipynb` - check benchmarks, regimes, feature stability and confidence coverage.
9. `notebooks/extended_2023_2026_full_pipeline.ipynb` - repeat the underlying pipeline on the separate longer history.
10. `notebooks/lstm_intraday_sequence_extension.ipynb` - try the smaller LSTM sequence experiment.
11. `notebooks/rq4_economic_meaningfulness.ipynb` - check whether the signals pick out more useful SPX moves.
12. `notebooks/rq4_economic_meaningfulness_extended.ipynb` - repeat that RQ4 check on the longer history.
13. `notebooks/rq5_options_data_retrieval.ipynb` - lock the dates and download the required option bars.
14. `notebooks/rq5_options_backtest.ipynb` - run the fixed ATM strategy and mean-reversion comparison.
15. `notebooks/rq5_exit_strategy_sensitivity.ipynb` - check the planned stop, target and other exit rules.
16. `notebooks/rq5_strategy_robustness_and_multi_contract.ipynb` - look at concentration, path behaviour and multi-contract examples.

The `probe_massive_2021_2022_underlying_access.ipynb` notebook is only a small access check. I can run it before trying to extend the history. Everything under `notebooks/legacy/` is kept as background and isn't part of the final evidence.

## Checks I kept in place

- Features only use information available before the 15:00 ET decision time.
- SPX and VIX are matched backwards, not to a later minute.
- Train, Validation and Test are kept in date order.
- Imputation, clipping, scaling, regime cut-offs and model selection are fitted inside the relevant training data.
- I don't describe an already-viewed test result as if it were a fresh test.
- The RQ5 trading and cost rules are fixed before any future holdout is used.

## Documentation and outputs

Every notebook and executable script has its own guide under `docs/notebooks/` or `docs/scripts/`. The guides explain what I was trying to do, what went in, what came out and what I would do next. The actual saved evidence stays under `outputs/`. The planned model filenames are listed in [models/README.md](models/README.md).

The two tuning notebooks can save the chosen RQ1-RQ3 classical models with `SAVE_MODEL_ARTIFACTS`. The LSTM notebook has the same switch for its exploratory refits and scalers. I haven't included the binary model files in this documentation change; they appear when those cells are actually run.

The main things to keep in mind are the small daily sample, changing market conditions, missing historical option quotes, made-up execution penalties and the lack of a completely fresh post-selection holdout so far.
