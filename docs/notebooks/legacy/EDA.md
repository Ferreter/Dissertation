# Legacy Preliminary EDA

**Executable:** `notebooks/legacy/EDA.ipynb`  
**Status:** Legacy exploratory work retained for provenance.

## Purpose

I used this earlier notebook to prototype intraday features, daily targets and simple models with yfinance data.

## Workflow

```mermaid
flowchart LR
    A["Earlier derived market data"] --> B["Exploratory distributions and correlations"]
    B --> C["Notebook plots and interim figures"]
    C --> D["Superseded maintained EDA"]
```

## Inputs

- SPX, VIX and SPY intraday data from yfinance

## Processing and rationale

- Clean sessions, combine tickers, engineer intraday features and inspect target behaviour.
- Fit preliminary logistic-regression checks.

## Outputs

- Displayed EDA tables and plots
- Interim figures under `outputs/Images/Interim-Report/`

## Representative outputs

![Interim final-hour return distribution](../../../outputs/Images/Interim-Report/final-hour-returns.png)

*Provenance figure: an earlier exploratory view retained for the project history, not the final maintained evidence.*

![Interim top features](../../../outputs/Images/Interim-Report/top-features.png)

*Provenance figure: an early feature summary superseded by the maintained EDA and modelling notebooks.*

## Findings and decisions

- This work helped define timing and feature ideas but was superseded by the minute-level Massive database pipeline.

## Limitations

- yfinance intraday history is short and the early notebook predates the final leakage controls.

## Next steps

- Use `notebooks/aligned_eda.ipynb` for the dissertation's maintained EDA.
