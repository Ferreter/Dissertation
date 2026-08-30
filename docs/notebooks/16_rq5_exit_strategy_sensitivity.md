# 16 - RQ5 Exit Strategy Sensitivity

**File:** [notebooks/16_rq5_exit_strategy_sensitivity.ipynb](../../notebooks/16_rq5_exit_strategy_sensitivity.ipynb)

**Role in the project:** This replays the same RQ5 trades with pre-specified exit rules. It is a sensitivity study, not a new strategy search.

## Overview

Hold-to-close can conceal substantial adverse movement before the final exit, while a stop or target may close the position earlier. This notebook evaluates each saved option minute and compares holding with the main -50% stop/+100% target rule and several clearly labelled alternatives. Every policy uses the same dates, contracts, direction and execution-cost scenario.

## Workflow

```mermaid
flowchart LR
    A["Saved RQ5 option paths"] --> B["Minute-by-minute exit simulation"]
    B --> C["Paired policy summaries"]
    C --> D["Robustness diagnosis"]
```

Using paired trades is important. Comparing one exit rule on a different set of dates would mix the effect of the policy with the effect of the sample.

## Inputs

- The frozen RQ5 trade dates and contract map.
- Option-minute OHLC paths.
- The same synthetic execution-cost scenarios as notebook 15.
- Hold-to-close and the pre-specified stop/target policy definitions.

## Processing

I replay the path rather than trying to infer stops from only the final entry and exit prices.

- Every minute after entry is checked for the stop and target levels.
- If one OHLC bar could have touched both, I assume the stop happened first. That is deliberately conservative.
- I record exit reason, exit time, holding length, favourable excursion and adverse excursion.
- Each policy is compared against holding the exact same trade.
- Cost, strike and policy summaries are kept separate so I can see whether a result depends on one assumption.

The extra policies help explain path dependence. I do not pick whichever one has the highest retrospective P&L and call it the new main rule.

## Outputs

- Minute-path simulations under `exit_strategy_sensitivity/`.
- Primary paired hold-versus-policy tables.
- Exit-reason, strike, cost and path-diagnostic summaries.
- An exit-strategy manifest and generated draft.

## Key outputs and figures

![Hold versus stop/target](../../outputs/rq5_options_trading/figures/rq5_hold_vs_stop50_tp100.png)

*Each point is the same trade under two exit rules, which is much clearer than comparing unrelated totals.*

![Exit-policy risk and return](../../outputs/rq5_options_trading/figures/rq5_exit_policy_risk_return.png)

*This shows the return/drawdown trade-off instead of ranking policies by profit alone.*

The [primary ATM policy table](../../outputs/rq5_options_trading/tables/rq5_exit_policy_primary_atm_medium_cost.csv) contains the main comparison. [Paired versus hold](../../outputs/rq5_options_trading/tables/rq5_exit_policy_paired_vs_hold.csv) shows the trade-level differences, while [option path diagnostics](../../outputs/rq5_options_trading/tables/rq5_option_path_diagnostics.csv) provides the MFE, MAE and timing evidence used later.

## Findings and decisions

- Hold-to-close produced the larger primary sample profit, but it also experienced greater interim adverse movement and a larger drawdown.
- The -50% stop/+100% target rule changed both the shape and timing of returns rather than simply reducing every loss.
- Several trades recovered after touching the stop level, so the hard stop could crystallise losses that later reversed.
- The conservative same-bar assumption prevents ambiguous OHLC bars from flattering the target rule.

## Limitations and considerations

- One-minute OHLC does not reveal the order of prices within a bar.
- The exit policies are development sensitivities and have very few trades.
- A stop simulated on trade aggregates still cannot reproduce queue position or an executable quote.

## Next stage

The path diagnostics feed [17 - robustness and multi-contract checks](17_rq5_strategy_robustness_and_multi_contract.md), where I look at recovery, concentration and scaling more directly.
