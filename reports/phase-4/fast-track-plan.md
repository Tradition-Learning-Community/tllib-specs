# Phase 4 fast-track plan

- Status: candidate planning proposal
- Source commit: `75814db2398b701e2f14c035ef8d63ca61fdfb26`
- Scope: scientific and algorithmic specification before implementation
- Scientific decisions performed by this document: none

## Operating principle

The objective is not to produce an exhaustive scientific article. The objective is to produce specifications that programmers can implement without silently inventing TLC semantics.

Work therefore proceeds on two tracks:

1. **Global coherence track** — only the cross-domain decisions that can invalidate several features.
2. **Implementation-readiness track** — small feature batches brought to an implementable scientific and algorithmic contract.

The 16 domains remain separately traceable, but every batch records its impact on the unified TLC theory.

## Fast-track rules

1. Do not wait for every historical pending decision before starting a pilot.
2. Triage decisions into `blocking_for_pilot`, `blocking_later`, `non_blocking_reservation`, `obsolete_or_superseded`.
3. Preserve unresolved items when they do not prevent a deterministic contract or oracle.
4. Never promote a candidate IR to canonical without an explicit human decision.
5. Prefer a provisional, limited-scope IR over an invented complete IR.
6. A programmer receives one implementation package per feature or inseparable feature group.
7. No C++ or Python implementation starts until that package is approved.

## Minimal implementation package

Each approved feature package contains only:

1. `decision.yaml` — approved scope, selected or provisional IR, reservations.
2. `contract.yaml` — inputs, outputs, types/shapes when known, preconditions, postconditions, invariants, errors.
3. `ir.yaml` — backend-neutral operations and dependencies.
4. `algorithm.md` — precise ordered algorithm or state machine, without backend code.
5. `oracle.yaml` — examples, properties, invariants, invalid cases, tolerances only when justified.
6. `implementation-task.md` — acceptance criteria readable by a programmer.

A package may be smaller when existing authoritative artifacts already provide one of these roles.

## Phase sequence

### P4.0 — Baseline refresh

One pull request only:

- update the global reconciliation to the current `main` commit;
- separate historical lineages, materialized candidates, contractable features, domain catalogue entries, and scientifically approved features;
- classify existing contracts and IRs by actual authority and executability;
- identify only the decisions that block the first pilot;
- do not rewrite `maths/` and do not select IRs.

### P4.1 — Pilot selection

Choose 6–10 features or inseparable groups representing:

- one foundational actor/context feature;
- one invariant or theorem-related feature;
- one dynamics or transformation feature;
- one normative feature;
- one relation or cross-domain feature.

Selection criteria:

- stable or explicitly limited boundary;
- traceable source;
- usable contract candidate;
- at least one IR candidate;
- dependencies bounded for the pilot;
- oracle possible from source-grounded properties.

### P4.2 — Scientific and technical adjudication

For each pilot item, allow exactly one outcome:

- `approved_canonical`;
- `approved_provisional_limited_scope`;
- `composite_group_required`;
- `revise_contract`;
- `revise_ir`;
- `targeted_extraction_required`;
- `deferred_blocked`;
- `rejected_for_implementation`.

No performance criterion may override scientific fidelity.

### P4.3 — Algorithm and oracle specification

Produce the minimal implementation package. Stop when a programmer can answer:

- What must be computed?
- From which inputs?
- In what order?
- Under which preconditions?
- Which invariants must hold?
- What constitutes a valid result or error?
- Which reservations remain outside the implemented scope?

### P4.4 — Reference implementation planning

Only after package approval:

- define a readable reference implementation task;
- define backend-conformance tests;
- defer optimization and hardware-specific lowering;
- prepare C++ and Python work only for approved packages.

### P4.5 — Expand by dependency-aware batches

Repeat the pilot method across all 16 domains. After each batch:

- update the global dependency view;
- check cross-domain compatibility;
- reopen only impacted decisions;
- do not restart completed domains wholesale.

## Role activation

Active now:

- orchestration and global reconciliation;
- scientific reviewer;
- targeted extraction and object correction only when proven necessary;
- functional-boundary review for explicitly unstable candidates;
- scientific review-package generator.

Waiting for prerequisites:

- IR architect for actual selection;
- pattern analysis;
- lowering and optimization;
- executable oracle implementation;
- developer-package generation;
- C++ core and Python bindings.

## Definition of progress

Progress is measured by approved implementation packages, not by the number of reports produced.

A batch is complete when:

- its scientific scope is explicit;
- its selected or provisional IR is explicit;
- its dependencies and reservations are bounded;
- its algorithm is specified;
- its oracle is specified;
- a programmer has unambiguous acceptance criteria.

## Immediate next work item

`P4.0 — Baseline refresh and blocker triage`.

The output must identify a small first pilot rather than requiring resolution of all historical pending decisions before any forward movement.