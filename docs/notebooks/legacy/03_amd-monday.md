# Legacy 03 - AMD Friday-to-Monday Exploration

**File:** [notebooks/legacy/03_amd-monday.ipynb](../../../notebooks/legacy/03_amd-monday.ipynb)

**Role in the project:** This is an old side experiment and has no role in the final SPX dissertation results.

## Overview

This notebook explores whether AMD's Friday close relates to the following Monday open or high. It came from an early trading idea rather than one of the final research questions and is retained to show how the project narrowed towards the controlled SPX final-hour study.

## Workflow

```mermaid
flowchart LR
    A["Recent AMD daily prices"] --> B["Friday/Monday pairing"]
    B --> C["Counts and plots"]
    C --> D["Idea parked"]
```

This does not feed any numbered notebook. It is provenance only, so a reader can safely skip it when reproducing the dissertation.

## Inputs

- Recent AMD daily OHLC data downloaded with yfinance.
- Calendar weekdays used to match each Friday with the next available Monday.

## Processing

The calculation is simple because I was checking the idea, not building a final strategy.

- I identify Friday observations and match the next Monday session.
- I compare the Friday close with Monday's open and high.
- I count the different gap patterns and inspect them in simple charts.
- The displayed examples remain in the notebook and are not exported into the final output folders.

The initial comparison did not provide enough evidence to justify a larger backtest and was outside the final SPX research questions.

## Outputs

- Paired Friday/Monday rows displayed in the notebook.
- Basic gap counts and exploratory charts.
- No maintained model, dataset or dissertation figure.

## Key outputs and figures

The paired rows and plots remain inside the [AMD legacy notebook](../../../notebooks/legacy/03_amd-monday.ipynb). They are not copied into the research output folders because this exploratory idea is outside the final evidence pipeline.

## Findings and decisions

- The notebook helped turn an early market idea into a clearly defined comparison.
- The apparent patterns were too dependent on a small, changing download window.
- The dissertation remained focused on SPX intraday prediction and options rather than adding another asset and horizon.

## Limitations and considerations

- The download window changes over time.
- There are no transaction costs, chronological validation rules or proper out-of-sample test.
- Monday holidays and unusual sessions can complicate a simple weekday pairing.

## Next stage

There is no next pipeline stage. The maintained workflow begins with [01 - the Massive database starter](../01_massive_database_starter.md).
