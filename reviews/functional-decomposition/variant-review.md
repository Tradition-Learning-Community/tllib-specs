# Candidate decomposition variant review

Status: `candidate`
Source commit: `d0d1e26ef6a488aa291e1f4e616b9b2748ff2370`

## Finding

All three variants (`minimal`, `balanced`, and `fine`) contain exactly the same 224 feature identifiers. The
registry therefore does not instantiate three alternative decompositions; it records three narrative boundary
policies around one catalog. The main feature catalog implicitly reflects this shared catalog, but no variant can
be shown to have been selected structurally.

## Comparative assessment

| Variant | Scientific fidelity | Testability | Main risk | Contract generation | Candidate recommendation |
|---|---|---|---|---|---|
| minimal | unresolved until boundaries are instantiated | lower for 17 aggregates | excessive aggregation | difficult for mixed groups | retain only as comparison baseline |
| balanced | unresolved; its name is not evidence | moderate in narrative only | hidden implicit selection | plausible after boundary decisions | retain, do not select yet |
| fine | unresolved until splits cite sources | potentially high | fragmentation and invented dependencies | good only for source-supported splits | retain for targeted boundary experiments |

No variant is rejected outright because the artifacts do not instantiate their distinct boundaries. Human review is
required for the 17 excessive aggregations. The candidate recommendation is to instantiate a small, traceable subset
of `fine` splits for those issues and compare it with unchanged boundaries; this is not approval of `fine` globally.

## Observed registry records

```yaml
- variant_id: TLC-FDV-001
  name: minimal
  candidate_count: 224
  observed_boundaries: Keep each source/role/status cluster intact.
  advantages:
  - Fewest candidate boundaries
  - Direct source-level traceability
  risks:
  - Large clusters may combine several scientific responsibilities
  testability: Lower isolation for large clusters.
  dependencies: Fewer aggregate nodes; relation-level hints remain explicit.
  blockages: Blocked clusters remain separate from admissible clusters.
  assessment: The three variants list the same 224 feature IDs; differences are narrative
    boundary policies, not instantiated alternative catalogs.
- variant_id: TLC-FDV-002
  name: balanced
  candidate_count: 224
  observed_boundaries: Use the generated source/role/status candidates as independent
    contract-selection units.
  advantages:
  - Separates behavior roles and readiness states
  - Preserves local blockers
  risks:
  - Some concept-heavy candidates still require targeted extraction
  testability: Behavior candidates are independently testable after contract selection.
  dependencies: Every scientific relation is retained as a candidate dependency.
  blockages: Provisional and blocked objects are isolated by status.
  assessment: The three variants list the same 224 feature IDs; differences are narrative
    boundary policies, not instantiated alternative catalogs.
- variant_id: TLC-FDV-003
  name: fine
  candidate_count: 224
  observed_boundaries: Split large candidates into one candidate per cited scientific
    behavior during a later reviewed pass.
  advantages:
  - Maximum test isolation
  - Small contract-review units
  risks:
  - Fragmentation may turn equations or data objects into artificial APIs
  testability: Highest potential isolation after additional boundary review.
  dependencies: Likely increases dependency count substantially.
  blockages: Each blocker can remain attached to one small unit.
  assessment: The three variants list the same 224 feature IDs; differences are narrative
    boundary policies, not instantiated alternative catalogs.
```
