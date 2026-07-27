# TLC-FC-10-VIRTUES-002 — Observational-learning assumption registration

## What is this feature?

A declarative structural operation that records supplied modelage, shadowing, apprenticeship, and community-exposure claims as opaque evidence.

## What must be implemented?

Implement `REGISTER-OBSERVATIONAL-LEARNING-ASSUMPTION`: validate the exact feature identity and provenance for `TLC-SO-VIRTUES-016`, preserve all supplied claims and evidence, propagate the unresolved value `scientific ambiguity`, and return a deterministic source-bound descriptor.

## Valid inputs and required output

Inputs are an opaque claim bundle, ordered provenance, and optional reservations. Success returns the unchanged claims with the unresolved item exactly once. Errors return no accepted result.

## Mandatory and forbidden behavior

Claim labels, evidence, context, source identity, order, reservations, and unresolved status are mandatory preservation obligations. Deriving an imitation rule, acquisition transition, learning algorithm, score, hierarchy, metric, threshold, ranking, or moral decision is forbidden.

## Implementation freedom

Internal representation, language, storage, ownership, and validation decomposition are free. Only validation and preservation must precede publication; the algorithm file does not impose a total internal sequence.

## Errors and conformance

Expose the authoritative source errors through the aliases in `contract.json`. Conformance is verified by `acceptance.json`, including exact unresolved propagation and failure atomicity.

## Unresolved science

Observational-learning semantics remain `preserved_unresolved`. The package supports declarative registration only, not scientific execution.