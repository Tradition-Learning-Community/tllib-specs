# TLC-FC-20-ROBUSTNESS-013 — Contextual transfer sign ambiguity guard

This finalized structural guard exists solely to prevent silent repair of the source term `T_0(P)-T_adapt(P,c)`. The chapter does not explain the counter-intuitive orientation, so the implementation must preserve it and surface the ambiguity. No typo correction, sign inversion, averaging, fallback, or learned adaptation convention is permitted.
