# TLC-FC-05-DYNAMICS-002 — Dynamics admissible

## What is this feature?

This feature assembles source-listed deterministic and stochastic equation records into an ordered, traceable, unevaluated Dynamics bundle.

## What must be implemented?

Implement `BUILD-UNEVALUATED-DYNAMICS-BUNDLE`. Validate equation identifiers, referenced symbols, and carrier shapes before returning a `DynamicsBundle[OpaqueEquation]` whose membership, order, payloads, classifications, provenance, unresolved items, and reservations reproduce the supplied sequence.

## Inputs and output

Inputs are `equation_sources: Sequence[OpaqueEquation]` and `symbols: SymbolTable`. An empty sequence is valid when carrier and symbol validation succeeds. The output is an immutable structural bundle.

## Mandatory and forbidden behavior

Preserve every supplied equation and its order. Do not solve, discretize, sample, initialize, classify beyond source metadata, create a trajectory, select a solver or distribution, or reinterpret derivative notation as an executable transition. No partial bundle may be exposed after failure.

## Implementation freedom

Language, storage, ownership, allocation, serialization format, concurrency policy, public naming, and internal validation decomposition remain free when observable behavior is preserved.

## Errors and conformance

Expose `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` as specified in `contract.json`. Conformance requires every test in `acceptance.json`. Equation types, state spaces, initial conditions, stochastic details, solvers, and discretization remain unresolved and require an external scientific transition engine.