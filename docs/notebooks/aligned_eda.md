# Look-Ahead-Safe Alignment and Exploratory Data Analysis

**Executable:** `notebooks/aligned_eda.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I align SPY, SPX and VIX minute observations without using future information, build the daily modelling table and examine the initial relationships with the final-hour SPX target.

## Inputs

- `data/market.duckdb`
- SPY, SPX and VIX one-minute observations

## Processing and rationale

- Use SPY as the minute clock and backward as-of match SPX and VIX within two minutes.
- Audit regular-session completeness and create features using bars strictly before 15:00 ET.
- Summarise distributions, missingness, class balance, time patterns and feature correlations.

## Outputs

- `data/derived/aligned_underlyings_1min.parquet`
- `data/derived/underlying_session_audit.parquet`
- `data/derived/daily_underlying_model_dataset.parquet`
- `outputs/eda_figures/`

## Findings and decisions

- The recorded run created 194,495 aligned minute rows, audited 501 sessions and retained 496 daily modelling sessions.
- Individual feature correlations with the final-hour return were weak, so I treat the EDA as evidence for careful validation rather than strong standalone predictability.
- The look-ahead checks passed and no Massive API calls were needed for this stage.

## Limitations

- As-of matching can retain stale observations within the allowed tolerance.
- EDA relationships are descriptive and do not establish out-of-sample predictive value.

## Next steps

- Review problem sessions, remove partial sessions and freeze chronological modelling splits.
