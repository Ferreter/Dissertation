# Dataset Cleaning and Pre-Modelling Setup

**Executable:** `notebooks/cleaning_modellingprep.ipynb`  
**Status:** Part of the maintained dissertation workflow.

## Purpose

I clean the aligned daily data, document session exclusions and prepare leakage-safe chronological datasets for modelling.

## Workflow

```mermaid
flowchart LR
    A["Aligned daily dataset"] --> B["Eligibility checks, cleaning and chronological splits"]
    B --> C["Clean development datasets and audit tables"]
    C --> D["Strict and relaxed variants"]
```

## Inputs

- `data/derived/daily_underlying_model_dataset.parquet`
- `data/derived/underlying_session_audit.parquet`

## Processing and rationale

- Remove duplicate, incomplete, early-close and timing-inconsistent sessions.
- Audit missing, non-finite, constant and highly correlated features.
- Fit median imputation and 1st/99th percentile clipping on training rows only.

## Outputs

- `data/derived/daily_underlying_model_dataset_clean.parquet`
- `data/derived/daily_underlying_model_dataset_clean_split.parquet`
- `data/derived/daily_underlying_model_dataset_model_ready.parquet`
- `outputs/cleaning/`

## Representative outputs

![Neutral-threshold sensitivity](../../outputs/cleaning/figures/neutral_threshold_sensitivity.png)

*Figure: how the direction-label balance changes across plausible neutral-return thresholds.*

The exact cleaning rules and retained rows are recorded in the [cleaning manifest](../../outputs/cleaning/cleaning_manifest.json).

## Findings and decisions

- The recorded run retained 434 strict binary-target sessions.
- Look-ahead, target-formula and duplicate checks passed.
- Several feature pairs were highly correlated, so the modelling stage must keep preprocessing inside each training fold.

## Limitations

- The strict eligibility rule reduces an already limited daily sample.
- The precomputed model-ready table is suitable only for simple benchmarks; formal validation should fit preprocessing inside the pipeline.

## Next steps

- Create strict and relaxed variants on identical calendar boundaries.
