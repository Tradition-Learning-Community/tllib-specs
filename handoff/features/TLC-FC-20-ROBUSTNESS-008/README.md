# TLC-FC-20-ROBUSTNESS-008 — Robustness weight right-hand side

This finalized package exposes the source right-hand side `dw_i/dt = f_i(E(t),P_pres(t))` as an externally supplied functional evaluation. It does not define `f_i`, integrate weights, choose time steps, normalize weights, solve trajectories, or infer environment/presence dynamics. The sum-of-weights condition remains a separate supplied-state constraint.
