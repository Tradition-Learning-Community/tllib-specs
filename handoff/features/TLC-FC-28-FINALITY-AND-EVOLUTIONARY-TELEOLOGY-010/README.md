# Hamiltonian preservation-sign ambiguity guard

Preserves the source term `+ lambda P_pres` exactly. No sign inversion, positivity assumption for `lambda`, objective reparameterization, or inferred penalty convention is introduced. The package records this sign as an unresolved scientific boundary and prevents downstream implementations from silently repairing it by intuition.
