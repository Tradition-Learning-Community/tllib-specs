# TLC-FC-19-REGULATION-010 — Coupled R right-hand side

Evaluate `dR/dt = I(t)T_tensions + J(t)S_solutions + K(t)F + L(t)grad E_context` using supplied tension, solution and context-gradient providers. Do not construct `T_tensions`, `S_solutions`, gradients, matrix dimensions, an ODE solver or a time integrator.
