# TLC-FC-20-ROBUSTNESS-027 — Adaptability index expression

This finalized package evaluates the source adaptability index from supplied expectations, fidelity, context norms/distance and alignment. `E[P|c_train]=0` and `||c_train||=0` are explicit structured singularities. The factor `1-||c_new-c_train||/||c_train||` is never clamped, even when negative. No expectation estimator, norm, context distance, alignment estimator, calibration, clipping, or fallback is introduced.
