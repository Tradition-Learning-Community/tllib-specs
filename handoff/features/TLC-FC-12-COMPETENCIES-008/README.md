# TLC-FC-12-COMPETENCIES-008 — Provisionally separated transformation descriptor

## What is this feature?

This feature preserves four distinct axiomatic equation records: `TLC-SO-COMPETENCIES-108`, `109`, `110`, and `111`. They share the same canonical name but are not equivalent.

## What must be implemented?

Implement one structural operation that validates the exact feature id, all four distinct object identities, complete provenance, and `structural_descriptor_only` mode, then emits one immutable descriptor in source order.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-008`; all four object IDs must occur exactly once; no object may be substituted merely because it has the same name; provenance must be complete; and only structural mode is valid.

## What is the required output?

Return a descriptor preserving category `transformation`, boundary `provisionally_separated`, ordered identities `[108, 109, 110, 111]`, opaque equations, provenance, reservations, and unresolved status.

## What behavior is mandatory?

Use ObjectId as identity, preserve all four records separately, validate before publication, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not merge, deduplicate, alias, or infer equivalence from the repeated canonical name. Do not prove axioms, evaluate equations, transfer context, compute decomposition, virtue effects, metrics, distances, or mastery levels.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies four-ID distinctness despite repeated names, exact order, opacity, deterministic output, stable failures, and rejection of proof, metric, comparison, or level requests.

## Are unresolved scientific semantics involved?

Yes. Axiomatic truth, contextual transfer, decomposition, virtue reinforcement, metric, distance, and mastery semantics remain unresolved.