# TLC-FC-09-VALUES-004 — Deferred value dynamics AST

## What is this feature?
A structural assembler for three scientifically deferred equations: consolidation, motivation, and collective feedback.

## What must be implemented?
Require exactly one equation for each named role, validate each source binding, retain each role-local scientific blocker, produce `DeferredValueDynamicsAst`, and attach complete traceability.

## Valid inputs and required output
Inputs are three source-addressable `SymbolicEquation` values named `consolidation`, `motivation`, and `collective_feedback`. The output contains exactly three distinct role-labelled nodes with unchanged opaque payloads.

## Mandatory and forbidden behavior
Exact role cardinality, source identity, deterministic structural construction, unresolved propagation, and atomic failure are mandatory. Scientific status promotion, equation evaluation, solver behavior, inferred role aliases, or invented formulas are forbidden.

## Implementation freedom
Representation, storage, ownership, language, allocation, serialization, and concurrency are free. Validation must complete before the three-node result is published, and traceability must be attached before return.

## Errors and conformance
Source errors `missing_required_role`, `source_role_mismatch`, and `unknown_source_identifier` are preserved through public aliases. All acceptance tests are mandatory and no partial AST is observable on failure.

## Unresolved science
`consolidation_semantics`, `motivation_semantics`, and `collective_feedback_semantics` remain preserved unresolved. Scientific execution requires an external provider.
