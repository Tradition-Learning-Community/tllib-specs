## Purpose

Describe the problem and the repository outcome this pull request delivers.

## Change class

- [ ] Editorial only
- [ ] Structural, non-behavioral
- [ ] Observable handoff contract change
- [ ] Algorithmic specification change
- [ ] Mathematical or scientific change
- [ ] Validation or tooling change
- [ ] Cross-domain change

## Scope

Affected domains:

Affected feature IDs:

Affected repository layers:

- [ ] `maths/`
- [ ] `registry/math-contracts/`
- [ ] `registry/ir/` or `registry/optimized-ir/`
- [ ] `registry/algorithms/`
- [ ] `registry/oracles/`
- [ ] `handoff/`
- [ ] `reports/`
- [ ] `tools/` or workflows
- [ ] documentation only

## Authority and traceability

Identify the scientific source, contract, decision record, issue, or existing artifact that authorizes the change.

## Scientific boundary

State what remains unresolved. Confirm that no missing equation, type, domain, threshold, relation meaning, proof result, provider behavior, or scientific default was invented.

- [ ] No unresolved scientific question was silently resolved.
- [ ] Distinct concepts were not merged solely because they share a representation.
- [ ] Illustrative algorithm steps were not promoted to normative total order without authority.

## Observable impact

Describe changes to valid inputs, outputs, errors, invariants, ordering, determinism, resources, examples, or implementation freedom.

- [ ] No observable handoff obligation changes.
- [ ] Observable changes are listed above and have compatibility treatment.

## Compatibility and migration

State package-version impact, downstream consumer impact, deprecations, substitutions, and migration steps. Write `Not applicable` only with a reason.

## Validation evidence

Commands or CI runs:

```text
<validation evidence>
```

For handoff changes, confirm as applicable:

- [ ] deterministic catalog check passed;
- [ ] official handoff validator passed;
- [ ] logical self-tests passed;
- [ ] all relevant standalone exports passed determinism checks;
- [ ] no generated archive or temporary artifact was committed.

## Reviewer focus

Call out the highest-risk assumptions, files, or decisions that need close review.

## Completion checklist

- [ ] The change is focused and free of unrelated formatting churn.
- [ ] Every affected layer is updated or explicitly declared unaffected.
- [ ] Traceability is complete.
- [ ] README or example prose introduces no obligation absent from normative contracts.
- [ ] No runtime implementation code was added.
- [ ] Documentation reflects the final repository state.
- [ ] All review threads and required checks are resolved.