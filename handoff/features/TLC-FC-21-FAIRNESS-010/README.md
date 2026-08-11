# TLC-FC-21-FAIRNESS-010 — Complementarity expression

Evaluate the exact complementarity formula from supplied collective performance, individual performances, cognitive diversity, and collective alignment. The denominator is `sum_i P_i`; if that sum is zero, return `ComplementarityDenominatorZero`. Preserve the numerator `P_collect - max_i P_i` exactly. Implementations must not clamp or normalize the denominator, normalize performances, change the numerator sign, or fabricate performance values.
