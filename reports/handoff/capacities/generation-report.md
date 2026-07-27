# Capacities Feature Handoff Package generation report

## Scope

- Domain: `capacities`
- Domain index: `11`
- Source branch: `handoff/integration-v1`
- Source commit: `c792e2f042580ae589e25fe466e7bd0cc79f40ca`
- Expected guard count: 15
- Authoritative active population: 15
- Packages produced: 15
- Foreign-domain packages modified: 0

## Authoritative population

1. `TLC-FC-11-CAPACITIES-001`
2. `TLC-FC-11-CAPACITIES-002`
3. `TLC-FC-11-CAPACITIES-003`
4. `TLC-FC-11-CAPACITIES-005`
5. `TLC-FC-11-CAPACITIES-006`
6. `TLC-FC-11-CAPACITIES-007`
7. `TLC-FC-11-CAPACITIES-008`
8. `TLC-FC-11-CAPACITIES-009`
9. `TLC-FC-11-CAPACITIES-010`
10. `TLC-FC-11-CAPACITIES-011`
11. `TLC-FC-11-CAPACITIES-012`
12. `TLC-FC-11-CAPACITIES-013`
13. `TLC-FC-11-CAPACITIES-014`
14. `TLC-FC-11-CAPACITIES-015`
15. `TLC-FC-11-CAPACITIES-018`

The contract, source IR, finalized IR, algorithm specification, test plan, and oracle populations are aligned with this list. No missing package was fabricated.

## Compilation decisions

Six admissible features (`001`, `005`, `008`, `010`, `013`, `018`) are compiled as opaque structural descriptors with no scientific evaluator. Nine features (`002`, `003`, `006`, `007`, `009`, `011`, `012`, `014`, `015`) preserve the exact blocker `scientific decision required` and remain structurally buildable but scientifically non-executable.

Algorithm step lists were treated as compilation inputs rather than mandatory total sequences. Each final contract uses `partially_constrained` strategy semantics: validation, preservation, blocker attachment, immutable construction, and failure atomicity must precede observable success, while internal decomposition is open.

Low-level runtime details are constrained only where justified: returned artifacts are immutable and failures expose no partial result. Ownership mechanism, layout, allocation, serialization, aliasing, concurrency, copy/move strategy, and language remain implementation-defined or unconstrained.

No `examples.json` was generated because the available artifacts support structural acceptance fixtures but no honest standalone scientific example values.

## Errors

Upstream PascalCase error identifiers were preserved exactly. No local error identifier was created.

## Shared contracts

Only existing shared contracts are referenced. No shared contract or global schema was modified. Two recurring local envelopes are recorded as `candidate_only` in `shared-contract-candidates.json`; neither implies scientific equivalence.

## Hashes and integrity

All package files are repository-relative Git blobs and therefore receive calculable Git blob SHA-1 identifiers in the committed tree. The catalog schema does not expose a per-file hash property, so hashes are not duplicated into schema-incompatible fields.

## Protected content

No scientific source, mathematical contract, IR, finalized IR, algorithm, oracle, test plan, shared contract, schema, workflow, implementation code, or other domain package was changed during package compilation. Any later CI compatibility correction will be documented separately and limited to non-scientific metadata if required.

## Validation state

Schema and repository-wide validation are pending GitHub Actions on the pull request. Final workflow evidence and any narrowly scoped correction will be recorded in `validation-report.json`.
