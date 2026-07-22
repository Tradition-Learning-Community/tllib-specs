# Candidate IR comparison — TLC-FC-09-VALUES-018

Source contract: `TLC-MC-TLC-FC-09-VALUES-018` at `7daa8758945e63feb0e64a2865acbb43dfab75dd`. Scientific validation remains pending.

## Semantic variant

- **Objective:** preserve every authorized object, symbol, constraint, property, precondition, postcondition, invariant, and uncertainty close to the contract.
- **Justification:** the contract contains one scientific object, two symbols, two constraints, and one property.
- **Advantages:** complete semantic coverage; undefined endpoints, categories, output, and `m` domain remain explicit.
- **Limits:** it is not an executable model and supplies no evaluation semantics.
- **Semantics preserved:** matrix shape, closed entry range, relation-category wording, candidate status, and traceability.
- **Structure made explicit:** distinct semantic, constraint, invariant, and opaque nodes.
- **Opaque information:** endpoint identity, category mapping, output type and semantics, domain of `m`.
- **Unresolved propagated:** `UNRES-M`, `UNRES-ENDPOINTS`, `UNRES-CATEGORIES`, `UNRES-OUTPUT`.
- **Additional decisions required:** `IMPL-MATRIX-REPRESENTATION`, `IMPL-RESULT`.
- **Implementation planning:** not ready.
- **Code generation:** not ready.
- **Contract conformity:** candidate; full coverage with opaque representation where required.

## Functional variant

- **Objective:** make the cited input–validation–output relationship explicit without inventing an evaluation algorithm.
- **Justification:** the contract names inputs, an evaluation output, a primary evaluation behavior, and two independently representable validations.
- **Advantages:** separates square-shape and entry-range validation from the opaque evaluation relationship.
- **Limits:** the central evaluator is an `OpaqueOperator`; no category mapping or result type is available.
- **Semantics preserved:** the same shape, range, candidate, and traceability requirements as the semantic variant.
- **Structure made explicit:** input and parameter ports, validation dependencies, opaque evaluation, and opaque output.
- **Opaque information:** evaluation operation, endpoint set, category mapping, output type, failure semantics.
- **Unresolved propagated:** `UNRES-M`, `UNRES-ENDPOINTS`, `UNRES-CATEGORIES`, `UNRES-OUTPUT`.
- **Additional decisions required:** `IMPL-MATRIX-REPRESENTATION`, `IMPL-RESULT`.
- **Implementation planning:** not ready.
- **Code generation:** not ready.
- **Contract conformity:** candidate; no function or operation beyond the contract is asserted.

## Variants not produced

- **Compute IR:** rejected because the contract provides no function, operator, equation, executable oracle, or authorized calculational flow. Turning the two constraints into a computation graph would invent operations.
- **Dynamic IR:** rejected because the contract contains no state, transition, temporal evolution, dynamic equation, or state invariant.

Neither produced variant loses a normative contract element. Scientifically undefined elements are deliberately represented as opaque rather than resolved.
