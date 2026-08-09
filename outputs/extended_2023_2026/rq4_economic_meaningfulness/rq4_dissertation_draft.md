
### RQ4: Economic Meaningfulness of the Predictive Signals

Unconditional directional forecasting did not outperform the 60-minute mean-reversion comparator on the same outer-fold observations. The selected RQ1 model achieved unconditional balanced accuracy
of 0.544, compared with
0.548 for the 60-minute mean-reversion rule.
Therefore, the machine-learning direction model should not be considered
economically useful solely on the basis of its unconditional directional score.

At the pre-specified 30% confidence coverage level, balanced accuracy increased to 0.556 across 132 sessions, but the selected observations did not also show a larger mean realised move. This provides only partial evidence of economic usefulness.

The RQ2 and RQ3 models were additionally used as opportunity filters rather
than as direct trading strategies. RQ2 supplied an estimate of absolute movement
magnitude, while RQ3 identified sessions with elevated large-movement risk.
The highest observed development-period enrichment for a 30+ bps move among rules retaining at least 10 sessions was 3.43x (10 sessions) under 'All three with RQ2 >= 30 bps'. Because this rule is identified from development-period diagnostics, it should not be interpreted as independently confirmed.

Overall, RQ4 should be interpreted in terms of whether the models concentrate
larger and more directionally predictable SPX movements into a smaller subset
of sessions. Any such enrichment is evidence of potential economic relevance,
not evidence of profitability. Whether the identified opportunities can overcome
0DTE option premiums, bid-ask spreads, slippage, commissions, rapid time decay
and realistic execution constraints remains an empirical question for RQ5.
