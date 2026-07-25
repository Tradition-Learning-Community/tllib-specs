# Practice domain completion — wave 3

- **Domain:** practice
- **Base commit:** d8e616c71173495b9a014d4a5909df9f30e2a7ae (preparation baseline); execution started from current branch HEAD recorded in the batch manifest.
- **Catalogue:** 10 canonical features: TLC-FC-13-PRACTICE-001, 003, 004, 005, 006, 007, 008, 009, 010, 012.

## Initial state

The domain was prepared as `complete_with_reservations`, with a contract production plan only and zero expected canonical contracts, IRs, and test plans.

## Reuse and consolidation

- Historical artifact assessment found no prior practice artifacts to promote or consolidate.
- The canonical catalogue, source objects, blockers, exclusions, inputs, outputs, preconditions, postconditions, and purposes were reused from the practice preparation artifacts.
- No historical pilot or variant was promoted to canonical status.

## Created canonical artifacts

For each catalogue feature, one active canonical contract, one canonical IR, and one canonical test plan were created:

- `registry/math-contracts/<FEATURE-ID>/contract.yaml`
- `registry/ir/<FEATURE-ID>/ir.yaml`
- `registry/test-plans/<FEATURE-ID>/test-plan.yaml`

Counts: 10 contracts, 10 IRs, 10 test plans.

## Classifications and readiness

All artifacts are declarative and non-executable. Features without explicit blockers are classified as `declarative_non_executable_with_reservations`; features with blockers are classified as `blocked_declarative_non_executable`.

Python readiness and C++ readiness are both `non_executable_declarative` or `blocked_by_scientific_decision` according to the propagated blockers. No artifact claims production readiness.

## Blockers and scientific questions

The following features retain scientific-decision blockers from the preparation artifacts:

- TLC-FC-13-PRACTICE-004
- TLC-FC-13-PRACTICE-006
- TLC-FC-13-PRACTICE-008
- TLC-FC-13-PRACTICE-010
- TLC-FC-13-PRACTICE-012

The unresolved questions are not resolved by this batch; they are propagated as `scientific_decisions_required` and reflected in blocked test entries.

## Validations

- `ruby tools/validate_practice_domain.rb` — passed: exact catalogue, contract, IR, and test-plan counts; canonical references; no `maths/` changes; no `artifact.yaml`.
- `git diff --check` — passed.
- `/usr/bin/python3 scripts/validate_practice_preparation.py` — environment warning: requires `origin/main...HEAD`, but this checkout has no `origin` remote.
- YAML parsing — all added/modified YAML parsed with PyYAML using `/usr/bin/python3`.
- Scope check — no files under `maths/` modified.

## Modified files

See `registry/ir-batches/practice-domain-completion-001/manifest.yaml` for the machine-readable file list.

## Conclusion

Practice is structurally complete for wave 3 at the same canonical artifact level as the referenced wave 2 domains: every canonical feature has one canonical contract, one canonical IR, and one canonical test plan, with non-executability and blockers represented honestly.
