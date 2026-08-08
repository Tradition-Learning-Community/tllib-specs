# Plan de production des domaines 16–35

## Contexte

Les domaines `00–15` disposent déjà de la chaîne complète de spécification et de handoff : inventaires scientifiques, décomposition fonctionnelle, registres, IR finalisées, contrats, algorithmes lorsque la théorie autorise une procédure, oracles, catalogues de domaine et Feature Handoff Packages validés.

Les domaines `16–35` disposent actuellement de leurs sources scientifiques sous `maths/`, avec un README par domaine et les documents scientifiques qui y sont déclarés. Les couches aval ne sont pas encore produites et ne doivent pas être précréées par cette phase 0.

`handoff/catalog.json` reste la référence stable publiée pour les seize premiers domaines et leurs 166 Feature Handoff Packages. La phase 0 ne régénère pas ce catalogue et ne modifie aucun package existant.

Le registre machine-readable de cette extension est `registry/domain-progress/extension-16-35.yaml`.

## Sources autoritatives

La préparation et les futures finalisations verticales utilisent uniquement les sources du dépôt :

- `maths/README.md` ;
- le README et les documents scientifiques de chaque domaine `16–35` ;
- `maths/integration/synthesis-and-supreme-integration.md` ;
- `maths/integration/towards-implementation.md` ;
- `maths/integration/tl-as-a-general-theory.md` ;
- les artefacts finalisés des domaines `00–15` comme conventions de production et de validation.

Les références historiques communes à plusieurs domaines peuvent motiver une analyse conjointe, mais ne constituent pas à elles seules une dépendance scientifique, runtime ou de contrat partagé.

## Conventions réutilisées

La production `16–35` conserve les conventions observées dans les domaines existants, notamment `00-master`, `01-disciple`, `02-community`, `08-principle` et `15-relations` :

- slugs de domaine stables et chemins de sources relatifs au dépôt ;
- identifiants de fonctionnalités attribués uniquement après la décomposition fonctionnelle ;
- population fonctionnelle autoritative figée avant la finalisation aval ;
- finalisation par domaine sous `registry/domain-finalization/<slug>/` ;
- IR finalisées sous `registry/optimized-ir/<slug>/<FEATURE_ID>/` ;
- algorithmes sous `registry/algorithms/<slug>/<FEATURE_ID>/` uniquement lorsque la théorie permet une procédure exploitable ;
- oracles sous `registry/oracles/<slug>/<FEATURE_ID>/` avec critères d’acceptation explicites ;
- conservation des ambiguïtés, valeurs opaques et réserves scientifiques au lieu de les résoudre silencieusement ;
- catalogue complet de domaine sous `handoff/domains/<slug>/catalog.json` avant publication de sa population ;
- Feature Handoff Packages autonomes, traçables, déterministes et validables sans lecture de toute la théorie ;
- validation handoff par `tools/handoff/validate_handoff.py` et export déterministe par `tools/handoff/export_bundle.py` lorsque le domaine atteint la porte de publication.

## Stratégie retenue

```text
Infrastructure commune minimale
        ↓
Domaine 16 Cohorte complet
        ↓
Domaines suivants par vagues
        ↓
Un domaine terminé jusqu’aux handoffs avant le suivant
        ↓
Finalisation globale 00–35
```

La stratégie est une **finalisation verticale complète domaine par domaine, organisée en vagues de dépendances**. Les vagues servent à ordonner l’analyse et la production ; elles ne constituent pas une nouvelle affirmation scientifique.

Une branche et une PR de production sont utilisées par domaine. Des domaines liés peuvent être analysés ensemble pour clarifier leurs dépendances, mais leur finalisation et leur fusion restent séparées.

## Définition de « domaine terminé »

Un domaine est terminé seulement lorsque toutes les couches suivantes sont présentes et validées :

```text
Théorie scientifique
Découpage fonctionnel
Registres
IR
Contrats
Algorithmes lorsque possibles
Oracles
Handoff Packages
Catalogue du domaine
Exports déterministes
```

La présence d’une source scientifique seule, d’un inventaire partiel ou d’un package vide ne constitue jamais une finalisation.

## Portes de validation

### Porte scientifique

La porte scientifique exige :

- une source complète et traçable ;
- un inventaire des symboles et objets utiles à la décomposition ;
- la conservation explicite des ambiguïtés, contradictions et éléments non résolus ;
- aucune définition, dépendance, dimension, équation ou procédure inventée pour combler un manque de la théorie.

### Porte fonctionnelle

La porte fonctionnelle exige :

- des fonctionnalités autonomes, compréhensibles et testables ;
- des identifiants stables attribués après le découpage scientifique ;
- des dépendances explicites et classées ;
- un nombre de fonctionnalités figé et justifié par l’inventaire retenu ;
- aucune fonctionnalité artificielle créée uniquement pour remplir une couche technique.

Avant cette porte, `feature_count` reste non déterminé.

### Porte IR et contrats

Pour chaque fonctionnalité retenue, la porte IR et contrats exige au minimum :

- entrées ;
- sorties ;
- types ;
- préconditions ;
- postconditions ;
- invariants ;
- erreurs ;
- cas limites ;
- traçabilité vers la source scientifique et les décisions de découpage.

Les informations non spécifiées restent non spécifiées. Une valeur opaque ou une réservation scientifique ne reçoit pas de valeur par défaut inventée.

### Porte algorithmes et oracles

Un algorithme est produit uniquement lorsque la théorie définit une procédure exploitable ou autorise explicitement une procédure structurelle. Une fonctionnalité déclarative peut disposer d’un contrat et d’un oracle sans imposer un algorithme scientifique inexistant.

Toute fonctionnalité implémentable doit disposer d’un oracle. Le type d’oracle doit être explicite : exact, structurel, propriété, métamorphique, différentiel, de conservation, ou autre catégorie effectivement justifiée par la fonctionnalité.

Un oracle ne transforme pas une ambiguïté scientifique en résultat supposé.

### Porte handoff

Chaque package handoff doit être autonome et contenir suffisamment d’information pour qu’un contributeur puisse implémenter la fonctionnalité sans lire toute la théorie. La porte exige :

- traçabilité complète ;
- contrat exploitable ;
- critères d’acceptation ;
- erreurs et cas limites ;
- dépendances résolues ou explicitement bloquantes ;
- conservation des réserves scientifiques ;
- aucun placeholder ou package vide.

Une fonctionnalité bloquée scientifiquement ne doit pas être présentée comme prête à l’implémentation.

### Porte de publication

Un domaine entre dans la publication globale uniquement lorsque :

- toutes les fonctionnalités retenues sont finalisées ;
- la traçabilité est complète ;
- les contrats sont complets ;
- les oracles sont présents et cohérents ;
- les validations handoff réussissent ;
- le catalogue du domaine est complet et valide ;
- les exports sont déterministes.

Un domaine incomplet ne doit pas entrer dans `handoff/catalog.json`. Aucun package vide ou placeholder ne doit être publié. Le catalogue global ne doit pas être régénéré lorsqu’aucun nouveau domaine finalisé n’est publié.

## Politique des dépendances

Les dépendances sont classées séparément :

- **analyse** : rapprochement opérationnel pour étudier ensemble des domaines liés ;
- **scientifique** : une définition, une procédure ou un objet d’un domaine dépend explicitement d’un autre texte scientifique ;
- **runtime** : une fonctionnalité exécutable requiert réellement un composant d’un autre domaine ;
- **contrat partagé** : plusieurs fonctionnalités ont démontré un besoin commun d’interface ou de type partagé.

Une dépendance est `confirmed` seulement lorsqu’une source ou un registre existant fournit une référence explicite. Une proximité thématique ou une origine `.tex` commune ne suffit pas. Une dépendance plausible mais non établie reste `provisional`, et une dépendance non connue reste inconnue.

Le graphe de la phase 0 est volontairement provisoire. Il contient uniquement les liens confirmés inspectés et les groupes d’analyse imposés par la stratégie. Il sera affiné pendant la finalisation verticale de chaque domaine sans modifier rétroactivement les 166 packages existants.

## Ordre des vagues

### Pilote

- `16 — Cohorte`

### Vague 1 — Fondations temporelles et contextuelles

- `22 — Temporalité`
- `23 — Mémoire`
- `24 — Contexte`
- `25 — Culture`
- `26 — Identité`
- `27 — Réflexivité`

Groupes d’analyse : `22 + 23`, `24 + 25`, `26 + 27`.

### Vague 2 — Mesure, contrôle et fidélité

- `18 — Évaluation`
- `19 — Régulation`
- `20 — Robustesse`
- `21 — Équité`
- `32 — Dérive et correction`
- `35 — Fidélité au noyau invariant`

Groupes d’analyse : `18 + 19`, `20 + 21`, `32 + 35`.

Les domaines 32 et 35 renvoient explicitement à `04-invariants` dans leurs textes scientifiques. Ce lien est enregistré comme dépendance scientifique confirmée, sans créer de dépendance runtime ou de contrat partagé par anticipation.

### Vague 3 — Finalité et propagation à grande échelle

- `28 — Finalité et téléologie évolutive`
- `29 — Propagation générationnelle`
- `30 — Expansion`
- `31 — Institutionnalisation`

Le groupe `29 + 30 + 31` partage une analyse de dépendances. Chaque domaine reste finalisé et fusionné séparément. Le texte d’Expansion renvoie explicitement au graphe défini par Propagation générationnelle ; ce lien scientifique est enregistré sans déduire d’autres dépendances du seul historique de sources communes.

### Vague 4 — Orchestration de la transmission

- `17 — Transmission en cascade`
- `34 — Cycle de transmission`

### Vague 5 — Architecture spécialisée

- `33 — Architecture pour environnements à faibles données`

Chaque index `16–35` appartient à une seule vague.

## Politique de publication progressive

1. Un domaine incomplet ne doit pas entrer dans `handoff/catalog.json`.
2. Aucun package vide ou placeholder ne doit être publié.
3. Un domaine entre dans le catalogue uniquement lorsque toutes ses fonctionnalités retenues sont finalisées, traçables, contractées, munies d’oracles, validées et exportables de manière déterministe.
4. Les domaines liés peuvent être analysés ensemble, mais sont fusionnés séparément.
5. Une branche et une PR de production sont utilisées par domaine.
6. Les contrats partagés ne sont ajoutés que lorsqu’un besoin réel est démontré.
7. Un algorithme n’est produit que lorsque la théorie définit une procédure exploitable.
8. Une fonctionnalité déclarative peut avoir un contrat et un oracle sans imposer un algorithme.
9. Les ambiguïtés scientifiques sont conservées et documentées.
10. Une fonctionnalité bloquée scientifiquement n’est pas transformée en tâche d’implémentation prétendument prête.

## Validation de la phase 0

`tools/domain-progress/validate_extension_16_35.py` valide uniquement le registre de pilotage et les garde-fous de cette phase. Il ne finalise aucun domaine et ne génère aucun artefact aval.

Le validateur contrôle :

- les 20 domaines et la couverture exacte `16–35` ;
- l’unicité des indices et des slugs ;
- l’existence des sources scientifiques déclarées ;
- l’appartenance unique à une vague ;
- la cohérence des groupes d’analyse ;
- l’absence de nombre de fonctionnalités fixé ;
- la publication handoff désactivée ;
- les couches aval à `not_started` ;
- l’absence d’identifiant de fonctionnalité futur instancié dans le manifeste ;
- l’absence de domaine futur ou d’identifiant futur dans le catalogue handoff global.

Aucun workflow GitHub Actions temporaire n’est ajouté. Les checks GitHub existants restent l’autorité CI disponible sur la PR.

## Prochaine action

La prochaine PR de production est :

**Domaine 16 — Cohorte : chaîne complète jusqu’aux Handoff Packages**

En anglais pour le handoff de production :

`Domain 16 — Cohort, complete vertical pipeline to validated Handoff Packages.`
