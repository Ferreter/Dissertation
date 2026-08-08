
### RQ1: Direction of the final-hour SPX return

Nested expanding-window tuning identified the
Histogram Gradient Boosting model using the
relaxed dataset and
full feature set as the leading
directional specification. Its mean outer-fold balanced accuracy was
0.544, with a standard
deviation of 0.070. On the
same outer test folds, the strongest simple comparator was
60-minute mean reversion, which achieved mean balanced
accuracy of 0.569.
The model's mean absolute improvement over this comparator was
-0.025. Taken
together, these results provide limited evidence of directional predictability. The confidence-selective
analysis achieved its highest balanced accuracy of
0.592 while retaining
30.7% of outer-fold
predictions; this result should be interpreted alongside the retained
sample size of 93 sessions.

### RQ2: Magnitude of the final-hour SPX movement

The strongest magnitude model was
RBF SVR using the
relaxed dataset and
reduced feature set. The model achieved a
mean outer-fold MAE of 13.97 basis
points, mean out-of-sample R-squared of
0.003, and mean Spearman correlation of
0.373. The fold-matched median
benchmark achieved mean MAE of
15.29 basis points. The
model therefore reduced MAE by an average of
1.32 basis points,
or 4.97% of
the benchmark error. This provides some evidence that the model can rank relative movement magnitude, but little evidence that it accurately predicts the absolute size of the movement.

### RQ3: Large-movement prediction and feature relevance

The leading large-movement configuration was
RBF SVC using the
strict dataset and
full feature set. Mean outer-fold average
precision was 0.501, with a
standard deviation of
0.189. Mean outer-test
large-movement prevalence was
0.275, giving mean
absolute average-precision lift of
0.226. Mean
recall after fold-specific threshold optimisation was
0.564. These results provide
evidence that the features can rank large-movement risk.

### Feature stability and regimes

The five highest mean outer-fold permutation-importance features were
dist_from_day_high_pct, ret_last_15m, vix_ret_last_15m, ret_last_60m, vix_ret_last_60m for RQ1; spy_volume_last_60m, atr_pct_open_to_1500, vix_ret_last_15m, ret_last_15m, rv_open_to_1500
for RQ2; and spy_cum_volume_to_1500, atr_pct_open_to_1500, rv_open_to_1500, ret_last_15m, dist_from_day_high_pct for RQ3. These rankings
should be interpreted together with their between-fold standard
deviations, positive-fold shares, and grouped importance because the
inputs are correlated. The regime tables report performance by VIX,
realised-volatility, and pre-15:00 trend states using thresholds fitted
only on each preceding outer training fold. Regime results with fewer
than 10 observations are flagged and should not be
used for strong conclusions.

### Overall conclusion

Hyperparameter tuning can improve model fit and decision thresholds,
but it cannot create genuine information that is absent from the
features. The dissertation should therefore report both positive and
negative findings. A weak or non-significant RQ1 result remains a
valid empirical conclusion, while stronger ranking or event-risk
results may still justify the subsequent options-data extension. The
selected configurations and all robustness analyses remain subject to
confirmation on the new untouched final holdout.
