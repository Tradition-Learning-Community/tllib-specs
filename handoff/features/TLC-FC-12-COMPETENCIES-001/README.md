# TLC-FC-12-COMPETENCIES-001 — Blocked constraint descriptor

## What is this feature?

This feature builds a provenance-preserving structural descriptor for the blocked-local constraint records identified by `TLC-SO-COMPETENCIES-044` and `TLC-SO-COMPETENCIES-099`.

## What must be implemented?

Implement one operation that accepts the exact feature identity, exactly the two required opaque scientific objects, complete per-object provenance, and the request mode `structural_descriptor_only`. It returns one immutable descriptor whose object order is `[TLC-SO-COMPETENCIES-044, TLC-SO-COMPETENCIES-099]`.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-001`; both required object identities must occur exactly once; no additional object is accepted; every object must have a source reference; and the request mode must be structural only.

## What is the required output?

Return a structurally valid descriptor preserving feature identity, category `constraint_evaluation`, boundary `blocked_locally`, ordered object identities, opaque payloads, provenance, reservations, and unresolved scientific status. No scientific truth value is returned.

## What behavior is mandatory?

Validate all structural obligations before publishing a result, preserve opaque data without interpretation, preserve source order, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not evaluate either constraint or axiom, calculate mastery, select thresholds, simulate dynamics, infer scientific types or dimensions, resolve the blocked boundary, or expose a successful partial descriptor after failure.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and the order among independent validation checks are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision` are the authoritative error codes.

## How is conformance verified?

`acceptance.json` verifies exact identity and membership, source-order preservation, opacity, deterministic output, stable errors, rejection of scientific evaluation, and complete traceability.

## Are unresolved scientific semantics involved?

Yes. Scientific evaluation and the blocked scientific decision remain preserved unresolved. This package is ready only for structural descriptor implementation.