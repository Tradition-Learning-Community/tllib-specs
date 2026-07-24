# Candidate mathematical contract report

Work item `TLC-MATH-CONTRACT-TLC-FC-05-DYNAMICS-001` processes only `TLC-FC-05-DYNAMICS-001`, verified at position 2 of `CONTRACT_WAVE_1`. It starts from `planning/math-contract-entry` at `7f73fd908ff887e6ab3b7d184ca46f0c8477ad68`.

## Inspection and provenance

Inspected inputs: the four `registry/math-contract-entry` registries; `registry/features/revised/feature-candidates.yaml`; `feature-lineage.yaml`; `registry/functional-decomposition/decomposition-input-snapshot.yaml`; and the authorized object entry in `registry/scientific-objects/dynamics/scientific-objects.candidate.yaml`. The only scientific source read was `maths/05-dynamics.md`, “Équations de la Communauté / Contraintes de viabilité”, lines 147–153. No algorithm was referenced or read. No reference was missing. Registry provenance consistently points to scientific source commit `68a4d4c`; the execution commit is `7f73fd9`.

## Contract summary

The sole object is `TLC-SO-DYNAMICS-015`; no scientific relation is authorized. Four exact source inequalities constrain minimum actor-set cardinality, connectivity through `λ₂(L(R(t)))`, community-values deviation, and integrated memory deviation. They use 15 declared symbols, four states, four scalar thresholds, three operators, and temporal variables `t` and `τ`. There are no associated equations, hypotheses, or source properties. One registry precondition, postcondition, and identity-preservation invariant are retained.

The exact expressions are preserved in `normalized-equations.tex`; only alignment and spacing change, with `exact_copy` equivalence. No discretization, integration method, tolerance, implementation type, or executable oracle is introduced.

No contract dependency emerged: entry artifacts declare no immediate feature dependency and authorize one local object with no relation. The four source constraints form the candidate oracle basis.

Five major issues block IR: temporal domain, `L`/`λ₂` definitions, normed spaces, memory notation/type, and output aggregation semantics. Missing dimensions are a minor issue. Consequently the contract is ready for independent scientific review but not for IR, tests, or implementation. Recommended human decision: `revise`.

Structural/YAML/reference validation, validator compilation, and Git checks are recorded by the final execution. No numerical validation was executed because no source example or sufficiently defined operands are authorized.
