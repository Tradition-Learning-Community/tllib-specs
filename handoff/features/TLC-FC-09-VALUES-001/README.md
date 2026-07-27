# TLC-FC-09-VALUES-001 — Axiomatic foundation constraint AST

## What is this feature?
A deterministic structural compiler for cited axiomatic-foundation statements. It produces a source-addressable constraint AST and does not decide whether any axiom is scientifically true.

## What must be implemented?
Validate the statement sequence and provenance, reject unknown or duplicate statement identities, preserve source order and opaque symbolic payloads, construct the declared AST, and attach complete traceability.

## Valid inputs and required output
Inputs are a non-empty ordered sequence of `AxiomaticStatement` values plus `SourceProvenance`. The output is one immutable `AxiomaticConstraintAst` carrying the exact feature, object, relation, unresolved-item, reservation, and provisional-assumption identities.

## Mandatory and forbidden behavior
Structural validation, source-order preservation, deterministic construction, opaque round-trip, and failure atomicity are mandatory. Truth evaluation, scientific approval, inferred formulas, ranking, aggregation, priority, measurement, or decision semantics are forbidden.

## Implementation freedom
Language, public API spelling, storage, ownership mechanism, allocation, serialization, concurrency policy, and internal decomposition are free. Only the observable partial order—validate before publishing the AST, then attach traceability before return—is normative.

## Errors and conformance
The source error identifiers `empty_statement_set`, `unknown_source_identifier`, and `duplicate_statement_identifier` are preserved through one-to-one schema-compatible public aliases in `contract.json`. No partial result is observable on failure. Every test in `acceptance.json` is mandatory.

## Unresolved science
`axiom_scientific_status` and `constraint_truth_semantics` remain preserved unresolved. Scientific evaluation requires a future external provider and is not part of this package.
