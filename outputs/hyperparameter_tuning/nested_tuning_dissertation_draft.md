
### RQ1: Direction of the final-hour SPX return

Nested expanding-window tuning identified the
Histogram Gradient Boosting model using the
relaxed dataset and
full feature set as the leading
directional specification. Its mean outer-fold balanced accuracy was
0.544, with a standard
deviation of 0.048.
Taken together, these results provide limited evidence of directional predictability. Any score only
slightly above 0.50 should be interpreted cautiously because the
available sample is small and the relationship varies across market
regimes.

### RQ2: Magnitude of the final-hour SPX movement

The strongest magnitude model was
Extra Trees using the
relaxed dataset and
reduced feature set. The model achieved a
mean outer-fold MAE of 13.77 basis
points, mean out-of-sample R-squared of
0.062, and mean Spearman correlation of
0.444. This provides modest evidence that intraday features contain information about movement magnitude.
The result should be described as incremental rather than strong if
the MAE improvement is small relative to the unconditional movement
distribution.

### RQ3: Large-movement prediction and feature relevance

The leading large-movement configuration was
RBF SVC using the
strict dataset and
full feature set. Mean outer-fold average
precision was 0.499, while
mean recall after fold-specific threshold optimisation was
0.789. These results provide
evidence that the features can rank large-movement risk. Feature-importance conclusions should be based on
repeated permutation importance and economic feature groups because
the input variables are correlated and individual rankings may be
unstable.

### Overall conclusion

Hyperparameter tuning can improve model fit and decision thresholds,
but it cannot create genuine information that is absent from the
features. The dissertation should therefore report both positive and
negative findings. A weak or non-significant RQ1 result remains a
valid empirical conclusion, while stronger RQ2 or RQ3 ranking results
may still justify the subsequent options-data extension.
