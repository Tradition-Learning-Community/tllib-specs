# Mathematical contract — TLC-FC-09-VALUES-018

Position 4 of `CONTRACT_WAVE_1`, compiled from `planning/math-contract-entry` at `7f73fd9`. The sole scientific source read is `maths/09-values.md:23`; the sole object is `TLC-SO-VALUES-047`; no scientific relation identifier is authorized.

The source defines systemic coherence `C` as an `m×m` matrix valued in `[-1,1]`, describing relations between values (compatibility, tension, opposition). The contract preserves this shape and range. It does not infer endpoint identities, the domain of `m`, category thresholds, or output semantics. There are 2 symbols, no state or equation, 2 constraints, 1 property, 1 precondition, 1 postcondition, and 1 registry invariant. No contract dependency or executable oracle is produced.

Three major unresolved issues concern endpoints, category mapping, and output semantics; the domain of `m` is minor. The contract is ready for independent scientific review. It can feed a deliberately abstract candidate IR, but is not marked ready for a concrete IR until endpoint and result semantics are decided. Recommended decision: `approved_with_reservations` for continued candidate compilation.
