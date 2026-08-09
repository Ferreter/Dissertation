# Legacy Preliminary EDA

**Executable:** `notebooks/legacy/EDA.ipynb`  
**Status:** I kept this as provenance from an older experiment. It isn't part of the final dissertation evidence.

## Purpose

This is an older EDA notebook where I first tried out intraday features, daily targets and some very simple models using yfinance.

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

- I clean the sessions, combine the tickers and try a first set of intraday features.
- I also run a few early logistic-regression checks to see whether the target setup makes sense.

## Outputs

- Displayed EDA tables and plots
- Interim figures under `outputs/Images/Interim-Report/`

## Representative outputs

![Interim final-hour return distribution](../../../outputs/Images/Interim-Report/final-hour-returns.png)

*This is an older project plot showing an earlier exploratory view retained for the project history, not the final maintained evidence.*

![Interim top features](../../../outputs/Images/Interim-Report/top-features.png)

*This is an older project plot showing an early feature summary superseded by the maintained EDA and modelling notebooks.*

## Findings and decisions

- It was useful for working out the timing and feature ideas, but the later Massive minute-data pipeline replaced it.

## Limitations

- yfinance only gave me a short intraday history, and this notebook was written before I added the final leakage checks.

## Next steps

- I keep this as background only. `notebooks/aligned_eda.ipynb` is the maintained EDA.
