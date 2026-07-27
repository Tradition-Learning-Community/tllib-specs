# Progressive Domain Validation Infrastructure

## Initial blocker

The Feature Handoff Package v1.0 foundation validator contained a foundation-only population assertion:

```text
handoff/features/ must contain exactly TLC-FC-00-MASTER-005
```

That assertion correctly protected the initial pilot, but it made every later domain compilation invalid by construction. A second foundation assumption called the pilot-specific validator for every discovered feature package, which would also reject any non-pilot package. Domain work was not permitted to modify the global validator, so the incompatibility required a dedicated infrastructure change before Master, Disciple, or any other domain could be integrated.

The handoff workflow also listened only to pull requests targeting `main`. Domain pull requests target `handoff/integration-v1`, so they could not receive the dedicated handoff validation without a workflow update.

## Removed rule

The validator no longer enforces:

```text
v1.0 foundation must contain only the declared pilot feature
```

It also no longer applies `validate_pilot()` to every feature package. Pilot validation is invoked only for `TLC-FC-00-MASTER-005`, and the validator separately proves that this pilot remains present and validated.

## Progressive population rule

The expected feature population is now computed as:

```text
foundation pilot
union
all feature IDs declared by every currently present domain catalog
```

The computed set must exactly equal the directory names under `handoff/features/`.

This gives progressive integration without weakening completeness:

- no domain catalog is required for the foundation-only state;
- a present domain catalog must declare its complete local population;
- every declared feature must have exactly one package directory;
- every package directory must be declared, except the foundation pilot before a Master catalog exists;
- a feature may be owned by only one domain catalog;
- package paths, versions, package statuses, and domain identities must agree with the catalog;
- the exact union of package shared dependencies must agree with the catalog dependency summary.

`handoff/catalog.json` remains a foundation catalog. It must remain syntactically coherent and preserve the pilot and the eight shared contracts, but it is not used as the progressive domain population authority.

## Domain catalog contract

A domain is declared by:

```text
handoff/domains/<domain-slug>/catalog.json
```

Every directory under `handoff/domains/` must contain a catalog. The catalog is validated against `handoff/schemas/domain-catalog.schema.json` and declares:

- schema and package-model versions;
- domain slug and numerical domain index;
- expected feature count;
- authoritative ordered feature IDs;
- one package entry per feature, in the same order;
- complete-population and validation statuses;
- the exact shared dependency union;
- the authoritative domain inventory and validation metadata.

The validator rejects a catalog if its count, list, package entries, order, paths, versions, statuses, dependencies, domain index, or domain identity disagree.

## Authoritative inventory validation

The validator does not embed the 166 feature IDs in Python. Each catalog must reference:

```text
registry/domain-finalization/<domain-slug>/feature-status.yaml
```

The catalog's ordered feature population must exactly match the `features` list in that authoritative domain inventory. The inventory count and domain identity are also checked. For every authoritative feature, the finalized IR, algorithm specification, and acceptance oracle paths must exist under their established domain trees.

This dependency is stable because domain finalization already defines the selected package population and because YAML parsing is read-only. The workflow installs `PyYAML` alongside `jsonschema`; no upstream YAML is modified or exposed as a handoff interface.

## Pilot controls preserved

`TLC-FC-00-MASTER-005` remains mandatory while model v1.0 declares it as the foundation pilot. The following checks remain active:

- exact feature identity;
- pilot, partially-defined, structural-only statuses;
- required object and relation references;
- required stable error codes;
- exactly one structural operation;
- partially constrained strategy mode;
- all eight oracle acceptance identifiers.

The logical self-test deliberately alters the pilot strategy and verifies that the pilot validator still rejects the package.

## Individual package controls preserved

Every discovered package still receives the existing checks:

- JSON syntax and JSON Schema validation;
- cross-file feature identity;
- package-version consistency;
- required and declared files;
- `examples.json` presence consistency;
- required non-empty traceability categories and resolvable repository-relative paths;
- globally unique acceptance test IDs;
- operation-scoped unique error codes;
- valid partial-order strategy references and prescribed-strategy evidence;
- exact manifest/contract shared dependency agreement and resolution;
- absence of normative C++, Rust, Ruby, or Python code.

## Logical scenarios

The validator provides `--self-test`, and CI executes it after repository validation.

### Accepted

A. **Foundation only** — `MASTER-005` is present and no domain catalog exists.

B. **Complete Master** — the Master catalog declares 16 IDs and all 16 package directories exist.

E. **Progressive domain** — Master is complete while Disciple is absent and undeclared.

F. **Two complete domains** — Master and Disciple are both complete and their feature populations are disjoint.

### Rejected

C. **Incomplete Master** — the catalog declares 16 features but only 15 package directories exist.

D. **Orphan package** — a Disciple package exists without a Disciple catalog.

G. **Collision** — two domains declare the same feature ID.

H. **Altered pilot** — the foundation pilot no longer satisfies its specific strategy or other source-backed controls.

The repository-level validator adds stronger checks beyond these set-based self-tests: authoritative inventory equality, package schemas, dependency summaries, path resolution, statuses, versions, traceability, and all preserved package-level controls.

## Parallel domain integration

Each domain pull request is validated from its own merged checkout against the current target branch content. After one domain merges, a second domain branch created from an older `handoff/integration-v1` head must be realigned before merge so its validation includes the already integrated catalog and packages.

Recommended realignment instructions for domain task owners:

1. Update the domain branch from the latest `handoff/integration-v1` using the project's normal GitHub branch-update or rebase workflow.
2. Resolve Git conflicts without deleting or rewriting another domain's catalog or feature packages.
3. Keep the domain's own complete catalog under `handoff/domains/<domain-slug>/catalog.json`.
4. Ensure its feature IDs are disjoint from every catalog already present.
5. Re-run the handoff workflow through the updated pull request.
6. Do not edit `tools/handoff/validate_handoff.py`, handoff schemas, shared contracts, or another domain's packages from a domain compilation task.

Automatic Git conflict resolution is intentionally out of scope. Population collision and incompleteness are rejected deterministically once the branch is evaluated.

## Files and scientific boundary

This infrastructure change modifies only the generic validator, the domain catalog schema, handoff documentation, the handoff workflow, and this report. It creates no feature package, scientific content, contract, IR, test plan, algorithm, oracle, or shared-contract change.
