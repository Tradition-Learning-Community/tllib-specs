# TLC-FC-11-CAPACITIES-018 — Capacity relation descriptor

## What is this feature?

A structural descriptor for the cited social/relational capacity object `TLC-SO-CAPACITIES-010`.

## What must be implemented?

Accept exactly that opaque object and complete provenance. Return an immutable `CapacityRelationDescriptor` preserving the object identity while representing relation endpoints as unknown unless the caller supplies source-backed endpoint references.

## Valid inputs and required output

The object occurs exactly once and has complete provenance. The result exposes its identity, provenance, reservations, unknown endpoint state, an empty unresolved list, and structural validity.

## Mandatory and forbidden behavior

Exact identity, coverage, provenance, opacity, unknown-endpoint preservation, determinism, and atomic failure are mandatory. Endpoint inference, relation evaluation, scientific equivalence, external-domain mutation, scoring, and partial success are forbidden.

## Implementation freedom

Language, relation representation, storage, ownership, allocation, serialization, and concurrency are implementation-defined.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`. All acceptance tests must pass.

## Unresolved science

The source does not define relation endpoints or executable relation semantics. They remain unknown rather than inferred.
