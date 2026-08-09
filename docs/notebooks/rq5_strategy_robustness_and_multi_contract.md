# RQ5 Strategy Robustness and Multi-Contract Scaling

**Executable:** `notebooks/rq5_strategy_robustness_and_multi_contract.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I examine profit concentration, path recovery, timing, option side, random-direction benchmarks and multi-contract scale-out rules.

## Inputs

- Primary RQ5 trade log
- Selected contracts, candidate sessions and option-minute bars

## Processing and rationale

- Run top-winner and leave-one-out concentration tests.
- Measure recovery after stop or target touches and P&L development through the hour.
- Compare multi-contract rules with holding the same number of contracts and report hypothetical account exposure.

## Outputs

- `outputs/rq5_options_trading/strategy_robustness/`
- Concentration, recovery, timing, random-direction, break-even-cost and multi-contract tables

## Findings and decisions

- The largest trade contributed about 41.6% of the primary strategy's net P&L.
- Among trades touching -50%, about 44.4% recovered to entry and 22.2% later reached +100%, showing why hard stops materially alter 0DTE outcomes.
- Multi-contract rules increased raw dollars through added capital but underperformed equal-size hold-to-close counterfactuals in the recorded comparison.

## Limitations

- The same 17 candidate dates underpin most robustness checks.
- Hypothetical account exposures are descriptive and not personalised investment advice.

## Next steps

- Keep the primary strategy frozen and evaluate it only on genuinely fresh option data.
