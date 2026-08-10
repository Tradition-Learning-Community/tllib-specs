# TLC-FC-18-EVALUATION-011 — Peer population and peer evaluation

This package preserves both the source peer filter and the peer-evaluation mean. A candidate peer is retained only when affinity, exposure and competence each satisfy the strict source threshold. If the retained population `P_d(t)` is empty, the source mean is undefined and the operation must return the structured `PeerPopulationEmpty` error before division. It may not return zero, NaN, mentor evaluation or another fallback. `Psi_p` remains provider-backed and all peer thresholds remain opaque rather than calibrated locally.
