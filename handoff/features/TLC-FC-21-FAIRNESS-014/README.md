# TLC-FC-21-FAIRNESS-014 — Temporal responsibility expression

Scale an externally supplied value for the exact source integral by `1/T`. The horizon `T` must be nonzero; `T = 0` yields `ResponsibilityHorizonZero`. This package deliberately does not differentiate alignment efficiency, perform quadrature, discretize or interpolate time, or define a time-series policy. The derivative, indicator inputs, fidelity function, and integral itself are provider responsibilities outside this handoff.
