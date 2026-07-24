# Candidate IR report — TLC-FC-05-DYNAMICS-001

This engineering-candidate IR was derived only from contract commit `41028d616ab28af0ae1ba2f328c8bb8add2d68dd`. Scientific validation remains pending.

The IR preserves four independent viability predicates: minimum actor-set cardinality, connectivity bound, community-values deviation bound, and integrated memory-deviation bound. Eleven contract inputs, four states, six parameters, six abstract/opaque operators, four predicates, and one opaque output are represented. Constraint identity and inclusive boundary comparators are preserved.

All five contract-level unresolved items are propagated. The temporal domain, `L`/`lambda2`, norms, memory notation, and output semantics are not decided. No boolean aggregation, discretization, numerical integration method, tolerance, precision, implementation language, library, solver, API, or executable oracle is produced.

The IR is suitable for architecture and downstream candidate-task decomposition. It is not suitable for concrete type lowering, executable tests, or implementation until the relevant unresolved items are scientifically resolved or explicitly accepted as external interfaces.
