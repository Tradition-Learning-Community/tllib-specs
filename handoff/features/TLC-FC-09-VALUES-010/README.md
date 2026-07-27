# TLC-FC-09-VALUES-010 — Essential-property predicate set

## What is this feature?
A structural assembler for the five cited essential value properties: invariance, hierarchy, motivation, context, and integration.

## What must be implemented?
Accept exactly one symbolic claim for each source-declared property kind, preserve their required order and distinct identities, produce `EssentialPropertyPredicateSet`, and attach complete provenance and unresolved semantics.

## Valid inputs and required output
Input is a mapping from the five `EssentialPropertyKind` roles to `SymbolicClaim` values. The output is one immutable ordered predicate set with exactly five distinct entries.

## Mandatory and forbidden behavior
Exact membership, cardinality, source order, identity separation, opaque round-trip, deterministic construction, and atomic failure are mandatory. Property evaluation, cross-property consistency decisions, merging, ranking, or invented precedence are forbidden.

## Implementation freedom
Mapping representation, internal storage, ownership, language, allocation, serialization, and concurrency are free. Validation precedes successful assembly; traceability precedes return.

## Errors and conformance
Source errors `missing_property_kind`, `duplicate_property_kind`, and `unknown_property_kind` are preserved through public aliases. Every acceptance test is mandatory.

## Unresolved science
`property_evaluation_semantics` and `cross_property_consistency` remain preserved unresolved. Scientific evaluation requires an external provider.
