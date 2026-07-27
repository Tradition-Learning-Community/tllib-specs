# TLC-FC-10-VIRTUES-007 — Virtue-function role-label invariant

## What is this feature?

A structural validator for the source-declared `V_fonction` role labels.

## What must be implemented?

Implement `CHECK-VIRTUE-FUNCTION-INVARIANT`: validate `TLC-FC-10-VIRTUES-007`, require provenance for `TLC-SO-VIRTUES-060`, and preserve `ancrage`, `guidage`, `unification`, and `contrainte` exactly as labels in their supplied order.

## Valid inputs and required output

The input is an opaque role-label artifact, ordered provenance, and optional reservations. Success returns the unchanged artifact and traceability; failure returns a named error without an accepted result.

## Mandatory and forbidden behavior

The four required labels, their spelling, their supplied ordering, opaque context, and additional caller-supplied labels must be preserved. Substitution, translation, normalization, prioritization, hierarchy, weighting, scoring, semantic expansion, or formula completion is forbidden.

## Implementation freedom

Internal storage and validation mechanisms are free. The package prescribes only exact label preservation and failure behavior, not a language, layout, serialization, or total algorithm.

## Errors and conformance

The public aliases in `contract.json` preserve the three authoritative source error identifiers. `acceptance.json` verifies exact labels, opacity, deterministic output, and atomic failure.

## Unresolved science

No executable meaning is assigned to the four labels; they remain source-bound labels only.