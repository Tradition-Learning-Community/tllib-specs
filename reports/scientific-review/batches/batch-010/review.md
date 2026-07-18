# batch-010 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0056

### Identité

- decision_id : `TLC-HR-0056`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0056 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-092`, `TLC-SO-COMPETENCIES-101`, `TLC-SO-PRACTICE-088`, `TLC-SO-VALUES-098`
- Objets : `TLC-SO-CAPACITIES-092`, `TLC-SO-COMPETENCIES-101`, `TLC-SO-PRACTICE-088`, `TLC-SO-VALUES-098`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation moteurs motivationnels et engagement
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [DifferentialEquation]}
- TLC-SO-CAPACITIES-092 — Équation — Moteurs motivationnels et engagement (DifferentialEquation), référence maths/11-capacities.md:191
- TLC-SO-COMPETENCIES-101 — Équation — Moteurs motivationnels et engagement (DifferentialEquation), référence maths/12-competencies.md:200
- TLC-SO-PRACTICE-088 — Équation — Moteurs motivationnels et engagement (DifferentialEquation), référence maths/13-practice.md:174
- TLC-SO-VALUES-098 — Équation — Moteurs motivationnels et engagement (DifferentialEquation), référence maths/09-values.md:174
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0056`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-092`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-101`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-088`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-098`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-092, TLC-SO-COMPETENCIES-101, TLC-SO-PRACTICE-088, TLC-SO-VALUES-098
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-092, TLC-SO-COMPETENCIES-101, TLC-SO-PRACTICE-088, TLC-SO-VALUES-098
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-092, TLC-SO-COMPETENCIES-101, TLC-SO-PRACTICE-088, TLC-SO-VALUES-098
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

## TLC-HR-0070

### Identité

- decision_id : `TLC-HR-0070`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0070 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-072`, `TLC-SO-COMPETENCIES-070`, `TLC-SO-PRACTICE-072`, `TLC-SO-VALUES-074`
- Objets : `TLC-SO-CAPACITIES-072`, `TLC-SO-COMPETENCIES-070`, `TLC-SO-PRACTICE-072`, `TLC-SO-VALUES-074`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: feedback reflexif
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-072 — Feedback réflexif (Concept), référence maths/11-capacities.md:124
- TLC-SO-COMPETENCIES-070 — Feedback réflexif (Concept), référence maths/12-competencies.md:102
- TLC-SO-PRACTICE-072 — Feedback réflexif (Concept), référence maths/13-practice.md:92
- TLC-SO-VALUES-074 — Feedback réflexif (Concept), référence maths/09-values.md:102
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0070`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-072`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-070`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-072`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-074`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-072, TLC-SO-COMPETENCIES-070, TLC-SO-PRACTICE-072, TLC-SO-VALUES-074
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-072, TLC-SO-COMPETENCIES-070, TLC-SO-PRACTICE-072, TLC-SO-VALUES-074
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-072, TLC-SO-COMPETENCIES-070, TLC-SO-PRACTICE-072, TLC-SO-VALUES-074
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

## TLC-HR-0051

### Identité

- decision_id : `TLC-HR-0051`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0051 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-059`, `TLC-SO-COMPETENCIES-065`, `TLC-SO-LIVED-EXPERIENCE-054`, `TLC-SO-PRACTICE-062`, `TLC-SO-VALUES-061`
- Objets : `TLC-SO-CAPACITIES-059`, `TLC-SO-COMPETENCIES-065`, `TLC-SO-LIVED-EXPERIENCE-054`, `TLC-SO-PRACTICE-062`, `TLC-SO-VALUES-061`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation domaines de validite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Equation]}
- TLC-SO-CAPACITIES-059 — Équation — Domaines de validité (Equation), référence maths/11-capacities.md:44
- TLC-SO-COMPETENCIES-065 — Équation — Domaines de validité (Equation), référence maths/12-competencies.md:56
- TLC-SO-LIVED-EXPERIENCE-054 — Équation — Domaines de validité (Equation), référence maths/14-lived-experience.md:42
- TLC-SO-PRACTICE-062 — Équation — Domaines de validité (Equation), référence maths/13-practice.md:45
- TLC-SO-VALUES-061 — Équation — Domaines de validité (Equation), référence maths/09-values.md:49
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0051`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-059`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-065`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-054`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-062`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-061`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-059, TLC-SO-COMPETENCIES-065, TLC-SO-LIVED-EXPERIENCE-054, TLC-SO-PRACTICE-062, TLC-SO-VALUES-061
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-059, TLC-SO-COMPETENCIES-065, TLC-SO-LIVED-EXPERIENCE-054, TLC-SO-PRACTICE-062, TLC-SO-VALUES-061
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-059, TLC-SO-COMPETENCIES-065, TLC-SO-LIVED-EXPERIENCE-054, TLC-SO-PRACTICE-062, TLC-SO-VALUES-061
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

## TLC-HR-0073

### Identité

- decision_id : `TLC-HR-0073`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0073 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-043`, `TLC-SO-COMPETENCIES-044`, `TLC-SO-LIVED-EXPERIENCE-039`, `TLC-SO-VALUES-038`
- Objets : `TLC-SO-CAPACITIES-043`, `TLC-SO-COMPETENCIES-044`, `TLC-SO-LIVED-EXPERIENCE-039`, `TLC-SO-VALUES-038`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: fondements axiomatiques
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Axiom]}
- TLC-SO-CAPACITIES-043 — Fondements axiomatiques (Axiom), référence maths/11-capacities.md:239
- TLC-SO-COMPETENCIES-044 — Fondements axiomatiques (Axiom), référence maths/12-competencies.md:254
- TLC-SO-LIVED-EXPERIENCE-039 — Fondements axiomatiques (Axiom), référence maths/14-lived-experience.md:165
- TLC-SO-VALUES-038 — Fondements axiomatiques (Axiom), référence maths/09-values.md:221
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0073`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-043`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-044`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-039`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-038`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-043, TLC-SO-COMPETENCIES-044, TLC-SO-LIVED-EXPERIENCE-039, TLC-SO-VALUES-038
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-043, TLC-SO-COMPETENCIES-044, TLC-SO-LIVED-EXPERIENCE-039, TLC-SO-VALUES-038
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-043, TLC-SO-COMPETENCIES-044, TLC-SO-LIVED-EXPERIENCE-039, TLC-SO-VALUES-038
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

## TLC-HR-0075

### Identité

- decision_id : `TLC-HR-0075`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0075 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-041`, `TLC-SO-COMPETENCIES-042`, `TLC-SO-LIVED-EXPERIENCE-036`, `TLC-SO-VALUES-036`
- Objets : `TLC-SO-CAPACITIES-041`, `TLC-SO-COMPETENCIES-042`, `TLC-SO-LIVED-EXPERIENCE-036`, `TLC-SO-VALUES-036`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: formalisation mathematique avancee
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-041 — Formalisation mathématique avancée (Concept), référence maths/11-capacities.md:231
- TLC-SO-COMPETENCIES-042 — Formalisation mathématique avancée (Concept), référence maths/12-competencies.md:243
- TLC-SO-LIVED-EXPERIENCE-036 — Formalisation mathématique avancée (Concept), référence maths/14-lived-experience.md:149
- TLC-SO-VALUES-036 — Formalisation mathématique avancée (Concept), référence maths/09-values.md:211
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0075`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-041`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-042`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-036`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-036`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-041, TLC-SO-COMPETENCIES-042, TLC-SO-LIVED-EXPERIENCE-036, TLC-SO-VALUES-036
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-041, TLC-SO-COMPETENCIES-042, TLC-SO-LIVED-EXPERIENCE-036, TLC-SO-VALUES-036
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-041, TLC-SO-COMPETENCIES-042, TLC-SO-LIVED-EXPERIENCE-036, TLC-SO-VALUES-036
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

## TLC-HR-0013

### Identité

- decision_id : `TLC-HR-0013`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0013 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-040`, `TLC-SO-VALUES-034`
- Objets : `TLC-SO-COMPETENCIES-040`, `TLC-SO-VALUES-034`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: boucles de retroaction dans l apprentissage collectif
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-040 — Boucles de rétroaction dans l’apprentissage collectif (Concept), référence maths/12-competencies.md:233
- TLC-SO-VALUES-034 — Boucles de rétroaction dans l’apprentissage collectif (Concept), référence maths/09-values.md:201
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0013`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-040`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-034`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-040, TLC-SO-VALUES-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-040, TLC-SO-VALUES-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-040, TLC-SO-VALUES-034
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

## TLC-HR-0047

### Identité

- decision_id : `TLC-HR-0047`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0047 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-106`, `TLC-SO-VALUES-101`
- Objets : `TLC-SO-COMPETENCIES-106`, `TLC-SO-VALUES-101`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation boucles de retroaction dans l apprentissage collectif
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [DifferentialEquation]}
- TLC-SO-COMPETENCIES-106 — Équation — Boucles de rétroaction dans l’apprentissage collectif (DifferentialEquation), référence maths/12-competencies.md:235
- TLC-SO-VALUES-101 — Équation — Boucles de rétroaction dans l’apprentissage collectif (DifferentialEquation), référence maths/09-values.md:203
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0047`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-106`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-101`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-106, TLC-SO-VALUES-101
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-106, TLC-SO-VALUES-101
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-106, TLC-SO-VALUES-101
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

## TLC-HR-0044

### Identité

- decision_id : `TLC-HR-0044`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0044 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-027`, `TLC-SO-PRACTICE-026`, `TLC-SO-VALUES-021`
- Objets : `TLC-SO-COMPETENCIES-027`, `TLC-SO-PRACTICE-026`, `TLC-SO-VALUES-021`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: dynamique temporelle et evolution
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMPETENCIES-027 — Dynamique temporelle et évolution (Concept), référence maths/12-competencies.md:162
- TLC-SO-PRACTICE-026 — Dynamique temporelle et évolution (Concept), référence maths/13-practice.md:136
- TLC-SO-VALUES-021 — Dynamique temporelle et évolution (Concept), référence maths/09-values.md:134
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0044`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-027`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-021`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-027, TLC-SO-PRACTICE-026, TLC-SO-VALUES-021
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-027, TLC-SO-PRACTICE-026, TLC-SO-VALUES-021
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-027, TLC-SO-PRACTICE-026, TLC-SO-VALUES-021
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

## TLC-HR-0010

### Identité

- decision_id : `TLC-HR-0010`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0010 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRACTICE-057`, `TLC-SO-VALUES-056`
- Objets : `TLC-SO-PRACTICE-057`, `TLC-SO-VALUES-056`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: articulation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRACTICE-057 — Articulation (Concept), référence maths/13-practice.md:37
- TLC-SO-VALUES-056 — Articulation (Concept), référence maths/09-values.md:40
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0010`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-057`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-056`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRACTICE-057, TLC-SO-VALUES-056
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRACTICE-057, TLC-SO-VALUES-056
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRACTICE-057, TLC-SO-VALUES-056
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

## TLC-HR-0022

### Identité

- decision_id : `TLC-HR-0022`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0022 ?

### Éléments concernés

- Identifiants : `TLC-SO-LIVED-EXPERIENCE-023`, `TLC-SO-PRACTICE-028`, `TLC-SO-VALUES-023`
- Objets : `TLC-SO-LIVED-EXPERIENCE-023`, `TLC-SO-PRACTICE-028`, `TLC-SO-VALUES-023`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: consolidation a long terme
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-LIVED-EXPERIENCE-023 — Consolidation à long terme (Concept), référence maths/14-lived-experience.md:100
- TLC-SO-PRACTICE-028 — Consolidation à long terme (Concept), référence maths/13-practice.md:145
- TLC-SO-VALUES-023 — Consolidation à long terme (Concept), référence maths/09-values.md:143
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0022`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-023`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-028`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-023`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-023, TLC-SO-PRACTICE-028, TLC-SO-VALUES-023
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-023, TLC-SO-PRACTICE-028, TLC-SO-VALUES-023
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-023, TLC-SO-PRACTICE-028, TLC-SO-VALUES-023
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

## TLC-HR-0049

### Identité

- decision_id : `TLC-HR-0049`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0049 ?

### Éléments concernés

- Identifiants : `TLC-SO-LIVED-EXPERIENCE-064`, `TLC-SO-PRACTICE-085`, `TLC-SO-VALUES-094`
- Objets : `TLC-SO-LIVED-EXPERIENCE-064`, `TLC-SO-PRACTICE-085`, `TLC-SO-VALUES-094`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation consolidation a long terme
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [DifferentialEquation]}
- TLC-SO-LIVED-EXPERIENCE-064 — Équation — Consolidation à long terme (DifferentialEquation), référence maths/14-lived-experience.md:103
- TLC-SO-PRACTICE-085 — Équation — Consolidation à long terme (DifferentialEquation), référence maths/13-practice.md:148
- TLC-SO-VALUES-094 — Équation — Consolidation à long terme (DifferentialEquation), référence maths/09-values.md:145
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0049`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-064`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-085`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-094`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-064, TLC-SO-PRACTICE-085, TLC-SO-VALUES-094
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-064, TLC-SO-PRACTICE-085, TLC-SO-VALUES-094
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-LIVED-EXPERIENCE-064, TLC-SO-PRACTICE-085, TLC-SO-VALUES-094
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

## TLC-HR-0031

### Identité

- decision_id : `TLC-HR-0031`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0031 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRACTICE-059`, `TLC-SO-RELATIONS-067`, `TLC-SO-VALUES-058`
- Objets : `TLC-SO-PRACTICE-059`, `TLC-SO-RELATIONS-067`, `TLC-SO-VALUES-058`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/13-practice.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: cultivation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-PRACTICE-059 — Cultivation (Concept), référence maths/13-practice.md:39
- TLC-SO-RELATIONS-067 — Cultivation (Concept), référence maths/15-relations.md:124
- TLC-SO-VALUES-058 — Cultivation (Concept), référence maths/09-values.md:42
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-059`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-067`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-058`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRACTICE-059, TLC-SO-RELATIONS-067, TLC-SO-VALUES-058
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRACTICE-059, TLC-SO-RELATIONS-067, TLC-SO-VALUES-058
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRACTICE-059, TLC-SO-RELATIONS-067, TLC-SO-VALUES-058
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
