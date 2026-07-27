# Support and questions

Use the pathway that matches the nature of the question. This keeps scientific review, specification maintenance, implementation feedback, and security reports separate.

## Scientific or mathematical question

Open a scientific question issue when the request concerns meaning, equations, domains, assumptions, proof status, relation semantics, thresholds, or unresolved terminology.

Include the exact source path, section, affected feature IDs, and whether the question blocks structural work or only scientific execution.

## Specification contradiction or defect

Open a specification defect issue when two files impose incompatible obligations, a handoff package is incomplete, traceability is broken, or an acceptance test contradicts the contract.

Include:

- feature ID;
- package version and bundle hash when available;
- exact files and fields;
- minimal conflicting example;
- expected impact on downstream implementers.

Do not resolve the contradiction by proposing an unsupported scientific default.

## Handoff consumer feedback

Downstream implementers should report problems against the exported bundle they used. Provide the feature ID, `bundle-lock.json` fingerprint, implementation language, and the specific decision that could not be derived from the package.

Implementation-specific build failures, performance problems, bindings, packaging, and platform behavior belong in the downstream implementation repository unless the handoff itself is defective.

## Validation or tooling problem

Report the command, commit, platform, Python version, complete diagnostic, and whether the failure is reproducible on an unchanged checkout.

## Sensitive security concern

Follow `SECURITY.md`. Do not disclose a practical bypass or exploit in a public issue.

## General discussion

Keep general design discussion tied to a concrete repository outcome: a source clarification, decision record, contract correction, validator improvement, or documented future proposal. Broad discussion without an actionable specification consequence should remain outside issue tracking until it can be scoped.