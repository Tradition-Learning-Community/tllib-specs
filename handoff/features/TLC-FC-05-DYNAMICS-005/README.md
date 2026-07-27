# TLC-FC-05-DYNAMICS-005 — Interaction operators

## What is this feature?

This feature constructs a traceable, unevaluated application of a source-listed interaction operator to ordered opaque entity references.

## What must be implemented?

Implement `CONSTRUCT-OPAQUE-INTERACTION-APPLICATION`. Validate the operator identifier, argument references, and carrier shapes before returning an immutable `UnevaluatedOperatorApplication` that preserves operator identity, argument identities, argument order, provenance, unresolved items, and reservations.

## Inputs and output

Inputs are `operator_id: InteractionOperatorId` and `arguments: Sequence[OpaqueEntityRef]`. The output is structural only and remains linked to TLC-SO-DYNAMICS-014 and TLC-SR-DYNAMICS-013.

## Mandatory and forbidden behavior

Do not infer arity, parameter types, codomain, return type, derivative contribution, execution behavior, or transition semantics. Do not reorder or mutate arguments. No successful partial result may be exposed after failure.

## Implementation freedom

Language, naming, storage, ownership, allocation, serialization format, concurrency policy, and internal validation decomposition remain implementation-defined when observable behavior is preserved.

## Errors and conformance

Expose `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` as defined in `contract.json`. Conformance requires every test in `acceptance.json`. Operator signatures and Community symbol reconciliation remain unresolved.