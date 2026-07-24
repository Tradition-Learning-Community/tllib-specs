# Candidate IR validation report — TLC-FC-09-VALUES-018

## Source and status

- Source contract: `TLC-MC-TLC-FC-09-VALUES-018`
- Source branch: `contract/TLC-FC-09-VALUES-018`
- Source commit: `7daa8758945e63feb0e64a2865acbb43dfab75dd`
- Source status: `candidate`
- Source `ready_for_ir`: `false`
- Progression mode: `candidate_with_preserved_reservations`
- IR status: `engineering_candidate`
- Scientific validation: `pending`

## Contract-to-IR checks

- All two symbols are represented in both produced variants.
- Both inputs and the unresolved output are represented.
- The contract has no states and no equations; none were introduced.
- Both constraints, the precondition, postcondition, and invariant are represented as nodes and global contract constraints.
- The sole property is represented opaquely because its category mapping is undefined.
- All four contract unresolved items are propagated to both IR files and `ir-open-questions.yaml`.
- Both implementation decisions are propagated without being made.
- Contract coverage contains 16 elements, 12 fully represented and 4 represented as opaque, with 0 missing.

## Non-invention checks

- No C++ or Python application structure is present.
- No target-language type, binding, public API, storage layout, numeric precision, backend, or library is selected.
- No solver, integration step, time step, discretization, approximation, or optimization is introduced.
- No nodes are fused for performance.
- No contract file is modified.
- Failure semantics remain unresolved.

## Variant aptitude

- Semantic IR: suitable for candidate architectural review; not ready for implementation planning or code generation.
- Functional IR: suitable only as an opaque candidate relationship; blocked for concrete functional lowering, implementation planning, and code generation.
- Compute IR: not produced because no authorized calculational flow exists.
- Dynamic IR: not produced because no state or temporal dynamics exist.

The IR is traceable and contract-preserving, but it is not a scientifically approved specification.
