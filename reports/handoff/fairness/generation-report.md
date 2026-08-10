# Fairness handoff generation report

## Publication identity

- Domain: `21 Fairness / Équité`
- Production branch: `pipeline/domain-21-fairness`
- Pull request: `#152 — Finalize domain 21 Fairness to implementation-ready handoffs`
- Post-Regulation baseline `main`: `4ca42ef7cf9a3aab451c1f54c163d97e8b243840`

## Scientific authority

- Authoritative source: `maths/21-fairness/fairness.md`
- Fairness source blob: `bbe983d3f74063072c97059e8ff7346b28d28158`
- Downstream analysis companion: `maths/20-robustness/robustness.md`
- Robustness companion blob: `71b575f114d1710b6b9556de06b17d103cb38c1e`
- Scientific direction: `20 Robustness -> 21 Fairness`
- Fairness scientific domain dependencies: none
- Fairness runtime domain dependencies: none

Robustness is a downstream scientific consumer because its procedural dimension is explicitly assigned to Fairness. Fairness does not depend on Robustness merely because Robustness consumes it.

## Scientific inventory

- Scientific objects: **108**
- Scientific relations: **31**
- Preserved unresolved items: **14**
- Finalized feature population: **18**

Execution distribution:

- `executable`: 1
- `conditionally_executable`: 12
- `structural_only`: 5

Scientific-status distribution:

- `defined`: 1
- `partially_defined`: 2
- `external_provider_required`: 8
- `preserved_unresolved`: 7

## Final feature population

1. `TLC-FC-21-FAIRNESS-001` — Procedural robustness expression
2. `TLC-FC-21-FAIRNESS-002` — Bias space descriptor
3. `TLC-FC-21-FAIRNESS-003` — Aggregate bias expression
4. `TLC-FC-21-FAIRNESS-004` — Decision correction expression
5. `TLC-FC-21-FAIRNESS-005` — Fair optimization problem descriptor
6. `TLC-FC-21-FAIRNESS-006` — Raw Fairness Lagrangian
7. `TLC-FC-21-FAIRNESS-007` — Master weight raw expression
8. `TLC-FC-21-FAIRNESS-008` — Plurality aggregation objective
9. `TLC-FC-21-FAIRNESS-009` — Cognitive diversity expression
10. `TLC-FC-21-FAIRNESS-010` — Complementarity expression
11. `TLC-FC-21-FAIRNESS-011` — Alignment loss expression
12. `TLC-FC-21-FAIRNESS-012` — Dynamic ethical-constraint expression
13. `TLC-FC-21-FAIRNESS-013` — Alignment efficiency expression
14. `TLC-FC-21-FAIRNESS-014` — Temporal responsibility expression
15. `TLC-FC-21-FAIRNESS-015` — Bias-decay inequality descriptor
16. `TLC-FC-21-FAIRNESS-016` — Contextual fairness expression
17. `TLC-FC-21-FAIRNESS-017` — Contextual fairness threshold assessment
18. `TLC-FC-21-FAIRNESS-018` — Fairness scientific non-invention guard

## Guard and non-invention surface

The finalized contracts preserve these source boundaries without repair:

- `R_proc` is not guaranteed in `[0,1]`; no clamp, normalization, or probability interpretation is permitted.
- `J`, score functions, expectations, transparency, justice, bias components, correlations, KL divergence, distances, extrema, minima, derivatives, gradients, and integrals remain provider-owned where the source does not operationalize them.
- Decision correction raises `CorrectionDenominatorZero` when `1 + alpha(z)(E[y|z]-E[y]) = 0`; no epsilon or fallback is introduced.
- The constrained Fairness optimization block is a problem descriptor, not an optimizer.
- The raw Fairness Lagrangian preserves the source value-minus-minimum signs; multiplier-sign and dual/KKT conventions remain unresolved.
- Master weights remain raw proportional factors; no normalization, sum-to-one claim, softmax, or partition function is invented.
- The plurality objective preserves the source entropy sign; no normative diversity interpretation or argmax search is invented.
- Cognitive diversity rejects `k < 2` rather than repairing `binomial(k,2)`.
- Complementarity rejects `sum_i P_i = 0` without changing the numerator sign.
- Alignment efficiency rejects `m = 0`.
- Temporal responsibility rejects `T = 0`; no numerical quadrature, differentiation, discretization, or interpolation is introduced.
- Residual legitimate bias remains unresolved; no legitimacy classifier, estimator, or universal convergence proof is created.
- Contextual fairness preserves explicit zero-denominator guards for `max P(c)`, `F_fid^max`, and `Alig_max`.
- The strict contextual predicate `E_ctx^T > 0.6` preserves the exact source threshold. `0.6` is declared operational, not derived, calibrated, or generalized.

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
- 18 Feature Handoff Packages, each with exactly `README.md`, `manifest.json`, `contract.json`, `acceptance.json`, and `traceability.json`

The canonical domain catalog is `handoff/domains/fairness/catalog.json`, with `domain = fairness`, `domain_index = 21`, `expected_feature_count = 18`, and statuses `population = complete`, `validation = validated`.

## Shared contracts

Fairness reuses the existing eight shared contracts without introducing a Fairness-specific shared contract:

- `TLC-HC-FEATURE-ID`
- `TLC-HC-SCIENTIFIC-REFERENCE`
- `TLC-HC-REFERENCE-COLLECTION`
- `TLC-HC-UNRESOLVED-ITEM`
- `TLC-HC-OPAQUE-VALUE`
- `TLC-HC-STRUCTURED-ERROR`
- `TLC-HC-TRACEABILITY`
- `TLC-HC-DESCRIPTOR-ENVELOPE`

## Global model

Baseline after Regulation 19:

- 25 domains
- 284 features
- 8 shared contracts

Fairness publication target:

- 26 domains
- 302 features
- 8 shared contracts

`fairness` is appended after `regulation` in the existing publication order; historical domains are not numerically re-sorted.

## Publication boundaries

- Evaluation 18 remains published.
- Regulation 19 remains published and retains its confirmed dependency on Evaluation 18.
- Fairness 21 is the only new Wave-2 domain selected for publication in this package.
- Robustness 20 remains unpublished and retains `dependencies.confirmed: [21]`.
- Drift and correction 32 remains unpublished.
- Fidelity to invariant core 35 remains unpublished.

## Repository hygiene

- Fairness scientific source is preserved unchanged at its authoritative blob.
- Robustness companion source is preserved unchanged at its authoritative blob.
- `tools/handoff/generate_catalog.py` remains the only authoritative global-catalog generator.
- `.github/workflows/handoff.yml` remains read-only with `contents: read`.
- No catalog helper, diagnostic materializer, temporary workflow, runtime Fairness framework, optimizer, solver, or generated bundle archive belongs to this publication.
- Global-catalog determinism is governed exclusively by `tools/handoff/generate_catalog.py` and the repository validation/export gates.
