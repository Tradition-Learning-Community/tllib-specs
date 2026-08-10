# TLC-FC-19-REGULATION-005 — Guided correction delta

Evaluate the exact three-part `Delta X_i` source expression. Require `N > 1`, supplied softmax weights, `X_ideal`, and `grad J_collective`. The output is a delta expression only: this package does not choose a new state, clip or normalize the delta, solve an optimization problem, or silently repair the `N-1` denominator.
