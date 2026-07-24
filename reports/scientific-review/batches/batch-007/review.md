# batch-007 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0002

### Identité

- decision_id : `TLC-HR-0002`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0002 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-051`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-090`
- Objets : `TLC-SO-CAPACITIES-051`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-090`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/11-capacities.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: activatibilite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Operator]}
- TLC-SO-CAPACITIES-051 — Activatibilité (Operator), référence maths/11-capacities.md:27
- TLC-SO-HUIT-DIMENSIONS-DE-TL-090 — Activatibilité (Operator), référence maths/03-huit-dimensions-de-tl.md:173
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-051`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-090`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-051, TLC-SO-HUIT-DIMENSIONS-DE-TL-090
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-051, TLC-SO-HUIT-DIMENSIONS-DE-TL-090
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-051, TLC-SO-HUIT-DIMENSIONS-DE-TL-090
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0128

### Identité

- decision_id : `TLC-HR-0128`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0128 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-052`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-091`
- Objets : `TLC-SO-CAPACITIES-052`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-091`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/11-capacities.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: structuralite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-052 — Structuralité (Concept), référence maths/11-capacities.md:28
- TLC-SO-HUIT-DIMENSIONS-DE-TL-091 — Structuralité (Concept), référence maths/03-huit-dimensions-de-tl.md:174
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0128`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-052`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-091`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-052, TLC-SO-HUIT-DIMENSIONS-DE-TL-091
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-052, TLC-SO-HUIT-DIMENSIONS-DE-TL-091
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-052, TLC-SO-HUIT-DIMENSIONS-DE-TL-091
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0130

### Identité

- decision_id : `TLC-HR-0130`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0130 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-054`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-093`
- Objets : `TLC-SO-CAPACITIES-054`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-093`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/11-capacities.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: structure riemannienne
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Metric]}
- TLC-SO-CAPACITIES-054 — Structure riemannienne (Metric), référence maths/11-capacities.md:30
- TLC-SO-HUIT-DIMENSIONS-DE-TL-093 — Structure riemannienne (Metric), référence maths/03-huit-dimensions-de-tl.md:176
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0130`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-054`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-093`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-054, TLC-SO-HUIT-DIMENSIONS-DE-TL-093
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-054, TLC-SO-HUIT-DIMENSIONS-DE-TL-093
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-054, TLC-SO-HUIT-DIMENSIONS-DE-TL-093
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0063

### Identité

- decision_id : `TLC-HR-0063`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0063 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-053`, `TLC-SO-COMPETENCIES-057`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-092`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-100`
- Objets : `TLC-SO-CAPACITIES-053`, `TLC-SO-COMPETENCIES-057`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-092`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-100`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: evolutivite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-053 — Évolutivité (Concept), référence maths/11-capacities.md:29
- TLC-SO-COMPETENCIES-057 — Évolutivité (Concept), référence maths/12-competencies.md:40
- TLC-SO-HUIT-DIMENSIONS-DE-TL-092 — Évolutivité (Concept), référence maths/03-huit-dimensions-de-tl.md:175
- TLC-SO-HUIT-DIMENSIONS-DE-TL-100 — Évolutivité (Concept), référence maths/03-huit-dimensions-de-tl.md:208
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0063`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-053`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-057`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-092`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-100`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-053, TLC-SO-COMPETENCIES-057, TLC-SO-HUIT-DIMENSIONS-DE-TL-092, TLC-SO-HUIT-DIMENSIONS-DE-TL-100
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-053, TLC-SO-COMPETENCIES-057, TLC-SO-HUIT-DIMENSIONS-DE-TL-092, TLC-SO-HUIT-DIMENSIONS-DE-TL-100
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-053, TLC-SO-COMPETENCIES-057, TLC-SO-HUIT-DIMENSIONS-DE-TL-092, TLC-SO-HUIT-DIMENSIONS-DE-TL-100
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0036

### Identité

- decision_id : `TLC-HR-0036`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0036 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-058`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-101`
- Objets : `TLC-SO-COMPETENCIES-058`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-101`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: demontrabilite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-058 — Démontrabilité (Concept), référence maths/12-competencies.md:41
- TLC-SO-HUIT-DIMENSIONS-DE-TL-101 — Démontrabilité (Concept), référence maths/03-huit-dimensions-de-tl.md:209
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0036`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-058`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-101`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-058, TLC-SO-HUIT-DIMENSIONS-DE-TL-101
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-058, TLC-SO-HUIT-DIMENSIONS-DE-TL-101
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-058, TLC-SO-HUIT-DIMENSIONS-DE-TL-101
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0086

### Identité

- decision_id : `TLC-HR-0086`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0086 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-105`, `TLC-SO-PRACTICE-053`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-105`, `TLC-SO-PRACTICE-053`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: intentionnalite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-105 — Intentionnalité (Concept), référence maths/03-huit-dimensions-de-tl.md:229
- TLC-SO-PRACTICE-053 — Intentionnalité (Concept), référence maths/13-practice.md:28
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0086`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-105`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-053`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-105, TLC-SO-PRACTICE-053
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-105, TLC-SO-PRACTICE-053
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-105, TLC-SO-PRACTICE-053
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0123

### Identité

- decision_id : `TLC-HR-0123`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0123 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-104`, `TLC-SO-PRACTICE-052`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-104`, `TLC-SO-PRACTICE-052`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: situativite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-104 — Situativité (Concept), référence maths/03-huit-dimensions-de-tl.md:228
- TLC-SO-PRACTICE-052 — Situativité (Concept), référence maths/13-practice.md:27
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0123`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-104`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-052`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-104, TLC-SO-PRACTICE-052
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-104, TLC-SO-PRACTICE-052
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-104, TLC-SO-PRACTICE-052
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0124

### Identité

- decision_id : `TLC-HR-0124`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0124 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-107`, `TLC-SO-PRACTICE-055`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-107`, `TLC-SO-PRACTICE-055`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: socialite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-107 — Socialité (Concept), référence maths/03-huit-dimensions-de-tl.md:231
- TLC-SO-PRACTICE-055 — Socialité (Concept), référence maths/13-practice.md:30
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0124`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-107`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-055`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-107, TLC-SO-PRACTICE-055
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-107, TLC-SO-PRACTICE-055
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-107, TLC-SO-PRACTICE-055
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0079

### Identité

- decision_id : `TLC-HR-0079`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0079 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-103`, `TLC-SO-PRACTICE-051`, `TLC-SO-RELATIONS-034`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-103`, `TLC-SO-PRACTICE-051`, `TLC-SO-RELATIONS-034`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/13-practice.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: incarnation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-103 — Incarnation (Concept), référence maths/03-huit-dimensions-de-tl.md:227
- TLC-SO-PRACTICE-051 — Incarnation (Concept), référence maths/13-practice.md:26
- TLC-SO-RELATIONS-034 — Incarnation (Concept), référence maths/15-relations.md:20
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0079`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-103`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-051`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-034`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-103, TLC-SO-PRACTICE-051, TLC-SO-RELATIONS-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-103, TLC-SO-PRACTICE-051, TLC-SO-RELATIONS-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-103, TLC-SO-PRACTICE-051, TLC-SO-RELATIONS-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0080

### Identité

- decision_id : `TLC-HR-0080`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0080 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-114`, `TLC-SO-LIVED-EXPERIENCE-048`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-114`, `TLC-SO-LIVED-EXPERIENCE-048`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: incorporation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-114 — Incorporation (Concept), référence maths/03-huit-dimensions-de-tl.md:255
- TLC-SO-LIVED-EXPERIENCE-048 — Incorporation (Concept), référence maths/14-lived-experience.md:28
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0080`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-114`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-048`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-114, TLC-SO-LIVED-EXPERIENCE-048
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-114, TLC-SO-LIVED-EXPERIENCE-048
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-114, TLC-SO-LIVED-EXPERIENCE-048
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0133

### Identité

- decision_id : `TLC-HR-0133`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0133 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-110`, `TLC-SO-LIVED-EXPERIENCE-044`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-110`, `TLC-SO-LIVED-EXPERIENCE-044`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: synthese temporelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Invariant]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-110 — Synthèse temporelle (Invariant), référence maths/03-huit-dimensions-de-tl.md:251
- TLC-SO-LIVED-EXPERIENCE-044 — Synthèse temporelle (Invariant), référence maths/14-lived-experience.md:24
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0133`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-110`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-044`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-110, TLC-SO-LIVED-EXPERIENCE-044
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-110, TLC-SO-LIVED-EXPERIENCE-044
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-110, TLC-SO-LIVED-EXPERIENCE-044
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```

## TLC-HR-0035

### Identité

- decision_id : `TLC-HR-0035`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0035 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-002`, `TLC-SO-COMPETENCIES-002`, `TLC-SO-LIVED-EXPERIENCE-002`, `TLC-SO-MESSAGE-003`, `TLC-SO-PRACTICE-002`, `TLC-SO-VALUES-002`, `TLC-SO-VIRTUES-002`
- Objets : `TLC-SO-CAPACITIES-002`, `TLC-SO-COMPETENCIES-002`, `TLC-SO-LIVED-EXPERIENCE-002`, `TLC-SO-MESSAGE-003`, `TLC-SO-PRACTICE-002`, `TLC-SO-VALUES-002`, `TLC-SO-VIRTUES-002`
- Relations : aucune
- Termes : aucun
- Sources : `maths/07-message.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: definition formelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Definition]}
- TLC-SO-CAPACITIES-002 — Définition formelle (Definition), référence maths/11-capacities.md:9
- TLC-SO-COMPETENCIES-002 — Définition formelle (Definition), référence maths/12-competencies.md:9
- TLC-SO-LIVED-EXPERIENCE-002 — Définition formelle (Definition), référence maths/14-lived-experience.md:9
- TLC-SO-MESSAGE-003 — Définition formelle (Definition), référence maths/07-message.md:7
- TLC-SO-PRACTICE-002 — Définition formelle (Definition), référence maths/13-practice.md:9
- TLC-SO-VALUES-002 — Définition formelle (Definition), référence maths/09-values.md:9
- TLC-SO-VIRTUES-002 — Définition formelle (Definition), référence maths/10-virtues.md:9
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0035`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-002`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-002, TLC-SO-COMPETENCIES-002, TLC-SO-LIVED-EXPERIENCE-002, TLC-SO-MESSAGE-003, TLC-SO-PRACTICE-002, TLC-SO-VALUES-002, TLC-SO-VIRTUES-002
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-002, TLC-SO-COMPETENCIES-002, TLC-SO-LIVED-EXPERIENCE-002, TLC-SO-MESSAGE-003, TLC-SO-PRACTICE-002, TLC-SO-VALUES-002, TLC-SO-VIRTUES-002
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-002, TLC-SO-COMPETENCIES-002, TLC-SO-LIVED-EXPERIENCE-002, TLC-SO-MESSAGE-003, TLC-SO-PRACTICE-002, TLC-SO-VALUES-002, TLC-SO-VIRTUES-002
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`merge_candidate` — reprise de l’audit, non normative.

### Décision humaine

```yaml
decision:
  status: pending
  selected_option: null
  decided_by: null
  decided_at: null
  justification: null
  reservations: []
  follow_up_actions: []
```
