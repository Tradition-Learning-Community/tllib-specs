# TLC-FC-20-ROBUSTNESS-012 — Contextual transfer expression

This finalized package preserves `T(P,c)=T_0(P)+alpha(c)(T_0(P)-T_adapt(P,c))+beta(c) grad_P F_fid` exactly. The counter-intuitive `T_0-T_adapt` sign is not repaired or reversed. The gradient and all transfer/adaptation operands are provider-supplied. No learner, gradient estimator, adaptation optimizer, projection, interpolation, or sign correction is introduced.
