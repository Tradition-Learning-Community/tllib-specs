# TLC-FC-16-COHORT-002 — Trait-profile similarity metrics

This handoff package defines the two source-authorized comparisons between supplied twelve-coordinate Disciple profiles: Euclidean distance and cosine similarity. The implementation must validate both profile shapes, evaluate the formulas exactly as stated in `maths/16-cohort/cohort.md`, and reject cosine evaluation when either profile has zero norm because the source quotient is then undefined. It must not impute coordinates, rescale profiles, or substitute a default similarity.

Conformance is determined by the mathematical contract, optimized IR, algorithm specification, test plan, oracle, and acceptance tests referenced by this package.
