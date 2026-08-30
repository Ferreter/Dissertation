# Model Artifact Helper - Saving the Models Without Losing Track of Them

**File:** [scripts/model_artifacts.py](../../scripts/model_artifacts.py)

**How I use it:** This is the maintained saving and checking helper for the classical and exploratory LSTM artifacts.

## The short version

Saving a model sounds like one line until I also need to know which notebook created it, what rows it saw, which threshold belongs with it and whether the file still opens. This helper keeps those jobs together. It saves to a temporary path first, replaces the canonical file only after a successful write, reloads the result and records a hash plus the training metadata in a manifest.

## Where it sits in the workflow

```mermaid
flowchart LR
    A["Fitted development model and metadata"] --> B["Atomic save"]
    B --> C["Immediate reload and prediction check"]
    C --> D["Hashed artifact and manifest"]
```

This helper never chooses or fits a model. The modelling notebook must enforce the split rules before it calls the save function.

## What it needs

- A fitted scikit-learn estimator or Keras model.
- A fitted sequence scaler when the model is an LSTM.
- A stable path below `models/classical/` or `models/lstm/`.
- Research question, target, features, dates, row counts, split exclusions, threshold, parameters and library versions.
- A small verification input for checking the prediction interface after reload.

## What I actually do here

The main aim is to make a saved binary understandable and safe to replace on a later clean rerun.

- I create the destination folder and write the artifact to a temporary sibling path.
- I move the finished temporary artifact over the canonical filename atomically.
- I immediately load it again with joblib or Keras.
- I check that the reloaded object has the expected structure and can predict on the verification input.
- I calculate a SHA-256 hash of every saved file.
- I convert NumPy values, dates and paths into clean JSON values.
- I write the three RQ entries into one stable manifest instead of producing timestamped duplicates.

If saving or reloading fails, the normal artifact should not be reported as successfully created. That is the reason for the temporary file and verification step.

## What it creates

- Canonical `.joblib` pipelines for RQ1-RQ3 under `models/classical/`.
- Exploratory `.keras` models and matching scaler `.joblib` files under `models/lstm/`.
- A `manifest.json` in each model family folder.
- Hashes and metadata that notebook 18 can verify before fresh scoring.

## Outputs worth opening

The [model folder README](../../models/README.md) lists the intended filenames and explains what is final classical evidence versus an exploratory LSTM refit. The current [classical manifest](../../models/classical/manifest.json) and [LSTM manifest](../../models/lstm/manifest.json) are the quickest outputs to inspect because they show features, thresholds, training scope and hashes without opening a binary file.

## What I took from it

- Stable filenames are easier for the fresh-holdout notebook to load and verify.
- A hash tells me whether the file changed, while the manifest explains why it changed.
- Reloading catches broken or incomplete saves, but it does not say anything about future model quality.
- Keeping thresholds beside classifiers matters because the project does not always use the library's default 0.5 cutoff.

## Things I wouldn't overclaim

- Binary compatibility can still break after large Python or library-version changes.
- The helper trusts the training metadata supplied by the notebook.
- It cannot prevent leakage if a notebook fits on Test or holdout rows before calling it.
- Exploratory LSTM refits are clearly labelled because they are not independently evaluated final models.

## What I run next

The saving cells in notebooks [07](../notebooks/07_hyperparameters_tuning.md), [08](../notebooks/08_hyperparameters_tuning_extended_robustness.md) and [11](../notebooks/11_lstm_intraday_sequence_extension.md) call this helper when `SAVE_MODEL_ARTIFACTS = True`. Notebook [18](../notebooks/18_fresh_holdout_end_to_end_evaluation.md) then verifies and loads the frozen files without fitting them again.
