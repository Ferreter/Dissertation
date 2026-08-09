# RQ4 Economic Meaningfulness

**Executable:** `notebooks/rq4_economic_meaningfulness.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I test whether the out-of-fold RQ1-RQ3 predictions concentrate larger or more directionally predictable SPX moves into a smaller set of sessions.

## Workflow

```mermaid
flowchart LR
    A["Original out-of-fold RQ1-RQ3 signals"] --> B["Confidence, move-size, lift and bootstrap analysis"]
    B --> C["RQ4 economic evidence"]
    C --> D["Options-strategy evaluation"]
```

## Inputs

- Selected-winner outer-fold predictions
- Strict and relaxed daily source data
- Tuned-winner summary

## Processing and rationale

- Measure directional accuracy conditional on realised movement and confidence.
- Combine RQ1 direction, RQ2 magnitude and RQ3 large-move signals.
- Estimate opportunity lift, regime sensitivity and moving-block bootstrap uncertainty.

## Outputs

- `outputs/rq4_economic_meaningfulness/`
- RQ4 tables, plots, bootstrap summary and dissertation draft

## Representative outputs

![Confidence and economic opportunity](../../outputs/rq4_economic_meaningfulness/figures/rq4_confidence_vs_accuracy_and_move_size.png)

*Figure: whether higher RQ1 confidence coincides with better direction accuracy and larger realised moves.*

![Thirty-basis-point opportunity lift](../../outputs/rq4_economic_meaningfulness/figures/rq4_30bps_opportunity_lift.png)

*Figure: the precision and lift of selected signals for economically larger opportunities.*

## Findings and decisions

- Unconditional RQ1 balanced accuracy was 0.532 versus 0.567 for the matched 60-minute mean-reversion rule.
- At 30% confidence coverage, RQ1 balanced accuracy rose to 0.592 across 93 sessions, but those sessions did not also have a larger mean realised move.
- The strongest qualifying three-model rule showed development-period enrichment, which I treat as potential relevance rather than proof of profitability.

## Limitations

- The strongest combined rule is identified from development diagnostics and is not independently confirmed.
- This stage does not model option premiums, spreads, slippage, commissions or time decay.

## Next steps

- Freeze the opportunity rule and test it at option level in RQ5.
