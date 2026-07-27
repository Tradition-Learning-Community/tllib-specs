# TLC-FC-09-VALUES-007 — Validity-domain membership AST

## What is this feature?
A structural compiler for the cited value-validity-domain set expression and its named tuple membership predicates.

## What must be implemented?
Validate the symbolic set expression and ordered tuple symbols, require every tuple component and known predicate identity, build `ValidityDomainMembershipAst`, and preserve all source and unresolved metadata.

## Valid inputs and required output
Inputs are one `SymbolicSetExpression` and an ordered `Sequence[SymbolId]`. The output is one immutable membership-query AST; it represents predicates but does not decide membership.

## Mandatory and forbidden behavior
Tuple-component preservation, source identity, predicate identity, source order, deterministic construction, and atomic failure are mandatory. Defining carrier sets, evaluating membership, inventing thresholds, or inferring admissibility are forbidden.

## Implementation freedom
Parser, AST layout, language, storage, ownership, allocation, serialization, and concurrency are free. Validation precedes construction and traceability precedes return.

## Errors and conformance
Source errors `missing_tuple_component`, `unknown_membership_predicate`, and `expression_parse_error` are preserved through public aliases. All acceptance tests are mandatory.

## Unresolved science
`carrier_set_definitions` and `membership_evaluation_policy` remain preserved unresolved; scientific membership evaluation requires an external provider.
