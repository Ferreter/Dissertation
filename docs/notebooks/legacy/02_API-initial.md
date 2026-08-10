# Legacy Massive API Entitlement Check

**Executable:** `notebooks/legacy/02_API-initial.ipynb`
**Status:** I kept this as provenance from an older experiment. It isn't part of the final dissertation evidence.

## Purpose

This was my first proper look at the Massive endpoints. I was mainly trying to work out what underlying, index and option data the account would actually let me use.

## Workflow

```mermaid
flowchart LR
    A["Early API request"] --> B["Inspect response structure"]
    B --> C["Notebook-only response tables"]
    C --> D["Superseded retrieval workflow"]
```

## Inputs

- Massive API credentials
- Recent test dates and tickers

## Processing and rationale

- I make a few small aggregate, contract and option requests.
- I display the replies and note where the subscription limits appear.

## Outputs

- Displayed API response tables; no required persistent research output

## Representative outputs

No maintained research artifact is produced. The response tables remain in the [legacy notebook](../../../notebooks/legacy/02_API-initial.ipynb) as provenance only.

## Findings and decisions

- The main lesson was that being able to see contracts and aggregates didn't mean I could also get historical Greeks, IV or open interest.

## Limitations

- This is an early access test, not the final downloader.
- The available history and API plan can change.

## Next steps

- For repeatable collection, I moved to the maintained database notebooks and `scripts/massive_database.py`.
