# TLC-FC-16-COHORT-012 — Configuration stability assessment

This package converts the source stability statement into a validation feature. The caller supplies the relevant Jacobian eigenvalues, the graph connectivity value `lambda_2`, the current diversity value `H_type`, and the scientific stability zone for diversity. The result is true only when every Jacobian eigenvalue has negative real part, `lambda_2>0`, and `H_type` belongs to the supplied stability zone.

The theory does not provide numerical bounds for that zone, so the implementation must not calibrate or infer them. The feature evaluates only the source conditions and treats missing or malformed stability-zone data as a structured input failure.
