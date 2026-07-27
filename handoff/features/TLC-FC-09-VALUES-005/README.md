# TLC-FC-09-VALUES-005 — Axiomatic dynamics expression node

## What is this feature?
A structural compiler for exactly one provisionally separated axiomatic-dynamics equation.

## What must be implemented?
Validate a non-empty symbolic expression and its exact source object, parse only enough structure to create `AxiomaticDynamicsExpressionNode`, preserve provisional separation and opaque payloads, and attach traceability.

## Valid inputs and required output
Inputs are one `SymbolicExpression` and one `ScientificObjectId`. The output is one immutable source-bound expression node with unresolved semantics and the provisional assumption preserved.

## Mandatory and forbidden behavior
Exact source binding, deterministic structural parsing, identity separation, opaque round-trip, and atomic failure are mandatory. Scientific classification, numerical evaluation, inferred aliases, or completion of missing semantics are forbidden.

## Implementation freedom
Parser technology, AST representation, storage, ownership, allocation, language, serialization, and concurrency are free. Validation must precede successful node publication and traceability must be complete before return.

## Errors and conformance
Source errors `empty_expression`, `unexpected_source_object`, and `expression_parse_error` are preserved through schema-compatible aliases. All acceptance tests are mandatory.

## Unresolved science
`axiomatic_dynamics_classification` and `evaluation_semantics` remain preserved unresolved. Any scientific evaluation is external to this package.
