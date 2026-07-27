# TLC-FC-12-COMPETENCIES-016 — Provisionally separated relation descriptor

## What is this feature?

This feature preserves the relation record `TLC-SO-COMPETENCIES-056` describing a possible technical/cognitive covariance association. Its relation endpoints are unresolved and the authoritative covered-relation set is empty.

## What must be implemented?

Implement one structural operation that validates the exact feature id, exactly one relation object, complete provenance, and `structural_descriptor_only` mode, then emits one immutable relation descriptor.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-016`; object `TLC-SO-COMPETENCIES-056` must occur exactly once; no extra object is valid; provenance must be present; and only structural mode is accepted. Caller-supplied endpoint claims are not authoritative.

## What is the required output?

Return a descriptor preserving category `relation_evaluation`, boundary `provisionally_separated`, object identity, opaque relation content, provenance, reservations, `covered_relations=[]`, and `relation_endpoints=unresolved`.

## What behavior is mandatory?

Validate before publication, preserve the empty relation set and unresolved endpoint status, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not infer technical or cognitive endpoints from symbols or labels. Do not create relation edges, covariance values, association strengths, truth values, component comparisons, scores, thresholds, or progression.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies the empty covered-relation set, unresolved endpoints, no endpoint inference, exact identity, opacity, deterministic output, stable failures, and rejection of relation evaluation.

## Are unresolved scientific semantics involved?

Yes. Endpoint identities, relation truth, covariance, association strength, comparison, and all relation-evaluation semantics remain unresolved.