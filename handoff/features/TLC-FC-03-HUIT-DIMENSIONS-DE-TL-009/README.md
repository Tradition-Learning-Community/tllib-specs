# TLC-FC-03-HUIT-DIMENSIONS-DE-TL-009 — Invariance declaration comparison

Implement a pure structural comparison record with two named sides: `definition_claim` from `TLC-SO-HUIT-DIMENSIONS-DE-TL-008` and `introduction_claim` from `TLC-SO-HUIT-DIMENSIONS-DE-TL-039`. Both exact source locations are required.

Return an immutable `InvarianceDeclarationComparison` preserving both distinct identities, types, payloads, source locations, nine unresolved identifiers, and `TLC-EA-HUIT-009-001`. Set equivalence, feature-boundary, and identity status to `unresolved`.

Do not infer equivalence, deduplicate lexically similar claims, interpret payloads, merge sides, resolve boundaries, mutate inputs, or return partial success. Language, storage, ownership, allocation, serialization, concurrency, and internal decomposition remain free. Conformance requires all tests in `acceptance.json`; scientific equivalence and identity remain deferred.
