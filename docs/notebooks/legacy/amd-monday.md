# Legacy AMD Friday-to-Monday Exploration

**Executable:** `notebooks/legacy/amd-monday.ipynb`  
**Status:** Legacy exploratory work retained for provenance.

## Purpose

I used this exploratory notebook to compare Friday closes with Monday opens and highs for AMD.

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

- Pair Friday and Monday observations.
- Count weekend-gap relationships and plot the paired prices.

## Outputs

- Displayed counts and charts in the notebook

## Representative outputs

No maintained research artifact is produced. The historical displays remain in the [legacy notebook](../../../notebooks/legacy/amd-monday.ipynb) as provenance only.

## Findings and decisions

- This was an early idea-development exercise and does not feed the SPX dissertation models.

## Limitations

- The result changes with the live yfinance window and does not include transaction costs or formal validation.

## Next steps

- Retain only as provenance; use the main SPX workflow for dissertation evidence.
