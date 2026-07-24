# batch-002 — Revue prioritaire des rapprochements

État : `pending`
Décisions : 13
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `high`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0003

### Identité

- decision_id : `TLC-HR-0003`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0003 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-054`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-097`
- Objets : `TLC-SO-COMPETENCIES-054`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-097`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: actualisation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Space]}
- TLC-SO-COMPETENCIES-054 — Actualisation (Space), référence maths/12-competencies.md:37
- TLC-SO-HUIT-DIMENSIONS-DE-TL-097 — Actualisation (Concept), référence maths/03-huit-dimensions-de-tl.md:205
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-054`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-097`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-054, TLC-SO-HUIT-DIMENSIONS-DE-TL-097
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-054, TLC-SO-HUIT-DIMENSIONS-DE-TL-097
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-054, TLC-SO-HUIT-DIMENSIONS-DE-TL-097
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

## TLC-HR-0025

### Identité

- decision_id : `TLC-HR-0025`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0025 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-055`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-098`
- Objets : `TLC-SO-COMPETENCIES-055`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-098`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: contextualisation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Operator]}
- TLC-SO-COMPETENCIES-055 — Contextualisation (Operator), référence maths/12-competencies.md:38
- TLC-SO-HUIT-DIMENSIONS-DE-TL-098 — Contextualisation (Concept), référence maths/03-huit-dimensions-de-tl.md:206
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0025`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-055`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-098`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-055, TLC-SO-HUIT-DIMENSIONS-DE-TL-098
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-055, TLC-SO-HUIT-DIMENSIONS-DE-TL-098
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-055, TLC-SO-HUIT-DIMENSIONS-DE-TL-098
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

## TLC-HR-0084

### Identité

- decision_id : `TLC-HR-0084`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0084 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-111`, `TLC-SO-LIVED-EXPERIENCE-045`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-111`, `TLC-SO-LIVED-EXPERIENCE-045`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: integration holistique
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Space, State]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-111 — Intégration holistique (Space), référence maths/03-huit-dimensions-de-tl.md:252
- TLC-SO-LIVED-EXPERIENCE-045 — Intégration holistique (State), référence maths/14-lived-experience.md:25
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0084`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-111`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-045`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-111, TLC-SO-LIVED-EXPERIENCE-045
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-111, TLC-SO-LIVED-EXPERIENCE-045
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-111, TLC-SO-LIVED-EXPERIENCE-045
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

## TLC-HR-0098

### Identité

- decision_id : `TLC-HR-0098`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0098 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-113`, `TLC-SO-LIVED-EXPERIENCE-047`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-113`, `TLC-SO-LIVED-EXPERIENCE-047`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: memoire vivante
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, State]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-113 — Mémoire vivante (Concept), référence maths/03-huit-dimensions-de-tl.md:254
- TLC-SO-LIVED-EXPERIENCE-047 — Mémoire vivante (State), référence maths/14-lived-experience.md:27
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0098`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-113`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-047`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-113, TLC-SO-LIVED-EXPERIENCE-047
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-113, TLC-SO-LIVED-EXPERIENCE-047
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-113, TLC-SO-LIVED-EXPERIENCE-047
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

## TLC-HR-0125

### Identité

- decision_id : `TLC-HR-0125`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0125 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-112`, `TLC-SO-LIVED-EXPERIENCE-046`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-112`, `TLC-SO-LIVED-EXPERIENCE-046`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: source de legitimite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Function]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-112 — Source de légitimité (Concept), référence maths/03-huit-dimensions-de-tl.md:253
- TLC-SO-LIVED-EXPERIENCE-046 — Source de légitimité (Function), référence maths/14-lived-experience.md:26
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0125`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-112`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-046`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-112, TLC-SO-LIVED-EXPERIENCE-046
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-112, TLC-SO-LIVED-EXPERIENCE-046
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-112, TLC-SO-LIVED-EXPERIENCE-046
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

## TLC-HR-0089

### Identité

- decision_id : `TLC-HR-0089`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0089 ?

### Éléments concernés

- Identifiants : `TLC-SO-INVARIANTS-021`, `TLC-SO-INVARIANTS-026`, `TLC-SO-INVARIANTS-031`, `TLC-SO-INVARIANTS-039`, `TLC-SO-INVARIANTS-044`, `TLC-SO-INVARIANTS-049`, `TLC-SO-PRINCIPLE-059`, `TLC-SO-RELATIONS-037`
- Objets : `TLC-SO-INVARIANTS-021`, `TLC-SO-INVARIANTS-026`, `TLC-SO-INVARIANTS-031`, `TLC-SO-INVARIANTS-039`, `TLC-SO-INVARIANTS-044`, `TLC-SO-INVARIANTS-049`, `TLC-SO-PRINCIPLE-059`, `TLC-SO-RELATIONS-037`
- Relations : aucune
- Termes : aucun
- Sources : `maths/04-invariants.md`, `maths/08-principle.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: interpretation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Invariant, Relation, State]}
- TLC-SO-INVARIANTS-021 — Interprétation (State), référence maths/04-invariants.md:22
- TLC-SO-INVARIANTS-026 — Interprétation (State), référence maths/04-invariants.md:36
- TLC-SO-INVARIANTS-031 — Interprétation (Invariant), référence maths/04-invariants.md:49
- TLC-SO-INVARIANTS-039 — Interprétation (State), référence maths/04-invariants.md:74
- TLC-SO-INVARIANTS-044 — Interprétation (Invariant), référence maths/04-invariants.md:87
- TLC-SO-INVARIANTS-049 — Interprétation (Invariant), référence maths/04-invariants.md:100
- TLC-SO-PRINCIPLE-059 — Interprétation (Relation), référence maths/08-principle.md:103
- TLC-SO-RELATIONS-037 — Interprétation (State), référence maths/15-relations.md:23
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0089`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-021`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-039`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-044`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-049`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-059`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-037`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-INVARIANTS-021, TLC-SO-INVARIANTS-026, TLC-SO-INVARIANTS-031, TLC-SO-INVARIANTS-039, TLC-SO-INVARIANTS-044, TLC-SO-INVARIANTS-049, TLC-SO-PRINCIPLE-059, TLC-SO-RELATIONS-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-INVARIANTS-021, TLC-SO-INVARIANTS-026, TLC-SO-INVARIANTS-031, TLC-SO-INVARIANTS-039, TLC-SO-INVARIANTS-044, TLC-SO-INVARIANTS-049, TLC-SO-PRINCIPLE-059, TLC-SO-RELATIONS-037
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-INVARIANTS-021, TLC-SO-INVARIANTS-026, TLC-SO-INVARIANTS-031, TLC-SO-INVARIANTS-039, TLC-SO-INVARIANTS-044, TLC-SO-INVARIANTS-049, TLC-SO-PRINCIPLE-059, TLC-SO-RELATIONS-037
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

## TLC-HR-0116

### Identité

- decision_id : `TLC-HR-0116`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0116 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-003`, `TLC-SO-COMPETENCIES-003`, `TLC-SO-LIVED-EXPERIENCE-003`, `TLC-SO-MESSAGE-004`, `TLC-SO-PRACTICE-003`, `TLC-SO-VALUES-003`, `TLC-SO-VIRTUES-003`
- Objets : `TLC-SO-CAPACITIES-003`, `TLC-SO-COMPETENCIES-003`, `TLC-SO-LIVED-EXPERIENCE-003`, `TLC-SO-MESSAGE-004`, `TLC-SO-PRACTICE-003`, `TLC-SO-VALUES-003`, `TLC-SO-VIRTUES-003`
- Relations : aucune
- Termes : aucun
- Sources : `maths/07-message.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: proprietes essentielles
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Axiom, Concept, Invariant, Metric, Operator]}
- TLC-SO-CAPACITIES-003 — Propriétés essentielles (Axiom), référence maths/11-capacities.md:24
- TLC-SO-COMPETENCIES-003 — Propriétés essentielles (Operator), référence maths/12-competencies.md:35
- TLC-SO-LIVED-EXPERIENCE-003 — Propriétés essentielles (Invariant), référence maths/14-lived-experience.md:22
- TLC-SO-MESSAGE-004 — Propriétés essentielles (Concept), référence maths/07-message.md:20
- TLC-SO-PRACTICE-003 — Propriétés essentielles (Concept), référence maths/13-practice.md:24
- TLC-SO-VALUES-003 — Propriétés essentielles (Invariant), référence maths/09-values.md:28
- TLC-SO-VIRTUES-003 — Propriétés essentielles (Metric), référence maths/10-virtues.md:25
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0116`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-003`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-003, TLC-SO-COMPETENCIES-003, TLC-SO-LIVED-EXPERIENCE-003, TLC-SO-MESSAGE-004, TLC-SO-PRACTICE-003, TLC-SO-VALUES-003, TLC-SO-VIRTUES-003
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-003, TLC-SO-COMPETENCIES-003, TLC-SO-LIVED-EXPERIENCE-003, TLC-SO-MESSAGE-004, TLC-SO-PRACTICE-003, TLC-SO-VALUES-003, TLC-SO-VIRTUES-003
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-003, TLC-SO-COMPETENCIES-003, TLC-SO-LIVED-EXPERIENCE-003, TLC-SO-MESSAGE-004, TLC-SO-PRACTICE-003, TLC-SO-VALUES-003, TLC-SO-VIRTUES-003
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

## TLC-HR-0015

### Identité

- decision_id : `TLC-HR-0015`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0015 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-100`, `TLC-SO-VALUES-032`
- Objets : `TLC-SO-PRINCIPLE-100`, `TLC-SO-VALUES-032`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: coherence entre disciples
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, State]}
- TLC-SO-PRINCIPLE-100 — Cohérence entre Disciples (State), référence maths/08-principle.md:229
- TLC-SO-VALUES-032 — Cohérence entre Disciples (Concept), référence maths/09-values.md:191
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0015`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-100`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-032`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-100, TLC-SO-VALUES-032
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-100, TLC-SO-VALUES-032
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-100, TLC-SO-VALUES-032
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

## TLC-HR-0097

### Identité

- decision_id : `TLC-HR-0097`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0097 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-018`, `TLC-SO-VALUES-014`
- Objets : `TLC-SO-PRINCIPLE-018`, `TLC-SO-VALUES-014`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: memoire et stockage
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Function]}
- TLC-SO-PRINCIPLE-018 — Mémoire et stockage (Concept), référence maths/08-principle.md:107
- TLC-SO-VALUES-014 — Mémoire et stockage (Function), référence maths/09-values.md:94
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0097`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-018`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-014`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-018, TLC-SO-VALUES-014
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-018, TLC-SO-VALUES-014
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-018, TLC-SO-VALUES-014
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

## TLC-HR-0087

### Identité

- decision_id : `TLC-HR-0087`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0087 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-031`, `TLC-SO-VALUES-031`, `TLC-SO-VIRTUES-039`
- Objets : `TLC-SO-PRINCIPLE-031`, `TLC-SO-VALUES-031`, `TLC-SO-VIRTUES-039`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/09-values.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: interaction avec la communaute et transmission collective
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, State]}
- TLC-SO-PRINCIPLE-031 — Interaction avec la communauté et transmission collective (State), référence maths/08-principle.md:227
- TLC-SO-VALUES-031 — Interaction avec la communauté et transmission collective (Concept), référence maths/09-values.md:189
- TLC-SO-VIRTUES-039 — Interaction avec la communauté et transmission collective (Concept), référence maths/10-virtues.md:218
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0087`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-031`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-039`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-031, TLC-SO-VALUES-031, TLC-SO-VIRTUES-039
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-031, TLC-SO-VALUES-031, TLC-SO-VIRTUES-039
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-031, TLC-SO-VALUES-031, TLC-SO-VIRTUES-039
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

## TLC-HR-0071

### Identité

- decision_id : `TLC-HR-0071`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0071 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-081`, `TLC-SO-VIRTUES-207`
- Objets : `TLC-SO-PRINCIPLE-081`, `TLC-SO-VIRTUES-207`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: fidelite adaptative
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Invariant]}
- TLC-SO-PRINCIPLE-081 — Fidélité adaptative (Invariant), référence maths/08-principle.md:167
- TLC-SO-VIRTUES-207 — Fidélité adaptative (Concept), référence maths/10-virtues.md:312
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0071`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-081`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-207`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-081, TLC-SO-VIRTUES-207
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-081, TLC-SO-VIRTUES-207
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-081, TLC-SO-VIRTUES-207
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

## TLC-HR-0074

### Identité

- decision_id : `TLC-HR-0074`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0074 ?

### Éléments concernés

- Identifiants : `TLC-SO-PRINCIPLE-004`, `TLC-SO-RELATIONS-008`, `TLC-SO-RELATIONS-014`, `TLC-SO-RELATIONS-020`, `TLC-SO-RELATIONS-026`, `TLC-SO-RELATIONS-032`
- Objets : `TLC-SO-PRINCIPLE-004`, `TLC-SO-RELATIONS-008`, `TLC-SO-RELATIONS-014`, `TLC-SO-RELATIONS-020`, `TLC-SO-RELATIONS-026`, `TLC-SO-RELATIONS-032`
- Relations : aucune
- Termes : aucun
- Sources : `maths/08-principle.md`, `maths/15-relations.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: formalisation mathematique
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Invariant, Proof, Relation]}
- TLC-SO-PRINCIPLE-004 — Formalisation mathématique (Concept), référence maths/08-principle.md:19
- TLC-SO-RELATIONS-008 — Formalisation mathématique (Invariant), référence maths/15-relations.md:54
- TLC-SO-RELATIONS-014 — Formalisation mathématique (Relation), référence maths/15-relations.md:99
- TLC-SO-RELATIONS-020 — Formalisation mathématique (Relation), référence maths/15-relations.md:143
- TLC-SO-RELATIONS-026 — Formalisation mathématique (Proof), référence maths/15-relations.md:183
- TLC-SO-RELATIONS-032 — Formalisation mathématique (Proof), référence maths/15-relations.md:224
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0074`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-008`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-014`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-020`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-RELATIONS-032`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-PRINCIPLE-004, TLC-SO-RELATIONS-008, TLC-SO-RELATIONS-014, TLC-SO-RELATIONS-020, TLC-SO-RELATIONS-026, TLC-SO-RELATIONS-032
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-PRINCIPLE-004, TLC-SO-RELATIONS-008, TLC-SO-RELATIONS-014, TLC-SO-RELATIONS-020, TLC-SO-RELATIONS-026, TLC-SO-RELATIONS-032
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-PRINCIPLE-004, TLC-SO-RELATIONS-008, TLC-SO-RELATIONS-014, TLC-SO-RELATIONS-020, TLC-SO-RELATIONS-026, TLC-SO-RELATIONS-032
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

## TLC-HR-0081

### Identité

- decision_id : `TLC-HR-0081`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0081 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-023`, `TLC-SO-COMPETENCIES-024`, `TLC-SO-LIVED-EXPERIENCE-019`, `TLC-SO-PRACTICE-023`, `TLC-SO-VALUES-018`, `TLC-SO-VIRTUES-023`
- Objets : `TLC-SO-CAPACITIES-023`, `TLC-SO-COMPETENCIES-024`, `TLC-SO-LIVED-EXPERIENCE-019`, `TLC-SO-PRACTICE-023`, `TLC-SO-VALUES-018`, `TLC-SO-VIRTUES-023`
- Relations : aucune
- Termes : aucun
- Sources : `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: indicateurs qualitatifs
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Metric]}
- TLC-SO-CAPACITIES-023 — Indicateurs qualitatifs (Concept), référence maths/11-capacities.md:135
- TLC-SO-COMPETENCIES-024 — Indicateurs qualitatifs (Metric), référence maths/12-competencies.md:139
- TLC-SO-LIVED-EXPERIENCE-019 — Indicateurs qualitatifs (Concept), référence maths/14-lived-experience.md:85
- TLC-SO-PRACTICE-023 — Indicateurs qualitatifs (Concept), référence maths/13-practice.md:122
- TLC-SO-VALUES-018 — Indicateurs qualitatifs (Concept), référence maths/09-values.md:116
- TLC-SO-VIRTUES-023 — Indicateurs qualitatifs (Concept), référence maths/10-virtues.md:130
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0081`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-023`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-024`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-019`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-023`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-018`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-023`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-023, TLC-SO-COMPETENCIES-024, TLC-SO-LIVED-EXPERIENCE-019, TLC-SO-PRACTICE-023, TLC-SO-VALUES-018, TLC-SO-VIRTUES-023
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-023, TLC-SO-COMPETENCIES-024, TLC-SO-LIVED-EXPERIENCE-019, TLC-SO-PRACTICE-023, TLC-SO-VALUES-018, TLC-SO-VIRTUES-023
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-023, TLC-SO-COMPETENCIES-024, TLC-SO-LIVED-EXPERIENCE-019, TLC-SO-PRACTICE-023, TLC-SO-VALUES-018, TLC-SO-VIRTUES-023
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
