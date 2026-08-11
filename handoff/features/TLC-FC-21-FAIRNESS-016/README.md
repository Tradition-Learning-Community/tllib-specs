# TLC-FC-21-FAIRNESS-016 — Contextual fairness expression

Evaluate contextual fairness only from externally supplied context performance, fidelity, alignment, extrema, and minimum values. The three denominators `max P(c)`, `F_fid^max`, and `Alig_max` must each be nonzero and have dedicated structured errors. This handoff does not search contexts, invent minimum or maximum operators over unsupplied populations, clamp denominators, normalize the result, or introduce a hidden calibration policy.
