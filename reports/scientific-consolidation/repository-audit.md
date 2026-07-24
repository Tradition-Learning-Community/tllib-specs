# Audit du dépôt — consolidation scientifique

## État Git observé

- Branche de travail : `audit/scientific-extraction-consolidation`
- État avant création des sorties : dépôt propre, branche de départ `main` en avance de 2 commits sur `origin/main`.
- Dernier commit observé : `5b97f06af955dc34c9f234a7b128b791929212ea Record competencies extraction push failure`
- État au moment de la génération : `## audit/scientific-extraction-consolidation
?? registry/scientific-objects/cross-source-duplicate-candidates.yaml
?? registry/scientific-objects/global-object-candidates.yaml
?? registry/scientific-objects/global-relation-candidates.yaml
?? registry/scientific-objects/global-unresolved-terms.yaml
?? reports/scientific-consolidation/
?? tools/`

## Sources détectées

- `maths/00-master.md`
- `maths/01-disciple.md`
- `maths/02-community.md`
- `maths/03-huit-dimensions-de-tl.md`
- `maths/04-invariants.md`
- `maths/05-dynamics.md`
- `maths/06-theorems.md`
- `maths/07-message.md`
- `maths/08-principle.md`
- `maths/09-values.md`
- `maths/10-virtues.md`
- `maths/11-capacities.md`
- `maths/12-competencies.md`
- `maths/13-practice.md`
- `maths/14-lived-experience.md`
- `maths/15-relations.md`

## Paquets détectés

`capacities`, `community`, `competencies`, `disciple`, `dynamics`, `huit-dimensions-de-tl`, `invariants`, `lived-experience`, `master`, `message`, `practice`, `principle`, `relations`, `theorems`, `values`, `virtues`

## Complétude

| Source | Slug | Objets | Relations | Non résolus | Doublons | Rapport | Décision | Complet | Anomalies |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| maths/11-capacities.md | capacities | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/02-community.md | community | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/12-competencies.md | competencies | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/01-disciple.md | disciple | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/05-dynamics.md | dynamics | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/03-huit-dimensions-de-tl.md | huit-dimensions-de-tl | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/04-invariants.md | invariants | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/14-lived-experience.md | lived-experience | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/00-master.md | master | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/07-message.md | message | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/13-practice.md | practice | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/08-principle.md | principle | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/15-relations.md | relations | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/06-theorems.md | theorems | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/09-values.md | values | oui | oui | oui | oui | oui | oui | oui | aucune |
| maths/10-virtues.md | virtues | oui | oui | oui | oui | oui | oui | oui | aucune |

## Anomalies structurelles

- Problèmes structurels : 0.
- Divergences de schéma de premier niveau : 0.
- Relations vers des objets absents : 0.
- Détails structurés : `schema-divergences.yaml` et `source-coverage-issues.yaml`.

## Conclusion

Paquets complets : 16/16. La consolidation reste candidate et doit passer par la file de revue humaine.
