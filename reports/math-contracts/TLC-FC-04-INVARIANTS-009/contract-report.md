# Final specialized contract — TLC-FC-04-INVARIANTS-009

- Responsibility: Construct the unevaluated symbolic interval constraint and the two source-stated out-of-interval consequence annotations for community cohesion.
- Callable: `construct_cohesion_interval_constraint`
- Input: `CohesionIntervalSymbols`
- Output: `SymbolicCohesionIntervalConstraint`
- Observable effect: Produces an immutable symbolic AST for interval membership, a below-lower-bound fragmentation annotation, and an above-upper-bound centralization-and-rigidity annotation, with TLC-UT-INVARIANTS-009 preserved.
- Opaque boundary: No numeric domain, comparator, ordering implementation, bound values, metric, score, transition rule, or cohesion evaluator is supplied or inferred.
- Reference Python ready: yes
- C++ prototype ready: yes
- Canonical IR and production ready: no
- Scientific reservations: preserved
