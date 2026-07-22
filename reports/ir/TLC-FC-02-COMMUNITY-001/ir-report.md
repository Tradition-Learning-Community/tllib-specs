# Candidate intermediate representation report

`TLC-IR-TLC-FC-02-COMMUNITY-001` transforms the candidate mathematical contract into one semantic IR. It preserves the C1 shared-values-core axiom as a graph of 13 nodes and 7 edges while retaining all four scientific unknowns.

The source contract is status `candidate`, has `ready_for_ir: false`, and recommends `revise`. This run therefore uses `candidate_with_preserved_reservations`; it does not scientifically validate or amend the contract. No critical contract issue exists, but four major issues block lowering and implementation planning: the measure, coherence predicate, actor domain, and result semantics are undefined. The normalization-equivalence reservation remains non-blocking for semantic preservation.

Only the semantic variant is justified. Functional lowering would require the missing result/evaluation semantics; compute lowering would require undefined operators and a dataflow; dynamic lowering has no source state or temporal basis. The output remains opaque, implementation decisions remain deferred, coverage has no missing element, and code generation is explicitly disabled.
