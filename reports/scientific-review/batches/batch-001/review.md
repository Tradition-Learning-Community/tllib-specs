# batch-001 — Revue transversale finale et limites documentaires

État : `pending`
Décisions : 13
Catégorie de paquet : `mixed_scientific_review`
Priorité maximale : `high`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0146

### Identité

- decision_id : `TLC-HR-0146`
- catégorie d’origine : `traceability`
- catégorie normalisée : `source_coverage`
- justification du classement : La question porte sur les sections signalées par l’audit de couverture et sur une éventuelle réextraction ciblée.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Les trous de couverture probables doivent-ils donner lieu à une extraction ciblée ?

### Éléments concernés

- Identifiants : `maths/00-master.md`, `maths/01-disciple.md`, `maths/02-community.md`, `maths/03-huit-dimensions-de-tl.md`, `maths/04-invariants.md`, `maths/05-dynamics.md`, `maths/06-theorems.md`, `maths/07-message.md`, `maths/08-principle.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`, `maths/15-relations.md`
- Objets : aucun
- Relations : aucune
- Termes : aucun
- Sources : `maths/00-master.md`, `maths/01-disciple.md`, `maths/02-community.md`, `maths/03-huit-dimensions-de-tl.md`, `maths/04-invariants.md`, `maths/05-dynamics.md`, `maths/06-theorems.md`, `maths/07-message.md`, `maths/08-principle.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`, `maths/15-relations.md`

### Éléments de preuve

- L’audit contient 496 signaux de couverture sur 16 sources.
- Le rapport de dépôt conclut à 16 paquets complets et à 0 anomalie structurelle ; les signaux restent des cibles documentaires à examiner.
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `reports/scientific-consolidation/source-coverage-issues.yaml`
- Référence : `reports/scientific-consolidation/repository-audit.md`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `request_targeted_reextraction` — Réviser uniquement les sections signalées.
- `mark_documentary_issue` — Conserver les trous comme limites connues.

### Conséquences

#### `request_targeted_reextraction`

- Objets touchés : aucun directement identifié
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : oui, ciblée.

#### `mark_documentary_issue`

- Objets touchés : aucun directement identifié
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

### Recommandation candidate

`targeted_revision` — reprise de l’audit, non normative.

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

## TLC-HR-0033

### Identité

- decision_id : `TLC-HR-0033`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0033 ?

### Éléments concernés

- Identifiants : `TLC-SO-DISCIPLE-002`, `TLC-SO-PRINCIPLE-002`
- Objets : `TLC-SO-DISCIPLE-002`, `TLC-SO-PRINCIPLE-002`
- Relations : aucune
- Termes : aucun
- Sources : `maths/01-disciple.md`, `maths/08-principle.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: definition conceptuelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Definition, Invariant]}
- TLC-SO-DISCIPLE-002 — Définition conceptuelle (Definition), référence maths/01-disciple.md:3
- TLC-SO-PRINCIPLE-002 — Définition conceptuelle (Invariant), référence maths/08-principle.md:3
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0033`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DISCIPLE-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-002`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-DISCIPLE-002, TLC-SO-PRINCIPLE-002
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-DISCIPLE-002, TLC-SO-PRINCIPLE-002
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-DISCIPLE-002, TLC-SO-PRINCIPLE-002
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

## TLC-HR-0088

### Identité

- decision_id : `TLC-HR-0088`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0088 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMMUNITY-012`, `TLC-SO-DYNAMICS-014`
- Objets : `TLC-SO-COMMUNITY-012`, `TLC-SO-DYNAMICS-014`
- Relations : aucune
- Termes : aucun
- Sources : `maths/02-community.md`, `maths/05-dynamics.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: interactions avec le maitre et le disciple
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Operator]}
- TLC-SO-COMMUNITY-012 — Interactions avec le Maître et le Disciple (Concept), référence maths/02-community.md:121
- TLC-SO-DYNAMICS-014 — Interactions avec le Maître et le Disciple (Operator), référence maths/05-dynamics.md:136
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0088`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMMUNITY-012`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-DYNAMICS-014`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMMUNITY-012, TLC-SO-DYNAMICS-014
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMMUNITY-012, TLC-SO-DYNAMICS-014
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMMUNITY-012, TLC-SO-DYNAMICS-014
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

## TLC-HR-0032

### Identité

- decision_id : `TLC-HR-0032`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0032 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-003`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-008`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-013`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-017`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-022`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-026`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-030`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-034`, `TLC-SO-INVARIANTS-017`, `TLC-SO-INVARIANTS-022`, `TLC-SO-INVARIANTS-027`, `TLC-SO-INVARIANTS-035`, `TLC-SO-INVARIANTS-040`, `TLC-SO-INVARIANTS-045`, `TLC-SO-INVARIANTS-053`, `TLC-SO-INVARIANTS-058`, `TLC-SO-INVARIANTS-062`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-003`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-008`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-013`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-017`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-022`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-026`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-030`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-034`, `TLC-SO-INVARIANTS-017`, `TLC-SO-INVARIANTS-022`, `TLC-SO-INVARIANTS-027`, `TLC-SO-INVARIANTS-035`, `TLC-SO-INVARIANTS-040`, `TLC-SO-INVARIANTS-045`, `TLC-SO-INVARIANTS-053`, `TLC-SO-INVARIANTS-058`, `TLC-SO-INVARIANTS-062`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/04-invariants.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: definition
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Definition, Invariant]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-003 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:20
- TLC-SO-HUIT-DIMENSIONS-DE-TL-008 — Définition (Invariant), référence maths/03-huit-dimensions-de-tl.md:54
- TLC-SO-HUIT-DIMENSIONS-DE-TL-013 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:88
- TLC-SO-HUIT-DIMENSIONS-DE-TL-017 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:118
- TLC-SO-HUIT-DIMENSIONS-DE-TL-022 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:159
- TLC-SO-HUIT-DIMENSIONS-DE-TL-026 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:189
- TLC-SO-HUIT-DIMENSIONS-DE-TL-030 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:216
- TLC-SO-HUIT-DIMENSIONS-DE-TL-034 — Définition (Definition), référence maths/03-huit-dimensions-de-tl.md:240
- TLC-SO-INVARIANTS-017 — Définition (Definition), référence maths/04-invariants.md:13
- TLC-SO-INVARIANTS-022 — Définition (Definition), référence maths/04-invariants.md:26
- TLC-SO-INVARIANTS-027 — Définition (Definition), référence maths/04-invariants.md:40
- TLC-SO-INVARIANTS-035 — Définition (Definition), référence maths/04-invariants.md:65
- TLC-SO-INVARIANTS-040 — Définition (Definition), référence maths/04-invariants.md:78
- TLC-SO-INVARIANTS-045 — Définition (Definition), référence maths/04-invariants.md:91
- TLC-SO-INVARIANTS-053 — Définition (Definition), référence maths/04-invariants.md:116
- TLC-SO-INVARIANTS-058 — Définition (Definition), référence maths/04-invariants.md:130
- TLC-SO-INVARIANTS-062 — Définition (Definition), référence maths/04-invariants.md:140
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0032`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-003`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-008`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-013`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-017`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-022`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-030`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-034`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-017`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-022`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-027`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-035`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-040`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-045`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-053`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-058`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-INVARIANTS-062`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-003, TLC-SO-HUIT-DIMENSIONS-DE-TL-008, TLC-SO-HUIT-DIMENSIONS-DE-TL-013, TLC-SO-HUIT-DIMENSIONS-DE-TL-017, TLC-SO-HUIT-DIMENSIONS-DE-TL-022, TLC-SO-HUIT-DIMENSIONS-DE-TL-026, TLC-SO-HUIT-DIMENSIONS-DE-TL-030, TLC-SO-HUIT-DIMENSIONS-DE-TL-034, TLC-SO-INVARIANTS-017, TLC-SO-INVARIANTS-022, TLC-SO-INVARIANTS-027, TLC-SO-INVARIANTS-035, TLC-SO-INVARIANTS-040, TLC-SO-INVARIANTS-045, TLC-SO-INVARIANTS-053, TLC-SO-INVARIANTS-058, TLC-SO-INVARIANTS-062
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-003, TLC-SO-HUIT-DIMENSIONS-DE-TL-008, TLC-SO-HUIT-DIMENSIONS-DE-TL-013, TLC-SO-HUIT-DIMENSIONS-DE-TL-017, TLC-SO-HUIT-DIMENSIONS-DE-TL-022, TLC-SO-HUIT-DIMENSIONS-DE-TL-026, TLC-SO-HUIT-DIMENSIONS-DE-TL-030, TLC-SO-HUIT-DIMENSIONS-DE-TL-034, TLC-SO-INVARIANTS-017, TLC-SO-INVARIANTS-022, TLC-SO-INVARIANTS-027, TLC-SO-INVARIANTS-035, TLC-SO-INVARIANTS-040, TLC-SO-INVARIANTS-045, TLC-SO-INVARIANTS-053, TLC-SO-INVARIANTS-058, TLC-SO-INVARIANTS-062
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-003, TLC-SO-HUIT-DIMENSIONS-DE-TL-008, TLC-SO-HUIT-DIMENSIONS-DE-TL-013, TLC-SO-HUIT-DIMENSIONS-DE-TL-017, TLC-SO-HUIT-DIMENSIONS-DE-TL-022, TLC-SO-HUIT-DIMENSIONS-DE-TL-026, TLC-SO-HUIT-DIMENSIONS-DE-TL-030, TLC-SO-HUIT-DIMENSIONS-DE-TL-034, TLC-SO-INVARIANTS-017, TLC-SO-INVARIANTS-022, TLC-SO-INVARIANTS-027, TLC-SO-INVARIANTS-035, TLC-SO-INVARIANTS-040, TLC-SO-INVARIANTS-045, TLC-SO-INVARIANTS-053, TLC-SO-INVARIANTS-058, TLC-SO-INVARIANTS-062
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

## TLC-HR-0111

### Identité

- decision_id : `TLC-HR-0111`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0111 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-039`, `TLC-SO-THEOREMS-019`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-039`, `TLC-SO-THEOREMS-019`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/06-theorems.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: principes
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Invariant]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-039 — Principes (Invariant), référence maths/03-huit-dimensions-de-tl.md:10
- TLC-SO-THEOREMS-019 — Principes (Concept), référence maths/06-theorems.md:82
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0111`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-039`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-THEOREMS-019`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-039, TLC-SO-THEOREMS-019
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-039, TLC-SO-THEOREMS-019
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-039, TLC-SO-THEOREMS-019
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

## TLC-HR-0095

### Identité

- decision_id : `TLC-HR-0095`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0095 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-002`, `TLC-SO-MESSAGE-001`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-002`, `TLC-SO-MESSAGE-001`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: le message message
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Entity]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-002 — Le Message (Message) (Concept), référence maths/03-huit-dimensions-de-tl.md:18
- TLC-SO-MESSAGE-001 — Le Message (Message) (Entity), référence maths/07-message.md:1
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0095`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-002`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-001`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-002, TLC-SO-MESSAGE-001
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-002, TLC-SO-MESSAGE-001
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-002, TLC-SO-MESSAGE-001
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

## TLC-HR-0140

### Identité

- decision_id : `TLC-HR-0140`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0140 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-051`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-066`, `TLC-SO-MESSAGE-030`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-051`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-066`, `TLC-SO-MESSAGE-030`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: transmissibilite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Space]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-051 — Transmissibilité (Space), référence maths/03-huit-dimensions-de-tl.md:33
- TLC-SO-HUIT-DIMENSIONS-DE-TL-066 — Transmissibilité (Concept), référence maths/03-huit-dimensions-de-tl.md:69
- TLC-SO-MESSAGE-030 — Transmissibilité (Concept), référence maths/07-message.md:22
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0140`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-051`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-066`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-030`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-051, TLC-SO-HUIT-DIMENSIONS-DE-TL-066, TLC-SO-MESSAGE-030
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-051, TLC-SO-HUIT-DIMENSIONS-DE-TL-066, TLC-SO-MESSAGE-030
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-051, TLC-SO-HUIT-DIMENSIONS-DE-TL-066, TLC-SO-MESSAGE-030
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

## TLC-HR-0029

### Identité

- decision_id : `TLC-HR-0029`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0029 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-070`, `TLC-SO-PRINCIPLE-072`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-070`, `TLC-SO-PRINCIPLE-072`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/08-principle.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: cristallisation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, State]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-070 — Cristallisation (Concept), référence maths/03-huit-dimensions-de-tl.md:83
- TLC-SO-PRINCIPLE-072 — Cristallisation (State), référence maths/08-principle.md:142
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0029`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-070`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-072`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-070, TLC-SO-PRINCIPLE-072
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-070, TLC-SO-PRINCIPLE-072
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-070, TLC-SO-PRINCIPLE-072
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

## TLC-HR-0042

### Identité

- decision_id : `TLC-HR-0042`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0042 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-011`, `TLC-SO-PRINCIPLE-020`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-011`, `TLC-SO-PRINCIPLE-020`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/08-principle.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: dynamique principe message
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Constraint]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-011 — Dynamique Principe‑Message (Constraint), référence maths/03-huit-dimensions-de-tl.md:77
- TLC-SO-PRINCIPLE-020 — Dynamique Principe‑Message (Concept), référence maths/08-principle.md:120
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0042`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-011`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-020`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-011, TLC-SO-PRINCIPLE-020
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-011, TLC-SO-PRINCIPLE-020
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-011, TLC-SO-PRINCIPLE-020
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

## TLC-HR-0127

### Identité

- decision_id : `TLC-HR-0127`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0127 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-064`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-079`, `TLC-SO-PRINCIPLE-009`, `TLC-SO-VIRTUES-063`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-064`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-079`, `TLC-SO-PRINCIPLE-009`, `TLC-SO-VIRTUES-063`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/08-principle.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: stabilite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, State]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-064 — Stabilité (State), référence maths/03-huit-dimensions-de-tl.md:67
- TLC-SO-HUIT-DIMENSIONS-DE-TL-079 — Stabilité (Concept), référence maths/03-huit-dimensions-de-tl.md:125
- TLC-SO-PRINCIPLE-009 — Stabilité (Concept), référence maths/08-principle.md:58
- TLC-SO-VIRTUES-063 — Stabilité (Concept), référence maths/10-virtues.md:27
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0127`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-064`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-079`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-009`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-063`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-064, TLC-SO-HUIT-DIMENSIONS-DE-TL-079, TLC-SO-PRINCIPLE-009, TLC-SO-VIRTUES-063
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-064, TLC-SO-HUIT-DIMENSIONS-DE-TL-079, TLC-SO-PRINCIPLE-009, TLC-SO-VIRTUES-063
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-064, TLC-SO-HUIT-DIMENSIONS-DE-TL-079, TLC-SO-PRINCIPLE-009, TLC-SO-VIRTUES-063
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

## TLC-HR-0083

### Identité

- decision_id : `TLC-HR-0083`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0083 ?

### Éléments concernés

- Identifiants : `TLC-SO-COMPETENCIES-056`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-082`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-099`, `TLC-SO-VALUES-080`, `TLC-SO-VIRTUES-066`, `TLC-SO-VIRTUES-124`, `TLC-SO-VIRTUES-144`
- Objets : `TLC-SO-COMPETENCIES-056`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-082`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-099`, `TLC-SO-VALUES-080`, `TLC-SO-VIRTUES-066`, `TLC-SO-VIRTUES-124`, `TLC-SO-VIRTUES-144`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/09-values.md`, `maths/10-virtues.md`, `maths/12-competencies.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: integration
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Function, Relation]}
- TLC-SO-COMPETENCIES-056 — Intégration (Relation), référence maths/12-competencies.md:39
- TLC-SO-HUIT-DIMENSIONS-DE-TL-082 — Intégration (Concept), référence maths/03-huit-dimensions-de-tl.md:128
- TLC-SO-HUIT-DIMENSIONS-DE-TL-099 — Intégration (Concept), référence maths/03-huit-dimensions-de-tl.md:207
- TLC-SO-VALUES-080 — Intégration (Function), référence maths/09-values.md:114
- TLC-SO-VIRTUES-066 — Intégration (Concept), référence maths/10-virtues.md:30
- TLC-SO-VIRTUES-124 — Intégration (Concept), référence maths/10-virtues.md:133
- TLC-SO-VIRTUES-144 — Intégration (Concept), référence maths/10-virtues.md:165
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0083`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-056`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-082`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-099`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-080`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-066`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-124`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-144`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-COMPETENCIES-056, TLC-SO-HUIT-DIMENSIONS-DE-TL-082, TLC-SO-HUIT-DIMENSIONS-DE-TL-099, TLC-SO-VALUES-080, TLC-SO-VIRTUES-066, TLC-SO-VIRTUES-124, TLC-SO-VIRTUES-144
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-COMPETENCIES-056, TLC-SO-HUIT-DIMENSIONS-DE-TL-082, TLC-SO-HUIT-DIMENSIONS-DE-TL-099, TLC-SO-VALUES-080, TLC-SO-VIRTUES-066, TLC-SO-VIRTUES-124, TLC-SO-VIRTUES-144
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-COMPETENCIES-056, TLC-SO-HUIT-DIMENSIONS-DE-TL-082, TLC-SO-HUIT-DIMENSIONS-DE-TL-099, TLC-SO-VALUES-080, TLC-SO-VIRTUES-066, TLC-SO-VIRTUES-124, TLC-SO-VIRTUES-144
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

## TLC-HR-0100

### Identité

- decision_id : `TLC-HR-0100`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0100 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-057`, `TLC-SO-COMPETENCIES-064`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-083`, `TLC-SO-PRACTICE-061`, `TLC-SO-VIRTUES-067`
- Objets : `TLC-SO-CAPACITIES-057`, `TLC-SO-COMPETENCIES-064`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-083`, `TLC-SO-PRACTICE-061`, `TLC-SO-VIRTUES-067`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/10-virtues.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: mesurabilite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Concept, Metric, Relation]}
- TLC-SO-CAPACITIES-057 — Mesurabilité (Concept), référence maths/11-capacities.md:38
- TLC-SO-COMPETENCIES-064 — Mesurabilité (Concept), référence maths/12-competencies.md:52
- TLC-SO-HUIT-DIMENSIONS-DE-TL-083 — Mesurabilité (Concept), référence maths/03-huit-dimensions-de-tl.md:129
- TLC-SO-PRACTICE-061 — Mesurabilité (Relation), référence maths/13-practice.md:41
- TLC-SO-VIRTUES-067 — Mesurabilité (Metric), référence maths/10-virtues.md:31
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0100`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-057`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-064`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-083`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-061`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-067`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-057, TLC-SO-COMPETENCIES-064, TLC-SO-HUIT-DIMENSIONS-DE-TL-083, TLC-SO-PRACTICE-061, TLC-SO-VIRTUES-067
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-057, TLC-SO-COMPETENCIES-064, TLC-SO-HUIT-DIMENSIONS-DE-TL-083, TLC-SO-PRACTICE-061, TLC-SO-VIRTUES-067
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-057, TLC-SO-COMPETENCIES-064, TLC-SO-HUIT-DIMENSIONS-DE-TL-083, TLC-SO-PRACTICE-061, TLC-SO-VIRTUES-067
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

## TLC-HR-0094

### Identité

- decision_id : `TLC-HR-0094`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `high`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0094 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-050`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-089`
- Objets : `TLC-SO-CAPACITIES-050`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-089`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/11-capacities.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: latence
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : high
- Différences observées : {object_types: [Axiom, Metric]}
- TLC-SO-CAPACITIES-050 — Latence (Axiom), référence maths/11-capacities.md:26
- TLC-SO-HUIT-DIMENSIONS-DE-TL-089 — Latence (Metric), référence maths/03-huit-dimensions-de-tl.md:172
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0094`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-050`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-089`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-050, TLC-SO-HUIT-DIMENSIONS-DE-TL-089
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-050, TLC-SO-HUIT-DIMENSIONS-DE-TL-089
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-050, TLC-SO-HUIT-DIMENSIONS-DE-TL-089
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
