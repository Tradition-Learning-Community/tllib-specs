# Candidate IR comparison — TLC-FC-08-PRINCIPLE-002

Source contract: `TLC-MC-TLC-FC-08-PRINCIPLE-002` at `3db96ff560ff110ccd0a0fbf7e30997ac3264aa7` (candidate; `ready_for_ir: false`). All produced variants use `candidate_with_preserved_reservations` and remain unsuitable for code generation.

## Semantic IR

- **Objective:** preserve all five symbols, their contract roles, the differential equation, and its postcondition.
- **Justification:** the contract contains a scientific object, symbols, an equation, and a compatibility relation.
- **Advantages:** closest representation to the contract; no executable interpretation is implied.
- **Limits:** symbol semantics, domains, regularity, shapes, units, and initial condition remain opaque.
- **Structure made explicit:** distinct nodes and semantic/constraint connections.
- **Planning/code generation:** not ready / not ready.
- **Conformity:** exact equality and ordered arguments are preserved.

## Functional IR

- **Objective:** expose the ordered application `E(P,D,t)` and its equality to `dP/dt`.
- **Justification:** the contract explicitly identifies inputs, an operator, an output, and an input-output relation.
- **Advantages:** ports and data dependencies are visible without defining an API or implementation.
- **Limits:** `E` remains opaque; the graph is descriptive, not executable.
- **Information deliberately opaque:** mathematical types, operator semantics, purity, error policy.
- **Planning/code generation:** not ready / not ready.
- **Conformity:** no additional operation or transformation is introduced.

## Dynamic IR

- **Objective:** distinguish state read, continuous derivative law, and derivative output.
- **Justification:** the contract identifies `P` as state and uses continuous derivative notation.
- **Advantages:** makes clear that the equation is not itself a discrete state update.
- **Limits:** no initial condition, integration, discretization, solver, step, or stopping rule exists.
- **Information deliberately opaque:** evolution domain and regularity.
- **Planning/code generation:** not ready / not ready.
- **Conformity:** no `IntegrationStep` or `StateUpdate` node is created.

## Rejected variant

The compute IR was considered and rejected. The contract provides no executable oracle, domain, types, implementation of `E`, numerical operation sequence, or authorized numerical realization. Turning the equality into an executable calculation graph would invent operations and types.

## Shared unresolved and deferred decisions

All variants propagate `UNRESOLVED-SYMBOL-SEMANTICS-001`, `UNRESOLVED-DOMAIN-001`, and `UNRESOLVED-INITIAL-CONDITION-001`. `IMPL-DEC-001` and `IMPL-DEC-002` remain deferred. No produced variant loses a normative contract element; opaque representation is intentional and recorded in `ir-coverage.yaml`.
