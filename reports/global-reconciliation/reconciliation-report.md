# Current global TLC registry through the IR layer

- Authority: `origin/main`
- Scientific baseline commit: `75814db2398b701e2f14c035ef8d63ca61fdfb26`
- Registry tooling commit at generation time: `04a14bd16af39c18a2cce80fee6b06ea9f3586b0`
- Generated: `2026-07-25T23:29:40+00:00`
- Scope: inventory and status normalization only.
- Scientific decisions made: none.
- `maths/` modified: no.

## Result

All sixteen domains are present. The current active catalogues contain **166 features**.
**166** feature sets contain a mathematical contract, an IR registry entry, an IR artifact,
and a structural test plan. Therefore `all_domains_reach_ir_layer` is **true**.

This is an IR-layer coverage statement. It is not a claim that all IRs have the same maturity, are canonically
selected, are executable, have complete algorithms or oracles, or are ready for C++ implementation.

## Domain inventory

| No. | Domain | Features | Contracts | IR artifacts | Test plans | IR layer complete | Canonical selection |
|---:|---|---:|---:|---:|---:|---|---|
| 00 | Master | 16 | 16 | 16 | 16 | yes | not_explicitly_completed |
| 01 | Disciple | 10 | 10 | 10 | 10 | yes | not_explicitly_completed |
| 02 | Community | 8 | 8 | 8 | 8 | yes | not_explicitly_completed |
| 03 | Huit Dimensions | 11 | 11 | 11 | 11 | yes | not_explicitly_completed |
| 04 | Invariants | 10 | 10 | 10 | 10 | yes | not_explicitly_completed |
| 05 | Dynamics | 7 | 7 | 7 | 7 | yes | not_explicitly_completed |
| 06 | Theorems | 9 | 9 | 9 | 9 | yes | not_explicitly_completed |
| 07 | Message | 6 | 6 | 6 | 6 | yes | not_explicitly_completed |
| 08 | Principle | 10 | 10 | 10 | 10 | yes | not_explicitly_completed |
| 09 | Values | 14 | 14 | 14 | 14 | yes | not_explicitly_completed |
| 10 | Virtues | 10 | 10 | 10 | 10 | yes | not_explicitly_completed |
| 11 | Capacities | 15 | 15 | 15 | 15 | yes | not_explicitly_completed |
| 12 | Competencies | 13 | 13 | 13 | 13 | yes | not_explicitly_completed |
| 13 | Practice | 10 | 10 | 10 | 10 | yes | not_explicitly_completed |
| 14 | Lived Experience | 12 | 12 | 12 | 12 | yes | not_explicitly_completed |
| 15 | Relations | 5 | 5 | 5 | 5 | yes | not_explicitly_completed |

## Normalized interpretation

- The sixteen domains have reached the IR layer.
- Canonical IR selection remains a separate domain-by-domain activity.
- Algorithmic specifications and scientific oracles remain later gates.
- Historical human-review queues and dependency cycles are not discarded, but they are handled only when
  they affect the domain currently under review.
- No domain is reopened automatically because another domain contains an unresolved item.

## Active next-phase sequence

The active strategy is recorded in `domain-review-sequence.yaml`: Master first, then Disciple, Community,
Huit Dimensions, Invariants, Dynamics, Theorems, Message, Principle, Values, Virtues, Capacities,
Competencies, Practice, Lived Experience, and Relations.

For each domain: confirm feature inventory, review unstable boundaries only, review contracts, select or revise
IRs, verify required dependencies, specify algorithms, specify oracles, and close the domain.

## Counts and status sources

The current authoritative active count is **166**. The previous aggregate of 175 recursively
counted nine identifiers under `legacy_goose_feature_ids` in the Capacities preparation. That source explicitly
marks those identifiers as non-authoritative. They are now preserved as lineage evidence but excluded from the
active feature matrix. Historical, rejected, deferred, and internal IR node identifiers are likewise excluded.

Raw contract, selection, scientific, and execution statuses are preserved in the feature matrices. No status
is silently promoted to `approved`, `selected`, `executable`, or `implementation_ready`.
