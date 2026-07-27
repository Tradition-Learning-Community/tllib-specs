# TLC-FC-05-DYNAMICS-007 — State blocked locally

## What is this feature?

This feature preserves an ambiguous source expression in an explicitly unclassified state-or-evolution node.

## What must be implemented?

Implement `PRESERVE-STATE-OR-EVOLUTION-EXPRESSION`. Validate the source identifier, expression carrier, and optional hint carrier; preserve the expression and hint unchanged; and return an immutable `UnclassifiedStateEvolutionNode` with unresolved classification, provenance, unresolved items, and reservations.

## Inputs and output

Inputs are `source_expression: OpaqueExpression` and `classification_hint: Optional[OpaqueTag]`. The hint may be absent. A present hint is non-authoritative metadata only and must never decide whether the expression denotes a state or an evolution.

## Mandatory and forbidden behavior

The output must remain explicitly unclassified. Do not classify it as a state or evolution, infer a derivative or transition, create initial or terminal states, execute stochastic notation, or mutate the supplied expression or hint. No successful partial result may be exposed after failure.

## Implementation freedom

Language, naming, storage, ownership, allocation, serialization format, concurrency policy, and internal validation decomposition remain implementation-defined when observable behavior is preserved.

## Errors and conformance

Expose `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` as defined in `contract.json`. Conformance requires every test in `acceptance.json`. TLC-UT-DYNAMICS-007 and the state-versus-evolution boundary remain preserved and unresolved.
