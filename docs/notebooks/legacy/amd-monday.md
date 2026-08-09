# Legacy AMD Friday-to-Monday Exploration

**Executable:** `notebooks/legacy/amd-monday.ipynb`  
**Status:** I kept this as provenance from an older experiment. It isn't part of the final dissertation evidence.

## Purpose

This was one of my early side ideas. I used it to compare AMD's Friday close with the following Monday open and high.

## Workflow

```mermaid
flowchart LR
    A["Historical market observations"] --> B["Exploratory weekday comparison"]
    B --> C["Notebook-only exploratory displays"]
    C --> D["Provenance only"]
```

## Inputs

- Recent AMD daily data downloaded with yfinance

## Processing and rationale

- I pair each Friday with the next Monday.
- I count the gap patterns and plot the two sets of prices.

## Outputs

- Displayed counts and charts in the notebook

## Representative outputs

No maintained research artifact is produced. The historical displays remain in the [legacy notebook](../../../notebooks/legacy/amd-monday.ipynb) as provenance only.

## Findings and decisions

- It helped me think through trading patterns, but it doesn't feed into the SPX dissertation models.

## Limitations

- The yfinance window changes when the notebook is rerun, and there are no costs or proper validation here.

## Next steps

- I keep this only to show where the project started. The main SPX notebooks contain the dissertation evidence.
