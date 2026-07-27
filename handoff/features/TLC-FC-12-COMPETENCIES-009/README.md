# TLC-FC-12-COMPETENCIES-009 — Admissible metric descriptor

## What is this feature?

This feature preserves three admissible metric records: `TLC-SO-COMPETENCIES-022`, `035`, and `085`.

## What must be implemented?

Implement one structural operation that validates the exact feature id, exact three-object population, complete provenance, and `structural_descriptor_only` mode, then emits one immutable descriptor in source order.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-009`; objects `022`, `035`, and `085` must occur exactly once; no extra object is valid; provenance must be complete; and only structural mode is accepted.

## What is the required output?

Return a descriptor preserving category `metric_evaluation`, boundary `admissible`, ordered object identities, opaque metric declarations, provenance, reservations, and unresolved status. A source object typed `Metric` remains descriptive and does not become an executable measurement.

## What behavior is mandatory?

Validate before publication, preserve source order and opacity, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not compute cognitive load, insight, mastery index, scores, levels, thresholds, ranks, diagnosis, comparison, or progression.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies the descriptive-only Metric type, exact order, opacity, no mastery or diagnostic result, deterministic output, stable failures, and rejection of evaluation.

## Are unresolved scientific semantics involved?

Yes. Measurement domains, inputs, units, evaluator rules, mastery index, cognitive-load, insight, and diagnosis remain unresolved.