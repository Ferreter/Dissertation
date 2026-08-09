
### Exploratory LSTM Sequence-Modelling Extension

A recurrent neural-network extension was implemented to test whether retaining
the temporal ordering of intraday observations provided incremental predictive
value beyond the engineered daily feature representation. Each observation
consisted of the 120 one-minute observations from 13:00 through 14:59 ET,
using only information available before the final-hour target period. The
models were evaluated with three expanding chronological outer folds. Within
each outer-training fold, the latest 20% of observations were reserved for
early stopping and, where applicable, classification-threshold selection.

For RQ1, the LSTM achieved mean outer-fold balanced accuracy of
0.524, compared with 0.552 for the strongest same-fold
mean-reversion comparator. The LSTM did not exceed the strongest same-fold mean-reversion benchmark, reinforcing the earlier finding that final-hour direction is difficult to forecast reliably.

For RQ2, mean outer-fold MAE was 14.40 bps compared with
14.17 bps for the training-median magnitude benchmark, while
mean Spearman rank correlation was 0.203. For magnitude prediction, the LSTM did not improve on the training-median benchmark.

For RQ3, mean outer-fold average precision was 0.434 compared with
mean large-movement prevalence of 0.240; mean recall was
0.747. For large-movement classification, average precision remained above the event-prevalence benchmark.

For RQ1 Direction, the LSTM did not outperform the selected classical model on the 427 overlapping OOF sessions using balanced_accuracy. For RQ2 Magnitude, the LSTM did not outperform the selected classical model on the 416 overlapping OOF sessions using mae_bps. For RQ3 Large Movement, the LSTM did not outperform the selected classical model on the 427 overlapping OOF sessions using average_precision.

The LSTM results should be interpreted as an exploratory model-complexity
check rather than a new model-selection exercise. Although the recurrent
architecture can model temporal dependencies directly, the number of
independent observations remains the number of trading sessions rather than
the number of one-minute bars. Consequently, a more complex sequence model
would require a clear and stable improvement over the simpler tabular
approaches to justify its additional modelling complexity.
