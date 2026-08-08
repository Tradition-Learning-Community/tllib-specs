# TLC-FC-16-COHORT-001 — Trait profile record and validation

This package defines the implementation handoff for the Cohort trait-profile record. The authoritative scientific source is `maths/16-cohort/cohort.md`, section 2. An implementation accepts exactly twelve ordered trait coordinates and preserves the source coordinate-domain descriptor. It must not repair the source inconsistency between the four three-dimensional tensor factors and the stated identification with `R^12`, and it must not choose a single coordinate interval where the source leaves `[0,1]` versus a continuous interval open.

The output is a source-faithful structural descriptor. Invalid coordinate count and attempted scientific canonicalization are errors. See the mathematical contract, optimized IR, algorithm specification, oracle, and acceptance tests referenced by this package.
