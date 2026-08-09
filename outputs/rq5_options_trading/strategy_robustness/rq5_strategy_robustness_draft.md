
### RQ5 Strategy Robustness and Multi-Contract Sensitivity

The primary ATM ML strategy produced total historical P&L of
$9551.00. Profit-concentration analysis showed that
the single largest trade accounted for approximately 41.6% of
net total P&L. Leave-one-trade-out and top-winner-removal tests were therefore
used to assess whether the result remained positive when unusually favourable
observations were excluded.

Path analysis also demonstrated why fixed stop-loss and take-profit rules can
materially change 0DTE outcomes. Among trades that touched the −50% level,
approximately 44.4% later recovered to the original
entry premium and 22.2% subsequently reached +100%.
Consequently, a hard stop can remove some positions that would later become
large winners. Conversely, the post-+100% analysis measures how much additional
upside remained after a conventional doubling-of-premium take-profit level had
already been reached.

The time-of-hour analysis was used to identify when the economic value of the
selected opportunities emerged between 15:00 and the close, while the
same-date random-direction Monte Carlo separated the value of directional
prediction from the value of the opportunity-selection filter.

The pre-specified two-contract scale-out rule generated total P&L of $11554.99 across 17 opportunities, with mean return on total initial premium of 33.0% and median capital requirement of $1893.00. Compared with simply buying two contracts and holding both to close, the partial-profit/runner logic reduced total historical P&L by $7547.01. This indicates that any improvement in raw dollar P&L from holding multiple contracts should not be confused with value added by the exit rule itself.

The multi-contract analysis should be interpreted cautiously. Buying two or
three SPX contracts increases the required premium approximately in proportion
to position size, meaning a strategy may earn more dollars while becoming less
appropriate for a small retail account. For this reason, the study reports both
dollar P&L and return on total initial premium, together with hypothetical
account-exposure measures.

Overall, these robustness tests are intended to explain the source and
fragility of the RQ5 backtest rather than to optimise a new strategy on the
same small historical sample.
