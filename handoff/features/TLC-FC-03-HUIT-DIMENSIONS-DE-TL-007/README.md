# TLC-FC-03-HUIT-DIMENSIONS-DE-TL-007 — Invariant group catalogue

Implement a pure structural operation that catalogues two separate opaque invariant groups: `value_invariant_group` (`TLC-SO-HUIT-DIMENSIONS-DE-TL-014`) and `lived_experience_invariant_group` (`TLC-SO-HUIT-DIMENSIONS-DE-TL-035`). Return an immutable `InvariantGroupCatalogue` with exactly two dimension-keyed entries and `proof_status` unresolved for each.

Preserve group identities, claims, source traces, eight unresolved identifiers, and `TLC-EA-HUIT-007-001`. Do not merge groups, prove claims, infer a common invariant or equivalence, treat lexical similarity as semantic, mutate inputs, or return a partial success. Runtime representation and internal architecture remain free. Conformance requires all tests in `acceptance.json`; scientific proof and evaluation remain unavailable.
