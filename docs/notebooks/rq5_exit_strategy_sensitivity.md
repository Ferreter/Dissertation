# RQ5 Exit Strategy Sensitivity

**Executable:** `notebooks/rq5_exit_strategy_sensitivity.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I compare hold-to-close with a pre-specified 50% stop-loss and 100% take-profit, then use other exit rules only as sensitivities.

## Workflow

```mermaid
flowchart LR
    A["Frozen RQ5 trade paths"] --> B["Apply pre-specified stops, targets and exits"]
    B --> C["Paired exit-policy evidence"]
    C --> D["Strategy robustness"]
```

## Inputs

- RQ5 candidate sessions, contract selection and option-minute bars
- Frozen execution-cost scenarios

## Processing and rationale

- Simulate path-dependent exits with conservative same-minute ambiguity handling.
- Compare policies on the same trades, strikes and costs.
- Record trigger frequency, holding time, P&L and drawdown effects.

## Outputs

- `outputs/rq5_options_trading/exit_strategy_sensitivity/`
- Exit-policy, paired-comparison, trigger and path-diagnostic tables

## Representative outputs

![Hold versus stop and target](../../outputs/rq5_options_trading/figures/rq5_hold_vs_stop50_tp100.png)

*Figure: the paired trade-level effect of the principal stop-loss and take-profit rule.*

![Exit-policy risk and return](../../outputs/rq5_options_trading/figures/rq5_exit_policy_risk_return.png)

*Figure: the return and drawdown trade-offs across the pre-specified exit policies.*

## Findings and decisions

- The medium-cost ATM hold-to-close baseline produced $9,551 in the recorded comparison.
- The primary stop/take-profit rule changes both return and drawdown, but I compare it with holding the same trades rather than selecting the best rule after seeing results.
- One-minute ambiguity is handled conservatively by assuming the stop is reached first.

## Limitations

- Minute OHLC bars do not reveal the within-minute order of stop and target touches.
- The alternative policies are development-period sensitivities, not independently validated strategies.

## Next steps

- Assess dependence on extreme winners, post-stop recovery and equal-capital multi-contract counterfactuals.
