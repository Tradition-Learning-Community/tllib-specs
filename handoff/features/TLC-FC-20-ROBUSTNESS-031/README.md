# TLC-FC-20-ROBUSTNESS-031 — Integrated dynamics right-hand side

This finalized package evaluates the four source right-hand sides for `dot R`, `dot E`, `dot A`, and `dot F` from supplied states, coefficients, gradients, maxima/optimum terms and `dot T`. It does not integrate the ODE system, choose a time step, construct gradients, estimate coefficients, solve trajectories, find fixed points, discretize time, or choose a numerical solver.
