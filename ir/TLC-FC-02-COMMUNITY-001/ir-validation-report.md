# IR validation report — TLC-FC-02-COMMUNITY-001

## Result

The semantic IR is an `engineering_candidate` derived from contract commit `2e0858acc21bd97fe6c59db50b2598fb73971e52`. Scientific validation remains pending. The source contract is not ready for IR, so progression uses `candidate_with_preserved_reservations`.

## Contract-to-IR checks

- All five declared symbols and the one opaque output are represented.
- All four constraints are represented as nodes and global constraints.
- The precondition, postcondition, and invariant are represented by dedicated nodes and global constraints.
- There are no contract states, equations, hypotheses, properties, or required contract dependencies to encode.
- The constraint-only oracle basis is retained; no executable oracle is asserted.
- Both implementation decisions are deferred.
- All four contract unresolved items appear in the IR, open questions, coverage matrix, and decision report.
- Coverage contains zero missing elements.

## Exclusion checks

No target-language API or representation, implementation numeric type, binding technology, solver, discretization, optimization, backend, memory format, approximation, or performance node fusion is introduced. The contract files are unchanged.

## Reference and aptitude checks

Node, edge, and constraint references are internally consistent. Provenance includes the source-contract branch and full commit, contract identifier/status, scientific source path/range/commit, feature identifier, scientific object identifier, and derivation classifications.

The semantic variant is suitable only for review and later contract revision. It is not ready for implementation planning or code generation. Functional, compute, and dynamic variants are excluded for the reasons recorded in `ir-comparison.md`.
