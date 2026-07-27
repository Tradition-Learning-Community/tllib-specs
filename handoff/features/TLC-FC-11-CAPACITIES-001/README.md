# TLC-FC-11-CAPACITIES-001 — Capacity constraint record

## What is this feature?

A structural constructor for the exact capacity-constraint objects `TLC-SO-CAPACITIES-013` and `TLC-SO-CAPACITIES-064`.

## What must be implemented?

Validate the exact feature identity, accept one opaque payload and one complete source reference for each required object, restore the contract object order, and return an immutable `CapacityPrototypeDescriptor`.

## Valid inputs and required output

The required object-key set is exactly `[TLC-SO-CAPACITIES-013, TLC-SO-CAPACITIES-064]`. The output exposes the feature id, artifact kind, ordered object identities, source symbols, provenance, reservations, an empty unresolved collection, and `structurally_valid = true`.

## Mandatory and forbidden behavior

Identity, exact membership, duplicate rejection, source-order restoration, provenance completeness, opacity, determinism, and failure atomicity are mandatory. Scientific evaluation, scoring, ranking, generated thresholds, numerical interpretation, temporal inference, payload rewriting, and partial success are forbidden.

## Implementation freedom

API spelling, language, storage, ownership, allocation, serialization, concurrency policy, and internal decomposition are implementation-defined. Only validation and preservation obligations must precede observable success; the upstream total step list is not a required internal algorithm.

## Errors and conformance

The observable error identifiers are `UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`. No partial descriptor may be exposed. Conformance requires every test in `acceptance.json` to pass.

## Unresolved science

Capacity strength, level, ordering, causal effect, learned value, and numerical semantics remain outside this package. The feature is structural only.
