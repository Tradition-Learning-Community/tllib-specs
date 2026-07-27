# TLC-FC-12-COMPETENCIES-007 — Blocked transformation descriptor

## What is this feature?

This feature preserves the validity-domain and collective-coordination equations `TLC-SO-COMPETENCIES-065` and `104` under the blocked-local boundary.

## What must be implemented?

Implement one structural operation that validates the exact feature id, both required objects, complete provenance, and `structural_descriptor_only` mode, then emits one immutable descriptor in source order.

## What are the valid inputs?

The feature id must be `TLC-FC-12-COMPETENCIES-007`; objects `065` and `104` must occur exactly once; no extra object is valid; provenance must be complete; and only structural mode is accepted.

## What is the required output?

Return a descriptor preserving category `transformation`, boundary `blocked_locally`, object order `[065, 104]`, opaque context and collective content, provenance, reservations, and unresolved status.

## What behavior is mandatory?

Validate before publication, preserve source order and opacity, and produce semantically identical output for identical structural inputs.

## What behavior is forbidden?

Do not evaluate validity predicates, affinity or time thresholds, favorable environments, collective aggregation, synergy, comparisons, or relation endpoints. Do not resolve the blocked boundary.

## What is left to the implementer?

Internal architecture, storage, ownership, allocation, serialization, concurrency, and independent validation order are implementation-defined.

## What errors must be observable?

`UnknownFeatureId`, `MissingCoveredObject`, `DuplicateCoveredObject`, `UnexpectedCoveredObject`, `MissingSourceReference`, `ScientificEvaluationRequested`, and `BlockedScientificDecision`.

## How is conformance verified?

`acceptance.json` verifies exact identity and order, opaque context preservation, non-inference of collective endpoints, deterministic output, stable failures, and rejection of threshold or collective computation.

## Are unresolved scientific semantics involved?

Yes. Context validity, thresholds, environment, collective coordination, and synergy remain unresolved. The package is structural only.