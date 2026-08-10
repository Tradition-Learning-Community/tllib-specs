# TLC-FC-19-REGULATION-015 — Lyapunov candidate expression

Evaluate only the source candidate `V(t) = 1/2||X-X_ideal||^2 + 1/2||F-F_opt||^2 + 1/2||R-R_opt||^2` from supplied norm values and reference states. The result is a candidate value, not a Lyapunov certificate: this package does not construct norms, compute `dV/dt`, prove decrease, or certify stability or convergence.
