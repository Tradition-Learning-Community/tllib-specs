# TLC-FC-21-FAIRNESS-001 — Procedural robustness expression

Evaluate the source-defined procedural robustness expression only when category, score, expectation, transparency, and justice operands are supplied by explicit providers. The output is deliberately not bounded by this contract: values outside `[0,1]` remain unchanged. Implementations must not invent categories, scores, expectation estimators, transparency, justice, clamping, or normalization.
