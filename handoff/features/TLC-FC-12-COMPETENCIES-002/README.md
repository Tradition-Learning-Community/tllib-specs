# TLC-FC-12-COMPETENCIES-002 — Provisionally separated constraint descriptor

## What is this feature?

This feature builds a structural descriptor for the provisionally separated mastery-progression constraint `TLC-SO-COMPETENCIES-031`.

## What must be implemented?

Implement one operation accepting the exact feature identity, exactly one opaque object payload, complete provenance, and request mode `structural_descriptor_only`. It returns one immutable descriptor preserving the source category and boundary.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-002`; object `TLC-SO-COMPETENCIES-031` must occur exactly once; no additional object is valid; provenance must be present; and only structural mode is authorized.

## What is the required output?

Return a structurally valid descriptor preserving category `constraint_evaluation`, boundary `provisionally_separated`, object identity, opaque payload, provenance, reservations, and unresolved status. No mastery result or constraint truth is returned.

## What behavior is mandatory?

Validate before construction, preserve source identity and opacity, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not calculate an argmax, mastery score, level, threshold, ethical constraint, comparison, or progression. Do not merge or resolve the provisionally separated scientific boundary.

## What is left to the implementer?

Internal data structures, ownership, allocation, serialization, concurrency, and the order among independent validations are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies exact identity, object membership, provenance, opacity, determinism, rejection of evaluation, stable failures, and traceability.

## Are unresolved scientific semantics involved?

Yes. Mastery optimization and ethical-constraint semantics remain unresolved and external. The package is structural only.