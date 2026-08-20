# Domain 31 — Institutionalization scientific freeze

- Baseline: `8b11e62a26c2d2a68753525941ce0ad457c31fdc`
- Authoritative source: `maths/31-institutionalization/institutionalization.md` (`f5ae9cb8ad54d41ab1108078b1f691f043cbe891`)
- Scientific objects: **91**
- Scientific relations: **54**
- Unresolved/provider boundaries: **34**
- Final features: **37**

## Dependency matrix

| Relation | Status | Normative treatment |
|---|---|---|
| 31 -> 04 | confirmed | Reuse `N_inv` and `pi_N`; no local redefinition |
| 31 -> 29 | confirmed | Reuse `G_t` and `V_t`; graph mutation remains provider-owned |
| 31 -> 24 | unresolved | Preserve the conflicting `tau_adapt` convention; no conversion/inversion |
| 31 -> 30 | not proven/rejected | Analysis companionship creates no dependency |
| runtime | `[]` | No runtime edge invented |

## Critical preserved boundaries

`Txt_ref` absent-case semantics, `Aut`, `pi_d`, correction persistence, competence vector ordering, `tau_adapt`, the reform growth law, and the range/clamping of `H_inst` remain explicitly unresolved or provider-backed. The two source uses of `lambda` and `X` are namespaced by semantic role and are not silently identified.
