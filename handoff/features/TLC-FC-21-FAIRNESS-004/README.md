# TLC-FC-21-FAIRNESS-004 — Decision correction expression

Evaluate the source correction formula exactly from supplied expectation, fidelity, and alignment values. The denominator `1 + alpha(z)(E[y|z]-E[y])` is a real scientific singularity: if it is zero, return the structured `CorrectionDenominatorZero` failure. Never add epsilon, substitute one, clamp the correction, fabricate an expectation estimator, or use NaN as an implicit policy.
