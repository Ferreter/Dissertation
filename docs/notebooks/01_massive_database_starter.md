# 01 - Massive API and Database Setup

**File:** [notebooks/01_massive_database_starter.ipynb](../../notebooks/01_massive_database_starter.ipynb)

**Role in the project:** This is a small validation notebook used before starting the full data retrieval.

## Overview

This notebook provides a preliminary systems check. I use a few small requests to make sure the API key works, see which endpoints the subscription actually allows, and confirm that Parquet and DuckDB are saving things in the layout expected by the later notebooks. Any access, schema or storage issue is resolved here before the full retrieval begins.

## Workflow

```mermaid
flowchart LR
    A["API key and a few test dates"] --> B["Small access and schema checks"]
    B --> C["Sample files and DuckDB views"]
    C --> D["Full raw-data download"]
```

Nothing from here is treated as a modelling result. It is an early warning system for account permissions, schema changes and local storage problems.

## Inputs

- `main.env`, which supplies `MASSIVE_API_KEY` without putting it in the notebook.
- A deliberately small set of recent dates and tickers.
- The Massive aggregates, option-contract and snapshot endpoints.
- The helper functions in `scripts/massive_database.py`.

## Processing

The requests are deliberately small. The aim is to identify access or schema problems before the full retrieval begins, rather than collect the research dataset at this stage.

- I probe SPY, SPX and VIX aggregates and print enough of the response to check the fields and timestamps.
- I try the option endpoints separately because an account can have underlying data access without the historical option data I need.
- I normalise a small sample, write it to the same partitioned layout used later, and check that DuckDB can register and query it.
- I leave empty responses and entitlement errors visible. I do not turn them into fake zero-row successes.

It also provides an efficient way to check whether the subscription or API behaviour has changed between retrieval runs.

## Outputs

- Small test partitions under `data/raw/`.
- The local database at `data/market.duckdb`.
- Displayed endpoint checks and ingestion-log rows inside the notebook.
- A confirmed storage path that the full retrieval notebook can reuse.

## Key outputs and figures

The most useful files to open after the test are the [local DuckDB database](../../data/market.duckdb) and the [underlying session audit](../../data/derived/underlying_session_audit.parquet). The audit is produced further downstream, but it is the easiest way to see whether the storage setup tested here eventually produced complete sessions.

I also check the notebook's displayed contract and snapshot samples. They are more useful than a screenshot because I can see the exact returned columns, the ticker format and any entitlement message.

## Findings and decisions

- The account can expose different amounts of history for underlyings, contracts and option bars, so I test them separately.
- A successful HTTP response is not enough; I also need rows, sensible timestamps and a file that can be queried again.
- Keeping one shared storage pattern here stopped the later notebooks from inventing their own folder structures.

## Limitations and considerations

- This only checks a handful of dates. It cannot prove that every historical session is available or complete.
- Massive access depends on the subscription and rolling history window, so an old successful run does not guarantee the same result today.
- The notebook checks retrieval and storage, not whether the data is economically useful.

## Next stage

If the probes, saved sample and DuckDB query all look normal, I move to [02 - raw retrieval](02_massive_database_raw_retrieve.md). If they do not, I fix the access or schema issue here instead of debugging it halfway through the main download.
