# Authoritative inventory key compatibility

Domain finalization inventories use two established metadata vocabularies:

- `domain` and `feature_count`;
- `domain_id` and `population_count`.

The progressive handoff validator now accepts either established pair. When both aliases are present, every value must agree with the catalog domain and the actual ordered feature population. Missing metadata and conflicting aliases remain validation failures.

This compatibility change does not alter domain inventories, scientific artifacts, schemas, shared contracts, package semantics, or population rules. It allows the validator to consume existing authoritative inventories without rewriting upstream history.
