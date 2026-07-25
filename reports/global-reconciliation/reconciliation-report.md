# Current global TLC registry through the IR layer

- Authority: `origin/main`
- Scientific baseline commit: `75814db2398b701e2f14c035ef8d63ca61fdfb26`
- Registry tooling commit at generation time: `16ccb6114f1548183819ecfeb3a8634403ef20d4`
- Generated: `2026-07-25T23:45:02+00:00`
- Scope: inventory and status normalization only.
- Scientific decisions made: none.
- `maths/` modified: no.

## Result

All sixteen domains are present. Their authoritative catalogues contain **166 active features**.
All 166 features have a mathematical contract, an IR artifact and a structural test plan.
Therefore `all_domains_reach_ir_layer` is **true**.

The former total of 175 included nine `legacy_goose_feature_ids` in the Capacities preparation. That same
source marks those identifiers as non-authoritative; the active Capacities catalogue contains 15 features.
The legacy identifiers remain in their source file as lineage evidence and are not deleted.

IR-layer coverage does not mean that all IRs use one storage layout, have the same maturity, pass a common
selection gate, are executable, have complete algorithms or oracles, or are ready for C++.

## Domain inventory

| No. | Domain | Features | Contracts | IR artifacts | Test plans | IR layer | Raw canonical labels | Common selection gate |
|---:|---|---:|---:|---:|---:|---|---:|---:|
| 00 | Master | 16 | 16 | 16 | 16 | yes | 0 | 0 |
| 01 | Disciple | 10 | 10 | 10 | 10 | yes | 0 | 0 |
| 02 | Community | 8 | 8 | 8 | 8 | yes | 0 | 0 |
| 03 | Huit Dimensions | 11 | 11 | 11 | 11 | yes | 0 | 0 |
| 04 | Invariants | 10 | 10 | 10 | 10 | yes | 0 | 0 |
| 05 | Dynamics | 7 | 7 | 7 | 7 | yes | 0 | 0 |
| 06 | Theorems | 9 | 9 | 9 | 9 | yes | 0 | 0 |
| 07 | Message | 6 | 6 | 6 | 6 | yes | 0 | 0 |
| 08 | Principle | 10 | 10 | 10 | 10 | yes | 0 | 0 |
| 09 | Values | 14 | 14 | 14 | 14 | yes | 0 | 0 |
| 10 | Virtues | 10 | 10 | 10 | 10 | yes | 0 | 0 |
| 11 | Capacities | 15 | 15 | 15 | 15 | yes | 0 | 0 |
| 12 | Competencies | 13 | 13 | 13 | 13 | yes | 13 | 0 |
| 13 | Practice | 10 | 10 | 10 | 10 | yes | 0 | 0 |
| 14 | Lived Experience | 12 | 12 | 12 | 12 | yes | 11 | 0 |
| 15 | Relations | 5 | 5 | 5 | 5 | yes | 5 | 0 |

## Active next phase

The active strategy is `domain-review-sequence.yaml`: Master first, then the other fifteen domains in theory
order. For each module, confirm its active features, review only unstable boundaries, review contracts, select
or revise IRs, check required dependencies, specify algorithms and oracles, then publish a closure manifest.
A dependency in another domain is examined only when required by the current module; it does not automatically
reopen all sixteen domains.

Historical targeted scientific-review artifacts retain their original source commits and are not relabelled by
this build. Raw statuses are preserved in the feature matrices; no candidate, prototype or declarative IR is
silently promoted.
