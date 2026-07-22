# IR variant comparison — TLC-FC-02-COMMUNITY-001

## Semantic IR — produced

- **Objective:** preserve C1's symbols, constraints, validation obligations, provenance, and unresolved semantics without claiming executability.
- **Justification:** the contract contains five symbols, one output, four constraints, one precondition, one postcondition, and one invariant.
- **Advantages:** complete contract coverage; undefined measure, coherence, actor domain, and output remain explicit; no implementation choice is introduced.
- **Limits:** it cannot define an evaluation procedure or executable result.
- **Semantics preserved:** existence/subset, positive measure, universal membership, minimum coherence, candidate-input status, result traceability, and object distinctness.
- **Structure made explicit:** separate symbol, constraint, opaque-operator, output, validation, and invariant nodes plus semantic/constraint edges.
- **Opaque information:** measure operator and space, coherence function and comparator, actor domain/type, output type/semantics, and failure semantics.
- **Unresolved propagated:** `UNRES-MEASURE`, `UNRES-COHERENCE`, `UNRES-ACTOR-DOMAIN`, `UNRES-OUTPUT`.
- **Additional decisions needed:** `IMPL-RESULT-REPRESENTATION`, `IMPL-MATH-TYPE-MAPPING` after scientific resolution.
- **Implementation planning:** not ready.
- **Code generation:** not ready.
- **Contract conformance:** candidate; structurally complete, scientifically pending.

## Functional IR — rejected

The contract declares no function or equation. Although it names a candidate evaluation behavior, the mathematical result semantics are absent and `IMPL-RESULT-REPRESENTATION` is explicitly blocking for IR. Creating input/output ports or an evaluation operator would choose an unsupported relation.

## Compute IR — rejected

No explicit calculational dataflow exists. The measure and coherence operators, actor domain, comparator, output semantics, and executable oracle are all absent or unresolved. A compute graph would invent operations or ordering.

## Dynamic IR — rejected

The contract contains no state, transition, temporal evolution, dynamic equation, or state invariant. Its temporal character is `not_specified`.
