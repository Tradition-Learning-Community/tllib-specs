# TLC-FC-34-TRANSMISSION-LIFECYCLE-045 - Moving-window repetition evaluator

This finalized Feature Handoff Package exposes the Domain 34 Transmission Lifecycle feature **Moving-window repetition evaluator**. Its normative boundary is `maths/34-transmission-lifecycle/impregnation-phase.md` and the explicitly declared provider/ownership relations.

Evaluate the source moving average only when a complete history on [t-T,t] and nonzero T are supplied.

Scientific status: `partially_defined`. Execution status: `conditionally_executable`. Confirmed scientific provider domains: `[]`. Unresolved scientific relation domains: `[]`. Runtime domain dependencies are empty.

Forbidden: Do not extrapolate negative-time observations or invent a warm-up convention.
