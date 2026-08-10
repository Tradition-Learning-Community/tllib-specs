# TLC-FC-21-FAIRNESS-017 — Contextual fairness threshold assessment

Evaluate one exact source predicate: `E_ctx^T > 0.6`. The comparison is strictly greater-than, so equality to `0.6` is false. The numeric value `0.6` is explicitly present in the Fairness source and may therefore be preserved here, but it is only a declared operational threshold for this contextual-fairness predicate. This package must not generalize it to other features, claim it is derived or calibrated, or silently replace it with a tuned value.
