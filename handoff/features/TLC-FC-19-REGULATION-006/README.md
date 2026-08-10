# TLC-FC-19-REGULATION-006 — Feedback-weight raw right-hand side

Preserve the raw source equation for `dW_f/dt`. The pairwise squared-error average is scalar while `delta(W_f_opt-W_f)` is matrix-valued under the source description; numerical combination is permitted only with explicit authoritative dimensional-compatibility evidence. Never broadcast the scalar, insert an identity matrix, change the sign, reinterpret the square as a gradient, or integrate in time.
