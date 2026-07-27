# TLC-FC-11-CAPACITIES-014 — Actualization operator signature

## What is this feature?

A structural signature descriptor for the actualization object `TLC-SO-CAPACITIES-051`.

## What must be implemented?

Accept the exact object, explicit symbols, complete provenance, and blocker `scientific decision required`. Return an immutable `CapacityOperatorSignature` preserving the operator token, latent-capacity domain token, acquired-capacity codomain/subset token, and blocker without applying the operator.

## Valid inputs and required output

The single object and explicit symbol entry occur exactly once. The result preserves all cited tokens, provenance, blocker, and a non-evaluation guard.

## Mandatory and forbidden behavior

Exact identity, source token preservation, provenance, opacity, blocker retention, determinism, and atomic failure are mandatory. Operator application, actualization, activation execution, endpoint coercion, set-membership decision, and partial success are forbidden.

## Implementation freedom

Language, signature representation, storage, ownership, allocation, serialization, and concurrency are implementation-defined.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `UnexpectedCoveredObject`, `ObjectOrderMismatch`, `MissingSymbolTableEntry`, `MissingSourceReference`, `MissingDecisionBlocker`, and `ScientificEvaluationRequested`. All acceptance tests must pass.

## Unresolved science

Actualization behavior and executable domain/codomain semantics remain preserved unresolved.
