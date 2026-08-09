# Legacy Preliminary EDA

**Executable:** `notebooks/legacy/EDA.ipynb`  
**Status:** Legacy exploratory work retained for provenance.

## Purpose

I used this earlier notebook to prototype intraday features, daily targets and simple models with yfinance data.

## Inputs

- SPX, VIX and SPY intraday data from yfinance

## Processing and rationale

- Clean sessions, combine tickers, engineer intraday features and inspect target behaviour.
- Fit preliminary logistic-regression checks.

## Outputs

- Displayed EDA tables and plots
- `outputs/legacy/feature_target_correlations.png` after path cleanup

## Findings and decisions

- This work helped define timing and feature ideas but was superseded by the minute-level Massive database pipeline.

## Limitations

- yfinance intraday history is short and the early notebook predates the final leakage controls.

## Next steps

- Use `notebooks/aligned_eda.ipynb` for the dissertation's maintained EDA.
