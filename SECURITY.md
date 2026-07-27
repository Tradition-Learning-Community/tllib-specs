# Security policy

`tllib-specs` contains scientific and engineering specifications, validators, and export tooling. It does not contain production runtime code. Security reports are nevertheless relevant when a defect could cause downstream implementations to accept unsafe, misleading, corrupted, or non-deterministic contracts.

## Supported scope

Reports are in scope when they concern:

- validator bypasses that allow malformed or contradictory packages;
- path traversal or unsafe file handling in repository tooling;
- dependency or bundle-lock integrity failures;
- hash or determinism weaknesses that could conceal changed content;
- workflow changes that weaken protected-source or implementation-code checks;
- schema defects that allow identity substitution, dependency confusion, or silent semantic loss;
- export behavior that includes unintended scientific, registry, secret, or temporary files;
- supply-chain risks in GitHub Actions or validation dependencies.

Runtime vulnerabilities in downstream implementations should be reported to the relevant implementation repository unless the root cause is a defect in a handoff contract.

## Reporting

Do not open a public issue containing exploit details, sensitive repository information, or a practical validator bypass.

Use GitHub's private vulnerability reporting feature for this repository when available. Include:

- affected commit, file, workflow, schema, or feature ID;
- impact and realistic attack or failure scenario;
- reproduction steps or proof of concept;
- whether generated catalogs or bundles are affected;
- suggested remediation when known.

If private vulnerability reporting is unavailable, contact the repository maintainers through the organization channels before public disclosure.

## Handling expectations

Maintainers should:

1. acknowledge the report;
2. determine whether the issue is specification, tooling, workflow, or downstream-runtime related;
3. preserve evidence and affected fingerprints;
4. prepare a minimal corrective change with regression coverage;
5. revalidate catalogs and standalone exports when relevant;
6. publish an advisory when users need to take action.

No guaranteed response time is promised until the project publishes a formal service-level policy.

## Non-security reports

Use a normal issue for documentation defects, scientific questions, ordinary contradictions, feature requests, and non-sensitive validation failures.