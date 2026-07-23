# Global domain preparation reconciliation

- Authority: `origin/main`
- Canonical commit: `2cd5a3c6dfe8786926e58d49387b5f4846697a66`
- Generated: `2026-07-23T15:57:37+00:00`
- Scope: reconciliation artifacts only; no contract, IR, optimization, oracle, C++, or Python binding was produced.

## Inventory

The canonical checkout contains 16 domains, 1383 scientific objects,
1365 scientific relations, 830 unresolved entries,
and 175 inventoried canonical feature identifiers. Capacities entries marked
`comparison_only` are excluded from canonical coverage.

## Dependency reconciliation

The graph contains 156 traceable edges. 14 stale availability statuses were
reclassified to `canonical_target_available_semantic_review_pending`; this confirms only that the target
is present in the canonical tree. No dependency was promoted to semantically validated. 0
edges still have no canonical target.

## Cycles and readiness

Detected cycles: 2; generation-blocking cycles: 0.
Ready for limited contract generation: 2. Ready for full contract generation: 0.
Ready for IR generation after the conservative contract gate: 0. Implementation and code
generation remain globally false.

## Execution

Six dependency-derived domain batches are recorded in `contract-execution-plan.yaml` and mirrored for IR
with the mandatory validated-contract gate. The minimum estimated remaining Codex tasks is 8: two global
scientific synchronization tasks plus six generation/review batches. This is an estimate, not a scientific decision.

## Reservations

- Target existence does not establish identifier or semantic compatibility.
- Candidate and pilot contracts/IR outside Master, Disciple, and Community require scientific review.
- Documented dependency cycles are preserved and not broken by inference.
- Existing per-domain readiness is tightened where the explicit contract gate is not demonstrable.
