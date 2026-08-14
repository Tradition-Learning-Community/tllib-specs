# Hamiltonian raw expression

Evaluates `H = p·F - L + lambda P_pres` only from caller-supplied final terms and preserves every source sign exactly. This package does not introduce a Hamiltonian optimizer, costate solver, gradient engine, control policy, or hidden minimization step. Any required dynamics or derivative providers remain external.
