# TLC-FC-03-HUIT-DIMENSIONS-DE-TL-008 — Partial invariance registry

Implement a pure structural operation that registers two distinct context-tagged claims: `value_partial_invariance` (`OpaquePerturbationInvariantClaim`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-073`) and `temporal_core_invariance` (`OpaqueTemporalCoreClaim`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-110`).

Return an immutable `PartialInvarianceRegistry` with exactly two entries, preserving contexts, identities, opaque payloads, traces, nine unresolved identifiers, and `TLC-EA-HUIT-008-001`. Set verification, feature-boundary, and identity status to `unresolved`.

Do not infer a shared invariant, verify either claim, merge or alias contexts, interpret perturbation or temporal procedures, mutate inputs, or produce partial success. Language, storage, ownership, allocation, serialization, concurrency, and internal decomposition remain free. Conformance requires all tests in `acceptance.json`; scientific verification and identity remain deferred.
