# TLC-FC-21-FAIRNESS-009 — Cognitive diversity expression

Evaluate cognitive diversity from externally supplied pairwise KL-divergence, perspective-distance, and traditional-distance values. The source denominator is exactly `C(k,2)`, so the feature requires at least two Masters. For `k < 2`, return `InsufficientMasterPopulation` rather than a fallback. The handoff does not implement KL divergence or either distance and does not silently replace the zero denominator.
