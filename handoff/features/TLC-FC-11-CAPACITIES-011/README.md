# TLC-FC-11-CAPACITIES-011 — Riemannian metric descriptor

## What is this feature?

A structural descriptor for the cited Riemannian structure object `TLC-SO-CAPACITIES-054`.

## What must be implemented?

Accept the exact object, explicit symbols, complete provenance, and blocker `scientific decision required`. Return an immutable `CapacityMetricDescriptor` exposing the capacity-space reference, metric symbol `g`, and only source-backed opaque geodesic or distance annotations.

## Valid inputs and required output

The single object and its symbol entry occur exactly once. The result preserves identity, symbols, provenance, blocker, and a non-evaluation guard.

## Mandatory and forbidden behavior

Exact identity, symbols, provenance, opacity, blocker retention, determinism, and atomic failure are mandatory. Distance, geodesic, norm, curvature, metric, or manifold computation is forbidden.

## Implementation freedom

Language, storage, ownership, allocation, serialization, concurrency, and internal decomposition are implementation-defined. No numeric or geometric runtime is prescribed.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `UnexpectedCoveredObject`, `ObjectOrderMismatch`, `MissingSymbolTableEntry`, `MissingSourceReference`, `MissingDecisionBlocker`, and `ScientificEvaluationRequested`. All acceptance tests must pass.

## Unresolved science

The Riemannian structure and all geometric operations remain preserved unresolved.
