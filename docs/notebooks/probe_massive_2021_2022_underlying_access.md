# Massive 2021-2022 Access Probe

**Executable:** `notebooks/probe_massive_2021_2022_underlying_access.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I check whether the current account can return one-minute SPY, SPX and VIX data for selected 2021 and 2022 dates before attempting an expansion.

## Inputs

- `main.env` with `MASSIVE_API_KEY`
- Pre-selected dates in 2021, 2022 and the 2023 control year

## Processing and rationale

- Request several ordinary weekdays for each ticker and year.
- Classify each response as available, no rows or error/entitlement.
- Record evidence without changing the database or raw-data folders.

## Outputs

- `outputs/underlying_history_probe/massive_2021_2022_probe_detail.csv`
- Probe summary CSV and JSON manifest

## Findings and decisions

- The manifest records observed entitlement responses without modifying any research dataset.
- Multiple dates are used so a single unusual session does not determine the decision for a whole year.

## Limitations

- Returned rows for sample dates do not guarantee full-year coverage or completeness.
- Entitlements can change after the probe is run.

## Next steps

- Expand the date range only if all three underlying series show usable access.
