# TLC-FC-20-ROBUSTNESS-016 — Robust guidance likelihood expression

This finalized package preserves the source softmax-like fraction multiplied afterward by `F_fid(O,P)`. Because of that final factor, the result is not silently treated as a normalized probability distribution. The denominator support must be supplied and non-empty/non-zero. No renormalization, outcome-space invention, alignment estimator, fidelity estimator, or probability completion is introduced.
