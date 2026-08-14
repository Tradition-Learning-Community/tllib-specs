# Teleological update provider descriptor

Preserves the source relation `G(t+1)=U(G(t),c(t))` and its declared typing without inventing an implementation for the update operator. The operator `U` remains externally supplied and opaque at runtime.

This handoff package therefore exposes the update relationship as a provider-backed descriptor only. It does not synthesize an update policy, optimizer, control law, numerical solver, or hidden state transition beyond what is explicitly present in the scientific source.
