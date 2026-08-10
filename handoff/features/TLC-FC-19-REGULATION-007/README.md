# TLC-FC-19-REGULATION-007 — Feedback-weight dimensional ambiguity guard

Structural guard for the source-acknowledged `dW_f/dt` incompatibility. It records that the squared-feedback-error term is scalar while the relaxation term is matrix-valued, with no source-defined diffusion rule or guaranteed error-reducing sign. It blocks unsupported numerical combination and never silently repairs the theory.
