# TLC-FC-19-REGULATION-003 — Collective solution aggregation

Evaluate the exact source aggregation for `R_solutions(t)` only when the solution domain is nonempty and all solution, weight, state, optimum, norm and sigma providers are supplied. Preserve the `1/|D|` factor and exponential denominator `2 sigma^2`; do not synthesize providers or clamp invalid denominators.
