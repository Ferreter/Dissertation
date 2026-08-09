# Strict and Relaxed Modelling Datasets

**Executable:** `notebooks/dataset_Splitting.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I build two defensible session-quality variants so I can test whether a modest increase in sample size changes the modelling conclusions.

## Workflow

```mermaid
flowchart LR
    A["Clean split dataset"] --> B["Apply strict and relaxed inclusion rules"]
    B --> C["Calendar-matched dataset variants"]
    C --> D["Baseline modelling"]
```

## Inputs

- Aligned minute data
- Daily modelling data
- Session-quality audit

## Processing and rationale

- Apply strict and relaxed session-eligibility rules.
- Use the strict sample to set common chronological train, validation and test dates.
- Verify feature completeness, target consistency and the pre-15:00 cutoff.

## Outputs

- `data/derived/daily_underlying_model_dataset_strict_split.parquet`
- `data/derived/daily_underlying_model_dataset_relaxed_split.parquet`
- `outputs/dataset_variants/`

## Representative outputs

![Strict and relaxed observation counts](../../outputs/dataset_variants/figures/strict_relaxed_observation_counts.png)

*Figure: the sample-size trade-off created by the two data-quality definitions.*

The complete rules are recorded in the [dataset-variant manifest](../../outputs/dataset_variants/dataset_variant_manifest.json).

## Findings and decisions

- The recorded run retained 434 strict sessions and 486 relaxed sessions.
- Both variants passed missingness, non-finite and look-ahead checks.
- I carry both variants into modelling and select between them using development-period evidence only.

## Limitations

- The relaxed rule accepts limited VIX gaps and therefore trades sample size against data quality.
- Neither variant removes the need for time-aware validation.

## Next steps

- Run identical baseline models and benchmarks on both variants.
