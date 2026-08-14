# Generational Propagation handoff generation report

## Publication identity

- Domain: `29 — Generational Propagation / Propagation générationnelle`
- Production branch: `pipeline/domain-29-generational-propagation`
- Pull request: pending creation at this report revision
- Baseline `main`: `b6b5f2a4acb46f04e91f809e8136822e2a77cd12`

## Scientific authority

- Authoritative source: `maths/29-generational-propagation/generational-propagation.md`
- Source blob: `19f894e70b5e6898cc0db2fbd8b402e7d843393f`
- Confirmed scientific provider: `04 Invariants`
- Invariants source: `maths/04-invariants/invariants.md`
- Invariants source blob: `5bddc38b4a74465c2bc3b1d2e9f8aac004e86800`

The Wave-3 cross-analysis confirms exactly `29 -> 04` as the scientific domain dependency and no runtime domain dependency. There is no `29 -> 28`, `29 -> 30`, or `29 -> 31` edge. In particular, the source-local `dJ/dx` used by domain 29 is not demonstrated to be the derivative of the teleological `J` from Finality 28 and is never bound to that domain. Expansion 30 and Institutionalization 31 are future consumers of domain-29 provider semantics, especially `G_t=(V_t,E_t,w)`. The unresolved `31 -> 24` relation is not changed by this publication.

## Scientific inventory

- Scientific objects: **81**
- Scientific relations: **36**
- Unresolved/provider-boundary items: **17**
- Finalized feature population: **28**

Execution distribution:

- `executable`: **5**
- `conditionally_executable`: **9**
- `structural_only`: **14**

Scientific-status distribution:

- `defined`: **8**
- `partially_defined`: **2**
- `external_provider_required`: **11**
- `preserved_unresolved`: **7**

## Final feature population

1. `TLC-FC-29-GENERATIONAL-PROPAGATION-001` — Secondary transmission threshold predicate
2. `TLC-FC-29-GENERATIONAL-PROPAGATION-002` — Social validation procedure boundary
3. `TLC-FC-29-GENERATIONAL-PROPAGATION-003` — Generational dynamics expression descriptor
4. `TLC-FC-29-GENERATIONAL-PROPAGATION-004` — Stochastic variation provider boundary
5. `TLC-FC-29-GENERATIONAL-PROPAGATION-005` — Constructive mutation predicate
6. `TLC-FC-29-GENERATIONAL-PROPAGATION-006` — Destructive mutation predicate
7. `TLC-FC-29-GENERATIONAL-PROPAGATION-007` — Innovation envelope predicate
8. `TLC-FC-29-GENERATIONAL-PROPAGATION-008` — dJdx identity and non-binding guard
9. `TLC-FC-29-GENERATIONAL-PROPAGATION-009` — Replication quality finite-core evaluator
10. `TLC-FC-29-GENERATIONAL-PROPAGATION-010` — Empty invariant-core guard
11. `TLC-FC-29-GENERATIONAL-PROPAGATION-011` — Zero delta-x-max guard
12. `TLC-FC-29-GENERATIONAL-PROPAGATION-012` — Replication time-decay preservation guard
13. `TLC-FC-29-GENERATIONAL-PROPAGATION-013` — Message erosion approximation descriptor
14. `TLC-FC-29-GENERATIONAL-PROPAGATION-014` — Erosion-rate expression evaluator
15. `TLC-FC-29-GENERATIONAL-PROPAGATION-015` — Erosion-time consistency ambiguity guard
16. `TLC-FC-29-GENERATIONAL-PROPAGATION-016` — Corrective-success predicate
17. `TLC-FC-29-GENERATIONAL-PROPAGATION-017` — Corrective algorithm unavailable guard
18. `TLC-FC-29-GENERATIONAL-PROPAGATION-018` — Corrective efficiency provider descriptor
19. `TLC-FC-29-GENERATIONAL-PROPAGATION-019` — Generational graph descriptor
20. `TLC-FC-29-GENERATIONAL-PROPAGATION-020` — Graph density evaluator
21. `TLC-FC-29-GENERATIONAL-PROPAGATION-021` — Directed connectivity ambiguity guard
22. `TLC-FC-29-GENERATIONAL-PROPAGATION-022` — Reproduction-rate evaluator
23. `TLC-FC-29-GENERATIONAL-PROPAGATION-023` — Reproduction regime classifier
24. `TLC-FC-29-GENERATIONAL-PROPAGATION-024` — Critical reproduction-threshold evaluator
25. `TLC-FC-29-GENERATIONAL-PROPAGATION-025` — Extinction-claim non-operational guard
26. `TLC-FC-29-GENERATIONAL-PROPAGATION-026` — Generational diversification predicate
27. `TLC-FC-29-GENERATIONAL-PROPAGATION-027` — School emergence and harmonious-diversity descriptor
28. `TLC-FC-29-GENERATIONAL-PROPAGATION-028` — Wave-3 provider ownership boundary

## Critical preserved boundaries

- The secondary-transmission threshold preserves the exact comparator sequence `>=`, `>=`, `<=`, `>=`, `>` and five-way conjunction. Thresholds remain uncalibrated.
- Master accompaniment and Community validation remain evidence/provider-backed; no vote, quorum, consensus, approval workflow, or automatic status transition is constructed.
- The generational dynamics keep the mixed `dx/dt` plus `dW` notation. No Itô rewrite, RNG, Brownian generator, ODE/SDE solver, integrator, or time-step policy is introduced.
- `dJ/dx` remains source-local, unresolved, and external-provider-required. It is not bound to Finality domain 28 and no domain-28 `J` is differentiated.
- Constructive and destructive mutation predicates preserve their exact comparators and logical structure; the destructive condition remains `A AND B AND (C OR D)`.
- `Q_rep(t)` retains the finite-cardinality divisor and `exp(-lambda t)`. A continuous `N_inv` is not replaced by a measure, integral, or sampling approximation. Empty finite cores and zero `delta_x^max` values are guarded explicitly.
- The unexplained temporal decay of perfect replication is preserved rather than corrected.
- Message erosion remains an approximation, not an equality. The inconsistency between time-varying `Q_rep(t)` and constant-form `d` remains unresolved; no `d(t)`, integral, or generation-product repair is introduced.
- Corrective-success inequalities only validate a supplied result. No repair optimizer, gradient procedure, projection method, or search algorithm is created. Correction efficiency remains an external `[0,1]` provider because no formula is supplied.
- `G_t=(V_t,E_t,w)` is owned by domain 29. Directed formation edges and `w in [0,1]` are preserved. The weak-versus-strong connected-component convention remains unresolved and no graph-analytics framework is created.
- Reproduction rate and graph density have explicit zero/small-denominator guards. The exact `R > 1`, `R = 1`, `R < 1` classification is preserved without creating `29 -> 30`.
- `R_c` uses only supplied statistics and supplied `f(rho,kappa)` and guards `E[R]=0`. No estimator, branching process, offspring law, or extinction certificate is invented.
- Generational diversification preserves the strict `< delta_rupture` predicate. School emergence and harmonious diversity remain conceptual descriptions; no state machine or `29 -> 31` dependency is introduced.

## Produced implementation-handoff artifacts

For each of the 28 features, the publication provides:

- 28 mathematical contracts
- 28 candidate IRs
- 28 registered IRs
- 28 test plans
- 28 optimized IRs
- 28 algorithms/guards
- 28 oracles
- 28 autonomous implementation tasks
- 28 Feature Handoff Packages, each containing exactly `README.md`, `manifest.json`, `contract.json`, `acceptance.json`, and `traceability.json`

The canonical domain catalog is `handoff/domains/generational-propagation/catalog.json`, with `domain_index = 29`, `expected_feature_count = 28`, `population = complete`, and `validation = validated`.

## Shared contracts

Generational Propagation reuses exactly the existing eight shared contracts and introduces no ninth contract:

- `TLC-HC-FEATURE-ID`
- `TLC-HC-SCIENTIFIC-REFERENCE`
- `TLC-HC-REFERENCE-COLLECTION`
- `TLC-HC-UNRESOLVED-ITEM`
- `TLC-HC-OPAQUE-VALUE`
- `TLC-HC-STRUCTURED-ERROR`
- `TLC-HC-TRACEABILITY`
- `TLC-HC-DESCRIPTOR-ENVELOPE`

## Global model

Baseline before domain 29 publication:

- 30 domains
- 395 features
- 8 shared contracts

Target after domain 29 publication:

- 31 domains
- 423 features
- 8 shared contracts

`generational-propagation` is appended after `finality-and-evolutionary-teleology` in the established publication order. Historical entries are not re-sorted numerically.

## Publication boundaries and repository hygiene

- Finality 28 remains published and intact.
- Generational Propagation 29 is the only domain selected for this publication.
- Expansion 30 and Institutionalization 31 remain unpublished while retaining their future consumer dependencies on 29.
- The unresolved `31 -> 24` relation remains unresolved.
- `maths/29-generational-propagation/generational-propagation.md` and `maths/04-invariants/invariants.md` remain unchanged at their authoritative blobs.
- `tools/handoff/generate_catalog.py` remains the sole authoritative global-catalog generator and is not instrumented or modified.
- `.github/workflows/handoff.yml` remains read-only with `permissions: contents: read`.
- No helper/materializer, temporary workflow, write permission, runtime stochastic solver, graph framework, branching simulator, correction optimizer, generated bundle archive, or ninth shared contract belongs to this publication.
