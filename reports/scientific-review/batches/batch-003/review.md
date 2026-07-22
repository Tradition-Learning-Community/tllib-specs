# batch-003 — Revue prioritaire des rapprochements

État : `pending`
Décisions : 13
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `high`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0053

### Identité

- decision_id : `TLC-HR-0053`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0053 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-098`, `TLC-SO-COMPETENCIES-108`, `TLC-SO-COMPETENCIES-109`, `TLC-SO-COMPETENCIES-110`, `TLC-SO-COMPETENCIES-111`, `TLC-SO-VALUES-102`
- Objets : `TLC-SO-CAPACITIES-098`, `TLC-SO-COMPETENCIES-108`, `TLC-SO-COMPETENCIES-109`, `TLC-SO-COMPETENCIES-110`, `TLC-SO-COMPETENCIES-111`, `TLC-SO-VALUES-102`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation fondements axiomatiques
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [DifferentialEquation, Equation]}
- TLC-SO-CAPACITIES-098 — Équation — Fondements axiomatiques (DifferentialEquation), référence maths/11-capacities.md:248
- TLC-SO-COMPETENCIES-108 — Équation — Fondements axiomatiques (Equation), référence maths/12-competencies.md:257
- TLC-SO-COMPETENCIES-109 — Équation — Fondements axiomatiques (Equation), référence maths/12-competencies.md:263
- TLC-SO-COMPETENCIES-110 — Équation — Fondements axiomatiques (Equation), référence maths/12-competencies.md:269
- TLC-SO-COMPETENCIES-111 — Équation — Fondements axiomatiques (Equation), référence maths/12-competencies.md:275
- TLC-SO-VALUES-102 — Équation — Fondements axiomatiques (DifferentialEquation), référence maths/09-values.md:226
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0053`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-098`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-108`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-109`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-110`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-111`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-102`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-098, TLC-SO-COMPETENCIES-108, TLC-SO-COMPETENCIES-109, TLC-SO-COMPETENCIES-110, TLC-SO-COMPETENCIES-111, TLC-SO-VALUES-102
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-098, TLC-SO-COMPETENCIES-108, TLC-SO-COMPETENCIES-109, TLC-SO-COMPETENCIES-110, TLC-SO-COMPETENCIES-111, TLC-SO-VALUES-102
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-098, TLC-SO-COMPETENCIES-108, TLC-SO-COMPETENCIES-109, TLC-SO-COMPETENCIES-110, TLC-SO-COMPETENCIES-111, TLC-SO-VALUES-102
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0041

### Identité

- decision_id : `TLC-HR-0041`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0041 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-005`, `TLC-SO-COMPETENCIES-005`, `TLC-SO-LIVED-EXPERIENCE-005`, `TLC-SO-PRACTICE-005`, `TLC-SO-VALUES-005`
- Objets : `TLC-SO-CAPACITIES-005`, `TLC-SO-COMPETENCIES-005`, `TLC-SO-LIVED-EXPERIENCE-005`, `TLC-SO-PRACTICE-005`, `TLC-SO-VALUES-005`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: domaines de validite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Function, Set, State]}
- TLC-SO-CAPACITIES-005 — Domaines de validité (Function), référence maths/11-capacities.md:41
- TLC-SO-COMPETENCIES-005 — Domaines de validité (Set), référence maths/12-competencies.md:54
- TLC-SO-LIVED-EXPERIENCE-005 — Domaines de validité (Set), référence maths/14-lived-experience.md:40
- TLC-SO-PRACTICE-005 — Domaines de validité (Concept), référence maths/13-practice.md:43
- TLC-SO-VALUES-005 — Domaines de validité (State), référence maths/09-values.md:46
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0041`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-005`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-005, TLC-SO-COMPETENCIES-005, TLC-SO-LIVED-EXPERIENCE-005, TLC-SO-PRACTICE-005, TLC-SO-VALUES-005
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-005, TLC-SO-COMPETENCIES-005, TLC-SO-LIVED-EXPERIENCE-005, TLC-SO-PRACTICE-005, TLC-SO-VALUES-005
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-005, TLC-SO-COMPETENCIES-005, TLC-SO-LIVED-EXPERIENCE-005, TLC-SO-PRACTICE-005, TLC-SO-VALUES-005
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0060

### Identité

- decision_id : `TLC-HR-0060`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0060 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-042`, `TLC-SO-COMPETENCIES-043`, `TLC-SO-LIVED-EXPERIENCE-037`, `TLC-SO-VALUES-037`
- Objets : `TLC-SO-CAPACITIES-042`, `TLC-SO-COMPETENCIES-043`, `TLC-SO-LIVED-EXPERIENCE-037`, `TLC-SO-VALUES-037`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: espaces et structures
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Example, Metric]}
- TLC-SO-CAPACITIES-042 — Espaces et structures (Metric), référence maths/11-capacities.md:233
- TLC-SO-COMPETENCIES-043 — Espaces et structures (Metric), référence maths/12-competencies.md:245
- TLC-SO-LIVED-EXPERIENCE-037 — Espaces et structures (Example), référence maths/14-lived-experience.md:151
- TLC-SO-VALUES-037 — Espaces et structures (Metric), référence maths/09-values.md:213
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0060`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-042`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-043`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-037`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-037`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-042, TLC-SO-COMPETENCIES-043, TLC-SO-LIVED-EXPERIENCE-037, TLC-SO-VALUES-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-042, TLC-SO-COMPETENCIES-043, TLC-SO-LIVED-EXPERIENCE-037, TLC-SO-VALUES-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-042, TLC-SO-COMPETENCIES-043, TLC-SO-LIVED-EXPERIENCE-037, TLC-SO-VALUES-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0137

### Identité

- decision_id : `TLC-HR-0137`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0137 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-044`, `TLC-SO-COMPETENCIES-045`, `TLC-SO-LIVED-EXPERIENCE-040`, `TLC-SO-VALUES-039`
- Objets : `TLC-SO-CAPACITIES-044`, `TLC-SO-COMPETENCIES-045`, `TLC-SO-LIVED-EXPERIENCE-040`, `TLC-SO-VALUES-039`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: theoremes fondamentaux
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Axiom, Theorem]}
- TLC-SO-CAPACITIES-044 — Théorèmes fondamentaux (Theorem), référence maths/11-capacities.md:253
- TLC-SO-COMPETENCIES-045 — Théorèmes fondamentaux (Theorem), référence maths/12-competencies.md:280
- TLC-SO-LIVED-EXPERIENCE-040 — Théorèmes fondamentaux (Axiom), référence maths/14-lived-experience.md:175
- TLC-SO-VALUES-039 — Théorèmes fondamentaux (Theorem), référence maths/09-values.md:235
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0137`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-044`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-045`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-040`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-039`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-044, TLC-SO-COMPETENCIES-045, TLC-SO-LIVED-EXPERIENCE-040, TLC-SO-VALUES-039
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-044, TLC-SO-COMPETENCIES-045, TLC-SO-LIVED-EXPERIENCE-040, TLC-SO-VALUES-039
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-044, TLC-SO-COMPETENCIES-045, TLC-SO-LIVED-EXPERIENCE-040, TLC-SO-VALUES-039
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0115

### Identité

- decision_id : `TLC-HR-0115`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0115 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-030`, `TLC-SO-COMPETENCIES-031`, `TLC-SO-LIVED-EXPERIENCE-025`, `TLC-SO-VIRTUES-031`
- Objets : `TLC-SO-CAPACITIES-030`, `TLC-SO-COMPETENCIES-031`, `TLC-SO-LIVED-EXPERIENCE-025`, `TLC-SO-VIRTUES-031`
- Relations : aucune
- Termes : aucun
- Sources : `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: progression vers la maitrise
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Constraint]}
- TLC-SO-CAPACITIES-030 — Progression vers la maîtrise (Constraint), référence maths/11-capacities.md:175
- TLC-SO-COMPETENCIES-031 — Progression vers la maîtrise (Constraint), référence maths/12-competencies.md:184
- TLC-SO-LIVED-EXPERIENCE-025 — Progression vers la maîtrise (Concept), référence maths/14-lived-experience.md:112
- TLC-SO-VIRTUES-031 — Progression vers la maîtrise (Concept), référence maths/10-virtues.md:174
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0115`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-030`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-025`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-031`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-030, TLC-SO-COMPETENCIES-031, TLC-SO-LIVED-EXPERIENCE-025, TLC-SO-VIRTUES-031
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-030, TLC-SO-COMPETENCIES-031, TLC-SO-LIVED-EXPERIENCE-025, TLC-SO-VIRTUES-031
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-030, TLC-SO-COMPETENCIES-031, TLC-SO-LIVED-EXPERIENCE-025, TLC-SO-VIRTUES-031
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0009

### Identité

- decision_id : `TLC-HR-0009`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0009 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-019`, `TLC-SO-VIRTUES-016`
- Objets : `TLC-SO-COMPETENCIES-019`, `TLC-SO-VIRTUES-016`
- Relations : aucune
- Termes : aucun
- Sources : `maths/10-virtues.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: apprentissage observationnel et imitation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Assumption, Concept]}
- TLC-SO-COMPETENCIES-019 — Apprentissage observationnel et imitation (Concept), référence maths/12-competencies.md:113
- TLC-SO-VIRTUES-016 — Apprentissage observationnel et imitation (Assumption), référence maths/10-virtues.md:92
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0009`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-019`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-016`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-019, TLC-SO-VIRTUES-016
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-019, TLC-SO-VIRTUES-016
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-019, TLC-SO-VIRTUES-016
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0016

### Identité

- decision_id : `TLC-HR-0016`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0016 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-037`, `TLC-SO-COMPETENCIES-038`, `TLC-SO-PRACTICE-037`
- Objets : `TLC-SO-CAPACITIES-037`, `TLC-SO-COMPETENCIES-038`, `TLC-SO-PRACTICE-037`
- Relations : aucune
- Termes : aucun
- Sources : `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: coherence et coordination entre disciples
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Metric]}
- TLC-SO-CAPACITIES-037 — Cohérence et coordination entre Disciples (Concept), référence maths/11-capacities.md:210
- TLC-SO-COMPETENCIES-038 — Cohérence et coordination entre Disciples (Metric), référence maths/12-competencies.md:220
- TLC-SO-PRACTICE-037 — Cohérence et coordination entre Disciples (Concept), référence maths/13-practice.md:196
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0016`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-037`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-038`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-037`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-037, TLC-SO-COMPETENCIES-038, TLC-SO-PRACTICE-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-037, TLC-SO-COMPETENCIES-038, TLC-SO-PRACTICE-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-037, TLC-SO-COMPETENCIES-038, TLC-SO-PRACTICE-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0001

### Identité

- decision_id : `TLC-HR-0001`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0001 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-028`, `TLC-SO-LIVED-EXPERIENCE-022`
- Objets : `TLC-SO-COMPETENCIES-028`, `TLC-SO-LIVED-EXPERIENCE-022`
- Relations : aucune
- Termes : aucun
- Sources : `maths/12-competencies.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: acquisition a court terme
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, State]}
- TLC-SO-COMPETENCIES-028 — Acquisition à court terme (Concept), référence maths/12-competencies.md:164
- TLC-SO-LIVED-EXPERIENCE-022 — Acquisition à court terme (State), référence maths/14-lived-experience.md:97
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0001`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-028`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-022`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-028, TLC-SO-LIVED-EXPERIENCE-022
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-028, TLC-SO-LIVED-EXPERIENCE-022
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-028, TLC-SO-LIVED-EXPERIENCE-022
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`requires_scientific_review` — reprise de l’audit, non normative.

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

## TLC-HR-0091

### Identité

- decision_id : `TLC-HR-0091`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0091 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMMUNITY-036`, `TLC-SO-MASTER-023`
- Objets : `TLC-SO-COMMUNITY-036`, `TLC-SO-MASTER-023`
- Relations : aucune
- Termes : aucun
- Sources : `maths/00-master.md`, `maths/02-community.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: invariant de transmission
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Invariant]}
- TLC-SO-COMMUNITY-036 — Invariant de transmission (Invariant), référence maths/02-community.md:95
- TLC-SO-MASTER-023 — Invariant de transmission (Invariant), référence maths/00-master.md:145
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0091`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMMUNITY-036`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MASTER-023`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMMUNITY-036, TLC-SO-MASTER-023
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMMUNITY-036, TLC-SO-MASTER-023
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMMUNITY-036, TLC-SO-MASTER-023
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

## TLC-HR-0092

### Identité

- decision_id : `TLC-HR-0092`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0092 ?

### Éléments concernés

- Identifiants : `TLC-SO-DISCIPLE-013`, `TLC-SO-INVARIANTS-007`
- Objets : `TLC-SO-DISCIPLE-013`, `TLC-SO-INVARIANTS-007`
- Relations : aucune
- Termes : aucun
- Sources : `maths/01-disciple.md`, `maths/04-invariants.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: invariants du disciple
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Invariant]}
- TLC-SO-DISCIPLE-013 — Invariants du Disciple (Invariant), référence maths/01-disciple.md:131
- TLC-SO-INVARIANTS-007 — Invariants du Disciple (Invariant), référence maths/04-invariants.md:59
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0092`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DISCIPLE-013`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-007`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-DISCIPLE-013, TLC-SO-INVARIANTS-007
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-DISCIPLE-013, TLC-SO-INVARIANTS-007
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-DISCIPLE-013, TLC-SO-INVARIANTS-007
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

## TLC-HR-0052

### Identité

- decision_id : `TLC-HR-0052`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0052 ?

### Éléments concernés

- Identifiants : `TLC-SO-DISCIPLE-052`, `TLC-SO-DYNAMICS-020`
- Objets : `TLC-SO-DISCIPLE-052`, `TLC-SO-DYNAMICS-020`
- Relations : aucune
- Termes : aucun
- Sources : `maths/01-disciple.md`, `maths/05-dynamics.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation evolution par trajectoire mathcal t
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [StochasticEquation]}
- TLC-SO-DISCIPLE-052 — Équation — Évolution par trajectoire $\mathcal{T}$ (StochasticEquation), référence maths/01-disciple.md:152
- TLC-SO-DYNAMICS-020 — Équation — Évolution par trajectoire $\mathcal{T}$ (StochasticEquation), référence maths/05-dynamics.md:64
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0052`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DISCIPLE-052`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DYNAMICS-020`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-DISCIPLE-052, TLC-SO-DYNAMICS-020
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-DISCIPLE-052, TLC-SO-DYNAMICS-020
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-DISCIPLE-052, TLC-SO-DYNAMICS-020
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

## TLC-HR-0062

### Identité

- decision_id : `TLC-HR-0062`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0062 ?

### Éléments concernés

- Identifiants : `TLC-SO-DISCIPLE-015`, `TLC-SO-DYNAMICS-008`
- Objets : `TLC-SO-DISCIPLE-015`, `TLC-SO-DYNAMICS-008`
- Relations : aucune
- Termes : aucun
- Sources : `maths/01-disciple.md`, `maths/05-dynamics.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: evolution par trajectoire mathcal t
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-DISCIPLE-015 — Évolution par trajectoire $\mathcal{T}$ (Concept), référence maths/01-disciple.md:151
- TLC-SO-DYNAMICS-008 — Évolution par trajectoire $\mathcal{T}$ (Concept), référence maths/05-dynamics.md:62
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0062`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DISCIPLE-015`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DYNAMICS-008`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-DISCIPLE-015, TLC-SO-DYNAMICS-008
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-DISCIPLE-015, TLC-SO-DYNAMICS-008
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-DISCIPLE-015, TLC-SO-DYNAMICS-008
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

## TLC-HR-0141

### Identité

- decision_id : `TLC-HR-0141`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0141 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMMUNITY-055`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-060`, `TLC-SO-MESSAGE-059`, `TLC-SO-MESSAGE-071`
- Objets : `TLC-SO-COMMUNITY-055`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-060`, `TLC-SO-MESSAGE-059`, `TLC-SO-MESSAGE-071`
- Relations : aucune
- Termes : aucun
- Sources : `maths/02-community.md`, `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: transmission
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-COMMUNITY-055 — Transmission (Concept), référence maths/02-community.md:155
- TLC-SO-HUIT-DIMENSIONS-DE-TL-060 — Transmission (Concept), référence maths/03-huit-dimensions-de-tl.md:49
- TLC-SO-MESSAGE-059 — Transmission (Concept), référence maths/07-message.md:116
- TLC-SO-MESSAGE-071 — Transmission (Concept), référence maths/07-message.md:136
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0141`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMMUNITY-055`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-060`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-059`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-071`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMMUNITY-055, TLC-SO-HUIT-DIMENSIONS-DE-TL-060, TLC-SO-MESSAGE-059, TLC-SO-MESSAGE-071
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMMUNITY-055, TLC-SO-HUIT-DIMENSIONS-DE-TL-060, TLC-SO-MESSAGE-059, TLC-SO-MESSAGE-071
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMMUNITY-055, TLC-SO-HUIT-DIMENSIONS-DE-TL-060, TLC-SO-MESSAGE-059, TLC-SO-MESSAGE-071
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
