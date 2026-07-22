# Candidate functional decomposition report

## Input actually read

- Work-item input commit: `a92f6dfe905c102c5688cc6843b65673e5bea088`.
- Snapshot provenance commit: `738cb14328d1f06661b57ba83c9b43df3661cb15`.
- Objects: 1383 (Counter({'admissible': 913, 'blocked_locally': 344, 'provisionally_separated': 126})).
- Relations: 1365 (Counter({'admissible': 1016, 'blocked_locally': 349})).
- Contract-blocking terms: 26; non-blocking uncertainties: 804.
- Sources: 16 mathematical documents plus `algorithms/example.md` inspected as non-normative implementation material.
- Consistency: object and relation identifiers are unique; relation endpoints exist; snapshot/status counts match; no object fusion was performed.

| Source | Objects | Relations |
|---|---:|---:|
| `maths/00-master.md` | 40 | 37 |
| `maths/01-disciple.md` | 70 | 69 |
| `maths/02-community.md` | 57 | 56 |
| `maths/03-huit-dimensions-de-tl.md` | 118 | 117 |
| `maths/04-invariants.md` | 69 | 68 |
| `maths/05-dynamics.md` | 26 | 25 |
| `maths/06-theorems.md` | 30 | 29 |
| `maths/07-message.md` | 72 | 71 |
| `maths/08-principle.md` | 103 | 102 |
| `maths/09-values.md` | 103 | 102 |
| `maths/10-virtues.md` | 218 | 217 |
| `maths/11-capacities.md` | 100 | 99 |
| `maths/12-competencies.md` | 114 | 113 |
| `maths/13-practice.md` | 93 | 92 |
| `maths/14-lived-experience.md` | 70 | 69 |
| `maths/15-relations.md` | 100 | 99 |

## Result

224 candidate features, 1365 relation-level candidate dependencies, 3 non-selected variants, and 17 boundary issues were generated. Blocked objects and relations occur only with explicit blocking fields. Provisionally separated objects remain distinct scientific identifiers.

## Readiness

| Status | Count |
|---|---:|
| `insufficient_definition` | 11 |
| `ready_for_math_contract` | 69 |
| `requires_targeted_extraction` | 31 |
| `requires_targeted_scientific_review` | 113 |

## Categories

| Category | Count |
|---|---:|
| `configuration_candidate` | 2 |
| `constraint_evaluation` | 21 |
| `data_validation` | 16 |
| `evolution_dynamics` | 22 |
| `invariant_check` | 21 |
| `metric_evaluation` | 21 |
| `relation_evaluation` | 12 |
| `scientific_operator` | 22 |
| `state_representation` | 45 |
| `test_oracle_candidate` | 21 |
| `transformation` | 21 |

## Boundary analysis

The balanced registry boundary separates source, role, and scientific status. The minimal and fine alternatives are documented but not selected. Large clusters are flagged for review. Unknown representation fields, types, dimensions, and observable acceptance values remain unresolved rather than invented. The algorithm example was not treated as normative because it proposes discretization and numerical choices excluded from this stage.
