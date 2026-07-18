# batch-012 — Revue transversale finale et limites documentaires

État : `pending`
Décisions : 12
Catégorie de paquet : `mixed_scientific_review`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0046

### Identité

- decision_id : `TLC-HR-0046`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0046 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-089`, `TLC-SO-PRACTICE-086`
- Objets : `TLC-SO-CAPACITIES-089`, `TLC-SO-PRACTICE-086`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation adaptation a de nouveaux contextes
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [DifferentialEquation]}
- TLC-SO-CAPACITIES-089 — Équation — Adaptation à de nouveaux contextes (DifferentialEquation), référence maths/11-capacities.md:171
- TLC-SO-PRACTICE-086 — Équation — Adaptation à de nouveaux contextes (DifferentialEquation), référence maths/13-practice.md:158
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0046`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-089`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-086`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-089, TLC-SO-PRACTICE-086
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-089, TLC-SO-PRACTICE-086
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-089, TLC-SO-PRACTICE-086
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

## TLC-HR-0006

### Identité

- decision_id : `TLC-HR-0006`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0006 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-029`, `TLC-SO-LIVED-EXPERIENCE-024`, `TLC-SO-PRACTICE-030`
- Objets : `TLC-SO-CAPACITIES-029`, `TLC-SO-LIVED-EXPERIENCE-024`, `TLC-SO-PRACTICE-030`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: adaptation a de nouveaux contextes
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-029 — Adaptation à de nouveaux contextes (Concept), référence maths/11-capacities.md:169
- TLC-SO-LIVED-EXPERIENCE-024 — Adaptation à de nouveaux contextes (Concept), référence maths/14-lived-experience.md:109
- TLC-SO-PRACTICE-030 — Adaptation à de nouveaux contextes (Concept), référence maths/13-practice.md:155
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0006`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-029`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-024`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-030`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-029, TLC-SO-LIVED-EXPERIENCE-024, TLC-SO-PRACTICE-030
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-029, TLC-SO-LIVED-EXPERIENCE-024, TLC-SO-PRACTICE-030
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-029, TLC-SO-LIVED-EXPERIENCE-024, TLC-SO-PRACTICE-030
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

## TLC-HR-0096

### Identité

- decision_id : `TLC-HR-0096`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0096 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-035`, `TLC-SO-LIVED-EXPERIENCE-030`
- Objets : `TLC-SO-CAPACITIES-035`, `TLC-SO-LIVED-EXPERIENCE-030`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: manifestation comportementale et habituelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-035 — Manifestation comportementale et habituelle (Concept), référence maths/11-capacities.md:202
- TLC-SO-LIVED-EXPERIENCE-030 — Manifestation comportementale et habituelle (Concept), référence maths/14-lived-experience.md:126
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0096`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-035`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-030`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-035, TLC-SO-LIVED-EXPERIENCE-030
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-035, TLC-SO-LIVED-EXPERIENCE-030
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-035, TLC-SO-LIVED-EXPERIENCE-030
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

## TLC-HR-0028

### Identité

- decision_id : `TLC-HR-0028`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0028 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-083`, `TLC-SO-PRACTICE-083`
- Objets : `TLC-SO-COMPETENCIES-083`, `TLC-SO-PRACTICE-083`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: creativite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-083 — Créativité (Concept), référence maths/12-competencies.md:141
- TLC-SO-PRACTICE-083 — Créativité (Concept), référence maths/13-practice.md:125
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0028`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-083`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-083`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-083, TLC-SO-PRACTICE-083
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-083, TLC-SO-PRACTICE-083
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-083, TLC-SO-PRACTICE-083
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

## TLC-HR-0055

### Identité

- decision_id : `TLC-HR-0055`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0055 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-072`, `TLC-SO-PRACTICE-068`
- Objets : `TLC-SO-COMPETENCIES-072`, `TLC-SO-PRACTICE-068`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation instruction directe et mentorat
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [DifferentialEquation]}
- TLC-SO-COMPETENCIES-072 — Équation — Instruction directe et mentorat (DifferentialEquation), référence maths/12-competencies.md:109
- TLC-SO-PRACTICE-068 — Équation — Instruction directe et mentorat (DifferentialEquation), référence maths/13-practice.md:72
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0055`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-072`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-068`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-072, TLC-SO-PRACTICE-068
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-072, TLC-SO-PRACTICE-068
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-072, TLC-SO-PRACTICE-068
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

## TLC-HR-0082

### Identité

- decision_id : `TLC-HR-0082`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0082 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-018`, `TLC-SO-PRACTICE-012`
- Objets : `TLC-SO-COMPETENCIES-018`, `TLC-SO-PRACTICE-012`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: instruction directe et mentorat
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-018 — Instruction directe et mentorat (Concept), référence maths/12-competencies.md:107
- TLC-SO-PRACTICE-012 — Instruction directe et mentorat (Concept), référence maths/13-practice.md:69
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0082`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-018`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-012`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-018, TLC-SO-PRACTICE-012
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-018, TLC-SO-PRACTICE-012
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-018, TLC-SO-PRACTICE-012
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

## TLC-HR-0107

### Identité

- decision_id : `TLC-HR-0107`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0107 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-041`, `TLC-SO-PRACTICE-040`
- Objets : `TLC-SO-COMPETENCIES-041`, `TLC-SO-PRACTICE-040`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: normes partagees standards et bonnes pratiques
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-041 — Normes partagées, standards et bonnes pratiques (Concept), référence maths/12-competencies.md:240
- TLC-SO-PRACTICE-040 — Normes partagées, standards et bonnes pratiques (Concept), référence maths/13-practice.md:213
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0107`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-041`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-040`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-041, TLC-SO-PRACTICE-040
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-041, TLC-SO-PRACTICE-040
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-041, TLC-SO-PRACTICE-040
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

## TLC-HR-0110

### Identité

- decision_id : `TLC-HR-0110`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0110 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-078`, `TLC-SO-PRACTICE-079`
- Objets : `TLC-SO-COMPETENCIES-078`, `TLC-SO-PRACTICE-079`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: precision
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-078 — Précision (Concept), référence maths/12-competencies.md:134
- TLC-SO-PRACTICE-079 — Précision (Concept), référence maths/13-practice.md:119
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0110`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-078`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-079`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-078, TLC-SO-PRACTICE-079
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-078, TLC-SO-PRACTICE-079
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-078, TLC-SO-PRACTICE-079
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

## TLC-HR-0142

### Identité

- decision_id : `TLC-HR-0142`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0142 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-017`, `TLC-SO-PRACTICE-011`
- Objets : `TLC-SO-COMPETENCIES-017`, `TLC-SO-PRACTICE-011`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: transmission et modalites d apprentissage
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-017 — Transmission et modalités d’apprentissage (Concept), référence maths/12-competencies.md:105
- TLC-SO-PRACTICE-011 — Transmission et modalités d’apprentissage (Concept), référence maths/13-practice.md:67
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0142`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-017`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-011`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-017, TLC-SO-PRACTICE-011
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-017, TLC-SO-PRACTICE-011
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-017, TLC-SO-PRACTICE-011
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

## TLC-HR-0144

### Identité

- decision_id : `TLC-HR-0144`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0144 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-025`, `TLC-SO-PRACTICE-025`
- Objets : `TLC-SO-COMPETENCIES-025`, `TLC-SO-PRACTICE-025`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: validation et assurance qualite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-025 — Validation et assurance qualité (Concept), référence maths/12-competencies.md:148
- TLC-SO-PRACTICE-025 — Validation et assurance qualité (Concept), référence maths/13-practice.md:130
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0144`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-025`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-025`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-025, TLC-SO-PRACTICE-025
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-025, TLC-SO-PRACTICE-025
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-025, TLC-SO-PRACTICE-025
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

## TLC-HR-0108

### Identité

- decision_id : `TLC-HR-0108`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0108 ?

### Éléments concernés

- Identifiants : `TLC-SO-LIVED-EXPERIENCE-038`, `TLC-SO-PRACTICE-018`
- Objets : `TLC-SO-LIVED-EXPERIENCE-038`, `TLC-SO-PRACTICE-018`
- Relations : aucune
- Termes : aucun
- Sources : `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: operateurs et transformations
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Operator]}
- TLC-SO-LIVED-EXPERIENCE-038 — Opérateurs et transformations (Operator), référence maths/14-lived-experience.md:158
- TLC-SO-PRACTICE-018 — Opérateurs et transformations (Operator), référence maths/13-practice.md:100
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0108`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-038`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-018`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-038, TLC-SO-PRACTICE-018
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-038, TLC-SO-PRACTICE-018
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-038, TLC-SO-PRACTICE-018
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

## TLC-HR-0147

### Identité

- decision_id : `TLC-HR-0147`
- catégorie d’origine : `non_blocking_warning`
- catégorie normalisée : `unresolved_term_resolution`
- justification du classement : La décision porte explicitement sur le maintien ou la revue scientifique des termes consolidés encore non résolus.
- priorité : `medium`
- portée du blocage : `non_blocking`

### Question à décider

Comment traiter les termes restant non résolus dans le corpus ?

### Éléments concernés

- Identifiants : `TLC-GU-00002`, `TLC-GU-00003`, `TLC-GU-00004`, `TLC-GU-00005`, `TLC-GU-00006`, `TLC-GU-00007`, `TLC-GU-00008`, `TLC-GU-00009`, `TLC-GU-00010`, `TLC-GU-00011`, `TLC-GU-00012`, `TLC-GU-00013`, `TLC-GU-00016`, `TLC-GU-00018`, `TLC-GU-00019`, `TLC-GU-00025`, `TLC-GU-00027`, `TLC-GU-00028`, `TLC-GU-00029`, `TLC-GU-00033`, `TLC-GU-00035`, `TLC-GU-00036`, `TLC-GU-00037`, `TLC-GU-00038`, `TLC-GU-00039`, `TLC-GU-00043`, `TLC-GU-00045`, `TLC-GU-00047`, `TLC-GU-00050`, `TLC-GU-00055`, `TLC-GU-00056`, `TLC-GU-00057`, `TLC-GU-00058`, `TLC-GU-00059`, `TLC-GU-00061`, `TLC-GU-00062`, `TLC-GU-00063`, `TLC-GU-00064`, `TLC-GU-00065`, `TLC-GU-00066`, `TLC-GU-00067`, `TLC-GU-00068`, `TLC-GU-00069`, `TLC-GU-00070`, `TLC-GU-00071`, `TLC-GU-00072`, `TLC-GU-00073`, `TLC-GU-00074`, `TLC-GU-00075`, `TLC-GU-00076`, `TLC-GU-00077`, `TLC-GU-00078`, `TLC-GU-00079`, `TLC-GU-00083`, `TLC-GU-00085`, `TLC-GU-00086`, `TLC-GU-00087`, `TLC-GU-00088`, `TLC-GU-00089`, `TLC-GU-00090`, `TLC-GU-00091`, `TLC-GU-00092`, `TLC-GU-00093`, `TLC-GU-00094`, `TLC-GU-00098`, `TLC-GU-00099`, `TLC-GU-00101`, `TLC-GU-00104`, `TLC-GU-00105`, `TLC-GU-00107`, `TLC-GU-00109`, `TLC-GU-00110`, `TLC-GU-00111`, `TLC-GU-00115`, `TLC-GU-00116`, `TLC-GU-00117`, `TLC-GU-00118`, `TLC-GU-00119`, `TLC-GU-00120`, `TLC-GU-00123`, `TLC-GU-00124`, `TLC-GU-00125`, `TLC-GU-00126`, `TLC-GU-00132`, `TLC-GU-00133`, `TLC-GU-00134`, `TLC-GU-00137`, `TLC-GU-00141`, `TLC-GU-00146`, `TLC-GU-00147`, `TLC-GU-00148`, `TLC-GU-00149`, `TLC-GU-00150`, `TLC-GU-00151`, `TLC-GU-00152`, `TLC-GU-00153`, `TLC-GU-00154`, `TLC-GU-00155`, `TLC-GU-00156`, `TLC-GU-00158`, `TLC-GU-00159`, `TLC-GU-00160`, `TLC-GU-00161`, `TLC-GU-00162`, `TLC-GU-00163`, `TLC-GU-00164`, `TLC-GU-00165`, `TLC-GU-00166`, `TLC-GU-00167`, `TLC-GU-00168`, `TLC-GU-00169`, `TLC-GU-00170`, `TLC-GU-00171`, `TLC-GU-00172`, `TLC-GU-00173`, `TLC-GU-00174`, `TLC-GU-00175`, `TLC-GU-00176`, `TLC-GU-00177`, `TLC-GU-00178`, `TLC-GU-00179`, `TLC-GU-00180`, `TLC-GU-00181`, `TLC-GU-00182`, `TLC-GU-00183`, `TLC-GU-00184`, `TLC-GU-00185`, `TLC-GU-00186`, `TLC-GU-00187`, `TLC-GU-00188`, `TLC-GU-00190`, `TLC-GU-00191`, `TLC-GU-00192`, `TLC-GU-00193`, `TLC-GU-00194`, `TLC-GU-00197`, `TLC-GU-00198`, `TLC-GU-00199`, `TLC-GU-00200`, `TLC-GU-00201`, `TLC-GU-00202`, `TLC-GU-00203`, `TLC-GU-00204`, `TLC-GU-00205`, `TLC-GU-00206`, `TLC-GU-00207`, `TLC-GU-00208`, `TLC-GU-00209`, `TLC-GU-00210`, `TLC-GU-00211`, `TLC-GU-00232`, `TLC-GU-00234`, `TLC-GU-00257`, `TLC-GU-00263`, `TLC-GU-00264`, `TLC-GU-00265`, `TLC-GU-00266`, `TLC-GU-00267`, `TLC-GU-00268`, `TLC-GU-00269`, `TLC-GU-00270`, `TLC-GU-00272`, `TLC-GU-00273`, `TLC-GU-00274`, `TLC-GU-00276`, `TLC-GU-00277`, `TLC-GU-00278`, `TLC-GU-00279`, `TLC-GU-00280`, `TLC-GU-00281`, `TLC-GU-00282`, `TLC-GU-00283`, `TLC-GU-00284`, `TLC-GU-00285`, `TLC-GU-00294`, `TLC-GU-00296`, `TLC-GU-00297`, `TLC-GU-00298`, `TLC-GU-00299`, `TLC-GU-00303`, `TLC-GU-00304`, `TLC-GU-00306`, `TLC-GU-00308`, `TLC-GU-00310`, `TLC-GU-00311`, `TLC-GU-00313`, `TLC-GU-00314`, `TLC-GU-00315`, `TLC-GU-00316`, `TLC-GU-00317`, `TLC-GU-00318`, `TLC-GU-00319`, `TLC-GU-00320`, `TLC-GU-00321`, `TLC-GU-00322`, `TLC-GU-00323`, `TLC-GU-00324`, `TLC-GU-00325`, `TLC-GU-00326`, `TLC-GU-00327`, `TLC-GU-00328`, `TLC-GU-00329`, `TLC-GU-00330`, `TLC-GU-00331`, `TLC-GU-00332`, `TLC-GU-00333`, `TLC-GU-00334`, `TLC-GU-00335`, `TLC-GU-00336`, `TLC-GU-00337`, `TLC-GU-00338`, `TLC-GU-00339`, `TLC-GU-00340`, `TLC-GU-00341`, `TLC-GU-00342`, `TLC-GU-00343`, `TLC-GU-00346`, `TLC-GU-00347`, `TLC-GU-00348`, `TLC-GU-00349`, `TLC-GU-00350`, `TLC-GU-00351`, `TLC-GU-00352`, `TLC-GU-00353`, `TLC-GU-00354`, `TLC-GU-00355`, `TLC-GU-00356`, `TLC-GU-00357`, `TLC-GU-00358`, `TLC-GU-00359`, `TLC-GU-00360`, `TLC-GU-00369`, `TLC-GU-00370`, `TLC-GU-00371`, `TLC-GU-00372`, `TLC-GU-00373`, `TLC-GU-00374`, `TLC-GU-00376`, `TLC-GU-00378`, `TLC-GU-00379`, `TLC-GU-00380`, `TLC-GU-00381`, `TLC-GU-00382`, `TLC-GU-00383`, `TLC-GU-00384`, `TLC-GU-00385`, `TLC-GU-00386`, `TLC-GU-00387`, `TLC-GU-00388`, `TLC-GU-00389`, `TLC-GU-00390`, `TLC-GU-00392`, `TLC-GU-00393`, `TLC-GU-00394`, `TLC-GU-00395`, `TLC-GU-00396`, `TLC-GU-00397`, `TLC-GU-00398`, `TLC-GU-00408`, `TLC-GU-00409`, `TLC-GU-00410`, `TLC-GU-00411`, `TLC-GU-00412`, `TLC-GU-00415`, `TLC-GU-00416`, `TLC-GU-00417`, `TLC-GU-00418`, `TLC-GU-00419`, `TLC-GU-00420`, `TLC-GU-00424`, `TLC-GU-00426`, `TLC-GU-00429`, `TLC-GU-00431`, `TLC-GU-00432`, `TLC-GU-00434`, `TLC-GU-00435`, `TLC-GU-00437`, `TLC-GU-00438`, `TLC-GU-00439`, `TLC-GU-00440`, `TLC-GU-00444`, `TLC-GU-00446`, `TLC-GU-00451`, `TLC-GU-00452`, `TLC-GU-00454`, `TLC-GU-00455`, `TLC-GU-00463`, `TLC-GU-00466`, `TLC-GU-00468`, `TLC-GU-00469`, `TLC-GU-00475`, `TLC-GU-00476`, `TLC-GU-00477`, `TLC-GU-00478`, `TLC-GU-00479`, `TLC-GU-00480`, `TLC-GU-00481`, `TLC-GU-00482`, `TLC-GU-00483`, `TLC-GU-00484`, `TLC-GU-00485`, `TLC-GU-00487`, `TLC-GU-00488`, `TLC-GU-00489`, `TLC-GU-00490`, `TLC-GU-00491`, `TLC-GU-00492`, `TLC-GU-00493`, `TLC-GU-00494`, `TLC-GU-00495`, `TLC-GU-00496`, `TLC-GU-00500`, `TLC-GU-00501`, `TLC-GU-00502`, `TLC-GU-00503`, `TLC-GU-00504`, `TLC-GU-00505`, `TLC-GU-00506`, `TLC-GU-00507`, `TLC-GU-00509`, `TLC-GU-00510`, `TLC-GU-00511`, `TLC-GU-00513`, `TLC-GU-00514`, `TLC-GU-00515`, `TLC-GU-00516`, `TLC-GU-00517`, `TLC-GU-00518`, `TLC-GU-00519`, `TLC-GU-00520`, `TLC-GU-00521`, `TLC-GU-00522`, `TLC-GU-00523`, `TLC-GU-00524`, `TLC-GU-00525`, `TLC-GU-00527`, `TLC-GU-00528`, `TLC-GU-00530`, `TLC-GU-00531`, `TLC-GU-00532`, `TLC-GU-00533`, `TLC-GU-00534`, `TLC-GU-00535`, `TLC-GU-00536`, `TLC-GU-00537`, `TLC-GU-00538`, `TLC-GU-00539`, `TLC-GU-00540`, `TLC-GU-00541`, `TLC-GU-00542`, `TLC-GU-00543`, `TLC-GU-00544`, `TLC-GU-00545`, `TLC-GU-00546`, `TLC-GU-00547`, `TLC-GU-00548`, `TLC-GU-00549`, `TLC-GU-00550`, `TLC-GU-00553`, `TLC-GU-00554`, `TLC-GU-00555`, `TLC-GU-00556`, `TLC-GU-00557`, `TLC-GU-00558`, `TLC-GU-00559`, `TLC-GU-00560`, `TLC-GU-00561`, `TLC-GU-00562`, `TLC-GU-00563`, `TLC-GU-00564`, `TLC-GU-00565`, `TLC-GU-00566`, `TLC-GU-00567`, `TLC-GU-00568`, `TLC-GU-00569`, `TLC-GU-00570`, `TLC-GU-00571`, `TLC-GU-00572`, `TLC-GU-00573`, `TLC-GU-00574`, `TLC-GU-00575`, `TLC-GU-00576`, `TLC-GU-00577`, `TLC-GU-00578`, `TLC-GU-00579`, `TLC-GU-00581`, `TLC-GU-00582`, `TLC-GU-00583`, `TLC-GU-00593`, `TLC-GU-00594`, `TLC-GU-00595`, `TLC-GU-00596`, `TLC-GU-00599`, `TLC-GU-00602`, `TLC-GU-00604`, `TLC-GU-00606`, `TLC-GU-00607`, `TLC-GU-00609`, `TLC-GU-00611`, `TLC-GU-00614`, `TLC-GU-00618`, `TLC-GU-00619`, `TLC-GU-00620`, `TLC-GU-00621`, `TLC-GU-00630`, `TLC-GU-00631`, `TLC-GU-00632`, `TLC-GU-00633`, `TLC-GU-00635`, `TLC-GU-00636`, `TLC-GU-00637`, `TLC-GU-00638`, `TLC-GU-00639`, `TLC-GU-00640`, `TLC-GU-00641`, `TLC-GU-00643`, `TLC-GU-00644`, `TLC-GU-00645`, `TLC-GU-00647`, `TLC-GU-00648`, `TLC-GU-00649`, `TLC-GU-00651`, `TLC-GU-00656`, `TLC-GU-00657`, `TLC-GU-00658`, `TLC-GU-00659`, `TLC-GU-00660`, `TLC-GU-00661`, `TLC-GU-00662`, `TLC-GU-00663`, `TLC-GU-00664`, `TLC-GU-00665`, `TLC-GU-00666`, `TLC-GU-00667`, `TLC-GU-00668`, `TLC-GU-00669`, `TLC-GU-00673`, `TLC-GU-00674`, `TLC-GU-00675`, `TLC-GU-00677`, `TLC-GU-00678`, `TLC-GU-00681`, `TLC-GU-00682`, `TLC-GU-00684`, `TLC-GU-00685`, `TLC-GU-00686`, `TLC-GU-00687`, `TLC-GU-00688`, `TLC-GU-00689`, `TLC-GU-00690`, `TLC-GU-00691`, `TLC-GU-00692`, `TLC-GU-00693`, `TLC-GU-00694`, `TLC-GU-00695`, `TLC-GU-00696`, `TLC-GU-00697`, `TLC-GU-00702`, `TLC-GU-00703`, `TLC-GU-00704`, `TLC-GU-00705`, `TLC-GU-00706`, `TLC-GU-00707`, `TLC-GU-00708`, `TLC-GU-00709`, `TLC-GU-00710`, `TLC-GU-00711`, `TLC-GU-00712`, `TLC-GU-00714`, `TLC-GU-00715`, `TLC-GU-00716`, `TLC-GU-00717`, `TLC-GU-00718`, `TLC-GU-00719`, `TLC-GU-00720`, `TLC-GU-00721`, `TLC-GU-00722`, `TLC-GU-00723`, `TLC-GU-00724`, `TLC-GU-00725`, `TLC-GU-00726`, `TLC-GU-00727`, `TLC-GU-00728`, `TLC-GU-00729`, `TLC-GU-00730`, `TLC-GU-00731`, `TLC-GU-00732`, `TLC-GU-00733`, `TLC-GU-00734`, `TLC-GU-00735`, `TLC-GU-00736`, `TLC-GU-00737`, `TLC-GU-00739`, `TLC-GU-00740`, `TLC-GU-00741`, `TLC-GU-00742`, `TLC-GU-00743`, `TLC-GU-00744`, `TLC-GU-00745`, `TLC-GU-00749`, `TLC-GU-00750`, `TLC-GU-00758`, `TLC-GU-00759`, `TLC-GU-00760`, `TLC-GU-00761`, `TLC-GU-00762`, `TLC-GU-00763`, `TLC-GU-00764`, `TLC-GU-00765`, `TLC-GU-00766`, `TLC-GU-00767`, `TLC-GU-00768`, `TLC-GU-00769`, `TLC-GU-00770`, `TLC-GU-00773`, `TLC-GU-00774`, `TLC-GU-00775`, `TLC-GU-00776`, `TLC-GU-00777`, `TLC-GU-00778`, `TLC-GU-00779`, `TLC-GU-00780`, `TLC-GU-00781`, `TLC-GU-00782`, `TLC-GU-00783`, `TLC-GU-00784`, `TLC-GU-00785`, `TLC-GU-00786`, `TLC-GU-00787`, `TLC-GU-00788`, `TLC-GU-00789`, `TLC-GU-00790`, `TLC-GU-00791`, `TLC-GU-00792`, `TLC-GU-00793`, `TLC-GU-00794`, `TLC-GU-00795`, `TLC-GU-00796`, `TLC-GU-00797`, `TLC-GU-00798`, `TLC-GU-00799`, `TLC-GU-00800`, `TLC-GU-00801`, `TLC-GU-00802`, `TLC-GU-00803`, `TLC-GU-00804`, `TLC-GU-00805`, `TLC-GU-00806`, `TLC-GU-00807`, `TLC-GU-00808`, `TLC-GU-00809`, `TLC-GU-00810`, `TLC-GU-00811`, `TLC-GU-00812`, `TLC-GU-00813`, `TLC-GU-00814`, `TLC-GU-00815`, `TLC-GU-00816`, `TLC-GU-00817`, `TLC-GU-00818`, `TLC-GU-00819`, `TLC-GU-00821`, `TLC-GU-00822`, `TLC-GU-00823`, `TLC-GU-00825`, `TLC-GU-00826`, `TLC-GU-00827`, `TLC-GU-00828`, `TLC-GU-00829`, `TLC-GU-00830`
- Objets : aucun
- Relations : aucune
- Termes : `TLC-GU-00002`, `TLC-GU-00003`, `TLC-GU-00004`, `TLC-GU-00005`, `TLC-GU-00006`, `TLC-GU-00007`, `TLC-GU-00008`, `TLC-GU-00009`, `TLC-GU-00010`, `TLC-GU-00011`, `TLC-GU-00012`, `TLC-GU-00013`, `TLC-GU-00016`, `TLC-GU-00018`, `TLC-GU-00019`, `TLC-GU-00025`, `TLC-GU-00027`, `TLC-GU-00028`, `TLC-GU-00029`, `TLC-GU-00033`, `TLC-GU-00035`, `TLC-GU-00036`, `TLC-GU-00037`, `TLC-GU-00038`, `TLC-GU-00039`, `TLC-GU-00043`, `TLC-GU-00045`, `TLC-GU-00047`, `TLC-GU-00050`, `TLC-GU-00055`, `TLC-GU-00056`, `TLC-GU-00057`, `TLC-GU-00058`, `TLC-GU-00059`, `TLC-GU-00061`, `TLC-GU-00062`, `TLC-GU-00063`, `TLC-GU-00064`, `TLC-GU-00065`, `TLC-GU-00066`, `TLC-GU-00067`, `TLC-GU-00068`, `TLC-GU-00069`, `TLC-GU-00070`, `TLC-GU-00071`, `TLC-GU-00072`, `TLC-GU-00073`, `TLC-GU-00074`, `TLC-GU-00075`, `TLC-GU-00076`, `TLC-GU-00077`, `TLC-GU-00078`, `TLC-GU-00079`, `TLC-GU-00083`, `TLC-GU-00085`, `TLC-GU-00086`, `TLC-GU-00087`, `TLC-GU-00088`, `TLC-GU-00089`, `TLC-GU-00090`, `TLC-GU-00091`, `TLC-GU-00092`, `TLC-GU-00093`, `TLC-GU-00094`, `TLC-GU-00098`, `TLC-GU-00099`, `TLC-GU-00101`, `TLC-GU-00104`, `TLC-GU-00105`, `TLC-GU-00107`, `TLC-GU-00109`, `TLC-GU-00110`, `TLC-GU-00111`, `TLC-GU-00115`, `TLC-GU-00116`, `TLC-GU-00117`, `TLC-GU-00118`, `TLC-GU-00119`, `TLC-GU-00120`, `TLC-GU-00123`, `TLC-GU-00124`, `TLC-GU-00125`, `TLC-GU-00126`, `TLC-GU-00132`, `TLC-GU-00133`, `TLC-GU-00134`, `TLC-GU-00137`, `TLC-GU-00141`, `TLC-GU-00146`, `TLC-GU-00147`, `TLC-GU-00148`, `TLC-GU-00149`, `TLC-GU-00150`, `TLC-GU-00151`, `TLC-GU-00152`, `TLC-GU-00153`, `TLC-GU-00154`, `TLC-GU-00155`, `TLC-GU-00156`, `TLC-GU-00158`, `TLC-GU-00159`, `TLC-GU-00160`, `TLC-GU-00161`, `TLC-GU-00162`, `TLC-GU-00163`, `TLC-GU-00164`, `TLC-GU-00165`, `TLC-GU-00166`, `TLC-GU-00167`, `TLC-GU-00168`, `TLC-GU-00169`, `TLC-GU-00170`, `TLC-GU-00171`, `TLC-GU-00172`, `TLC-GU-00173`, `TLC-GU-00174`, `TLC-GU-00175`, `TLC-GU-00176`, `TLC-GU-00177`, `TLC-GU-00178`, `TLC-GU-00179`, `TLC-GU-00180`, `TLC-GU-00181`, `TLC-GU-00182`, `TLC-GU-00183`, `TLC-GU-00184`, `TLC-GU-00185`, `TLC-GU-00186`, `TLC-GU-00187`, `TLC-GU-00188`, `TLC-GU-00190`, `TLC-GU-00191`, `TLC-GU-00192`, `TLC-GU-00193`, `TLC-GU-00194`, `TLC-GU-00197`, `TLC-GU-00198`, `TLC-GU-00199`, `TLC-GU-00200`, `TLC-GU-00201`, `TLC-GU-00202`, `TLC-GU-00203`, `TLC-GU-00204`, `TLC-GU-00205`, `TLC-GU-00206`, `TLC-GU-00207`, `TLC-GU-00208`, `TLC-GU-00209`, `TLC-GU-00210`, `TLC-GU-00211`, `TLC-GU-00232`, `TLC-GU-00234`, `TLC-GU-00257`, `TLC-GU-00263`, `TLC-GU-00264`, `TLC-GU-00265`, `TLC-GU-00266`, `TLC-GU-00267`, `TLC-GU-00268`, `TLC-GU-00269`, `TLC-GU-00270`, `TLC-GU-00272`, `TLC-GU-00273`, `TLC-GU-00274`, `TLC-GU-00276`, `TLC-GU-00277`, `TLC-GU-00278`, `TLC-GU-00279`, `TLC-GU-00280`, `TLC-GU-00281`, `TLC-GU-00282`, `TLC-GU-00283`, `TLC-GU-00284`, `TLC-GU-00285`, `TLC-GU-00294`, `TLC-GU-00296`, `TLC-GU-00297`, `TLC-GU-00298`, `TLC-GU-00299`, `TLC-GU-00303`, `TLC-GU-00304`, `TLC-GU-00306`, `TLC-GU-00308`, `TLC-GU-00310`, `TLC-GU-00311`, `TLC-GU-00313`, `TLC-GU-00314`, `TLC-GU-00315`, `TLC-GU-00316`, `TLC-GU-00317`, `TLC-GU-00318`, `TLC-GU-00319`, `TLC-GU-00320`, `TLC-GU-00321`, `TLC-GU-00322`, `TLC-GU-00323`, `TLC-GU-00324`, `TLC-GU-00325`, `TLC-GU-00326`, `TLC-GU-00327`, `TLC-GU-00328`, `TLC-GU-00329`, `TLC-GU-00330`, `TLC-GU-00331`, `TLC-GU-00332`, `TLC-GU-00333`, `TLC-GU-00334`, `TLC-GU-00335`, `TLC-GU-00336`, `TLC-GU-00337`, `TLC-GU-00338`, `TLC-GU-00339`, `TLC-GU-00340`, `TLC-GU-00341`, `TLC-GU-00342`, `TLC-GU-00343`, `TLC-GU-00346`, `TLC-GU-00347`, `TLC-GU-00348`, `TLC-GU-00349`, `TLC-GU-00350`, `TLC-GU-00351`, `TLC-GU-00352`, `TLC-GU-00353`, `TLC-GU-00354`, `TLC-GU-00355`, `TLC-GU-00356`, `TLC-GU-00357`, `TLC-GU-00358`, `TLC-GU-00359`, `TLC-GU-00360`, `TLC-GU-00369`, `TLC-GU-00370`, `TLC-GU-00371`, `TLC-GU-00372`, `TLC-GU-00373`, `TLC-GU-00374`, `TLC-GU-00376`, `TLC-GU-00378`, `TLC-GU-00379`, `TLC-GU-00380`, `TLC-GU-00381`, `TLC-GU-00382`, `TLC-GU-00383`, `TLC-GU-00384`, `TLC-GU-00385`, `TLC-GU-00386`, `TLC-GU-00387`, `TLC-GU-00388`, `TLC-GU-00389`, `TLC-GU-00390`, `TLC-GU-00392`, `TLC-GU-00393`, `TLC-GU-00394`, `TLC-GU-00395`, `TLC-GU-00396`, `TLC-GU-00397`, `TLC-GU-00398`, `TLC-GU-00408`, `TLC-GU-00409`, `TLC-GU-00410`, `TLC-GU-00411`, `TLC-GU-00412`, `TLC-GU-00415`, `TLC-GU-00416`, `TLC-GU-00417`, `TLC-GU-00418`, `TLC-GU-00419`, `TLC-GU-00420`, `TLC-GU-00424`, `TLC-GU-00426`, `TLC-GU-00429`, `TLC-GU-00431`, `TLC-GU-00432`, `TLC-GU-00434`, `TLC-GU-00435`, `TLC-GU-00437`, `TLC-GU-00438`, `TLC-GU-00439`, `TLC-GU-00440`, `TLC-GU-00444`, `TLC-GU-00446`, `TLC-GU-00451`, `TLC-GU-00452`, `TLC-GU-00454`, `TLC-GU-00455`, `TLC-GU-00463`, `TLC-GU-00466`, `TLC-GU-00468`, `TLC-GU-00469`, `TLC-GU-00475`, `TLC-GU-00476`, `TLC-GU-00477`, `TLC-GU-00478`, `TLC-GU-00479`, `TLC-GU-00480`, `TLC-GU-00481`, `TLC-GU-00482`, `TLC-GU-00483`, `TLC-GU-00484`, `TLC-GU-00485`, `TLC-GU-00487`, `TLC-GU-00488`, `TLC-GU-00489`, `TLC-GU-00490`, `TLC-GU-00491`, `TLC-GU-00492`, `TLC-GU-00493`, `TLC-GU-00494`, `TLC-GU-00495`, `TLC-GU-00496`, `TLC-GU-00500`, `TLC-GU-00501`, `TLC-GU-00502`, `TLC-GU-00503`, `TLC-GU-00504`, `TLC-GU-00505`, `TLC-GU-00506`, `TLC-GU-00507`, `TLC-GU-00509`, `TLC-GU-00510`, `TLC-GU-00511`, `TLC-GU-00513`, `TLC-GU-00514`, `TLC-GU-00515`, `TLC-GU-00516`, `TLC-GU-00517`, `TLC-GU-00518`, `TLC-GU-00519`, `TLC-GU-00520`, `TLC-GU-00521`, `TLC-GU-00522`, `TLC-GU-00523`, `TLC-GU-00524`, `TLC-GU-00525`, `TLC-GU-00527`, `TLC-GU-00528`, `TLC-GU-00530`, `TLC-GU-00531`, `TLC-GU-00532`, `TLC-GU-00533`, `TLC-GU-00534`, `TLC-GU-00535`, `TLC-GU-00536`, `TLC-GU-00537`, `TLC-GU-00538`, `TLC-GU-00539`, `TLC-GU-00540`, `TLC-GU-00541`, `TLC-GU-00542`, `TLC-GU-00543`, `TLC-GU-00544`, `TLC-GU-00545`, `TLC-GU-00546`, `TLC-GU-00547`, `TLC-GU-00548`, `TLC-GU-00549`, `TLC-GU-00550`, `TLC-GU-00553`, `TLC-GU-00554`, `TLC-GU-00555`, `TLC-GU-00556`, `TLC-GU-00557`, `TLC-GU-00558`, `TLC-GU-00559`, `TLC-GU-00560`, `TLC-GU-00561`, `TLC-GU-00562`, `TLC-GU-00563`, `TLC-GU-00564`, `TLC-GU-00565`, `TLC-GU-00566`, `TLC-GU-00567`, `TLC-GU-00568`, `TLC-GU-00569`, `TLC-GU-00570`, `TLC-GU-00571`, `TLC-GU-00572`, `TLC-GU-00573`, `TLC-GU-00574`, `TLC-GU-00575`, `TLC-GU-00576`, `TLC-GU-00577`, `TLC-GU-00578`, `TLC-GU-00579`, `TLC-GU-00581`, `TLC-GU-00582`, `TLC-GU-00583`, `TLC-GU-00593`, `TLC-GU-00594`, `TLC-GU-00595`, `TLC-GU-00596`, `TLC-GU-00599`, `TLC-GU-00602`, `TLC-GU-00604`, `TLC-GU-00606`, `TLC-GU-00607`, `TLC-GU-00609`, `TLC-GU-00611`, `TLC-GU-00614`, `TLC-GU-00618`, `TLC-GU-00619`, `TLC-GU-00620`, `TLC-GU-00621`, `TLC-GU-00630`, `TLC-GU-00631`, `TLC-GU-00632`, `TLC-GU-00633`, `TLC-GU-00635`, `TLC-GU-00636`, `TLC-GU-00637`, `TLC-GU-00638`, `TLC-GU-00639`, `TLC-GU-00640`, `TLC-GU-00641`, `TLC-GU-00643`, `TLC-GU-00644`, `TLC-GU-00645`, `TLC-GU-00647`, `TLC-GU-00648`, `TLC-GU-00649`, `TLC-GU-00651`, `TLC-GU-00656`, `TLC-GU-00657`, `TLC-GU-00658`, `TLC-GU-00659`, `TLC-GU-00660`, `TLC-GU-00661`, `TLC-GU-00662`, `TLC-GU-00663`, `TLC-GU-00664`, `TLC-GU-00665`, `TLC-GU-00666`, `TLC-GU-00667`, `TLC-GU-00668`, `TLC-GU-00669`, `TLC-GU-00673`, `TLC-GU-00674`, `TLC-GU-00675`, `TLC-GU-00677`, `TLC-GU-00678`, `TLC-GU-00681`, `TLC-GU-00682`, `TLC-GU-00684`, `TLC-GU-00685`, `TLC-GU-00686`, `TLC-GU-00687`, `TLC-GU-00688`, `TLC-GU-00689`, `TLC-GU-00690`, `TLC-GU-00691`, `TLC-GU-00692`, `TLC-GU-00693`, `TLC-GU-00694`, `TLC-GU-00695`, `TLC-GU-00696`, `TLC-GU-00697`, `TLC-GU-00702`, `TLC-GU-00703`, `TLC-GU-00704`, `TLC-GU-00705`, `TLC-GU-00706`, `TLC-GU-00707`, `TLC-GU-00708`, `TLC-GU-00709`, `TLC-GU-00710`, `TLC-GU-00711`, `TLC-GU-00712`, `TLC-GU-00714`, `TLC-GU-00715`, `TLC-GU-00716`, `TLC-GU-00717`, `TLC-GU-00718`, `TLC-GU-00719`, `TLC-GU-00720`, `TLC-GU-00721`, `TLC-GU-00722`, `TLC-GU-00723`, `TLC-GU-00724`, `TLC-GU-00725`, `TLC-GU-00726`, `TLC-GU-00727`, `TLC-GU-00728`, `TLC-GU-00729`, `TLC-GU-00730`, `TLC-GU-00731`, `TLC-GU-00732`, `TLC-GU-00733`, `TLC-GU-00734`, `TLC-GU-00735`, `TLC-GU-00736`, `TLC-GU-00737`, `TLC-GU-00739`, `TLC-GU-00740`, `TLC-GU-00741`, `TLC-GU-00742`, `TLC-GU-00743`, `TLC-GU-00744`, `TLC-GU-00745`, `TLC-GU-00749`, `TLC-GU-00750`, `TLC-GU-00758`, `TLC-GU-00759`, `TLC-GU-00760`, `TLC-GU-00761`, `TLC-GU-00762`, `TLC-GU-00763`, `TLC-GU-00764`, `TLC-GU-00765`, `TLC-GU-00766`, `TLC-GU-00767`, `TLC-GU-00768`, `TLC-GU-00769`, `TLC-GU-00770`, `TLC-GU-00773`, `TLC-GU-00774`, `TLC-GU-00775`, `TLC-GU-00776`, `TLC-GU-00777`, `TLC-GU-00778`, `TLC-GU-00779`, `TLC-GU-00780`, `TLC-GU-00781`, `TLC-GU-00782`, `TLC-GU-00783`, `TLC-GU-00784`, `TLC-GU-00785`, `TLC-GU-00786`, `TLC-GU-00787`, `TLC-GU-00788`, `TLC-GU-00789`, `TLC-GU-00790`, `TLC-GU-00791`, `TLC-GU-00792`, `TLC-GU-00793`, `TLC-GU-00794`, `TLC-GU-00795`, `TLC-GU-00796`, `TLC-GU-00797`, `TLC-GU-00798`, `TLC-GU-00799`, `TLC-GU-00800`, `TLC-GU-00801`, `TLC-GU-00802`, `TLC-GU-00803`, `TLC-GU-00804`, `TLC-GU-00805`, `TLC-GU-00806`, `TLC-GU-00807`, `TLC-GU-00808`, `TLC-GU-00809`, `TLC-GU-00810`, `TLC-GU-00811`, `TLC-GU-00812`, `TLC-GU-00813`, `TLC-GU-00814`, `TLC-GU-00815`, `TLC-GU-00816`, `TLC-GU-00817`, `TLC-GU-00818`, `TLC-GU-00819`, `TLC-GU-00821`, `TLC-GU-00822`, `TLC-GU-00823`, `TLC-GU-00825`, `TLC-GU-00826`, `TLC-GU-00827`, `TLC-GU-00828`, `TLC-GU-00829`, `TLC-GU-00830`
- Sources : voir les références de preuve

### Éléments de preuve

- La décision référence 570 identifiants, dont 570 retrouvés dans le registre consolidé des termes non résolus.
- Le rapport de consolidation annonce 830 termes non résolus et 260 termes probablement résolus transversalement.
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/global-unresolved-terms.yaml`
- Référence : `reports/scientific-consolidation/consolidation-report.md`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `custom_human_decision` — Décision scientifique terme par terme.
- `mark_unresolved` — Maintenir explicitement les termes non résolus.

### Conséquences

#### `custom_human_decision`

- Objets touchés : aucun directement identifié
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 570
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `mark_unresolved`

- Objets touchés : aucun directement identifié
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 570
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`scientific_review` — reprise de l’audit, non normative.

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
