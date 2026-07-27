# TLC-FC-05-DYNAMICS-003 — Dynamics blocked locally

## What is this feature?

This feature preserves a locally blocked stochastic expression as a traceable `UnevaluatedStochasticEquation`.

## What must be implemented?

Implement `PRESERVE-STOCHASTIC-EXPRESSION`. Validate the source and symbol identifiers and carrier shapes, copy the opaque expression without transformation, retain the locally blocked status, and attach provenance, unresolved items, and reservations.

## Inputs and output

Inputs are `source_expression: OpaqueStochasticExpression` and `symbols: SymbolTable`. The output is an immutable, explicitly unevaluated and locally blocked stochastic-equation record.

## Mandatory and forbidden behavior

The expression payload must round-trip unchanged. Do not infer a distribution, filtration, covariance, process type, stochastic integration convention, solver, seed, sample, probability law, or executable transition. No partial output may be exposed after failure.

## Implementation freedom

Language, naming, storage, ownership, allocation, serialization format, concurrency policy, and internal validation decomposition remain free when observable preservation is unchanged.

## Errors and conformance

Expose `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` as defined in `contract.json`. Conformance requires every test in `acceptance.json`. The local catalogue block and stochastic semantics remain preserved unresolved.