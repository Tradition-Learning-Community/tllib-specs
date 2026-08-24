# TLC-FC-33-LOW-DATA-ARCHITECTURE-012 — Eta_loss inverse-compression boundary

**Status:** finalized · **Scientific:** external_provider_required · **Execution:** conditionally_executable.

## Purpose

Preserve the eta_loss expression while treating C^-1 and reconstruction semantics as external or unresolved.

## Source authority

This package is bounded by `maths/33-low-data-architecture/architectural-principles-for-low-data-environments.md`. It does not add missing spaces, norms, dimensions, probability models, distributions beyond the explicit Gaussian declaration, thresholds, solvers, inverses, convergence rules, numerical defaults, normalization, reconstruction procedures, or cross-domain authority.

## Required preservation

Do not presume invertibility of compression or invent a decompressor/reconstructor.

Domain-level dependency policy: no confirmed scientific edge; `33 -> 04` remains unresolved; thematic links to Domains 0, 1, 2, 13, 17, 23, 29, 34 and 35 remain non-proven. Runtime dependencies are empty and the shared-contract population remains exactly eight.
