# Legacy Weekend Gap Analysis

**Executable:** `notebooks/legacy/yfinance_weekend_gap_analysis.ipynb`  
**Status:** Legacy exploratory work retained for provenance.

## Purpose

I compare Friday closes with Monday opens and subsequent Monday movement as an early trading-pattern exploration.

## Inputs

- Daily market data downloaded with yfinance

## Processing and rationale

- Pair consecutive Friday and Monday observations and chart gaps and Monday moves.

## Outputs

- Displayed paired tables and charts

## Findings and decisions

- The notebook is exploratory provenance and is not used by the final SPX prediction pipeline.

## Limitations

- The live download period changes over time and the analysis is not a controlled backtest.

## Next steps

- Keep the experiment separate from the dissertation results.
