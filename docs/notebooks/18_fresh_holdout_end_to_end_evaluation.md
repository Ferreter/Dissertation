# Fresh Post-Freeze Holdout Evaluation

**Executable:** `notebooks/18_fresh_holdout_end_to_end_evaluation.ipynb`  
**Status:** Final holdout workflow. The first successful run consumes the post-17 July 2026 holdout.

## Purpose

I use this notebook to test the already-frozen RQ1-RQ3 models on later market observations without fitting them again. It also carries the fixed signals into RQ4 and, when candidate dates and option bars are available, RQ5.

## Workflow

```mermaid
flowchart LR
    A["Post-17 July underlying minutes"] --> B["Backward alignment and frozen features"]
    B --> C["Saved RQ1-RQ3 models"]
    C --> D["Fresh RQ1-RQ4 metrics"]
    D --> E["Frozen RQ5 candidate dates"]
    E --> F["Option retrieval and strategy checks"]
```

## Inputs

- `main.env` containing `MASSIVE_API_KEY`
- Canonical artifacts and manifests under `models/classical/`
- Optional exploratory artifacts under `models/lstm/`
- The development-period RQ1 confidence cutoff and frozen RQ2/RQ3 rules

## Processing and rationale

- Downloads only sessions after 17 July 2026 into an isolated data folder.
- Uses the original backward alignment, features and strict/relaxed eligibility rules.
- Verifies model hashes and calls `predict`/`predict_proba` without calling `fit`.
- Reports classification metrics for RQ1/RQ3 and error metrics for RQ2.
- Applies the frozen RQ4 filter without recalculating the top-30% cutoff on holdout rows.
- Retrieves RQ5 options only for selected dates and applies the existing strike, cost and exit assumptions.

## Outputs

- `data/fresh_holdout_post_2026_07_17/`
- `outputs/fresh_holdout_post_2026_07_17/<start_end>/tables/`
- Fresh-holdout figures, option evidence and `fresh_holdout_manifest.json`

## Findings and decisions

- No fresh results are written here in advance. They are created only by the first confirmed run.
- The notebook starts disabled and requires an explicit confirmation string.
- The first successful run is preserved as the final holdout evidence.
- RQ5 may legitimately contain no trades if the combined rule selects no dates or option bars are unavailable.
- The optional LSTM comparison remains exploratory.

## Limitations

- A few weeks of later sessions may be too small for stable conclusions.
- Historical option aggregates are trade-derived rather than NBBO quotes.
- Once viewed, these dates cannot be reused as an untouched holdout for a changed model.

## Next steps

When I am ready to consume the holdout, I change the confirmation string and run the notebook once from top to bottom. I then preserve the generated folder and use its metrics, figures and manifest when writing the results chapter.
