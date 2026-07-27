# TLC-FC-11-CAPACITIES-015 — Capacity validity-domain predicate AST

## What is this feature?

A structural predicate AST for the cited validity-domain object `TLC-SO-CAPACITIES-005`.

## What must be implemented?

Accept the exact object, explicit symbols, complete provenance, and blocker `scientific decision required`. Return an immutable `CapacityValidityDomainPredicateAst` preserving source-backed tuple, domain-product, affinity, time, favorable-environment membership, and comparison tokens.

## Valid inputs and required output

The single object occurs once. The result contains only cited predicate tokens, provenance, blocker, and a non-evaluation guard.

## Mandatory and forbidden behavior

Exact identity, token preservation, provenance, opacity, blocker retention, determinism, and atomic failure are mandatory. Threshold decisions, context scoring, membership evaluation, comparison results, generated predicates, and partial success are forbidden.

## Implementation freedom

Language, AST layout, storage, ownership, allocation, serialization, and concurrency are implementation-defined. No predicate evaluator is prescribed.

## Errors and conformance

Errors are `UnknownFeatureId`, `MissingCoveredObject`, `UnexpectedCoveredObject`, `ObjectOrderMismatch`, `MissingSymbolTableEntry`, `MissingSourceReference`, `MissingDecisionBlocker`, and `ScientificEvaluationRequested`. All acceptance tests must pass.

## Unresolved science

Validity thresholds and executable predicate semantics remain preserved unresolved.
