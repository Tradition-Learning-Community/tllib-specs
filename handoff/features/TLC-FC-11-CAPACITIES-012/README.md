# TLC-FC-11-CAPACITIES-012 — Hilbert/Riemannian component index

## What is this feature?

A structural index for the cited space-and-structure object `TLC-SO-CAPACITIES-042`.

## What must be implemented?

Accept the exact object, explicit symbol entry, complete provenance, and blocker `scientific decision required`. Return an immutable `CapacityMetricStructureIndex` that supports structural lookup of the capacity space, metric `g`, tangent-space token, point token, geodesic annotations, and curvature token only as source-backed symbols.

## Valid inputs and required output

The result maps component roles to the cited symbol and provenance without computing any geometry.

## Mandatory and forbidden behavior

Exact identity, source-backed role lookup, symbols, provenance, opacity, blocker retention, determinism, and atomic failure are mandatory. Curvature, geodesic, tangent-space, norm, or metric computation is forbidden.

## Implementation freedom

Language, index structure, storage, ownership, allocation, serialization, and concurrency are implementation-defined.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `UnexpectedCoveredObject`, `ObjectOrderMismatch`, `MissingSymbolTableEntry`, `MissingSourceReference`, `MissingDecisionBlocker`, and `ScientificEvaluationRequested`. All acceptance tests must pass.

## Unresolved science

Hilbert/Riemannian semantics and geometric evaluators remain preserved unresolved.
