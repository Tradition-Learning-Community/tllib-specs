# Engineering-candidate IR report — TLC-FC-09-VALUES-018

Work item `TLC-IR-TLC-FC-09-VALUES-018` lowers only contract `TLC-MC-TLC-FC-09-VALUES-018` from branch `contract/TLC-FC-09-VALUES-018` at commit `7daa8758945e63feb0e64a2865acbb43dfab75dd`.

The source contract has candidate status and explicitly reports `ready_for_ir: false`. This IR therefore uses `candidate_with_preserved_reservations`; it is an engineering candidate, not a scientific validation. The contract validator passes and all 12 source artifacts are present.

Two variants are produced. The semantic variant preserves the scientific object, matrix and order symbols, interval set, two constraints, relation-category property, precondition, postcondition, and invariant. The functional variant separates shape and range validations from an opaque relation evaluator and opaque result. It asserts no evaluation algorithm. A compute variant is not authorized because the contract contains no function, operator, equation, executable oracle, or calculational flow. A dynamic variant is not authorized because it contains no state or temporal evolution.

All four source uncertainties are propagated: the domain and meaning of `m`, endpoint identities and index set, numeric category mapping, and evaluation-result semantics. Two implementation decisions remain deferred: finite matrix representation and evaluation-result representation. Consequently the IR is not ready for implementation planning or code generation.

Coverage contains 16 contract elements: 12 fully represented, 4 represented as opaque, and none missing. No target language, storage layout, precision, public API, solver, discretization, backend, library, approximation, or optimization is selected.
