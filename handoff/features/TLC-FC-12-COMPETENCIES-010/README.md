# TLC-FC-12-COMPETENCIES-010 — Blocked quantitative metric descriptor

## What is this feature?

This feature preserves the quantitative-measures record `TLC-SO-COMPETENCIES-023` under the blocked-local boundary.

## What must be implemented?

Implement one structural operation that validates the exact feature id, exactly one opaque object, complete provenance, and `structural_descriptor_only` mode, then emits one immutable descriptor.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-010`; object `TLC-SO-COMPETENCIES-023` must occur exactly once; no extra object is valid; provenance must be present; and only structural mode is accepted.

## What is the required output?

Return a descriptor preserving category `metric_evaluation`, boundary `blocked_locally`, the opaque quantitative formulas and symbols, provenance, reservations, and unresolved status. The formulas remain descriptive strings or symbols, not executable calculations.

## What behavior is mandatory?

Validate before publication, preserve source identity and opacity, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not calculate accuracy, efficiency, success probability, actualization rate, expectation, norm, division, zero-denominator behavior, units, scores, levels, or comparisons. Do not resolve the blocked boundary.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies exact identity, opacity of formulas, deterministic output, stable failures, and rejection of quantitative computation including zero-denominator questions.

## Are unresolved scientific semantics involved?

Yes. Numerators, denominators, units, data sources, zero handling, and evaluator semantics remain unresolved.