# Independent scientific review of candidate functional decomposition

Status: `candidate`
Input commit: `d0d1e26ef6a488aa291e1f4e616b9b2748ff2370`

## Executive result

The review recommends **revise**. All 224 feature candidates and all 1,365 dependency candidates were classified.
No feature is accepted without reservation because none of the 69 nominally ready candidates identifies an explicit
required oracle. Two nominally ready candidates retain blocking relations. Seventeen candidates have unresolved
excessive-aggregation boundaries. Of the dependencies, 554 are invalid self-edges,
811 are scientific context rather than software dependencies, and
0 correspond to an immediate dependency declared by the source feature.

The supplied execution manifest identifies this review as `TLC-FUNCTIONAL-DECOMPOSITION-REVIEW-001` and authorizes the candidate decomposition
for independent review with reservations. Its prior-stage decision explicitly states that no feature is approved, no
variant is selected, and no dependency is normative. The dependency classifications below therefore remain review
recommendations and do not promote any candidate edge to normative status.

## Verified counts

| Item | Count |
|---|---:|
| Features reviewed | 224 |
| ACCEPT_FOR_MATH_CONTRACT | 0 |
| ACCEPT_WITH_RESERVATIONS | 66 |
| REVISE_FEATURE_BOUNDARY | 17 |
| REQUIRES_TARGETED_EXTRACTION | 20 |
| REQUIRES_SCIENTIFIC_DECISION | 77 |
| REJECT_AS_SOFTWARE_FEATURE | 44 |
| Ready-linked dependencies fully reviewed | 252 |
| Boundary issues reviewed | 17 |
| Variants compared | 3 |

## Input schemas and anomalies

The feature registry is a mapping with `count` and a `features` sequence; each feature nests scientific basis, scope,
behavior, dependencies, testability, readiness, risks, and status. The dependency registry contains a single
`scientific_requires` type. Boundary issues contain only `feature_too_large`. Each variant repeats all 224 feature IDs
and differs only in narrative metadata. The input report in the working tree was locally modified before this review;
the audit used the committed input at `d0d1e26ef6a488aa291e1f4e616b9b2748ff2370` and did not include that modification.

Material anomalies: 554 self-dependencies; all 1,365 dependency types mechanically use `scientific_requires`; two ready
features retain explicit blocking relations; no ready feature names an explicit required oracle; and the three variants
do not instantiate distinct feature sets. No required file was missing.

The manifest provides no separate schemas and instructs the reviewer to preserve the actual repository structures;
the validator consequently checks the observed mappings and sequences rather than imposing an external schema.

## Review method and limits

Ready features received detailed field-by-field review. Their source ranges, candidate inputs/outputs, behavior,
preconditions, postconditions, constraints, invariants, test strategies, blockers, immediate dependencies, and boundary
membership are retained in `scientific-review.yaml`. Other statuses received structured classification. Every dependency
touching a ready feature was fully evaluated; remaining dependencies were classified by the same deterministic rules.
This review does not infer types, dimensions, equations, APIs, or missing scientific definitions.

`CONTRACT_WAVE_1` is only a candidate order of eight small, traceable behaviors. It is not ready to start until an
explicit source-grounded oracle is recorded for each entry and retained immediate dependencies are confirmed.

## Files actually read

- `registry/features/feature-candidates.yaml`
- `registry/features/feature-decomposition-variants.yaml`
- `registry/features/feature-boundary-issues.yaml`
- `registry/features/dependency-hints.yaml`
- `reports/functional-decomposition/feature-decomposition-report.md`
- `reports/functional-decomposition/feature-catalog.md`
- `reports/functional-decomposition/dependency-report.md`
- `reports/functional-decomposition/prioritization.yaml`
- `registry/functional-decomposition/decomposition-input-snapshot.yaml`
- `reports/functional-decomposition-input/blockers.yaml`
- `reports/functional-decomposition-input/unresolved-impact.yaml`
- `algorithms/example.md`
- `maths/00-master.md`
- `maths/01-disciple.md`
- `maths/02-community.md`
- `maths/03-huit-dimensions-de-tl.md`
- `maths/04-invariants.md`
- `maths/05-dynamics.md`
- `maths/06-theorems.md`
- `maths/07-message.md`
- `maths/08-principle.md`
- `maths/09-values.md`
- `maths/10-virtues.md`
- `maths/11-capacities.md`
- `maths/12-competencies.md`
- `maths/13-practice.md`
- `maths/14-lived-experience.md`
- `maths/15-relations.md`
