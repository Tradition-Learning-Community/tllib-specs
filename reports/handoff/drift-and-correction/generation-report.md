# Drift and Correction handoff generation report

## Publication identity

- Domain: `32 Drift and Correction / Stabilité, dérive et correction`
- Production branch: `pipeline/domain-32-drift-and-correction`
- Pull request: `#155 — Finalize domain 32 Drift and Correction to implementation-ready handoffs`
- Baseline `main`: `15caf75756e49d43689cb14a7a4db3d2394f461d`

## Scientific authority

- Authoritative Drift source: `maths/32-drift-and-correction/stability-drift-and-correction.md`
- Drift source blob: `c43d581fcbd33d086c1acb84ec43ac6d48ed95a3`
- Normative provider domain: `04 Invariants`
- Invariants source: `maths/04-invariants/invariants.md`
- Invariants source blob: `5bddc38b4a74465c2bc3b1d2e9f8aac004e86800`
- Analysis companion: `35 Fidelity to the Invariant Core`
- Fidelity source: `maths/35-fidelity-to-invariant-core/fidelity-to-the-invariant-core.md`
- Fidelity source blob: `5a6e0dcdcbc66bd74bb7d6816d34f2bcd0e73817`

The source-backed scientific dependency is exactly `32 -> 04`. The Drift chapter states that `kappa(e)` is a diagnostic of fidelity and does not replace the fundamental invariants. The published domain-04 handoffs expose ten structural/diagnostic features and no scientifically executable `N_inv`, `pi_N`, `d_D`, norm, or threshold-calibration operator. Drift therefore keeps these quantities opaque/external where needed and invents no feature-level provider binding.

Fidelity 35 is retained only as an analysis companion for vocabulary and scope comparison. Neither the Drift source nor the published Fidelity specification establishes a normative `32 -> 35` or `35 -> 32` dependency. Drift therefore publishes with `dependencies.confirmed: [4]`, `provisional: []`, `unknown: false`, and no runtime domain dependency.

## Scientific inventory

- Scientific objects: **76**
- Scientific relations: **45**
- Unresolved/provider-boundary items: **14**
- Finalized feature population: **18**

Execution distribution:

- `executable`: 3
- `conditionally_executable`: 9
- `structural_only`: 6

Scientific-status distribution:

- `defined`: 5
- `partially_defined`: 1
- `external_provider_required`: 8
- `preserved_unresolved`: 4

## Final feature population

1. `TLC-FC-32-DRIFT-AND-CORRECTION-001` — Core diagnostic aggregate score
2. `TLC-FC-32-DRIFT-AND-CORRECTION-002` — Resistance-to-change expression
3. `TLC-FC-32-DRIFT-AND-CORRECTION-003` — Core-periphery classification
4. `TLC-FC-32-DRIFT-AND-CORRECTION-004` — Suppression-test unavailable guard
5. `TLC-FC-32-DRIFT-AND-CORRECTION-005` — Incorporation-by-repetition expression
6. `TLC-FC-32-DRIFT-AND-CORRECTION-006` — Writing-pressure expression
7. `TLC-FC-32-DRIFT-AND-CORRECTION-007` — Writing-pressure calibration guard
8. `TLC-FC-32-DRIFT-AND-CORRECTION-008` — Dogmatization index
9. `TLC-FC-32-DRIFT-AND-CORRECTION-009` — Institutional rigidity index
10. `TLC-FC-32-DRIFT-AND-CORRECTION-010` — Mission intensity index
11. `TLC-FC-32-DRIFT-AND-CORRECTION-011` — Rupture predicate
12. `TLC-FC-32-DRIFT-AND-CORRECTION-012` — Schism-path ambiguity descriptor
13. `TLC-FC-32-DRIFT-AND-CORRECTION-013` — Reform-cycle unavailable-model guard
14. `TLC-FC-32-DRIFT-AND-CORRECTION-014` — Reset admissibility predicate
15. `TLC-FC-32-DRIFT-AND-CORRECTION-015` — Reset continuity expression
16. `TLC-FC-32-DRIFT-AND-CORRECTION-016` — Reset continuity zero-denominator guard
17. `TLC-FC-32-DRIFT-AND-CORRECTION-017` — Invalid mnemonic metric exclusion guard
18. `TLC-FC-32-DRIFT-AND-CORRECTION-018` — Invariants non-replacement and companion-boundary guard

## Critical preserved boundaries and guards

- `kappa(e)` preserves exactly the unweighted `1/5` mean of the five supplied components. The source does not establish that the five components are normalized to `[0,1]`; Drift therefore does not normalize, clamp, reweight, or assert that `kappa(e)` lies in `[0,1]`.
- `kappa_supp` remains an unavailable simulated-suppression component. No simulation, intervention algorithm, causal estimator, or graph-deletion experiment is created.
- `kappa_res(e) = 1 - ||Delta e||/||Delta e||_max` preserves its sign and uses provider-final norm values. `||Delta e||_max = 0` yields structured `ResistanceReferenceNormZero`; no epsilon repair or silent NaN is allowed.
- Core membership preserves strict `kappa(e) > kappa_min`; equality is periphery. `kappa_min` is supplied, never calibrated here, and the diagnostic does not replace domain-04 invariants.
- `I_inc(n) = I_inc_max(1-exp(-lambda n))` preserves the exact negative exponent and creates no repetition process, scheduler, or lambda estimator.
- Writing pressure preserves all five weighted source terms and signs. `sigma` remains an opaque supplied source function; no logistic form is assumed. Units, calibration, and commensurability are absent and are not repaired by normalization, standardization, or alpha calibration.
- `Delta_dog` preserves the exact product-of-ratios expression, guards both source denominators, and remains unbounded unless additional assumptions are supplied. It is never clamped or converted to a probability.
- `I_rig` preserves the exact source product, guards `N_rules^0` and `tau_decision^0`, and remains unbounded; it is never clamped or normalized.
- `I_mis` preserves the exact product of vitality, engagement, and joy ratios, guards all three maxima, and does not construct `J_joy` or any maximum.
- The rupture predicate preserves exactly four simultaneous conditions joined by `AND`. `N_inv`, `d_D`, branch-state, value, environment-support, and threshold semantics remain external; no `OR` conversion is permitted.
- The conceptual schism paths—doctrinal, institutional, cultural, personal—remain labels only. The unresolved relation between these paths and the four-way mathematical conjunction is preserved without synthetic equations or four classifiers.
- The reform cycle remains a descriptive sequence of diagnosis, proclamation, resistance, expansion, and institutionalization. The source explicitly omits a detailed model, so no state machine, workflow, transition probabilities, or orchestrator are introduced.
- Reset admissibility preserves all three strict conditions simultaneously: projection distance `< epsilon_reset`, vitality increase, and burden decrease. It tests a supplied candidate and never generates, searches, mutates, or optimizes `X'`.
- Reset continuity preserves `C_cont = 1 - ||pi_N(X')-pi_N(X)|| / ||pi_N(X)||`, strict `C_cont > C_min`, and vitality increase. A zero denominator yields structured `ResetContinuityDenominatorZero`, with no epsilon repair or identity substitution.
- `pi_N` and `d_D` are never constructed by Drift and Fidelity 35 is never used as an implicit runtime provider.
- **The invalid mnemonic ritual metric is excluded, not repaired.** The source explicitly states that the earlier expression divides by `||X-X|| = 0`, is undefined, and is not retained as a valid metric. Feature 017 is only a scientific-exclusion guard: it does not reconstruct the historical formula, replace its denominator, repair it, or expose any executable mnemonic-efficiency calculation.

## Produced implementation-handoff artifacts

For each of the 18 features:

- 18 mathematical contracts
- 18 candidate IRs
- 18 registered IRs
- 18 test plans
- 18 optimized IRs
- 18 algorithms/guards
- 18 oracles
- 18 autonomous implementation tasks
- 18 Feature Handoff Packages, each containing exactly `README.md`, `manifest.json`, `contract.json`, `acceptance.json`, and `traceability.json`

The canonical domain catalog is `handoff/domains/drift-and-correction/catalog.json`, with `domain = drift-and-correction`, `domain_index = 32`, `expected_feature_count = 18`, `population = complete`, and `validation = validated`.

## Shared contracts

Drift reuses exactly the existing eight shared contracts:

- `TLC-HC-FEATURE-ID`
- `TLC-HC-SCIENTIFIC-REFERENCE`
- `TLC-HC-REFERENCE-COLLECTION`
- `TLC-HC-UNRESOLVED-ITEM`
- `TLC-HC-OPAQUE-VALUE`
- `TLC-HC-STRUCTURED-ERROR`
- `TLC-HC-TRACEABILITY`
- `TLC-HC-DESCRIPTOR-ENVELOPE`

No Drift-specific ninth shared contract is introduced.

## Global model

Baseline after Fidelity 35:

- 28 domains
- 355 features
- 8 shared contracts

Drift publication target:

- 29 domains
- 373 features
- 8 shared contracts

`drift-and-correction` is appended after `fidelity-to-invariant-core` in the established publication order; historical domains are not numerically re-sorted.

## Wave-2 publication boundary

Already published Wave-2 domains are Evaluation 18, Regulation 19, Robustness 20, Fairness 21, and Fidelity 35. Drift 32 is the sole remaining Wave-2 publication in this branch. This report does **not** declare Wave 2 complete before merge: formal closure requires Drift to be merged, audited directly on `main`, and all six Wave-2 domains to be confirmed published there. No Wave-3, Wave-4, or Wave-5 domain is included in this publication.

## Repository hygiene

- `maths/32-drift-and-correction/stability-drift-and-correction.md` remains unchanged at its authoritative blob.
- `maths/04-invariants/invariants.md` remains unchanged at its provider blob.
- `maths/35-fidelity-to-invariant-core/fidelity-to-the-invariant-core.md` remains unchanged at its companion blob.
- `tools/handoff/generate_catalog.py` remains the sole authoritative global-catalog generator and must remain uninstrumented.
- `.github/workflows/handoff.yml` remains read-only with `permissions: contents: read`.
- No catalog helper, temporary workflow, write permission, simulation engine, causal estimator, reform engine, reset optimizer, projection builder, doctrinal-distance learner, threshold-calibration engine, mnemonic-formula repair, runtime Drift framework, or generated bundle archive belongs to this publication.
