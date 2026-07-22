# Candidate IR report — TLC-FC-08-PRINCIPLE-002

## Executive decision

Three engineering-candidate variants were produced from contract commit `3db96ff560ff110ccd0a0fbf7e30997ac3264aa7`: semantic, functional, and dynamic. The recommended decision is **approved with reservations** for preservation and review only. Implementation planning and code generation remain blocked.

## Source state

The source contract is `candidate`, passes its validator, and reports `ready_for_ir: false`. It contains one differential equation, five symbols, one state, two inputs, one output, one postcondition, three unresolved items, and two implementation decisions. It has no independent executable oracle.

## Representation

The semantic variant preserves contract objects and roles. The functional variant exposes the ordered operator application `E(P,D,t)` and equality to `dP/dt`. The dynamic variant distinguishes the read of state `P` from the continuous derivative law and explicitly avoids a state update or integration step. A compute variant was rejected because it would require invented types and operations.

## Reservations

The meanings and mathematical spaces of `P`, `D`, `t`, and `E`; the evolution domain and regularity; and the existence or source of an initial condition remain unresolved. Type mapping and any numerical method remain deferred. These reservations block implementation planning and code generation but do not prevent a descriptive candidate IR.

## Traceability and scope

All normative symbols, equation content, argument ordering, postcondition, oracle basis, unresolved items, and deferred decisions are represented. No other feature was read or modified. No C++, Python application code, binding, API, backend, memory representation, solver, discretization, or optimization is specified.
