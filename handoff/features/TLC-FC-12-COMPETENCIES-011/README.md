# TLC-FC-12-COMPETENCIES-011 — Provisionally separated qualitative metric descriptor

## What is this feature?

This feature preserves the qualitative-indicator, collective-coordination, and structural-space metric records `TLC-SO-COMPETENCIES-024`, `038`, and `043`.

## What must be implemented?

Implement one structural operation that validates the exact feature id, exact three-object population, complete provenance, and `structural_descriptor_only` mode, then emits one immutable descriptor in source order.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-011`; objects `024`, `038`, and `043` must occur exactly once; no extra object is valid; provenance must be complete; and only structural mode is accepted.

## What is the required output?

Return a descriptor preserving category `metric_evaluation`, boundary `provisionally_separated`, ordered identities `[024, 038, 043]`, opaque qualitative, collective, mastery, and geometric content, provenance, reservations, and unresolved status.

## What behavior is mandatory?

Validate before publication, preserve source order and opacity, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not generate qualitative ratings, observer results, mastery indices, collective synergy, identity compatibility, Hilbertian geometry, curvature, projection, scores, levels, thresholds, comparisons, or relation endpoints.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies exact order, descriptive Metric type, no observer or relation inference, mastery opacity, deterministic output, stable failures, and rejection of qualitative, collective, or geometric evaluation.

## Are unresolved scientific semantics involved?

Yes. Qualitative scales, observer rules, mastery weighting, collective metrics, geometry, projection, and comparison remain unresolved.