# TLC-FC-19-REGULATION-009 — Coupled F right-hand side

Evaluate `dF/dt = E(t)X + F(t) I_collective + G(t) dX/dt + H(t) grad V` only from supplied operands. `dX/dt` and `grad V` are inputs/providers, not quantities this feature differentiates or derives. The feature returns an RHS only and introduces no ODE solver, integrator or inferred state space.
