# Look-Ahead-Safe Alignment and Exploratory Data Analysis

**Executable:** `notebooks/aligned_eda.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I align SPY, SPX and VIX minute observations without using future information, build the daily modelling table and examine the initial relationships with the final-hour SPX target.

## Workflow

```mermaid
flowchart LR
    A["Raw SPY, SPX and VIX minutes"] --> B["Backward alignment and EDA"]
    B --> C["Aligned Parquet data and figures"]
    C --> D["Cleaning and modelling preparation"]
```

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

## Representative outputs

![SPX alignment staleness](../../outputs/eda_figures/02_spx_alignment_staleness.png)

*Figure: the age of backward-looking SPX matches, used to confirm that the alignment is timely without looking forward.*

![Feature-target correlations](../../outputs/eda_figures/15_feature_target_correlations.png)

*Figure: the univariate relationships that guided later modelling while remaining descriptive rather than causal.*

## Findings and decisions

- The recorded run created 194,495 aligned minute rows, audited 501 sessions and retained 496 daily modelling sessions.
- Individual feature correlations with the final-hour return were weak, so I treat the EDA as evidence for careful validation rather than strong standalone predictability.
- The look-ahead checks passed and no Massive API calls were needed for this stage.

## Limitations

- As-of matching can retain stale observations within the allowed tolerance.
- EDA relationships are descriptive and do not establish out-of-sample predictive value.

## Next steps

- Review problem sessions, remove partial sessions and freeze chronological modelling splits.
