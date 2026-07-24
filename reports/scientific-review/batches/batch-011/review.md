# batch-011 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0106

### Identité

- decision_id : `TLC-HR-0106`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0106 ?

### Éléments concernés

- Identifiants : `TLC-SO-LIVED-EXPERIENCE-035`, `TLC-SO-VALUES-035`
- Objets : `TLC-SO-LIVED-EXPERIENCE-035`, `TLC-SO-VALUES-035`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: normes et standards partages
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-LIVED-EXPERIENCE-035 — Normes et standards partagés (Concept), référence maths/14-lived-experience.md:146
- TLC-SO-VALUES-035 — Normes et standards partagés (Concept), référence maths/09-values.md:208
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0106`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-035`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-035`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-035, TLC-SO-VALUES-035
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-035, TLC-SO-VALUES-035
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-035, TLC-SO-VALUES-035
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

## TLC-HR-0043

### Identité

- decision_id : `TLC-HR-0043`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0043 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-026`, `TLC-SO-LIVED-EXPERIENCE-021`, `TLC-SO-VIRTUES-027`
- Objets : `TLC-SO-CAPACITIES-026`, `TLC-SO-LIVED-EXPERIENCE-021`, `TLC-SO-VIRTUES-027`
- Relations : aucune
- Termes : aucun
- Sources : `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: dynamique temporelle et developpementale
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-026 — Dynamique temporelle et développementale (Concept), référence maths/11-capacities.md:154
- TLC-SO-LIVED-EXPERIENCE-021 — Dynamique temporelle et développementale (Concept), référence maths/14-lived-experience.md:95
- TLC-SO-VIRTUES-027 — Dynamique temporelle et développementale (Concept), référence maths/10-virtues.md:154
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0043`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-021`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-027`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-026, TLC-SO-LIVED-EXPERIENCE-021, TLC-SO-VIRTUES-027
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-026, TLC-SO-LIVED-EXPERIENCE-021, TLC-SO-VIRTUES-027
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-026, TLC-SO-LIVED-EXPERIENCE-021, TLC-SO-VIRTUES-027
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

## TLC-HR-0119

### Identité

- decision_id : `TLC-HR-0119`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0119 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-080`, `TLC-SO-LIVED-EXPERIENCE-060`, `TLC-SO-VIRTUES-125`
- Objets : `TLC-SO-CAPACITIES-080`, `TLC-SO-LIVED-EXPERIENCE-060`, `TLC-SO-VIRTUES-125`
- Relations : aucune
- Termes : aucun
- Sources : `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: resilience
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-080 — Résilience (Concept), référence maths/11-capacities.md:138
- TLC-SO-LIVED-EXPERIENCE-060 — Résilience (Concept), référence maths/14-lived-experience.md:88
- TLC-SO-VIRTUES-125 — Résilience (Concept), référence maths/10-virtues.md:134
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0119`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-080`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-060`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-125`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-080, TLC-SO-LIVED-EXPERIENCE-060, TLC-SO-VIRTUES-125
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-080, TLC-SO-LIVED-EXPERIENCE-060, TLC-SO-VIRTUES-125
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-080, TLC-SO-LIVED-EXPERIENCE-060, TLC-SO-VIRTUES-125
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

## TLC-HR-0076

### Identité

- decision_id : `TLC-HR-0076`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0076 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRACTICE-078`, `TLC-SO-VIRTUES-118`
- Objets : `TLC-SO-PRACTICE-078`, `TLC-SO-VIRTUES-118`
- Relations : aucune
- Termes : aucun
- Sources : `maths/10-virtues.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: frequence
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRACTICE-078 — Fréquence (Concept), référence maths/13-practice.md:118
- TLC-SO-VIRTUES-118 — Fréquence (Concept), référence maths/10-virtues.md:125
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0076`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-078`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-118`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRACTICE-078, TLC-SO-VIRTUES-118
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRACTICE-078, TLC-SO-VIRTUES-118
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRACTICE-078, TLC-SO-VIRTUES-118
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

## TLC-HR-0122

### Identité

- decision_id : `TLC-HR-0122`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0122 ?

### Éléments concernés

- Identifiants : `TLC-SO-LIVED-EXPERIENCE-058`, `TLC-SO-VIRTUES-080`
- Objets : `TLC-SO-LIVED-EXPERIENCE-058`, `TLC-SO-VIRTUES-080`
- Relations : aucune
- Termes : aucun
- Sources : `maths/10-virtues.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: sagesse
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-LIVED-EXPERIENCE-058 — Sagesse (Concept), référence maths/14-lived-experience.md:86
- TLC-SO-VIRTUES-080 — Sagesse (Concept), référence maths/10-virtues.md:65
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0122`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-058`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-080`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-058, TLC-SO-VIRTUES-080
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-058, TLC-SO-VIRTUES-080
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-058, TLC-SO-VIRTUES-080
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

## TLC-HR-0057

### Identité

- decision_id : `TLC-HR-0057`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0057 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-090`, `TLC-SO-COMPETENCIES-099`
- Objets : `TLC-SO-CAPACITIES-090`, `TLC-SO-COMPETENCIES-099`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation progression vers la maitrise
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Constraint]}
- TLC-SO-CAPACITIES-090 — Équation — Progression vers la maîtrise (Constraint), référence maths/11-capacities.md:177
- TLC-SO-COMPETENCIES-099 — Équation — Progression vers la maîtrise (Constraint), référence maths/12-competencies.md:186
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0057`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-090`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-099`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-090, TLC-SO-COMPETENCIES-099
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-090, TLC-SO-COMPETENCIES-099
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-090, TLC-SO-COMPETENCIES-099
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

## TLC-HR-0134

### Identité

- decision_id : `TLC-HR-0134`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0134 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-077`, `TLC-SO-COMPETENCIES-081`
- Objets : `TLC-SO-CAPACITIES-077`, `TLC-SO-COMPETENCIES-081`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: taux d actualisation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-077 — Taux d’actualisation (Concept), référence maths/11-capacities.md:133
- TLC-SO-COMPETENCIES-081 — Taux d’actualisation (Concept), référence maths/12-competencies.md:137
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0134`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-077`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-081`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-077, TLC-SO-COMPETENCIES-081
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-077, TLC-SO-COMPETENCIES-081
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-077, TLC-SO-COMPETENCIES-081
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

## TLC-HR-0027

### Identité

- decision_id : `TLC-HR-0027`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0027 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-071`, `TLC-SO-COMPETENCIES-069`, `TLC-SO-PRACTICE-071`
- Objets : `TLC-SO-CAPACITIES-071`, `TLC-SO-COMPETENCIES-069`, `TLC-SO-PRACTICE-071`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: correction immediate
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-071 — Correction immédiate (Concept), référence maths/11-capacities.md:123
- TLC-SO-COMPETENCIES-069 — Correction immédiate (Concept), référence maths/12-competencies.md:101
- TLC-SO-PRACTICE-071 — Correction immédiate (Concept), référence maths/13-practice.md:91
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0027`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-071`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-069`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-071`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-071, TLC-SO-COMPETENCIES-069, TLC-SO-PRACTICE-071
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-071, TLC-SO-COMPETENCIES-069, TLC-SO-PRACTICE-071
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-071, TLC-SO-COMPETENCIES-069, TLC-SO-PRACTICE-071
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

## TLC-HR-0045

### Identité

- decision_id : `TLC-HR-0045`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0045 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-075`, `TLC-SO-COMPETENCIES-079`, `TLC-SO-PRACTICE-080`
- Objets : `TLC-SO-CAPACITIES-075`, `TLC-SO-COMPETENCIES-079`, `TLC-SO-PRACTICE-080`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: efficacite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-075 — Efficacité (Concept), référence maths/11-capacities.md:131
- TLC-SO-COMPETENCIES-079 — Efficacité (Concept), référence maths/12-competencies.md:135
- TLC-SO-PRACTICE-080 — Efficacité (Concept), référence maths/13-practice.md:120
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0045`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-075`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-079`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-080`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-075, TLC-SO-COMPETENCIES-079, TLC-SO-PRACTICE-080
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-075, TLC-SO-COMPETENCIES-079, TLC-SO-PRACTICE-080
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-075, TLC-SO-COMPETENCIES-079, TLC-SO-PRACTICE-080
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

## TLC-HR-0048

### Identité

- decision_id : `TLC-HR-0048`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0048 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-095`, `TLC-SO-COMPETENCIES-104`, `TLC-SO-PRACTICE-091`
- Objets : `TLC-SO-CAPACITIES-095`, `TLC-SO-COMPETENCIES-104`, `TLC-SO-PRACTICE-091`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation coherence et coordination entre disciples
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Equation]}
- TLC-SO-CAPACITIES-095 — Équation — Cohérence et coordination entre Disciples (Equation), référence maths/11-capacities.md:212
- TLC-SO-COMPETENCIES-104 — Équation — Cohérence et coordination entre Disciples (Equation), référence maths/12-competencies.md:222
- TLC-SO-PRACTICE-091 — Équation — Cohérence et coordination entre Disciples (Equation), référence maths/13-practice.md:199
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0048`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-095`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-104`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-091`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-095, TLC-SO-COMPETENCIES-104, TLC-SO-PRACTICE-091
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-095, TLC-SO-COMPETENCIES-104, TLC-SO-PRACTICE-091
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-095, TLC-SO-COMPETENCIES-104, TLC-SO-PRACTICE-091
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

## TLC-HR-0069

### Identité

- decision_id : `TLC-HR-0069`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0069 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-073`, `TLC-SO-COMPETENCIES-071`, `TLC-SO-PRACTICE-073`
- Objets : `TLC-SO-CAPACITIES-073`, `TLC-SO-COMPETENCIES-071`, `TLC-SO-PRACTICE-073`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: feedback par les pairs
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-073 — Feedback par les pairs (Concept), référence maths/11-capacities.md:125
- TLC-SO-COMPETENCIES-071 — Feedback par les pairs (Concept), référence maths/12-competencies.md:103
- TLC-SO-PRACTICE-073 — Feedback par les pairs (Concept), référence maths/13-practice.md:93
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0069`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-073`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-071`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-073`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-073, TLC-SO-COMPETENCIES-071, TLC-SO-PRACTICE-073
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-073, TLC-SO-COMPETENCIES-071, TLC-SO-PRACTICE-073
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-073, TLC-SO-COMPETENCIES-071, TLC-SO-PRACTICE-073
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

## TLC-HR-0113

### Identité

- decision_id : `TLC-HR-0113`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0113 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-079`, `TLC-SO-COMPETENCIES-082`, `TLC-SO-PRACTICE-081`
- Objets : `TLC-SO-CAPACITIES-079`, `TLC-SO-COMPETENCIES-082`, `TLC-SO-PRACTICE-081`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: profondeur
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-079 — Profondeur (Concept), référence maths/11-capacities.md:137
- TLC-SO-COMPETENCIES-082 — Profondeur (Concept), référence maths/12-competencies.md:140
- TLC-SO-PRACTICE-081 — Profondeur (Concept), référence maths/13-practice.md:123
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0113`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-079`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-082`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-081`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-079, TLC-SO-COMPETENCIES-082, TLC-SO-PRACTICE-081
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-079, TLC-SO-COMPETENCIES-082, TLC-SO-PRACTICE-081
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-079, TLC-SO-COMPETENCIES-082, TLC-SO-PRACTICE-081
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
