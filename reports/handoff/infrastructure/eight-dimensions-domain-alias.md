# Eight Dimensions domain identifier normalization

The authoritative feature identifiers use the token `HUIT-DIMENSIONS-DE-TL`, while the authoritative domain registry and package namespace use `huit-dimensions`.

The handoff validator compatibility entry point normalizes a trailing `-de-tl` identifier token only when the corresponding authoritative `registry/domain-finalization/<normalized-domain>/` directory exists. This preserves strict index, inventory, package-path, ownership, and artifact checks while avoiding a lexical false negative.

The domain inventory also exposes `feature_count: 11` as a non-scientific metadata alias for the existing `active_feature_count: 11`, following the established domain-compilation pattern.
