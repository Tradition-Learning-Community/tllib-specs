# TLC-FC-19-REGULATION-002 — Collective self-correction right-hand side

Evaluate exactly the source right-hand side for `dI_collective/dt` from supplied operands. Preserve all five terms and signs, require the context-gradient provider, and return an RHS value only. No temporal integration, state advancement, gradient construction or matrix-shape invention belongs to this package.
