# IR validation report — TLC-FC-08-PRINCIPLE-002

## Result

The semantic, functional, and dynamic candidate IRs preserve the candidate contract with explicit reservations. Scientific validation remains pending. Because the source reports `ready_for_ir: false`, all variants use `candidate_with_preserved_reservations` and are not ready for implementation planning or code generation.

## Contract-to-IR checks

| Check | Result |
|---|---|
| Five contract symbols covered | Pass; unresolved properties retained |
| One state, two inputs, one output covered | Pass |
| Equation covered | Pass; exact normalized LaTeX retained |
| Operand order `P,D,t` covered | Pass |
| Postcondition covered | Pass; failure semantics unresolved |
| Preconditions, invariants, hypotheses | Pass; none supplied, none invented |
| Three contract unresolved items | Pass; all propagated |
| Two implementation decisions | Pass; both deferred |
| Oracle basis | Pass; equation retained, no executable oracle claimed |
| Traceability | Pass; contract commit, object, source path, and references present |

## Non-invention checks

No target-language choice, public API, memory format, scalar/vector/tensor assumption, solver, time step, discretization, optimization, node fusion, approximation, initial condition, or error policy is introduced. No `IntegrationStep`, `StateUpdate`, loop, or executable compute graph is present. The contract files are unchanged.

## Variant fitness

- Semantic: structurally useful for review, but blocked for implementation planning by symbol and domain questions.
- Functional: clarifies ordered ports, but is non-executable because `E` and all mapping spaces are unresolved.
- Dynamic: preserves state and derivative character, but cannot lower to a transition or numerical evolution.
- Compute: rejected because an operation sequence cannot be constructed without invention.

Coverage has no missing element. The authoritative machine checks are implemented by `tools/ir/TLC-FC-08-PRINCIPLE-002/validate_ir.py`.
