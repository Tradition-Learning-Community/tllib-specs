# Current global TLC registry through the IR layer

- Authority: `origin/main`
- Scientific baseline commit: `75814db2398b701e2f14c035ef8d63ca61fdfb26`
- Registry tooling commit at generation time: `ad3d0ad646fb6790fd7bd320e16a407db7967490`
- Generated: `2026-07-25T23:23:19+00:00`
- Scope: inventory and status normalization only.
- Scientific decisions made: none.
- `maths/` modified: no.

## Result

All sixteen domains are present. The current active catalogues contain **175 features**.
**37** feature sets contain a mathematical contract, an IR registry entry, an IR artifact,
and a structural test plan. Therefore `all_domains_reach_ir_layer` is **false**.

This is an IR-layer coverage statement. It is not a claim that all IRs have the same maturity, are canonically
selected, are executable, have complete algorithms or oracles, or are ready for C++ implementation.

## Domain inventory

| No. | Domain | Features | Contracts | IR artifacts | Test plans | IR layer complete | Canonical selection |
|---:|---|---:|---:|---:|---:|---|---|
| 00 | Master | 16 | 16 | 16 | 16 | yes | not_explicitly_completed |
| 01 | Disciple | 10 | 10 | 10 | 10 | yes | not_explicitly_completed |
| 02 | Community | 8 | 8 | 8 | 8 | yes | not_explicitly_completed |
| 03 | Huit Dimensions | 11 | 11 | 11 | 0 | no | not_explicitly_completed |
| 04 | Invariants | 10 | 10 | 10 | 0 | no | not_explicitly_completed |
| 05 | Dynamics | 7 | 7 | 7 | 7 | no | not_explicitly_completed |
| 06 | Theorems | 9 | 9 | 0 | 9 | no | not_explicitly_completed |
| 07 | Message | 6 | 6 | 0 | 6 | no | not_explicitly_completed |
| 08 | Principle | 10 | 10 | 1 | 10 | no | not_explicitly_completed |
| 09 | Values | 14 | 14 | 1 | 14 | no | not_explicitly_completed |
| 10 | Virtues | 10 | 10 | 0 | 10 | no | not_explicitly_completed |
| 11 | Capacities | 24 | 15 | 0 | 15 | no | not_explicitly_completed |
| 12 | Competencies | 13 | 13 | 0 | 13 | no | not_explicitly_completed |
| 13 | Practice | 10 | 10 | 0 | 10 | no | not_explicitly_completed |
| 14 | Lived Experience | 12 | 12 | 1 | 12 | no | not_explicitly_completed |
| 15 | Relations | 5 | 5 | 0 | 5 | no | not_explicitly_completed |

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

The legacy aggregate count of 175 is retained as the current active feature inventory because it is reproduced
from the sixteen domain catalogues and matched to the generated feature matrices. Historical lineages, rejected
or deferred candidates, and internal IR node identifiers are not added to this active count.

Raw contract, selection, scientific, and execution statuses are preserved in the feature matrices. No status
is silently promoted to `approved`, `selected`, `executable`, or `implementation_ready`.
