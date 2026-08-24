# TLC-FC-33-LOW-DATA-ARCHITECTURE-019 — Practice similarity and loss approximation

**Status:** finalized · **Scientific:** partially_defined · **Execution:** conditionally_executable.

## Purpose

Preserve Pi_rep and P(loss) approximately exp(-kappa Pi_rep n) with approximation status intact.

## Source authority

This package is bounded by `maths/33-low-data-architecture/architectural-principles-for-low-data-environments.md`. It does not add missing spaces, norms, dimensions, probability models, distributions beyond the explicit Gaussian declaration, thresholds, solvers, inverses, convergence rules, numerical defaults, normalization, reconstruction procedures, or cross-domain authority.

## Required preservation

Do not invent sim, probabilistic calibration, independence, kappa, or replace approximation by equality.

Domain-level dependency policy: no confirmed scientific edge; `33 -> 04` remains unresolved; thematic links to Domains 0, 1, 2, 13, 17, 23, 29, 34 and 35 remain non-proven. Runtime dependencies are empty and the shared-contract population remains exactly eight.
