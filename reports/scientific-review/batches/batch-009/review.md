# batch-009 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0054

### Identité

- decision_id : `TLC-HR-0054`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0054 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-033`, `TLC-SO-RELATIONS-047`, `TLC-SO-RELATIONS-048`, `TLC-SO-RELATIONS-064`, `TLC-SO-RELATIONS-077`, `TLC-SO-RELATIONS-088`, `TLC-SO-RELATIONS-100`
- Objets : `TLC-SO-PRINCIPLE-033`, `TLC-SO-RELATIONS-047`, `TLC-SO-RELATIONS-048`, `TLC-SO-RELATIONS-064`, `TLC-SO-RELATIONS-077`, `TLC-SO-RELATIONS-088`, `TLC-SO-RELATIONS-100`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation formalisation mathematique
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Equation]}
- TLC-SO-PRINCIPLE-033 — Équation — Formalisation mathématique (Equation), référence maths/08-principle.md:23
- TLC-SO-RELATIONS-047 — Équation — Formalisation mathématique (Equation), référence maths/15-relations.md:56
- TLC-SO-RELATIONS-048 — Équation — Formalisation mathématique (Equation), référence maths/15-relations.md:69
- TLC-SO-RELATIONS-064 — Équation — Formalisation mathématique (Equation), référence maths/15-relations.md:101
- TLC-SO-RELATIONS-077 — Équation — Formalisation mathématique (Equation), référence maths/15-relations.md:145
- TLC-SO-RELATIONS-088 — Équation — Formalisation mathématique (Equation), référence maths/15-relations.md:185
- TLC-SO-RELATIONS-100 — Équation — Formalisation mathématique (Equation), référence maths/15-relations.md:226
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0054`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-033`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-047`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-048`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-064`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-077`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-088`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-100`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-033, TLC-SO-RELATIONS-047, TLC-SO-RELATIONS-048, TLC-SO-RELATIONS-064, TLC-SO-RELATIONS-077, TLC-SO-RELATIONS-088, TLC-SO-RELATIONS-100
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-033, TLC-SO-RELATIONS-047, TLC-SO-RELATIONS-048, TLC-SO-RELATIONS-064, TLC-SO-RELATIONS-077, TLC-SO-RELATIONS-088, TLC-SO-RELATIONS-100
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-033, TLC-SO-RELATIONS-047, TLC-SO-RELATIONS-048, TLC-SO-RELATIONS-064, TLC-SO-RELATIONS-077, TLC-SO-RELATIONS-088, TLC-SO-RELATIONS-100
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

## TLC-HR-0011

### Identité

- decision_id : `TLC-HR-0011`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0011 ?

### Éléments concernés

- Identifiants : `TLC-SO-VALUES-083`, `TLC-SO-VIRTUES-123`
- Objets : `TLC-SO-VALUES-083`, `TLC-SO-VIRTUES-123`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: authenticite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-VALUES-083 — Authenticité (Concept), référence maths/09-values.md:119
- TLC-SO-VIRTUES-123 — Authenticité (Concept), référence maths/10-virtues.md:132
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0011`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-083`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-123`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-VALUES-083, TLC-SO-VIRTUES-123
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-VALUES-083, TLC-SO-VIRTUES-123
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-VALUES-083, TLC-SO-VIRTUES-123
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

## TLC-HR-0021

### Identité

- decision_id : `TLC-HR-0021`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0021 ?

### Éléments concernés

- Identifiants : `TLC-SO-VALUES-078`, `TLC-SO-VIRTUES-119`
- Objets : `TLC-SO-VALUES-078`, `TLC-SO-VIRTUES-119`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: consistance
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-VALUES-078 — Consistance (Concept), référence maths/09-values.md:112
- TLC-SO-VIRTUES-119 — Consistance (Concept), référence maths/10-virtues.md:126
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0021`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-078`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-119`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-VALUES-078, TLC-SO-VIRTUES-119
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-VALUES-078, TLC-SO-VIRTUES-119
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-VALUES-078, TLC-SO-VIRTUES-119
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

## TLC-HR-0039

### Identité

- decision_id : `TLC-HR-0039`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0039 ?

### Éléments concernés

- Identifiants : `TLC-SO-VALUES-065`, `TLC-SO-VIRTUES-108`
- Objets : `TLC-SO-VALUES-065`, `TLC-SO-VIRTUES-108`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: dialogue
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-VALUES-065 — Dialogue (Concept), référence maths/09-values.md:79
- TLC-SO-VIRTUES-108 — Dialogue (Concept), référence maths/10-virtues.md:107
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0039`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-065`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-108`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-VALUES-065, TLC-SO-VIRTUES-108
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-VALUES-065, TLC-SO-VIRTUES-108
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-VALUES-065, TLC-SO-VIRTUES-108
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

## TLC-HR-0012

### Identité

- decision_id : `TLC-HR-0012`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0012 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-085`, `TLC-SO-COMPETENCIES-090`, `TLC-SO-VALUES-088`, `TLC-SO-VIRTUES-129`
- Objets : `TLC-SO-CAPACITIES-085`, `TLC-SO-COMPETENCIES-090`, `TLC-SO-VALUES-088`, `TLC-SO-VIRTUES-129`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: auto evaluation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-085 — Auto‑évaluation (Concept), référence maths/11-capacities.md:145
- TLC-SO-COMPETENCIES-090 — Auto‑évaluation (Concept), référence maths/12-competencies.md:152
- TLC-SO-VALUES-088 — Auto‑évaluation (Concept), référence maths/09-values.md:126
- TLC-SO-VIRTUES-129 — Auto‑évaluation (Concept), référence maths/10-virtues.md:140
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0012`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-085`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-090`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-088`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-129`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-085, TLC-SO-COMPETENCIES-090, TLC-SO-VALUES-088, TLC-SO-VIRTUES-129
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-085, TLC-SO-COMPETENCIES-090, TLC-SO-VALUES-088, TLC-SO-VIRTUES-129
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-085, TLC-SO-COMPETENCIES-090, TLC-SO-VALUES-088, TLC-SO-VIRTUES-129
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

## TLC-HR-0061

### Identité

- decision_id : `TLC-HR-0061`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0061 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-083`, `TLC-SO-COMPETENCIES-088`, `TLC-SO-VALUES-086`, `TLC-SO-VIRTUES-127`
- Objets : `TLC-SO-CAPACITIES-083`, `TLC-SO-COMPETENCIES-088`, `TLC-SO-VALUES-086`, `TLC-SO-VIRTUES-127`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: evaluation par les pairs
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-083 — Évaluation par les pairs (Concept), référence maths/11-capacities.md:143
- TLC-SO-COMPETENCIES-088 — Évaluation par les pairs (Concept), référence maths/12-competencies.md:150
- TLC-SO-VALUES-086 — Évaluation par les pairs (Concept), référence maths/09-values.md:124
- TLC-SO-VIRTUES-127 — Évaluation par les pairs (Concept), référence maths/10-virtues.md:138
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0061`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-083`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-088`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-086`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-127`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-083, TLC-SO-COMPETENCIES-088, TLC-SO-VALUES-086, TLC-SO-VIRTUES-127
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-083, TLC-SO-COMPETENCIES-088, TLC-SO-VALUES-086, TLC-SO-VIRTUES-127
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-083, TLC-SO-COMPETENCIES-088, TLC-SO-VALUES-086, TLC-SO-VIRTUES-127
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

## TLC-HR-0135

### Identité

- decision_id : `TLC-HR-0135`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0135 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-082`, `TLC-SO-COMPETENCIES-087`, `TLC-SO-VALUES-085`, `TLC-SO-VIRTUES-126`
- Objets : `TLC-SO-CAPACITIES-082`, `TLC-SO-COMPETENCIES-087`, `TLC-SO-VALUES-085`, `TLC-SO-VIRTUES-126`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: tests situationnels
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-082 — Tests situationnels (Concept), référence maths/11-capacities.md:142
- TLC-SO-COMPETENCIES-087 — Tests situationnels (Concept), référence maths/12-competencies.md:149
- TLC-SO-VALUES-085 — Tests situationnels (Concept), référence maths/09-values.md:123
- TLC-SO-VIRTUES-126 — Tests situationnels (Concept), référence maths/10-virtues.md:137
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0135`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-082`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-087`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-085`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-126`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-082, TLC-SO-COMPETENCIES-087, TLC-SO-VALUES-085, TLC-SO-VIRTUES-126
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-082, TLC-SO-COMPETENCIES-087, TLC-SO-VALUES-085, TLC-SO-VIRTUES-126
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-082, TLC-SO-COMPETENCIES-087, TLC-SO-VALUES-085, TLC-SO-VIRTUES-126
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

## TLC-HR-0104

### Identité

- decision_id : `TLC-HR-0104`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0104 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-033`, `TLC-SO-COMPETENCIES-034`, `TLC-SO-LIVED-EXPERIENCE-028`, `TLC-SO-PRACTICE-033`, `TLC-SO-VALUES-028`, `TLC-SO-VIRTUES-036`
- Objets : `TLC-SO-CAPACITIES-033`, `TLC-SO-COMPETENCIES-034`, `TLC-SO-LIVED-EXPERIENCE-028`, `TLC-SO-PRACTICE-033`, `TLC-SO-VALUES-028`, `TLC-SO-VIRTUES-036`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: moteurs motivationnels et engagement
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-033 — Moteurs motivationnels et engagement (Concept), référence maths/11-capacities.md:189
- TLC-SO-COMPETENCIES-034 — Moteurs motivationnels et engagement (Concept), référence maths/12-competencies.md:198
- TLC-SO-LIVED-EXPERIENCE-028 — Moteurs motivationnels et engagement (Concept), référence maths/14-lived-experience.md:120
- TLC-SO-PRACTICE-033 — Moteurs motivationnels et engagement (Concept), référence maths/13-practice.md:171
- TLC-SO-VALUES-028 — Moteurs motivationnels et engagement (Concept), référence maths/09-values.md:172
- TLC-SO-VIRTUES-036 — Moteurs motivationnels et engagement (Concept), référence maths/10-virtues.md:200
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0104`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-033`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-034`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-028`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-033`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-028`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-036`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-033, TLC-SO-COMPETENCIES-034, TLC-SO-LIVED-EXPERIENCE-028, TLC-SO-PRACTICE-033, TLC-SO-VALUES-028, TLC-SO-VIRTUES-036
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-033, TLC-SO-COMPETENCIES-034, TLC-SO-LIVED-EXPERIENCE-028, TLC-SO-PRACTICE-033, TLC-SO-VALUES-028, TLC-SO-VIRTUES-036
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-033, TLC-SO-COMPETENCIES-034, TLC-SO-LIVED-EXPERIENCE-028, TLC-SO-PRACTICE-033, TLC-SO-VALUES-028, TLC-SO-VIRTUES-036
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

## TLC-HR-0093

### Identité

- decision_id : `TLC-HR-0093`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0093 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-084`, `TLC-SO-COMPETENCIES-089`, `TLC-SO-LIVED-EXPERIENCE-063`, `TLC-SO-VALUES-087`, `TLC-SO-VIRTUES-128`
- Objets : `TLC-SO-CAPACITIES-084`, `TLC-SO-COMPETENCIES-089`, `TLC-SO-LIVED-EXPERIENCE-063`, `TLC-SO-VALUES-087`, `TLC-SO-VIRTUES-128`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: jugement du maitre
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-084 — Jugement du Maître (Concept), référence maths/11-capacities.md:144
- TLC-SO-COMPETENCIES-089 — Jugement du Maître (Concept), référence maths/12-competencies.md:151
- TLC-SO-LIVED-EXPERIENCE-063 — Jugement du Maître (Concept), référence maths/14-lived-experience.md:93
- TLC-SO-VALUES-087 — Jugement du Maître (Concept), référence maths/09-values.md:125
- TLC-SO-VIRTUES-128 — Jugement du Maître (Concept), référence maths/10-virtues.md:139
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0093`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-084`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-089`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-063`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-087`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-128`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-084, TLC-SO-COMPETENCIES-089, TLC-SO-LIVED-EXPERIENCE-063, TLC-SO-VALUES-087, TLC-SO-VIRTUES-128
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-084, TLC-SO-COMPETENCIES-089, TLC-SO-LIVED-EXPERIENCE-063, TLC-SO-VALUES-087, TLC-SO-VIRTUES-128
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-084, TLC-SO-COMPETENCIES-089, TLC-SO-LIVED-EXPERIENCE-063, TLC-SO-VALUES-087, TLC-SO-VIRTUES-128
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

## TLC-HR-0112

### Identité

- decision_id : `TLC-HR-0112`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0112 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-024`, `TLC-SO-LIVED-EXPERIENCE-020`, `TLC-SO-VALUES-019`, `TLC-SO-VIRTUES-024`
- Objets : `TLC-SO-CAPACITIES-024`, `TLC-SO-LIVED-EXPERIENCE-020`, `TLC-SO-VALUES-019`, `TLC-SO-VIRTUES-024`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: procedures de validation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-024 — Procédures de validation (Concept), référence maths/11-capacities.md:141
- TLC-SO-LIVED-EXPERIENCE-020 — Procédures de validation (Concept), référence maths/14-lived-experience.md:90
- TLC-SO-VALUES-019 — Procédures de validation (Concept), référence maths/09-values.md:122
- TLC-SO-VIRTUES-024 — Procédures de validation (Concept), référence maths/10-virtues.md:136
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0112`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-024`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-020`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-019`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-024`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-024, TLC-SO-LIVED-EXPERIENCE-020, TLC-SO-VALUES-019, TLC-SO-VIRTUES-024
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-024, TLC-SO-LIVED-EXPERIENCE-020, TLC-SO-VALUES-019, TLC-SO-VIRTUES-024
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-024, TLC-SO-LIVED-EXPERIENCE-020, TLC-SO-VALUES-019, TLC-SO-VIRTUES-024
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

## TLC-HR-0101

### Identité

- decision_id : `TLC-HR-0101`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0101 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-023`, `TLC-SO-LIVED-EXPERIENCE-018`, `TLC-SO-PRACTICE-022`, `TLC-SO-VALUES-017`, `TLC-SO-VIRTUES-022`
- Objets : `TLC-SO-COMPETENCIES-023`, `TLC-SO-LIVED-EXPERIENCE-018`, `TLC-SO-PRACTICE-022`, `TLC-SO-VALUES-017`, `TLC-SO-VIRTUES-022`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: mesures quantitatives
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Metric]}
- TLC-SO-COMPETENCIES-023 — Mesures quantitatives (Metric), référence maths/12-competencies.md:133
- TLC-SO-LIVED-EXPERIENCE-018 — Mesures quantitatives (Metric), référence maths/14-lived-experience.md:80
- TLC-SO-PRACTICE-022 — Mesures quantitatives (Metric), référence maths/13-practice.md:117
- TLC-SO-VALUES-017 — Mesures quantitatives (Metric), référence maths/09-values.md:110
- TLC-SO-VIRTUES-022 — Mesures quantitatives (Metric), référence maths/10-virtues.md:124
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0101`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-023`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-018`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-022`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-017`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-022`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-023, TLC-SO-LIVED-EXPERIENCE-018, TLC-SO-PRACTICE-022, TLC-SO-VALUES-017, TLC-SO-VIRTUES-022
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-023, TLC-SO-LIVED-EXPERIENCE-018, TLC-SO-PRACTICE-022, TLC-SO-VALUES-017, TLC-SO-VIRTUES-022
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-023, TLC-SO-LIVED-EXPERIENCE-018, TLC-SO-PRACTICE-022, TLC-SO-VALUES-017, TLC-SO-VIRTUES-022
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

## TLC-HR-0059

### Identité

- decision_id : `TLC-HR-0059`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0059 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-099`, `TLC-SO-CAPACITIES-100`, `TLC-SO-COMPETENCIES-112`, `TLC-SO-COMPETENCIES-113`, `TLC-SO-VALUES-103`
- Objets : `TLC-SO-CAPACITIES-099`, `TLC-SO-CAPACITIES-100`, `TLC-SO-COMPETENCIES-112`, `TLC-SO-COMPETENCIES-113`, `TLC-SO-VALUES-103`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation theoremes fondamentaux
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Theorem]}
- TLC-SO-CAPACITIES-099 — Équation — Théorèmes fondamentaux (Theorem), référence maths/11-capacities.md:257
- TLC-SO-CAPACITIES-100 — Équation — Théorèmes fondamentaux (Theorem), référence maths/11-capacities.md:264
- TLC-SO-COMPETENCIES-112 — Équation — Théorèmes fondamentaux (Theorem), référence maths/12-competencies.md:284
- TLC-SO-COMPETENCIES-113 — Équation — Théorèmes fondamentaux (Theorem), référence maths/12-competencies.md:290
- TLC-SO-VALUES-103 — Équation — Théorèmes fondamentaux (Theorem), référence maths/09-values.md:244
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0059`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-099`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-100`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-112`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-113`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-103`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-099, TLC-SO-CAPACITIES-100, TLC-SO-COMPETENCIES-112, TLC-SO-COMPETENCIES-113, TLC-SO-VALUES-103
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-099, TLC-SO-CAPACITIES-100, TLC-SO-COMPETENCIES-112, TLC-SO-COMPETENCIES-113, TLC-SO-VALUES-103
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-099, TLC-SO-CAPACITIES-100, TLC-SO-COMPETENCIES-112, TLC-SO-COMPETENCIES-113, TLC-SO-VALUES-103
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
