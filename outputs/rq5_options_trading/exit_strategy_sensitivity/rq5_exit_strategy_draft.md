
### RQ5 Exit-Strategy Sensitivity

The original RQ5 analysis used a simple hold-to-close exit so that the
economic value of the predictive signal could be evaluated without introducing
additional trading-rule complexity. A second analysis therefore examined
whether an explicit retail-style risk-management policy changed the results.

The primary alternative used a hard stop-loss at 50% below the executed
option premium and a take-profit at 100% above entry. If neither threshold was
reached, the position was closed near the end of the final trading hour.

For the ML ATM strategy under the medium-cost execution assumptions,
holding to close generated total P&L of
$9551.00, whereas the −50%/+100% policy generated
$3025.71. Using the −50% stop / +100% take-profit rule reduced historical total P&L by $6525.29 relative to holding the ATM option until the end-of-hour exit. However, absolute maximum drawdown improved by $597.06.
The stop/target strategy produced a win rate of
52.9%, mean return on premium of
17.7%, and median holding time of
17.0 minutes.

Because one-minute option aggregates do not reveal whether the high or low
occurred first within a minute, a conservative stop-first assumption was used
when both thresholds were touched in the same bar. There were
0 such ambiguous simulated observations across the primary
comparison table.

The additional stop, target, break-even, trailing-stop and fixed-time exit
rules should be interpreted as sensitivity analyses rather than as independent
strategies selected after observing historical profitability. Given the small
number of trade opportunities, the purpose of this analysis is to determine
whether reasonable risk management materially changes the original RQ5
conclusion, not to optimise an exit rule on the development sample.
