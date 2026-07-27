# TLC-FC-05-DYNAMICS-004 — Feedback equations

## What is this feature?

This feature constructs the source-defined feedback integral and kernel representation as one traceable, unevaluated expression.

## What must be implemented?

Implement `CONSTRUCT-SYMBOLIC-FEEDBACK-EXPRESSION`. Validate source and parameter identifiers and carrier shapes, preserve the external signal, kernel, and parameter map as distinct opaque inputs, and return an immutable `UnevaluatedIntegralExpression`.

## Inputs and output

Inputs are `external_input: OpaqueSignal`, `kernel: OpaqueKernel`, and `parameters: ParameterMap`. The output retains both scientific object identities, both relation identities, the integration-history notation, provenance, unresolved items, and reservations.

## Mandatory and forbidden behavior

Do not evaluate the integral, infer a kernel domain or parameter type, assert convergence, create a numerical result, or infer a transition. No successful partial result may be exposed after failure.

## Implementation freedom

Language, naming, storage, ownership, allocation, serialization format, concurrency policy, and internal validation decomposition remain implementation-defined when observable behavior is unchanged.

## Errors and conformance

Expose `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` as defined in `contract.json`. Conformance requires every test in `acceptance.json`. Kernel parameter types, integration domains, and convergence remain unresolved.