# TLC-FC-09-VALUES-011 — Quantitative measure catalog

## What is this feature?
A structural declaration catalog for cited quantitative measures. Formulas, units, scales, and interpretations remain opaque metadata.

## What must be implemented?
Validate a sequence of uniquely identified measure declarations, require source provenance, preserve source order and every opaque scientific field, return `QuantitativeMeasureCatalog`, and attach complete traceability.

## Valid inputs and required output
Input is a source-addressable `Sequence[OpaqueMeasureDeclaration]`. The output is one immutable ordered catalog with no computed metric values.

## Mandatory and forbidden behavior
Unique identifiers, provenance, source order, opaque round-trip, deterministic construction, and atomic failure are mandatory. Formula evaluation, unit or scale inference, comparison, normalization, scoring, or aggregation are forbidden.

## Implementation freedom
Catalog representation, storage, ownership, language, allocation, serialization, and concurrency are free. Validation precedes publication; traceability precedes return.

## Errors and conformance
Source errors `duplicate_measure_identifier`, `missing_measure_provenance`, and `unknown_source_identifier` are preserved through public aliases. Every acceptance test is mandatory.

## Unresolved science
`metric_formulas`, `scales_and_units`, and `comparison_semantics` remain preserved unresolved. An external evaluator is required for any metric computation.
