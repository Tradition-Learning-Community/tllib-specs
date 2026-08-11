# TLC-FC-21-FAIRNESS-007 — Master weight raw expression

Compute only the unnormalized factor on the right side of the source proportionality for `w_i^T`, using externally supplied probability, KL-divergence, diversity, and alignment values. The source uses `proportional to`, not a normalized equality. This package never assumes weights sum to one, never applies softmax, never constructs a partition function, and never implements KL divergence. A normalized weight requires an explicit normalization provider.
