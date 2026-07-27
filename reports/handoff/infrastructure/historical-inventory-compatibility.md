# Historical authoritative-inventory compatibility

## Scope

This infrastructure change extends the existing compatibility layer used by Feature Handoff Package v1.0 validation. It does not modify scientific sources, feature identities, feature statuses, package contracts, domain catalogs, schemas, shared contracts, or runtime behavior.

## Accepted historical shapes

The compatibility validator accepts authoritative `features` populations in either of the repository's established forms:

- a list of objects containing `feature_id`;
- an insertion-ordered mapping keyed by `feature_id`.

The extracted order remains authoritative and is compared exactly with the domain catalog.

## Count aliases

Every count alias present in an authoritative inventory is checked against the real extracted population. Established root aliases include `feature_count`, `population_count`, `active_feature_count`, `authoritative_feature_count`, `authoritative_population_count`, `expected_count`, `expected_active_count`, `expected_feature_count`, and `expected_active_feature_count`. Established summary aliases are also checked when present.

When an inventory contains no count field, the validator may read the sibling domain-finalization manifest. Any manifest population used as evidence must match the authoritative inventory exactly and in order, and every recognized manifest count must equal that same population.

## Conflict policy

No alias is preferred over another. Missing evidence, non-integer values, conflicting values, wrong population order, or a mismatch with the actual feature population causes validation failure. Historical metadata compatibility never changes or normalizes a `feature_id`.

## Verification

Compatibility self-tests cover list-form features, mapping-form features, agreeing count aliases, and rejection of conflicting count aliases. The existing progressive validator checks and all package, schema, traceability, dependency, strategy, identity, and no-implementation-code controls remain active.
