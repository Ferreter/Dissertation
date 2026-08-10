# LSTM Intraday Sequence Extension

**Executable:** `notebooks/11_lstm_intraday_sequence_extension.ipynb`
**Status:** I use this in the main dissertation workflow.

## Purpose

I added this as a smaller side experiment to see whether the actual 13:00-14:59 price path contains something that the daily engineered features miss. It isn't meant to replace the classical models automatically.

## Workflow

```mermaid
flowchart LR
    A["Extended minute sequences and daily targets"] --> B["Expanding-fold LSTM evaluation and development refit"]
    B --> C["Exploratory evidence and model artifacts"]
    C --> D["Compare with classical evidence"]
```

## Inputs

- Extended aligned one-minute data
- Extended strict daily split dataset
- Classical tuned-model outputs

## Processing and rationale

- I turn each session into a 120-minute sequence with 16 market, volume, alignment and time features.
- I fit the scaler inside each chronological fold and use the latest part of the training block for early stopping.
- I run the same three research questions without touching the existing test block or the future holdout.

## Outputs

- `outputs/extended_2023_2026/lstm_sequence_extension/`
- LSTM fold, prediction, importance, history and manifest files

## Representative outputs

![Example LSTM input sequence](../../outputs/extended_2023_2026/lstm_sequence_extension/figures/lstm_example_input_sequence.png)

*This plot shows the minute-by-minute channels presented to the sequence model before the decision time.*

![LSTM validation loss](../../outputs/extended_2023_2026/lstm_sequence_extension/figures/lstm_validation_loss_curves.png)

*This plot shows the chronological training and validation behaviour used to assess overfitting and choose epochs.*

## Findings and decisions

- I keep the LSTM as exploratory because the dataset is small for deep learning.
- The network is deliberately small, and I didn't run a huge search just to find a better-looking result.
- The saved predictions let me compare the LSTM and classical models on the dates they have in common.

## Limitations

- Neural networks can move around between runs, and there aren't many daily sequences here.
- The sequences don't include options variables and haven't been checked on a genuinely fresh holdout.

## Next steps

- I compare it with the classical winners, but I would keep the simpler model unless the sequence result improves in a stable way.
