# batch-008 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0050

### Identité

- decision_id : `TLC-HR-0050`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0050 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-045`, `TLC-SO-COMPETENCIES-047`, `TLC-SO-COMPETENCIES-053`, `TLC-SO-LIVED-EXPERIENCE-041`, `TLC-SO-MESSAGE-025`, `TLC-SO-PRACTICE-046`, `TLC-SO-VALUES-040`, `TLC-SO-VIRTUES-057`
- Objets : `TLC-SO-CAPACITIES-045`, `TLC-SO-COMPETENCIES-047`, `TLC-SO-COMPETENCIES-053`, `TLC-SO-LIVED-EXPERIENCE-041`, `TLC-SO-MESSAGE-025`, `TLC-SO-PRACTICE-046`, `TLC-SO-VALUES-040`, `TLC-SO-VIRTUES-057`
- Relations : aucune
- Termes : aucun
- Sources : `maths/07-message.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation definition formelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Definition]}
- TLC-SO-CAPACITIES-045 — Équation — Définition formelle (Definition), référence maths/11-capacities.md:13
- TLC-SO-COMPETENCIES-047 — Équation — Définition formelle (Definition), référence maths/12-competencies.md:13
- TLC-SO-COMPETENCIES-053 — Équation — Définition formelle (Definition), référence maths/12-competencies.md:26
- TLC-SO-LIVED-EXPERIENCE-041 — Équation — Définition formelle (Definition), référence maths/14-lived-experience.md:13
- TLC-SO-MESSAGE-025 — Équation — Définition formelle (Definition), référence maths/07-message.md:11
- TLC-SO-PRACTICE-046 — Équation — Définition formelle (Definition), référence maths/13-practice.md:13
- TLC-SO-VALUES-040 — Équation — Définition formelle (Definition), référence maths/09-values.md:13
- TLC-SO-VIRTUES-057 — Équation — Définition formelle (Definition), référence maths/10-virtues.md:15
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0050`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-045`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-047`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-053`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-041`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-025`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-046`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-040`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-057`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-045, TLC-SO-COMPETENCIES-047, TLC-SO-COMPETENCIES-053, TLC-SO-LIVED-EXPERIENCE-041, TLC-SO-MESSAGE-025, TLC-SO-PRACTICE-046, TLC-SO-VALUES-040, TLC-SO-VIRTUES-057
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-045, TLC-SO-COMPETENCIES-047, TLC-SO-COMPETENCIES-053, TLC-SO-LIVED-EXPERIENCE-041, TLC-SO-MESSAGE-025, TLC-SO-PRACTICE-046, TLC-SO-VALUES-040, TLC-SO-VIRTUES-057
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-045, TLC-SO-COMPETENCIES-047, TLC-SO-COMPETENCIES-053, TLC-SO-LIVED-EXPERIENCE-041, TLC-SO-MESSAGE-025, TLC-SO-PRACTICE-046, TLC-SO-VALUES-040, TLC-SO-VIRTUES-057
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

## TLC-HR-0120

### Identité

- decision_id : `TLC-HR-0120`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0120 ?

### Éléments concernés

- Identifiants : `TLC-SO-MESSAGE-044`, `TLC-SO-VIRTUES-120`
- Objets : `TLC-SO-MESSAGE-044`, `TLC-SO-VIRTUES-120`
- Relations : aucune
- Termes : aucun
- Sources : `maths/07-message.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: resistance
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-MESSAGE-044 — Résistance (Concept), référence maths/07-message.md:83
- TLC-SO-VIRTUES-120 — Résistance (Concept), référence maths/10-virtues.md:127
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0120`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-044`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-120`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-MESSAGE-044, TLC-SO-VIRTUES-120
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-MESSAGE-044, TLC-SO-VIRTUES-120
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-MESSAGE-044, TLC-SO-VIRTUES-120
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

## TLC-HR-0034

### Identité

- decision_id : `TLC-HR-0034`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0034 ?

### Éléments concernés

- Identifiants : `TLC-SO-MESSAGE-002`, `TLC-SO-RELATIONS-003`, `TLC-SO-RELATIONS-010`, `TLC-SO-RELATIONS-016`, `TLC-SO-RELATIONS-022`, `TLC-SO-RELATIONS-028`
- Objets : `TLC-SO-MESSAGE-002`, `TLC-SO-RELATIONS-003`, `TLC-SO-RELATIONS-010`, `TLC-SO-RELATIONS-016`, `TLC-SO-RELATIONS-022`, `TLC-SO-RELATIONS-028`
- Relations : aucune
- Termes : aucun
- Sources : `maths/07-message.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: definition et nature
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Definition]}
- TLC-SO-MESSAGE-002 — Définition et nature (Definition), référence maths/07-message.md:3
- TLC-SO-RELATIONS-003 — Définition et nature (Definition), référence maths/15-relations.md:11
- TLC-SO-RELATIONS-010 — Définition et nature (Definition), référence maths/15-relations.md:75
- TLC-SO-RELATIONS-016 — Définition et nature (Definition), référence maths/15-relations.md:118
- TLC-SO-RELATIONS-022 — Définition et nature (Definition), référence maths/15-relations.md:161
- TLC-SO-RELATIONS-028 — Définition et nature (Definition), référence maths/15-relations.md:201
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0034`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-010`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-016`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-022`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-028`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-MESSAGE-002, TLC-SO-RELATIONS-003, TLC-SO-RELATIONS-010, TLC-SO-RELATIONS-016, TLC-SO-RELATIONS-022, TLC-SO-RELATIONS-028
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-MESSAGE-002, TLC-SO-RELATIONS-003, TLC-SO-RELATIONS-010, TLC-SO-RELATIONS-016, TLC-SO-RELATIONS-022, TLC-SO-RELATIONS-028
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-MESSAGE-002, TLC-SO-RELATIONS-003, TLC-SO-RELATIONS-010, TLC-SO-RELATIONS-016, TLC-SO-RELATIONS-022, TLC-SO-RELATIONS-028
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

## TLC-HR-0138

### Identité

- decision_id : `TLC-HR-0138`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0138 ?

### Éléments concernés

- Identifiants : `TLC-SO-MESSAGE-042`, `TLC-SO-RELATIONS-068`
- Objets : `TLC-SO-MESSAGE-042`, `TLC-SO-RELATIONS-068`
- Relations : aucune
- Termes : aucun
- Sources : `maths/07-message.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: traduction
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-MESSAGE-042 — Traduction (Concept), référence maths/07-message.md:81
- TLC-SO-RELATIONS-068 — Traduction (Concept), référence maths/15-relations.md:125
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0138`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-042`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-068`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-MESSAGE-042, TLC-SO-RELATIONS-068
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-MESSAGE-042, TLC-SO-RELATIONS-068
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-MESSAGE-042, TLC-SO-RELATIONS-068
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

## TLC-HR-0068

### Identité

- decision_id : `TLC-HR-0068`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0068 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-019`, `TLC-SO-VALUES-015`
- Objets : `TLC-SO-PRINCIPLE-019`, `TLC-SO-VALUES-015`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: feedback et adaptation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRINCIPLE-019 — Feedback et adaptation (Concept), référence maths/08-principle.md:113
- TLC-SO-VALUES-015 — Feedback et adaptation (Concept), référence maths/09-values.md:100
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0068`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-019`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-015`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-019, TLC-SO-VALUES-015
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-019, TLC-SO-VALUES-015
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-019, TLC-SO-VALUES-015
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

## TLC-HR-0103

### Identité

- decision_id : `TLC-HR-0103`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0103 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-016`, `TLC-SO-VALUES-012`
- Objets : `TLC-SO-PRINCIPLE-016`, `TLC-SO-VALUES-012`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: modes de transmission
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRINCIPLE-016 — Modes de transmission (Concept), référence maths/08-principle.md:91
- TLC-SO-VALUES-012 — Modes de transmission (Concept), référence maths/09-values.md:73
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0103`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-016`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-012`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-016, TLC-SO-VALUES-012
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-016, TLC-SO-VALUES-012
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-016, TLC-SO-VALUES-012
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

## TLC-HR-0117

### Identité

- decision_id : `TLC-HR-0117`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0117 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-017`, `TLC-SO-VALUES-013`
- Objets : `TLC-SO-PRINCIPLE-017`, `TLC-SO-VALUES-013`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: reception et interpretation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [State]}
- TLC-SO-PRINCIPLE-017 — Réception et interprétation (State), référence maths/08-principle.md:98
- TLC-SO-VALUES-013 — Réception et interprétation (State), référence maths/09-values.md:84
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0117`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-017`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-013`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-017, TLC-SO-VALUES-013
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-017, TLC-SO-VALUES-013
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-017, TLC-SO-VALUES-013
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

## TLC-HR-0040

### Identité

- decision_id : `TLC-HR-0040`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0040 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-031`, `TLC-SO-COMPETENCIES-032`, `TLC-SO-LIVED-EXPERIENCE-026`, `TLC-SO-PRACTICE-031`, `TLC-SO-PRINCIPLE-030`, `TLC-SO-VALUES-026`, `TLC-SO-VIRTUES-034`
- Objets : `TLC-SO-CAPACITIES-031`, `TLC-SO-COMPETENCIES-032`, `TLC-SO-LIVED-EXPERIENCE-026`, `TLC-SO-PRACTICE-031`, `TLC-SO-PRINCIPLE-030`, `TLC-SO-VALUES-026`, `TLC-SO-VIRTUES-034`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: dimensions ethiques motivationnelles et cognitives
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-031 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/11-capacities.md:181
- TLC-SO-COMPETENCIES-032 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/12-competencies.md:190
- TLC-SO-LIVED-EXPERIENCE-026 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/14-lived-experience.md:115
- TLC-SO-PRACTICE-031 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/13-practice.md:162
- TLC-SO-PRINCIPLE-030 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/08-principle.md:218
- TLC-SO-VALUES-026 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/09-values.md:163
- TLC-SO-VIRTUES-034 — Dimensions éthiques, motivationnelles et cognitives (Concept), référence maths/10-virtues.md:192
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0040`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-032`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-030`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-034`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-031, TLC-SO-COMPETENCIES-032, TLC-SO-LIVED-EXPERIENCE-026, TLC-SO-PRACTICE-031, TLC-SO-PRINCIPLE-030, TLC-SO-VALUES-026, TLC-SO-VIRTUES-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-031, TLC-SO-COMPETENCIES-032, TLC-SO-LIVED-EXPERIENCE-026, TLC-SO-PRACTICE-031, TLC-SO-PRINCIPLE-030, TLC-SO-VALUES-026, TLC-SO-VIRTUES-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-031, TLC-SO-COMPETENCIES-032, TLC-SO-LIVED-EXPERIENCE-026, TLC-SO-PRACTICE-031, TLC-SO-PRINCIPLE-030, TLC-SO-VALUES-026, TLC-SO-VIRTUES-034
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

## TLC-HR-0118

### Identité

- decision_id : `TLC-HR-0118`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0118 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-063`, `TLC-SO-LIVED-EXPERIENCE-053`, `TLC-SO-PRACTICE-060`, `TLC-SO-PRINCIPLE-057`, `TLC-SO-VALUES-059`
- Objets : `TLC-SO-COMPETENCIES-063`, `TLC-SO-LIVED-EXPERIENCE-053`, `TLC-SO-PRACTICE-060`, `TLC-SO-PRINCIPLE-057`, `TLC-SO-VALUES-059`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: reconnaissance
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-063 — Reconnaissance (Concept), référence maths/12-competencies.md:51
- TLC-SO-LIVED-EXPERIENCE-053 — Reconnaissance (Concept), référence maths/14-lived-experience.md:38
- TLC-SO-PRACTICE-060 — Reconnaissance (Concept), référence maths/13-practice.md:40
- TLC-SO-PRINCIPLE-057 — Reconnaissance (Concept), référence maths/08-principle.md:101
- TLC-SO-VALUES-059 — Reconnaissance (Concept), référence maths/09-values.md:43
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0118`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-063`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-053`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-060`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-057`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-059`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-063, TLC-SO-LIVED-EXPERIENCE-053, TLC-SO-PRACTICE-060, TLC-SO-PRINCIPLE-057, TLC-SO-VALUES-059
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-063, TLC-SO-LIVED-EXPERIENCE-053, TLC-SO-PRACTICE-060, TLC-SO-PRINCIPLE-057, TLC-SO-VALUES-059
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-063, TLC-SO-LIVED-EXPERIENCE-053, TLC-SO-PRACTICE-060, TLC-SO-PRINCIPLE-057, TLC-SO-VALUES-059
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

## TLC-HR-0064

### Identité

- decision_id : `TLC-HR-0064`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0064 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRACTICE-058`, `TLC-SO-PRINCIPLE-076`, `TLC-SO-VALUES-057`
- Objets : `TLC-SO-PRACTICE-058`, `TLC-SO-PRINCIPLE-076`, `TLC-SO-VALUES-057`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: exemplification
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRACTICE-058 — Exemplification (Concept), référence maths/13-practice.md:38
- TLC-SO-PRINCIPLE-076 — Exemplification (Concept), référence maths/08-principle.md:160
- TLC-SO-VALUES-057 — Exemplification (Concept), référence maths/09-values.md:41
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0064`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-058`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-076`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-057`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRACTICE-058, TLC-SO-PRINCIPLE-076, TLC-SO-VALUES-057
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRACTICE-058, TLC-SO-PRINCIPLE-076, TLC-SO-VALUES-057
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRACTICE-058, TLC-SO-PRINCIPLE-076, TLC-SO-VALUES-057
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

## TLC-HR-0007

### Identité

- decision_id : `TLC-HR-0007`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0007 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-032`, `TLC-SO-PRINCIPLE-096`
- Objets : `TLC-SO-CAPACITIES-032`, `TLC-SO-PRINCIPLE-096`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/11-capacities.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: alignement avec les valeurs et vertus
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-032 — Alignement avec les Valeurs et Vertus (Concept), référence maths/11-capacities.md:183
- TLC-SO-PRINCIPLE-096 — Alignement avec les valeurs et vertus (Concept), référence maths/08-principle.md:222
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0007`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-032`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-096`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-032, TLC-SO-PRINCIPLE-096
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-032, TLC-SO-PRINCIPLE-096
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-032, TLC-SO-PRINCIPLE-096
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

## TLC-HR-0005

### Identité

- decision_id : `TLC-HR-0005`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0005 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-091`, `TLC-SO-RELATIONS-038`
- Objets : `TLC-SO-PRINCIPLE-091`, `TLC-SO-RELATIONS-038`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: adaptation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRINCIPLE-091 — adaptation (Concept), référence maths/08-principle.md:207
- TLC-SO-RELATIONS-038 — Adaptation (Concept), référence maths/15-relations.md:24
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-091`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-038`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-091, TLC-SO-RELATIONS-038
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-091, TLC-SO-RELATIONS-038
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-091, TLC-SO-RELATIONS-038
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
