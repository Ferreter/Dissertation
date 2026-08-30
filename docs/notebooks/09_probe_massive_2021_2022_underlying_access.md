# 09 - Checking Whether 2021-2022 Data Was Actually Available

**File:** [notebooks/09_probe_massive_2021_2022_underlying_access.ipynb](../../notebooks/09_probe_massive_2021_2022_underlying_access.ipynb)

**How I use it:** This is a non-destructive entitlement check, not a modelling notebook.

## The short version

Before asking the downloader for two extra years, I test a few ordinary dates from 2021 and 2022 for all three underlying series. The notebook writes the replies to a separate output folder and does not touch the main database. It saved me from starting an extension based on an assumption about what the paid plan included.

## Where it sits in the workflow

```mermaid
flowchart LR
    A["Selected 2021-2023 test dates"] --> B["Small entitlement requests"]
    B --> C["Detail, summary and manifest"]
    C --> D["Decision on history extension"]
```

The 2023 dates act as a control. If they work while 2021-2022 fail, that points toward history entitlement rather than a broken ticker or API key.

## What it needs

- `main.env` with the Massive API key.
- A small fixed set of normal weekdays in 2021 and 2022.
- Equivalent 2023 control dates.
- SPY, `I:SPX` and `I:VIX` aggregate requests.

## What I actually do here

I intentionally keep this separate from raw retrieval so the probe cannot partially extend the research dataset by accident.

- I request each ticker-date and record the HTTP/response outcome.
- Responses are labelled as available, empty or error/entitlement-related.
- The detail table keeps every attempt, while the summary collapses the result by ticker and year.
- A manifest records when and how the check was run.

One date can always be odd, which is why the probe uses several dates before making a year-level decision.

## What it creates

- `massive_2021_2022_probe_detail.csv`.
- `massive_2021_2022_probe_summary.csv`.
- `massive_2021_2022_probe_manifest.json`.
- No changes to the maintained raw-data folders.

## Outputs worth opening

The [probe detail](../../outputs/underlying_history_probe/massive_2021_2022_probe_detail.csv) is where I check the exact ticker-date responses. The [summary](../../outputs/underlying_history_probe/massive_2021_2022_probe_summary.csv) makes the year-level pattern easier to read, and the [manifest](../../outputs/underlying_history_probe/massive_2021_2022_probe_manifest.json) preserves the account-dependent result.

There is no chart because a small availability table is clearer than dressing a few entitlement checks up as analysis.

## What I took from it

- The notebook gave me a repeatable way to distinguish missing history from a general API failure.
- Testing all three feeds mattered because a longer SPY history alone would not support the aligned feature set.
- The account result is treated as a practical data constraint, not a research finding.

## Things I wouldn't overclaim

- A few successful dates cannot prove complete annual coverage.
- Entitlements and rolling windows can change after the manifest is created.
- The probe says whether rows are returned, not whether every minute inside those rows is complete.

## What I run next

I only expand the historical dataset when SPY, SPX and VIX all look usable. The separate longer run is documented in [10 - extended 2023-2026 pipeline](10_extended_2023_2026_full_pipeline.md).
