# TLC-FC-12-COMPETENCIES-012 — Admissible scientific operator descriptor

## What is this feature?

This feature preserves the technical or functional competencies record `TLC-SO-COMPETENCIES-007`, whose source type is `Function`, as an admissible structural operator descriptor.

## What must be implemented?

Implement one structural operation that validates the exact feature id, exactly one opaque object, complete provenance, and `structural_descriptor_only` mode, then emits one immutable descriptor preserving the descriptive technical scope.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-012`; object `TLC-SO-COMPETENCIES-007` must occur exactly once; no extra object is valid; provenance must be present; and only structural mode is accepted.

## What is the required output?

Return a descriptor preserving category `scientific_operator`, boundary `admissible`, object identity, descriptive technical or functional scope, opaque payload, provenance, reservations, and unresolved status. Source type `Function` remains non-callable.

## What behavior is mandatory?

Validate before publication, preserve the descriptive scope and source identity, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not execute gestures, tools, procedures, techniques, repetition, refinement, acquisition, mastery, performance, observation, or assessment. Do not promote the source Function type to a callable runtime operation or competency enum.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies exact identity, descriptive-only scope, non-callability, opacity, deterministic output, stable failures, and rejection of action or mastery requests.

## Are unresolved scientific semantics involved?

Yes. Action signatures, domains, procedures, acquisition, practice, observation, performance, and mastery remain unresolved.