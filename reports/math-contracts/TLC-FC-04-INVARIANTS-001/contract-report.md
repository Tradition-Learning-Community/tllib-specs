# Specialized limited engineering contract — TLC-FC-04-INVARIANTS-001

- Responsibility: Register the four source-backed admissibility or rupture axioms as a constraint set without evaluating them.
- Callable: `build_admissibility_constraint_set`
- Input: `AdmissibilityAxiomRecord[]`
- Output: `ConstraintSet`
- Observable effect: Returns a set containing exactly one immutable entry per supplied axiom ID, with source order and references retained.
- Reference Python ready: yes
- C++ prototype ready: yes
- Scientific reservations: preserved
