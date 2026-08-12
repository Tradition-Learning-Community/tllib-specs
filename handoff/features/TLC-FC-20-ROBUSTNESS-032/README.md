# TLC-FC-20-ROBUSTNESS-032 — Fixed-point stability assessment descriptor

This finalized package conditionally assesses the source stability condition from provider-supplied Jacobian spectral values and component/threshold values. It does not build a Jacobian, compute eigenvalues, find a fixed point, solve the dynamics, infer thresholds, prove stability, or issue a universal stability certificate. `Re(sigma(J))<0` remains a supplied spectral assessment.
