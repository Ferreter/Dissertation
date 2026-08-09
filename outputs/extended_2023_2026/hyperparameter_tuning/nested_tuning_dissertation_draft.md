
### RQ1: Direction of the final-hour SPX return

Nested expanding-window tuning identified the
Extra Trees model using the
strict dataset and
full feature set as the leading
directional specification. Its mean outer-fold balanced accuracy was
0.537, with a standard
deviation of 0.026. On the
same outer test folds, the strongest simple comparator was
15-minute mean reversion, which achieved mean balanced
accuracy of 0.550.
The model's mean absolute improvement over this comparator was
-0.013. Taken
together, these results provide limited evidence of directional predictability. The confidence-selective
analysis achieved its highest balanced accuracy of
0.571 while retaining
10.4% of outer-fold
predictions; this result should be interpreted alongside the retained
sample size of 45 sessions.

### RQ2: Magnitude of the final-hour SPX movement

The strongest magnitude model was
RBF SVR using the
relaxed dataset and
full feature set. The model achieved a
mean outer-fold MAE of 11.88 basis
points, mean out-of-sample R-squared of
0.135, and mean Spearman correlation of
0.409. The fold-matched median
benchmark achieved mean MAE of
13.02 basis points. The
model therefore reduced MAE by an average of
1.14 basis points,
or 7.85% of
the benchmark error. This provides modest evidence that intraday features contain information about movement magnitude.

### RQ3: Large-movement prediction and feature relevance

The leading large-movement configuration was
RBF SVC using the
strict dataset and
reduced feature set. Mean outer-fold average
precision was 0.538, with a
standard deviation of
0.151. Mean outer-test
large-movement prevalence was
0.238, giving mean
absolute average-precision lift of
0.300. Mean
recall after fold-specific threshold optimisation was
0.819. These results provide
evidence that the features can rank large-movement risk.

### Feature stability and regimes

The five highest mean outer-fold permutation-importance features were
vix_ret_last_30m, vix_level_1500, vix_ret_last_60m, position_in_day_range, vix_ret_last_15m for RQ1; atr_pct_open_to_1500, realized_vol_60m, vix_level_1500, realized_vol_30m, rv_open_to_1500
for RQ2; and atr_pct_open_to_1500, rv_open_to_1500, realized_vol_120m, spy_volume_accel_60m_vs_avg, vix_ret_last_60m for RQ3. These rankings
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
