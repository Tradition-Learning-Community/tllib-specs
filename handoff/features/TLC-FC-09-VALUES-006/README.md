# TLC-FC-09-VALUES-006 — Value transformation AST

## What is this feature?
A structural assembler for the cited decision-influence and collective-understanding equations as two distinct symbolic transformation branches.

## What must be implemented?
Require exactly one `decision_equation` and one `collective_equation`, validate their source bindings and symbols, preserve each branch and opaque payload, build `ValueTransformationAst`, and attach complete traceability.

## Valid inputs and required output
The two inputs are source-addressable `SymbolicEquation` values. The output is one immutable AST containing distinct decision and collective-intelligence branches.

## Mandatory and forbidden behavior
Branch distinction, source identity, source-declared relations, deterministic construction, and atomic failure are mandatory. Input/output domain inference, execution of the equations, invented comparisons, invented aggregations, or decision selection are forbidden.

## Implementation freedom
Language, internal AST, storage, ownership, allocation, serialization, and concurrency are free. Validation precedes successful construction; traceability precedes return.

## Errors and conformance
Source errors `missing_transformation_branch`, `branch_source_mismatch`, and `unbound_symbol` are exposed through one-to-one aliases. All tests in `acceptance.json` are mandatory.

## Unresolved science
`input_output_domains` and `evaluation_algorithm` remain preserved unresolved. Any evaluation requires an external provider.
