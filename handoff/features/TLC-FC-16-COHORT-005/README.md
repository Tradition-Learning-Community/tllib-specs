# TLC-FC-16-COHORT-005 — Typological diversity index

This package implements the source diversity expression as the entropy of six supplied type proportions plus a caller-supplied calibration coefficient times a supplied expected typological-distance term. The package does not evaluate `d_type` itself because the type geometry is unresolved, and it does not calibrate the coefficient. It also preserves the source ambiguity in which the diversity formula writes `d_type(D_i,D_j)` although the distance was defined on typological objects.

An implementation is conforming only when all missing scientific values are explicit inputs, the source aggregation is evaluated without reinterpretation, and the D/T argument mismatch remains visible in traceability rather than silently corrected.
