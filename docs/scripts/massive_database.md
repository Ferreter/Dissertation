# Massive Database Helpers

**Executable:** `scripts/massive_database.py`  
**Status:** Reusable support code for the maintained dissertation workflow.

## Purpose

I keep the common Massive API, normalisation, Parquet and DuckDB operations in one module so that every retrieval notebook follows the same rules.

## Inputs

- A Massive API key passed by the calling notebook.
- Tickers, date ranges and retrieval parameters.
- A local data root and DuckDB connection.

## Processing and rationale

- Wrap REST requests with pagination, retry and rate-limit handling.
- Normalise underlying, option and contract responses into consistent tables.
- Write partitioned daily Parquet files and record download status in DuckDB.
- Register views only when the corresponding Parquet dataset exists.
- Select near-ATM contracts and retrieve deterministic reference prices.

## Outputs

- Normalised pandas DataFrames returned to the notebooks.
- Partitioned files below `data/raw/` or the data root supplied by the caller.
- DuckDB ingestion-log rows and registered analytical views.

## Findings and decisions

- I use `timestamp_utc` as the canonical instant and keep New York wall-clock time for session filtering.
- Successful ticker-date downloads are skipped unless overwrite is explicitly requested.
- Empty and failed requests are logged rather than silently treated as valid observations.

## Limitations

- The helper cannot provide data outside the connected account's entitlements.
- Retry handling improves resilience but does not guarantee completion during long outages.
- API response-schema changes may require updates to the normalisation functions.

## Next steps

- Add focused unit tests if the retrieval layer is extended beyond the current dissertation scope.
- Keep endpoint and schema assumptions aligned with the provider documentation.
