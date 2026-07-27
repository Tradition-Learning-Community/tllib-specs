# TLC-FC-09-VALUES-018 — Systemic-coherence matrix validation

## What is this feature?
A deterministic structural validator for the cited systemic-coherence matrix constraints: its shape must match the declared square order and every entry must lie in the sourced closed interval `[-1, 1]`.

## What must be implemented?
Validate a positive declared order, verify exact square shape, verify every opaque scalar entry against the sourced closed interval without assigning category semantics, return `CoherenceMatrixValidationResult`, and attach complete active-source traceability.

## Valid inputs and required output
Inputs are `matrix: Matrix[OpaqueScalar]` and `declared_order: PositiveInteger`. The output is one immutable structural validation result. The interval endpoints `-1` and `1` are valid.

## Mandatory and forbidden behavior
Order/shape agreement, square shape, closed-interval validation, deterministic result, source identity, unresolved propagation, and atomic failure are mandatory. Endpoint identity inference, compatibility/tension/opposition mapping, matrix evaluation, equivalence inference, or output-category invention is forbidden.

## Implementation freedom
Row traversal, scalar carrier, storage, ownership, language, allocation, serialization, and concurrency are free. Shape and interval checks may be internally ordered independently after input validation; both must complete before success is published.

## Errors and conformance
Source errors `declared_order_mismatch`, `non_square_matrix`, and `entry_outside_closed_interval` are preserved through public aliases. Every acceptance test is mandatory.

## Unresolved science
`UNRES-M`, `UNRES-ENDPOINTS`, `UNRES-CATEGORIES`, and `UNRES-OUTPUT` remain unresolved. Historical candidate IRs are comparison-only; the active mathematical contract and active registry IR govern this package.
