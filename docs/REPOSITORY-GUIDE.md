# Repository operating guide

This guide explains how work moves through `tllib-specs`, who owns which decisions, and how to change the repository without weakening scientific integrity or downstream usability.

## Operating model

The repository is a controlled transformation system:

```text
scientific authority
    → mathematical contracts
    → source intermediate representations
    → finalized engineering IR
    → algorithm specifications
    → acceptance oracles
    → Feature Handoff Packages
    → standalone bundles for downstream implementation
```

Each layer has a distinct responsibility. Later layers may clarify structure and testability, but they may not invent scientific meaning absent from earlier authority.

## Who does what

### Scientists and domain experts

Primary responsibility:

- define or clarify domain meaning;
- identify unsupported assumptions;
- review unresolved scientific questions;
- provide evidence, sources, and adjudication proposals;
- distinguish unknown, undefined, disputed, and external-provider semantics.

They should normally begin in `maths/` and the scientific review records, then identify all affected feature IDs.

A scientifically useful contribution does not need to contain implementation advice. It must, however, state the consequences of the clarification for observable behavior when those consequences are known.

### Mathematicians

Primary responsibility:

- formal definitions;
- domains and codomains;
- assumptions;
- invariants;
- proof obligations;
- admissible equivalences;
- numerical or symbolic constraints.

They should avoid implementation vocabulary unless it is needed to express an observable property. Missing mathematical content remains explicit rather than being replaced with software defaults.

### Algorithm designers

Primary responsibility:

- characterize valid computation or transformation families;
- distinguish required operations from illustrative decomposition;
- specify partial ordering only when necessary;
- define deterministic or stochastic obligations;
- justify complexity or resource requirements;
- align algorithms with acceptance oracles.

An algorithm designer must state whether a procedure is open, partially constrained, or prescribed.

### Specification engineers

Primary responsibility:

- maintain identity and traceability across layers;
- compile authoritative content into coherent contracts;
- preserve unresolved semantics;
- prevent accidental equivalence between distinct concepts;
- maintain schemas, catalogs, validators, and deterministic exports;
- ensure final handoff packages remain autonomous.

Specification engineers do not adjudicate science by themselves.

### Runtime implementers

Primary responsibility in this repository:

- consume exported bundles;
- identify ambiguities, contradictions, missing observable obligations, or untestable acceptance criteria;
- provide minimal implementation-facing reproductions.

Production code, bindings, build files, memory policies, and platform optimizations belong downstream.

### Reviewers and maintainers

Primary responsibility:

- ensure the right expertise reviewed the right dimension;
- require evidence for normative changes;
- protect the scientific boundary;
- prevent repository-wide churn for local changes;
- ensure CI evidence matches the actual proposed tree;
- keep decision history discoverable.

## Decision ownership

| Decision | Primary authority | Required consultation |
|---|---|---|
| Scientific meaning | scientist or domain expert | mathematician, affected specification owners |
| Formal mathematical definition | mathematician | domain expert, algorithm designer where executable |
| Required algorithmic order | algorithm designer with source authority | mathematician, specification engineer |
| Handoff structure | specification engineer | downstream implementer, validator maintainer |
| Concrete language API | downstream implementation project | handoff consumer, runtime maintainers |
| Memory layout and allocation | downstream implementation project | performance and safety reviewers |
| Resolution of a preserved scientific question | scientific adjudication process | all affected domains |

No single role should silently make a decision outside its authority.

## Change impact levels

### Level 0 — Editorial

Examples: spelling, broken links, clearer non-normative prose.

Requirements:

- no semantic change;
- no package fingerprint change unless the edited file is part of the fingerprint by design;
- focused review.

### Level 1 — Structural, non-behavioral

Examples: traceability repair, deterministic tooling improvement, stricter malformed-input rejection without changing valid packages.

Requirements:

- validator evidence;
- affected package or catalog analysis;
- no scientific adjudication.

### Level 2 — Observable contract change

Examples: valid input set, required output field, stable error, ordering, determinism, or acceptance criterion changes.

Requirements:

- source authority;
- feature impact list;
- compatibility analysis;
- package version decision;
- downstream migration note.

### Level 3 — Scientific change

Examples: equation, type, relation meaning, proof status, provider semantics, threshold, or causal interpretation.

Requirements:

- scientific evidence and adjudication;
- cross-layer propagation plan;
- affected-domain review;
- explicit treatment of previously unresolved questions;
- no merge until authority is clear.

## Definition of ready

A proposed change is ready for implementation when:

- the affected features are known;
- the authority is cited;
- unresolved questions are listed;
- the expected repository layers are identified;
- compatibility impact is understood;
- acceptance evidence is defined;
- the change can be reviewed as one coherent unit.

## Definition of done

A change is done when:

- all affected layers are updated or explicitly declared unaffected;
- traceability is complete;
- validators pass;
- catalogs and exports are deterministic;
- documentation reflects the final state;
- no unresolved item has been silently closed;
- the pull request contains reviewable evidence;
- temporary files and generated archives are absent.

## Cross-domain changes

Cross-domain work should use a dedicated integration branch and explicit inventory. Do not modify sixteen domains in parallel without first stabilizing shared schemas and contracts.

For cross-domain changes:

1. define the shared change centrally;
2. identify every affected domain and feature;
3. update domains in isolated branches or commits;
4. reconcile shared abstractions only after observing real repetition;
5. run global population and export validation;
6. publish one final integration pull request.

Shared representation never proves shared scientific identity.

## Decision records

Create a decision record under `docs/decisions/` for changes that are:

- cross-domain;
- difficult to reverse;
- normative for contributors or downstream consumers;
- likely to be questioned later;
- based on a rejected alternative that may recur.

Use `docs/decisions/0000-template.md`. Decision records explain why a choice was made; they do not replace normative contracts.

## Repository hygiene

Keep the repository production-grade:

- no decorative generated noise;
- no committed bundle archives;
- no duplicated validation authority;
- no hidden compatibility aliases;
- no unbounded catch-all documents;
- no mass formatting unrelated to the change;
- no misleading status badges;
- no claims unsupported by committed evidence;
- no implementation-language examples presented as normative.

## Release posture

Feature Handoff Package v1.0 is a specification release, not a runtime release. Future model versions should publish:

- a versioned catalog;
- migration notes;
- compatibility classification;
- deterministic fingerprints;
- validation evidence;
- explicit deprecations and substitutions;
- unchanged unresolved-science inventory unless scientific adjudication occurred.

## Suggested review routing

- Scientific changes: domain expert + mathematician.
- Algorithm changes: algorithm designer + mathematician or domain expert.
- Handoff changes: specification engineer + downstream implementer.
- Validator changes: tooling reviewer + adversarial test reviewer.
- Cross-domain changes: at least one reviewer outside the initiating domain.
- Security-sensitive changes: private review under `SECURITY.md`.