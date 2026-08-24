# Contributing to `tllib-specs`

`tllib-specs` is the authoritative specification repository preparing `tllib`, the principal software library of the Tradition Learning Community.

Tradition Learning is the theory and research programme. The Tradition Learning Community (TLC) is the community of people advancing it. `tllib` is the downstream AI library intended to complement machine learning, deep learning, reinforcement learning, and related methods. This repository is the upstream scientific and engineering specification workspace; it is not the runtime implementation repository.

The theoretical domain named **Community** is Domain 02 of the 36-domain Tradition Learning corpus. It is distinct from the Tradition Learning Community organization.

Contributions are accepted when they improve scientific clarity, mathematical precision, algorithmic contracts, traceability, validation, or the language-neutral Feature Handoff Packages without inventing unresolved science.

## Choose the right contribution path

| Contributor role | Start here | Typical output | Must not do |
|---|---|---|---|
| Scientist or domain expert | `maths/`, scientific review inventory, traceability | clarified source statement, evidence, explicit unresolved question, adjudication proposal | silently rewrite implementation contracts without source impact analysis |
| Mathematician | `registry/math-contracts/`, source references, invariants | formal definition, domain/codomain, assumptions, proof obligation, counterexample | infer missing equations, types, domains, thresholds, or truth values |
| Algorithm designer | `registry/algorithms/`, finalized IR, oracles | observable algorithmic obligation, admissible strategy family, partial-order constraint, complexity requirement when justified | turn an illustrative step list into a mandatory total order without authority |
| Specification engineer | `registry/`, `handoff/`, schemas, validators | traceable contract transformation, consistency repair, deterministic tooling | merge distinct concepts because they share a representation |
| Runtime implementer | exported bundle from `handoff/` | issue against an ambiguous or contradictory handoff package | add production C++, Rust, Ruby, Python, bindings, solvers, or runtime code here |
| Reviewer or auditor | changed feature chain and validation reports | contradiction report, traceability review, non-invention review, validation evidence | approve by directory count alone or ignore unresolved semantics |

## Repository layers

```text
maths/          Tradition Learning scientific authority
registry/       compiler-like intermediate specification pipeline
handoff/        final language-neutral programmer interface for tllib
reports/        audit evidence and reconciliation records
tools/          deterministic validation, catalog, and export tooling
```

A downstream `tllib` programmer normally starts with a resolved bundle containing `feature/`, `shared/`, and `bundle-lock.json`. The upstream layers remain available for audit and scientific review.

## Contribution classes

### 1. Scientific clarification

Use this path when a source statement, equation, concept, domain, relation, proof, or scientific decision needs clarification.

Required evidence:

- exact scientific source path and section;
- affected feature IDs;
- whether the proposal resolves, narrows, or only documents an ambiguity;
- consequences for contracts, IRs, algorithms, or oracles;
- explicit statement that no unrelated feature semantics change.

A scientific clarification is not complete until downstream traceability is updated or an explicit follow-up is recorded.

### 2. Mathematical contract change

A mathematical change must identify:

- definitions and symbols affected;
- assumptions and domains;
- input and output meaning;
- invariants and failure conditions;
- proof obligations or unresolved proof status;
- backward compatibility or versioning consequences.

Do not use convenient implementation defaults to fill mathematical gaps.

### 3. Algorithmic specification change

Separate three things explicitly:

1. observable behavior;
2. scientifically or numerically required ordering;
3. internal implementation strategy.

Use `open`, `partially_constrained`, or `prescribed` strategy semantics according to the actual authority. Performance constraints are normative only when justified by the specification, not merely desirable.

### 4. Handoff package correction

A handoff change must preserve the authority order documented in `handoff/README.md` and keep the package autonomous for downstream implementation.

For every affected feature, check:

- `manifest.json` identity and statuses;
- `contract.json` observable obligations;
- `acceptance.json` conformance coverage;
- `traceability.json` source completeness;
- optional examples classification;
- shared-contract dependency closure;
- deterministic catalog and bundle fingerprints.

The root README, feature README, or example cannot create a normative obligation absent from the structured contracts.

### 5. Tooling or validation change

Validation changes require adversarial tests. A validator must reject malformed or misleading artifacts rather than merely accept the current repository.

At minimum, consider:

- false acceptance;
- false rejection;
- duplicate or reordered identities;
- unresolved dependency paths;
- status inconsistency;
- non-deterministic output;
- implementation-language leakage;
- protected-source modification;
- synthetic feature creation.

`tools/handoff/validate_handoff.py` remains the sole official handoff validation CLI.

## Workflow

1. Open or identify a focused issue when the change is scientific, cross-domain, normative, or potentially breaking.
2. Create a branch from current `main`.
3. Keep the change within one coherent concern.
4. Update every affected layer or explicitly document why a layer is unchanged.
5. Run the relevant validators.
6. Open a pull request using the repository template.
7. Address all review threads and validation failures.
8. Merge only after required checks succeed.

Recommended branch prefixes:

```text
science/
math/
algorithm/
spec/
handoff/
validation/
docs/
```

## Required validation

For handoff-related changes:

```bash
python tools/handoff/generate_catalog.py --check
python tools/handoff/validate_handoff.py
python tools/handoff/validate_handoff.py --self-test
python tools/handoff/export_bundle.py --all --check --verify-determinism
```

For global specification changes, also run the global finalization validator documented by the repository workflows.

## Pull request quality standard

A production-quality pull request is:

- narrow enough to review;
- complete across affected layers;
- explicit about unresolved science;
- deterministic;
- traceable to source authority;
- free of unrelated formatting churn;
- free of runtime implementation code;
- accompanied by evidence, not only assertions.

The pull request description must state:

- what changed and why;
- affected domains and feature IDs;
- scientific authority used;
- unresolved items preserved;
- validation commands or CI runs;
- compatibility and migration impact;
- whether any public handoff obligation changed.

## Review standard

Reviewers should evaluate four independent dimensions:

### Scientific integrity

Does the change accurately represent the source? Were unknowns left unknown?

### Structural correctness

Are identities, dependencies, ordering, statuses, and schemas coherent?

### Implementation neutrality

Does the contract define observable behavior without choosing an unjustified language, container, allocation strategy, layout, or error transport?

### Verifiability

Can acceptance tests and validators detect a non-conforming implementation or package?

Approval in one dimension does not substitute for review in another.

## Contradictions

When two authoritative artifacts appear contradictory:

1. stop the affected finalization or implementation path;
2. record the exact files, fields, and obligations in conflict;
3. preserve current statuses;
4. provide a minimal reproducer or conflicting acceptance cases;
5. request scientific or specification adjudication;
6. do not choose the most convenient meaning.

## Backward compatibility and versioning

Treat the following as potentially breaking:

- changing observable behavior;
- changing valid or invalid input sets;
- changing required output fields;
- changing stable error codes;
- strengthening lifetime, ordering, determinism, or resource obligations;
- changing shared-contract meaning;
- removing a feature, operation, mode, or normative fixture.

A breaking proposal must state the affected package versions, migration path, and replacement or deprecation policy.

## Security and responsible disclosure

Specification defects may create downstream safety or integrity risks. Follow `SECURITY.md` for sensitive reports. Do not publish exploit details in a public issue before maintainers have assessed the impact.

## What belongs elsewhere

The following belong in downstream `tllib` implementation repositories:

- runtime source code;
- bindings;
- build-system integration;
- concrete memory ownership conventions;
- platform-specific optimizations;
- binary packaging;
- production benchmarks;
- release artifacts.

An implementation problem that reveals a specification ambiguity should be reported here with the affected feature ID and bundle fingerprint.
