# Legacy 03 - A Quick AMD Friday-to-Monday Idea

**File:** [notebooks/legacy/03_amd-monday.ipynb](../../../notebooks/legacy/03_amd-monday.ipynb)

**How I use it:** This is an old side experiment and has no role in the final SPX dissertation results.

## The short version

I briefly explored whether AMD's Friday close said anything useful about the following Monday open or high. This came from an early trading idea rather than one of the final research questions. I left it in the repository because it shows how the project narrowed from several loose ideas into one controlled SPX final-hour study.

## Where it sits in the workflow

```mermaid
flowchart LR
    A["Recent AMD daily prices"] --> B["Friday/Monday pairing"]
    B --> C["Counts and plots"]
    C --> D["Idea parked"]
```

This does not feed any numbered notebook. It is provenance only, so a reader can safely skip it when reproducing the dissertation.

## What it needs

- Recent AMD daily OHLC data downloaded with yfinance.
- Calendar weekdays used to match each Friday with the next available Monday.

## What I actually do here

The calculation is simple because I was checking the idea, not building a final strategy.

- I identify Friday observations and match the next Monday session.
- I compare the Friday close with Monday's open and high.
- I count the different gap patterns and inspect them in simple charts.
- I keep the displayed examples in the notebook but do not export them into the final output folders.

It was interesting enough as a quick check, but it pulled the project away from the SPX research questions and did not justify a larger backtest.

## What it creates

- Paired Friday/Monday rows displayed in the notebook.
- Basic gap counts and exploratory charts.
- No maintained model, dataset or dissertation figure.

## Outputs worth opening

The paired rows and plots remain inside the [AMD legacy notebook](../../../notebooks/legacy/03_amd-monday.ipynb). I have not copied them into the research output folders because doing that would make this abandoned idea look like part of the final evidence.

## What I took from it

- The notebook helped me practise turning a loose market idea into a clearly defined comparison.
- The apparent patterns were too dependent on a small, changing download window.
- I decided to keep the dissertation focused on SPX intraday prediction and options rather than add another asset and horizon.

## Things I wouldn't overclaim

- The download window changes over time.
- There are no transaction costs, chronological validation rules or proper out-of-sample test.
- Monday holidays and unusual sessions can complicate a simple weekday pairing.

## What I run next

There is no next pipeline stage. The maintained workflow begins with [01 - the Massive database starter](../01_massive_database_starter.md).
