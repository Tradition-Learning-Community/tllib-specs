# TLC-FC-22-TEMPORALITY-004 — Hereditary temporal flux right-hand side

This finalized handoff evaluates only the right-hand side of the hereditary Temporalité flow. The non-autonomous `F_tau` result and the hereditary Memory integral are external scientific inputs; this package merely preserves the source addition and returns `dphi/dtau`. It selects no quadrature and advances no state in time.

The source explicitly depends on Memory through a kernel `K` and mnemonic operator `M`. Published Memory features 003 and 004 are recorded as scientific provenance, but their richer observable signatures are not silently adapted into direct runtime calls. Runtime dependencies therefore remain empty.
