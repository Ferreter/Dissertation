# RQ5 0DTE SPX Options Backtest

**Executable:** `notebooks/rq5_options_backtest.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I test whether the frozen RQ1-RQ3 opportunity rule produces economically meaningful 0DTE option results after execution-cost sensitivity.

## Workflow

```mermaid
flowchart LR
    A["Frozen signals and audited option bars"] --> B["Simulate ATM strategy, comparator and costs"]
    B --> C["Trade logs and RQ5 evidence"]
    C --> D["Exit and robustness checks"]
```

## Inputs

- Saved RQ5 option bars and contract map
- Frozen candidate sessions
- RQ1 direction and 60-minute mean-reversion comparator

## Processing and rationale

- Choose the pre-specified ATM contract and deterministic entry/exit bars.
- Apply frictionless, low, medium and severe adverse-execution scenarios.
- Compare ML and mean reversion, affordability, strike offsets, regimes and bootstrap uncertainty.

## Outputs

- `outputs/rq5_options_trading/backtest/`
- RQ5 summary, comparator, cost, affordability, regime and bootstrap tables
- `outputs/rq5_options_trading/rq5_backtest_manifest.json`

## Representative outputs

![Cumulative PnL under medium costs](../../outputs/rq5_options_trading/figures/rq5_cumulative_pnl_medium_cost.png)

*Figure: the cumulative path of the frozen strategy after the medium transaction-cost assumption.*

![OTM affordability sensitivity](../../outputs/rq5_options_trading/figures/rq5_otm_affordability_sensitivity.png)

*Figure: the trade-off between cheaper contracts and the resulting strategy outcomes.*

## Findings and decisions

- The ATM ML strategy produced $11,855 before costs across 17 historical trades and remained profitable under the pre-specified medium-cost assumptions.
- On the same dates, ML did not consistently outperform the 60-minute mean-reversion direction benchmark.
- Bootstrap intervals were wide, so the positive historical P&L is not treated as a precise expectation.

## Limitations

- There are only 17 primary trades and no historical bid-ask quotes.
- Synthetic execution penalties, development-period selection and 0DTE path dependence limit generalisation.

## Next steps

- Test the pre-specified stop/take-profit alternative and examine concentration and path dependence.
