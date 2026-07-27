# Community stability state descriptor

## What is this feature?

This feature constructs the source-traceable structural context used by theorem C5. It links an opaque community sequence, an opaque limit community, four covered object identifiers, three covered relation identifiers, and three unresolved scientific term identifiers.

## What must be implemented?

Implement `construct_community_stability_state`. Require the sequence and limit identities, require every covered relation to target a covered state component, preserve all opaque payloads, and attach exactly `TLC-UT-THEOREMS-002`, `TLC-UT-THEOREMS-003`, and `TLC-UT-THEOREMS-004` once each.

## Valid inputs and required output

Valid inputs provide the sequence, limit, and a context containing exactly objects `TLC-SO-THEOREMS-001`, `012`, `013`, and `015` plus relations `TLC-SR-THEOREMS-011`, `012`, and `014`, with no dangling target. The output is an immutable `CommunityStabilityStateDescriptor`. Relation storage order is not semantically constrained and may be normalized by identifier.

## Mandatory and forbidden behavior

Preserve exact identities, payloads, relation targets, unresolved identifiers, and partial proof reference `PROOF-THEOREMS-001`. Do not evaluate Gromov-Hausdorff convergence, stability, spectral conditions, or theorem truth. Structural success must assert neither convergence nor stability.

## Implementation freedom

Internal relation ordering, data structures, ownership, allocation, serialization, and concurrency are implementation-defined. Exact populations, relation integrity, unresolved preservation, stable errors, and deterministic semantics are normative.

## Observable errors

- `MISSING_COMMUNITY_SEQUENCE`: the sequence identity is absent.
- `MISSING_LIMIT_STATE`: the limit state identity is absent.
- `DANGLING_STABILITY_RELATION`: a covered relation targets an uncovered component.

No successful partial descriptor may be observable on error.

## Conformance and unresolved scientific semantics

Acceptance verifies exact populations, relation integrity, opaque preservation, unresolved propagation, stable errors, determinism, and absence of stability assertions. The three unresolved scientific terms remain `preserved_unresolved`; structural implementation is ready without defining them.
