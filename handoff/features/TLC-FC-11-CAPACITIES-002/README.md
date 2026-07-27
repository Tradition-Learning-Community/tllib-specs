# TLC-FC-11-CAPACITIES-002 — Mastery constraint AST

## What is this feature?

A structural constructor for an unevaluated constraint AST joining the cited axiom object `TLC-SO-CAPACITIES-043` and mastery-progression object `TLC-SO-CAPACITIES-090`.

## What must be implemented?

Accept the exact ordered object sequence, an explicit symbol-table entry and complete provenance for each object, plus the exact decision blocker `scientific decision required`. Return an immutable `CapacityConstraintAst` whose root records the axiom node before the constraint node.

## Valid inputs and required output

The ordered sequence is exactly `[TLC-SO-CAPACITIES-043, TLC-SO-CAPACITIES-090]`. The output preserves both nodes, their symbols and provenance, the blocker in the unresolved collection, and a non-evaluation guard.

## Mandatory and forbidden behavior

Exact identity, membership, order, explicit symbol entries, provenance, blocker preservation, deterministic output, and atomic failure are mandatory. Truth evaluation, satisfiability, optimization, scoring, thresholds, progression inference, numerical interpretation, and partial success are forbidden.

## Implementation freedom

Language, storage, ownership, allocation, serialization, concurrency policy, and internal decomposition are free. Only the observable validation, preservation, blocker, and publication constraints are normative; no unique total algorithm is required.

## Errors and conformance

Observable errors are `UnknownFeatureId`, `MissingCoveredObject`, `UnexpectedCoveredObject`, `ObjectOrderMismatch`, `MissingSymbolTableEntry`, `MissingSourceReference`, `MissingDecisionBlocker`, and `ScientificEvaluationRequested`. Conformance requires every acceptance test to pass with no partial result.

## Unresolved science

The blocker remains `scientific decision required`; scientific truth and executable constraint semantics are not supplied by this package.
