
### RQ5: 0DTE Options Trading Evaluation

The RQ5 backtest converted the previously developed RQ1–RQ3 opportunity
signals into same-day SPX option positions. Trades were restricted to sessions
meeting the pre-specified high-confidence RQ1, RQ2 predicted-magnitude, and
RQ3 large-movement conditions. The primary specification used the nearest
available ATM 0DTE contract, with RQ1 determining Call versus Put direction.

In the frictionless reference case, the ATM ML strategy produced total P&L of $11855.00 across 17 trades. The primary ML strategy remained profitable under the pre-specified medium_cost execution-cost assumptions. Under this primary cost scenario, the ML
strategy completed 17 trades, generated total P&L of
$9551.00, achieved a win rate of
64.7%, and had mean return on premium of
53.5%. The corresponding profit factor
was 2.843 and maximum dollar drawdown was
$2143.20.

On the same opportunity dates and ATM contract specification, the 60-minute mean-reversion comparator generated at least as much cumulative P&L as the ML direction. This comparison is important because the simple
mean-reversion rule previously outperformed the machine-learning model on
unconditional directional balanced accuracy.

The lowest median entry-capital requirement among the tested strike distances occurred at approximately 30 SPX points OTM ($126.50 median capital at risk). Its near-total-loss rate was 82.4%. This highlights the trade-off between affordability and the greater probability of substantial premium loss in farther-OTM 0DTE options.

Because historical NBBO quote data were unavailable under the Options Starter
dataset, exact historical bid-ask execution could not be reconstructed.
The results therefore use trade-derived minute aggregates together with
pre-specified adverse-execution and commission sensitivity scenarios.
Consequently, RQ5 should be concluded from the consistency of profitability
across these cost assumptions, the comparison against the mean-reversion
benchmark, and the stability of results across strike distances rather than
from the frictionless result alone.
