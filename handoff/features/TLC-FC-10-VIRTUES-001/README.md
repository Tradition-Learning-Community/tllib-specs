# TLC-FC-10-VIRTUES-001 — Apprenticeship responsibility handoff

## What is this feature?

A structural validator for an apprenticeship responsibility handoff record. It preserves source-bound bounded-role and guided-responsibility material without grading virtue.

## What must be implemented?

Implement the observable operation `CHECK-APPRENTICESHIP-RESPONSIBILITY`: validate the exact feature identity, require provenance for `TLC-SO-VIRTUES-100`, reject unsupported scientific or moral completion, and return the supplied artifact, reservations, assumptions, and provenance unchanged in a deterministic result envelope.

## Valid inputs and required output

The input is an opaque handoff artifact, an ordered provenance collection containing the required source object, and optional opaque reservations. Success returns an accepted source-bound descriptor. Failure returns one of the public errors defined in `contract.json` and no accepted result.

## Mandatory and forbidden behavior

Bounded-role and guided-responsibility fields, source-object identity, source order, opaque context, and caller reservations must be preserved. Scoring, ranking, weighting, thresholding, hierarchy construction, metric selection, formula completion, moral judgment, and source mutation are forbidden.

## Implementation freedom

Language, API spelling, storage, allocation, ownership, serialization, and internal decomposition are implementation-defined. Validation and preservation must complete before success becomes observable; no total internal algorithm is prescribed.

## Errors and conformance

The authoritative source errors `invalid_feature_id`, `missing_provenance`, and `unsupported_scientific_completion_request` are exposed through schema-compatible aliases. Conformance requires every test in `acceptance.json` to pass with failure atomicity.

## Unresolved science

No unresolved item is propagated by this feature, but virtue meaning and moral evaluation remain outside the executable contract.