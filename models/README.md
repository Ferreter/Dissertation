# Saved model files

The `models` folder only fills up after I run one of the modelling notebooks with `SAVE_MODEL_ARTIFACTS = True`. I kept the filenames fixed so a rerun replaces the normal version instead of creating lots of nearly identical files.

```text
models/
|-- classical/
|   |-- rq1_direction.joblib
|   |-- rq2_magnitude.joblib
|   |-- rq3_large_move.joblib
|   `-- manifest.json
`-- lstm/
    |-- rq1_direction.keras
    |-- rq1_direction_scaler.joblib
    |-- rq2_magnitude.keras
    |-- rq2_magnitude_scaler.joblib
    |-- rq3_large_move.keras
    |-- rq3_large_move_scaler.joblib
    `-- manifest.json
```

The classical models are fitted on Train + Validation from the original dataset. The LSTM files are exploratory refits using the allowed part of the extended dataset. Neither setup is allowed to fit on Test rows or the fresh data after 17 July 2026.

Each manifest keeps the useful background: which notebook made the file, the target, feature order, training dates, row count, excluded splits, parameters, classification cut-off, package versions and file hash. It also records whether the file opened again after saving.

I haven't generated the actual `.joblib` or `.keras` files as part of the project tidy-up. They will appear when I run the documented saving cells in the dissertation environment.
