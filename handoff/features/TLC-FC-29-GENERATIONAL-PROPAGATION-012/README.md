# Replication time-decay preservation guard

Finalized Feature Handoff Package v1.0 for domain 29 Generational Propagation. The source Q_rep expression contains exp(-lambda t), including when delta_x(t)=0. This structural guard requires that the exponential time-decay factor remain present exactly as written. The unexplained decay is preserved rather than corrected: implementations must not remove the factor, compensate for it, or reinterpret lambda to neutralize it. This package adds no runtime dependency or extra scientific model.
