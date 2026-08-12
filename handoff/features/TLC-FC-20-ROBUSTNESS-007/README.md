# TLC-FC-20-ROBUSTNESS-007 — Integrated systemic robustness expression

This finalized package evaluates the source systemic robustness index only when all eight factors, time-dependent weights, covariance contributions, and tradition-gradient norm are already supplied. It preserves the geometric product and exponential penalty exactly. It does not derive eight factors from the earlier four-component decomposition, estimate covariance, construct gradients, normalize weights, solve weight trajectories, or infer `f_i`.
