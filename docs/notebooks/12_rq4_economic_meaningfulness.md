# RQ4 Economic Meaningfulness

**Executable:** `notebooks/12_rq4_economic_meaningfulness.ipynb`
**Status:** I use this in the main dissertation workflow.

## Purpose

A model score on its own doesn't say whether a signal is useful. Here I check whether the RQ1-RQ3 out-of-fold predictions pick out days with bigger or more predictable final-hour SPX moves.

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

- I check direction accuracy at different realised moves and confidence levels.
- I combine the RQ1 direction, RQ2 magnitude and RQ3 large-move signals in a few fixed ways.
- I then look at opportunity lift, regimes and moving-block bootstrap ranges.

## Outputs

- `outputs/rq4_economic_meaningfulness/`
- RQ4 tables, plots, bootstrap summary and dissertation draft

## Representative outputs

![Confidence and economic opportunity](../../outputs/rq4_economic_meaningfulness/figures/rq4_confidence_vs_accuracy_and_move_size.png)

*This plot checks whether higher RQ1 confidence coincides with better direction accuracy and larger realised moves.*

![Thirty-basis-point opportunity lift](../../outputs/rq4_economic_meaningfulness/figures/rq4_30bps_opportunity_lift.png)

*This plot shows the precision and lift of selected signals for economically larger opportunities.*

## Findings and decisions

- Overall RQ1 balanced accuracy was 0.532, while the matched 60-minute mean-reversion rule reached 0.567.
- At 30% coverage the RQ1 result rose to 0.592 across 93 sessions, although those days didn't also have a bigger average realised move.
- The strongest three-model rule found a more concentrated set of opportunities in development. I treat that as interesting, not as proof of profit.

## Limitations

- The best combined rule came from development checks and hasn't been confirmed independently.
- This notebook doesn't include option premiums, spreads, slippage, commission or time decay.

## Next steps

- I freeze the opportunity rule here, then test what it looks like with actual option bars in RQ5.
