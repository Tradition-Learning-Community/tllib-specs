# Practice domain finalization

## Baseline and scope

- Main HEAD used: `c34d40713bf444d38f92f76e1c6239ee596d5a18`.
- Branch: `phase4/practice-domain-finalization-001`.
- Authoritative population: 10 active features from the current global reconciliation baseline and domain feature matrix.
- Source layer: 10 contracts, 10 source IRs and 10 source test plans, all preserved.

## Finalized population

- `TLC-FC-13-PRACTICE-001` — constraint candidate.
- `TLC-FC-13-PRACTICE-003` — admissible dynamics candidates.
- `TLC-FC-13-PRACTICE-004` — locally blocked dynamics candidates.
- `TLC-FC-13-PRACTICE-005` — admissible equation candidates.
- `TLC-FC-13-PRACTICE-006` — locally blocked equation candidates.
- `TLC-FC-13-PRACTICE-007` — admissible metric candidates.
- `TLC-FC-13-PRACTICE-008` — locally blocked quantitative metric candidate.
- `TLC-FC-13-PRACTICE-009` — admissible function and operator candidates.
- `TLC-FC-13-PRACTICE-010` — locally blocked aggregate operator candidate.
- `TLC-FC-13-PRACTICE-012` — provisionally separated relation candidate.

No feature was rejected. All source IR statuses were retained: five `declarative_non_executable_with_reservations` and five `blocked_declarative_non_executable`.

## Patterns and normalization

The source IRs demonstrate one reusable software envelope: opaque candidate inputs, opaque unresolved results, source provenance, structured blockers and structural determinism. This is structural duplication, not scientific equivalence.

The finalization normalizes identity validation, required input validation, provenance, serialization, deserialization, structural comparison, opaque-value propagation and structured errors. It retains each feature identity, source object list, documentary order, reservations and scientific decision set.

No equation, operator, metric or relation was merged. No documentary relation was upgraded to an execution dependency. The Practice dependency matrix establishes no canonical functional edge between the 10 active features.

## Implementation boundary

The package is ready to implement the representation, validation and serialization layer. It does not claim that the scientific content is executable.

For every feature, the finalized algorithm can construct and validate a declarative representation, preserve source references, serialize, deserialize, compare structurally and propagate opaque values. Requests for scientific execution require an external executor. Metric or relation evaluation requires an external evaluator. Features 004, 006, 008, 010 and 012 additionally return their preserved scientific decision references.

Descriptions mentioning repetition, evolution, habits, temporal quantities, metrics or effects were not converted into loops, schedules, progression rules, thresholds, success conditions or guaranteed effects.

## Finalized artifacts

Each of the 10 features now has:

- a finalized IR under `registry/optimized-ir/practice/<FEATURE_ID>/ir.yaml`;
- an algorithm specification under `registry/algorithms/practice/<FEATURE_ID>/algorithm.yaml`;
- an oracle under `registry/oracles/practice/<FEATURE_ID>/oracle.yaml`.

The module package contains the manifest, feature status, patterns, complete module specification, implementation tasks and decision classification under `registry/domain-finalization/practice/`.

## Real remaining blockers

There is no blocker to implementing the structural Practice package.

Scientific evaluation remains deferred for:

- `TLC-FC-13-PRACTICE-004`;
- `TLC-FC-13-PRACTICE-006`;
- `TLC-FC-13-PRACTICE-008`;
- `TLC-FC-13-PRACTICE-010`;
- `TLC-FC-13-PRACTICE-012`.

These decisions block only unspecified scientific evaluation. They do not reject the feature or its declarative representation.

## Conservation statement

- No source contract was modified.
- No source IR was modified or replaced.
- No source test plan was modified.
- No file under `maths/` was modified.
- No artifact of another domain was modified.
- No global registry was regenerated.
- No practice, step, sequence, duration, frequency, repetition rule, progression rule, success condition, stop rule or effect was invented.
- No C++ code, Python binding or reference implementation was produced.

## Closure

Practice is complete for this phase through the implementation-ready specification package: finalized IRs, algorithms, oracles, module integration and future developer tasks for all 10 authoritative active features.

## GitHub validation result

- GitHub Actions validation: PASSED.
- Practice validator: PASSED.
- Whitespace check: PASSED.
- Changed-path and protected-source checks: PASSED.
