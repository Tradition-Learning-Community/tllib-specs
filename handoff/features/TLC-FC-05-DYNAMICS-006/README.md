# TLC-FC-05-DYNAMICS-006 — State admissible

## What is this feature?

This feature builds a structural `StateCandidateRecord` from opaque values keyed by the twelve covered scientific-object identifiers.

## What must be implemented?

Implement `CONSTRUCT-OPAQUE-STATE-CANDIDATE-RECORD`. Validate every supplied component identifier and opaque value carrier, preserve all supplied key/value pairs, attach per-component provenance, unresolved items, and reservations, and return an immutable candidate record.

## Inputs and output

The input is `components: Mapping[ScientificObjectId, OpaqueValue]`. Complete, partial, and empty mappings are valid. The output retains every supplied key/value pair; omitted components remain absent. Completeness and state-space membership remain unasserted.

## Mandatory and forbidden behavior

Do not invent missing components, defaults, an explicit state type, a state space, initial or terminal states, completeness, or transitions. Opaque component values must not be evaluated or mutated. No successful partial result may be exposed after failure.

## Implementation freedom

Language, naming, storage, ownership, allocation, serialization format, concurrency policy, map implementation, and internal validation decomposition remain free when observable behavior is preserved.

## Errors and conformance

Expose `UNKNOWN_SOURCE_IDENTIFIER`, `TYPE_SHAPE_MISMATCH`, and `UNRESOLVED_SCIENTIFIC_SEMANTICS` as defined in `contract.json`. Conformance requires every test in `acceptance.json`. The eleven source unresolved identifiers and the absence of an explicit state space remain preserved.