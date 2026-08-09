# RQ5 SPX 0DTE Option Data Retrieval

**Executable:** `notebooks/rq5_options_data_retrieval.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I freeze the RQ5 candidate dates, discover same-day SPX contracts and download the minute bars required for the backtest.

## Inputs

- RQ4 combined outer-fold predictions
- Massive API credentials
- Frozen confidence, magnitude and large-move filters

## Processing and rationale

- Select candidate sessions without looking at option outcomes.
- Discover ATM and 5-30 point OTM calls and puts for each date.
- Download 14:55-16:00 minute aggregates and audit usable entry and exit windows.

## Outputs

- `outputs/rq5_options_trading/raw/rq5_option_minute_bars.parquet`
- Contract-selection, download-log, quality and candidate-session tables
- `outputs/rq5_options_trading/rq5_retrieval_manifest.json`

## Findings and decisions

- The recorded run downloaded 15,279 option-minute rows.
- Seventeen call and seventeen put contracts were usable at each tested strike offset, while three early contracts per side had no bars.
- The later backtest uses saved contracts and bars rather than rediscovering them after seeing P&L.

## Limitations

- Trade-derived aggregates are not historical NBBO quotes.
- The rolling Massive history window can make older candidate dates unavailable.

## Next steps

- Apply the frozen entry, exit, execution-cost and comparator rules in the RQ5 backtest.
