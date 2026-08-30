# How the Dissertation Workflow Fits Together

This page is my quick map of the whole artefact. I wrote the individual notebook guides so I can open one file and understand what it needs, what it does and what came out of it without reading every code cell first. This page does the same job at project level.

The main workflow is numbered from 01 to 18. The files under `legacy/` are earlier ideas and experiments that I kept for provenance. They are useful for showing how the topic developed, but they are not mixed into the final evidence.

## The full route

```mermaid
flowchart TD
    A["01-02: retrieve and store underlying data"] --> B["03: align SPY, SPX and VIX and explore them"]
    B --> C["04-05: clean sessions and freeze chronological variants"]
    C --> D["06: simple RQ1-RQ3 baselines"]
    D --> E["07-08: nested tuning, robustness and saved classical models"]
    E --> F["12: RQ4 confidence, magnitude and large-move checks"]
    E --> G["09-10: separate longer-history sensitivity run"]
    G --> H["11: exploratory LSTM comparison"]
    G --> I["13: repeat RQ4 on the longer history"]
    F --> J["14: discover and download frozen RQ5 option contracts"]
    J --> K["15: fixed 0DTE backtest"]
    K --> L["16-17: exit, concentration and multi-contract checks"]
    L --> M["18: one post-freeze evaluation on newer data"]
```

## If I only want to reproduce one part

### Getting and preparing the data

I start with [01 - the database starter](notebooks/01_massive_database_starter.md), [02 - raw retrieval](notebooks/02_massive_database_raw_retrieve.md) and [the shared database helper](scripts/massive_database.md). Notebook 03 then aligns the sources backwards in time, which is important because it prevents a later SPX or VIX value from being matched to an earlier decision row. Notebooks [04](notebooks/04_cleaning_modellingprep.md) and [05](notebooks/05_dataset_Splitting.md) turn that aligned minute data into the final daily feature rows and chronological Train, Validation and Test variants.

![How old the matched SPX observations are](../outputs/eda_figures/02_spx_alignment_staleness.png)

*This is one of the checks I use before modelling. A matched value can exist and still be too stale to trust.*

![Final-hour return distribution](../outputs/eda_figures/05_final_hour_return_distribution.png)

*This gives a feel for the noisy target distribution and the relatively rare large-move days RQ3 is trying to identify.*

### Building RQ1, RQ2 and RQ3

[06 - baseline modelling](notebooks/06_modeling_baseline.md) sets honest simple comparisons before tuning. [07 - nested tuning](notebooks/07_hyperparameters_tuning.md) selects and evaluates the classical models chronologically, while [08 - robustness and saving](notebooks/08_hyperparameters_tuning_extended_robustness.md) checks whether those conclusions survive alternative assumptions and creates the canonical artifacts. The [model helper](scripts/model_artifacts.md) handles atomic saving, reload checks, hashes and manifests; it does not fit or select anything itself.

![RQ1 outer-fold balanced accuracy](../outputs/hyperparameter_tuning/figures/rq1_nested_balanced_accuracy.png)

*The fold-to-fold movement matters more to me than one neat average because it shows how unstable direction prediction can be through time.*

![RQ3 feature importance](../outputs/hyperparameter_tuning/figures/rq3_outer_fold_permutation_importance.png)

*This is the output that directly helps answer which momentum, volatility and price-positioning features mattered most for predicting large final-hour moves.*

The model filenames, training scope and warnings are summarised in [the model README](../models/README.md). Saved classical models use development data only. The Test split and fresh holdout are excluded from fitting.

### Longer-history and sequence-model checks

[09](notebooks/09_probe_massive_2021_2022_underlying_access.md) checks whether the older provider history is genuinely available before I promise a bigger sample. [10](notebooks/10_extended_2023_2026_full_pipeline.md) is a separate period-sensitivity run rather than an extension that silently overwrites the original results. [11](notebooks/11_lstm_intraday_sequence_extension.md) compares an exploratory LSTM with matched classical models using chronological sequence data.

I keep this evidence separate because changing the modelling period can change the conclusion. The LSTM development refits are saved for reproducibility, but they are labelled exploratory rather than independently evaluated final models.

### Turning predictions into an economic question

[12 - RQ4](notebooks/12_rq4_economic_meaningfulness.md) asks whether confidence, predicted magnitude and large-move flags concentrate more useful opportunities. [13](notebooks/13_rq4_economic_meaningfulness_extended.md) repeats the same checks on the separate longer-history run instead of redesigning the rule around it.

![RQ4 opportunity lift](../outputs/rq4_economic_meaningfulness/figures/rq4_30bps_opportunity_lift.png)

*This is where the project moves from “was a label predicted?” to “did the filter concentrate sessions with a larger realised final-hour move?”*

These notebooks still use the underlying index outcome. They do not claim that a filtered day automatically becomes a profitable option trade.

### Testing the RQ5 option strategy

[14](notebooks/14_rq5_options_data_retrieval.md) freezes the selected dates and discovers the dated SPXW contracts without looking at their eventual P&L. [15](notebooks/15_rq5_options_backtest.md) uses the fixed entry, exit, strike and synthetic cost rules. [16](notebooks/16_rq5_exit_strategy_sensitivity.md) replays stops and targets, while [17](notebooks/17_rq5_strategy_robustness_and_multi_contract.md) checks concentration, recovery, direction and multi-contract scaling.

![RQ5 cumulative P&L under medium costs](../outputs/rq5_options_trading/figures/rq5_cumulative_pnl_medium_cost.png)

*The line finishes positive, but there are only 17 trades and a large part of the result comes from a small number of winners.*

![RQ5 random-direction check](../outputs/rq5_options_trading/figures/rq5_random_direction_monte_carlo.png)

*This gives the signal direction a more useful reality check than looking at profit by itself.*

The main exact numbers are in the [strategy summary](../outputs/rq5_options_trading/tables/rq5_strategy_summary.csv), [paired ML comparison](../outputs/rq5_options_trading/tables/rq5_paired_ml_vs_mean_reversion_summary.csv) and [profit-concentration table](../outputs/rq5_options_trading/tables/rq5_profit_concentration.csv).

### The newer post-freeze check

[18 - fresh holdout evaluation](notebooks/18_fresh_holdout_end_to_end_evaluation.md) has now been run for 20 July to 19 August 2026. It rebuilds the same features, checks the model hashes and scores the frozen workflow without fitting again. RQ1 was poor, RQ2 was limited, and RQ3 plus the combined filter found one very large down day. That one selected option trade was highly profitable in the hypothetical backtest, but one trade is a case study, not evidence of a stable strategy.

![Fresh RQ1 and RQ3 confusion matrices](../outputs/fresh_holdout_post_2026_07_17/20260718_20260819/figures/fresh_holdout_confusion_matrices.png)

*The newer data gives a mixed picture rather than one tidy success story. I think that makes it more useful to discuss honestly.*

## The rules I keep fixed

- Train + Validation is the largest allowed fitting sample for the saved classical models. Test and post-17 July 2026 rows stay out.
- RQ1 and RQ3 thresholds come from chronological development predictions, not from looking at Test outcomes.
- The exploratory LSTM uses its internal chronological validation block for epoch and threshold choices before a clearly labelled development refit.
- RQ5 dates, option side, strike offsets, cost cases and exit definitions are decided before the matching option outcome is used.
- The July-August 2026 holdout is now consumed. I can report it, but I cannot tune on it and still call the same period fresh.
- Updating these guides does not change a notebook, model or stored research result. It only makes the existing workflow easier to follow.

## Where the older files fit

The five [legacy notebook guides](notebooks/legacy/01_EDA.md) and two legacy script guides document yfinance experiments, weekend-gap ideas and gamma-page browser captures. They show how I arrived at the final topic, but none of their values feed the maintained datasets, models or RQ5 trade log.
