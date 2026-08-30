# 05 - Making the Strict and Relaxed Dataset Versions

**File:** [notebooks/05_dataset_Splitting.ipynb](../../notebooks/05_dataset_Splitting.ipynb)

**How I use it:** This creates the two modelling datasets that every classical model uses afterwards.

## The short version

I did not want one arbitrary missing-data rule to decide the whole dissertation, so this notebook makes two versions. Strict keeps only the cleanest sessions. Relaxed allows a small amount of VIX missingness but keeps the important timing anchors. Both use the same chronological boundaries, which means their results can be compared without sneaking different market periods into the comparison.

## Where it sits in the workflow

```mermaid
flowchart LR
    A["Clean daily and minute data"] --> B["Strict and relaxed eligibility rules"]
    B --> C["Calendar-matched split datasets"]
    C --> D["Baseline RQ1-RQ3 models"]
```

The two variants are a sensitivity check, not two chances to pick whichever final result looks nicer.

## What it needs

- The aligned minute data and daily modelling table.
- The cleaned split assignments from notebook 04.
- The session-quality audit.
- Fixed Train, Validation and Test date boundaries taken from the strict sample.

## What I actually do here

The important detail is that the strict and relaxed rows are made independently but compared over equivalent periods.

- Strict requires the full SPY session, exact SPX anchors and complete final-two-hour SPX/VIX coverage.
- Relaxed keeps the same SPY/SPX rules but permits a small number of VIX gaps when the required VIX anchors remain timely.
- I apply the strict calendar boundaries to both variants rather than letting the larger relaxed sample choose easier dates.
- I rerun missing-value, infinity, target and look-ahead checks before saving either dataset.
- Separate tables record strict-only, relaxed-only and excluded sessions so the difference is inspectable.

This makes the later model selection question clearer: is any apparent improvement coming from the algorithm, or just from allowing more sessions?

## What it creates

- `data/derived/daily_underlying_model_dataset_strict_split.parquet`.
- `data/derived/daily_underlying_model_dataset_relaxed_split.parquet`.
- Variant summaries and row-level quality comparisons under `outputs/dataset_variants/`.
- A JSON manifest containing the exact inclusion rules.

## Outputs worth opening

![Strict and relaxed observation counts](../../outputs/dataset_variants/figures/strict_relaxed_observation_counts.png)

*This is the quickest visual explanation of what I gain and lose by relaxing the VIX rule.*

The [variant summary](../../outputs/dataset_variants/variant_summary.csv) gives the row counts and date ranges, and [strict versus relaxed session quality](../../outputs/dataset_variants/strict_relaxed_session_quality.csv) lets me inspect individual days. [Relaxed-only sessions](../../outputs/dataset_variants/relaxed_only_sessions.csv) shows exactly which observations create the extra sample. The fixed rules are stored in the [variant manifest](../../outputs/dataset_variants/dataset_variant_manifest.json).

## What I took from it

- Strict retained 434 sessions and relaxed retained 486.
- Both saved versions passed the target, missing-value, infinity and timing checks.
- The relaxed gain comes from tolerating limited VIX gaps, not from weakening the SPX decision or outcome timestamps.
- I carry both forward and let development-period validation decide whether the extra rows help.

## Things I wouldn't overclaim

- The relaxed sample has more observations but slightly weaker VIX completeness.
- Neither version solves the small-sample problem.
- The Test block remains chronologically later, but it had already been inspected during baseline work and is not treated as fresh during tuning.

## What I run next

Both files feed [06 - baseline modelling](06_modeling_baseline.md), where the same rules and models are run against each variant.
