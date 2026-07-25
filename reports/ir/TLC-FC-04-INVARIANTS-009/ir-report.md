# Final specialized prototype IR — TLC-FC-04-INVARIANTS-009

- Main operation: `construct_cohesion_interval_constraint`
- Classification: `substantive_and_implementable`
- Technical result: Produces an immutable symbolic AST for interval membership, a below-lower-bound fragmentation annotation, and an above-upper-bound centralization-and-rigidity annotation, with TLC-UT-INVARIANTS-009 preserved.
- Remaining opaque boundary: No numeric domain, comparator, ordering implementation, bound values, metric, score, transition rule, or cohesion evaluator is supplied or inferred.
- Ready for reference Python/C++ prototype: yes
- Ready for canonical IR/production: no
