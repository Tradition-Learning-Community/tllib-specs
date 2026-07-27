# TLC-FC-09-VALUES-003 — Admissible value dynamics AST

## What is this feature?
A structural assembler for the four cited admissible value-dynamics equations. It binds equations to source objects and symbol identities without solving them.

## What must be implemented?
Validate the equation sequence and symbol table, preserve declared equation order and dynamic roles, reject missing sources, unbound symbols, or duplicate roles, produce `AdmissibleValueDynamicsAst`, and attach complete traceability.

## Valid inputs and required output
Inputs are an ordered non-empty `Sequence[SymbolicDynamicsEquation]` and one `SymbolTable`. The output is one immutable dynamics AST preserving every source object, relation, opaque expression, unresolved item, reservation, and provisional assumption.

## Mandatory and forbidden behavior
Exact role and source binding, order preservation, deterministic structure, opaque round-trip, and atomic failure are mandatory. Solving, discretization, initial-condition inference, state-domain inference, numerical evaluation, ranking, or aggregation are forbidden.

## Implementation freedom
Internal representation, parser, storage, ownership, allocation, serialization, language, and concurrency policy remain implementation-defined. Validation must precede successful assembly, and traceability must be attached before publication.

## Errors and conformance
Source errors `missing_equation_source`, `unbound_symbol`, and `duplicate_equation_role` have one-to-one public aliases in `contract.json`. Every acceptance test is required and no partial result may escape.

## Unresolved science
`state_domains`, `initial_conditions`, and `solver_and_discretization` remain preserved unresolved. An external scientific provider is required for any execution beyond structural assembly.
