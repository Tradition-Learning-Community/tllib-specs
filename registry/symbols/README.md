# TLC canonical identifiers, namespaces, and representations

This directory defines the **engineering-level canonical naming system** for `tllib-specs`.

It is intentionally limited. It does not attempt to rename every term in the theory or impose one globally unique mathematical glyph for every scientific concept.

## Scope

The canonical system covers:

- stable scientific, feature, relation, contract, IR, algorithm, and oracle identifiers;
- domain-qualified namespaces;
- shared structural types;
- public module interfaces;
- explicit alias declarations;
- mappings from distinct semantic types to reusable internal representations.

## Non-goals

This registry does not:

- rewrite the authoritative notation under `maths/`;
- infer that equal symbols denote equal concepts;
- merge objects because their normalized names match;
- require every local theoretical term to become a public software type;
- assert scientific equivalence from a shared runtime carrier.

## Core rule

> Semantic identity is determined by a stable identifier and its qualified namespace, not by a short mathematical symbol or by its internal representation.

Two distinct concepts may use the same source symbol or the same internal carrier while remaining scientifically and semantically distinct.

## Files

- `namespaces.yaml` — canonical domain and infrastructure namespaces;
- `canonical-identifiers.yaml` — authoritative identifier classes and source registries;
- `representation-policy.yaml` — separation between semantic identity, aliases, and shared internal representations.

Shared structural types remain authoritative in `registry/global-finalization/shared-types.yaml`. Public module boundaries remain authoritative in `registry/global-finalization/module-interfaces.yaml`.
