# TLC-FC-11-CAPACITIES-010 — Capacity metric descriptor

## What is this feature?

A structural descriptor for four cited metric-related objects: capacity evaluation, quantitative metrics, cognitive load/integration, and presence of potential.

## What must be implemented?

Accept exactly objects `021`, `022`, `034`, and `055`, preserve their opaque payloads, source-backed symbols, provenance, and contract order, and return an immutable `CapacityPrototypeDescriptor`.

## Valid inputs and required output

Every object occurs exactly once and has complete provenance. The result exposes exact identities, symbols, provenance, reservations, an empty unresolved list, and structural validity.

## Mandatory and forbidden behavior

Exact coverage, identity, order, opacity, provenance, determinism, and atomic failure are mandatory. Measurement execution, ratio or variance calculation, distance or norm evaluation, scoring, ranking, thresholds, comparison decisions, and partial success are forbidden.

## Implementation freedom

Language, storage, ownership, allocation, serialization, concurrency, and internal decomposition are implementation-defined. No numeric type or metric engine is prescribed.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`. All acceptance tests must pass.

## Unresolved science

Metric values, units, evaluators, norms, and measurement semantics remain unavailable.
