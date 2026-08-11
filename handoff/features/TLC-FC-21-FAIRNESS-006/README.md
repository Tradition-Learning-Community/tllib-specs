# TLC-FC-21-FAIRNESS-006 — Raw Fairness Lagrangian

Evaluate the Lagrangian exactly as written in the Fairness source when all raw operands are supplied. In particular, preserve the lower-bound terms as `(R_perf-theta_min)` and `(F_fid-phi_min)`. The source does not state multiplier signs or a dual convention, so this package may not invert signs, impose non-negativity on `mu` or `nu`, derive KKT conditions, or claim a correct dual optimization procedure.
