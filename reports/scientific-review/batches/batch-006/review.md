# batch-006 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0078

### Identité

- decision_id : `TLC-HR-0078`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0078 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-053`, `TLC-SO-MESSAGE-032`, `TLC-SO-VIRTUES-203`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-053`, `TLC-SO-MESSAGE-032`, `TLC-SO-VIRTUES-203`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: impact transformateur
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-053 — Impact transformateur (Concept), référence maths/03-huit-dimensions-de-tl.md:35
- TLC-SO-MESSAGE-032 — Impact transformateur (Concept), référence maths/07-message.md:24
- TLC-SO-VIRTUES-203 — Impact transformateur (Concept), référence maths/10-virtues.md:306
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0078`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-053`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-032`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-203`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-053, TLC-SO-MESSAGE-032, TLC-SO-VIRTUES-203
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-053, TLC-SO-MESSAGE-032, TLC-SO-VIRTUES-203
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-053, TLC-SO-MESSAGE-032, TLC-SO-VIRTUES-203
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

## TLC-HR-0077

### Identité

- decision_id : `TLC-HR-0077`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0077 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-069`, `TLC-SO-PRINCIPLE-071`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-069`, `TLC-SO-PRINCIPLE-071`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/08-principle.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: germination
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-069 — Germination (Concept), référence maths/03-huit-dimensions-de-tl.md:82
- TLC-SO-PRINCIPLE-071 — Germination (Concept), référence maths/08-principle.md:141
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0077`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-069`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-071`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-069, TLC-SO-PRINCIPLE-071
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-069, TLC-SO-PRINCIPLE-071
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-069, TLC-SO-PRINCIPLE-071
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

## TLC-HR-0126

### Identité

- decision_id : `TLC-HR-0126`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0126 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-071`, `TLC-SO-PRINCIPLE-073`, `TLC-SO-VIRTUES-145`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-071`, `TLC-SO-PRINCIPLE-073`, `TLC-SO-VIRTUES-145`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/08-principle.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: stabilisation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-071 — Stabilisation (Concept), référence maths/03-huit-dimensions-de-tl.md:84
- TLC-SO-PRINCIPLE-073 — Stabilisation (Concept), référence maths/08-principle.md:143
- TLC-SO-VIRTUES-145 — Stabilisation (Concept), référence maths/10-virtues.md:166
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0126`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-071`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRINCIPLE-073`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-145`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-071, TLC-SO-PRINCIPLE-073, TLC-SO-VIRTUES-145
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-071, TLC-SO-PRINCIPLE-073, TLC-SO-VIRTUES-145
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-071, TLC-SO-PRINCIPLE-073, TLC-SO-VIRTUES-145
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

## TLC-HR-0004

### Identité

- decision_id : `TLC-HR-0004`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0004 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-076`, `TLC-SO-VALUES-054`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-076`, `TLC-SO-VALUES-054`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: adaptabilite contextuelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-076 — Adaptabilité contextuelle (Concept), référence maths/03-huit-dimensions-de-tl.md:110
- TLC-SO-VALUES-054 — Adaptabilité contextuelle (Concept), référence maths/09-values.md:33
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-076`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-054`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-076, TLC-SO-VALUES-054
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-076, TLC-SO-VALUES-054
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-076, TLC-SO-VALUES-054
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

## TLC-HR-0008

### Identité

- decision_id : `TLC-HR-0008`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0008 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-075`, `TLC-SO-VALUES-053`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-075`, `TLC-SO-VALUES-053`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: alignement motivationnel
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-075 — Alignement motivationnel (Concept), référence maths/03-huit-dimensions-de-tl.md:109
- TLC-SO-VALUES-053 — Alignement motivationnel (Concept), référence maths/09-values.md:32
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0008`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-075`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-053`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-075, TLC-SO-VALUES-053
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-075, TLC-SO-VALUES-053
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-075, TLC-SO-VALUES-053
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

## TLC-HR-0030

### Identité

- decision_id : `TLC-HR-0030`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0030 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-077`, `TLC-SO-VALUES-055`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-077`, `TLC-SO-VALUES-055`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: croissance integrative
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-077 — Croissance intégrative (Concept), référence maths/03-huit-dimensions-de-tl.md:111
- TLC-SO-VALUES-055 — Croissance intégrative (Concept), référence maths/09-values.md:34
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0030`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-077`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-055`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-077, TLC-SO-VALUES-055
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-077, TLC-SO-VALUES-055
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-077, TLC-SO-VALUES-055
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

## TLC-HR-0090

### Identité

- decision_id : `TLC-HR-0090`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0090 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-073`, `TLC-SO-VALUES-051`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-073`, `TLC-SO-VALUES-051`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: invariance partielle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Invariant]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-073 — Invariance partielle (Invariant), référence maths/03-huit-dimensions-de-tl.md:107
- TLC-SO-VALUES-051 — Invariance partielle (Invariant), référence maths/09-values.md:30
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0090`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-073`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-051`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-073, TLC-SO-VALUES-051
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-073, TLC-SO-VALUES-051
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-073, TLC-SO-VALUES-051
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

## TLC-HR-0102

### Identité

- decision_id : `TLC-HR-0102`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0102 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-074`, `TLC-SO-VALUES-052`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-074`, `TLC-SO-VALUES-052`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/09-values.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: metastabilite hierarchique
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-074 — Métastabilité hiérarchique (Concept), référence maths/03-huit-dimensions-de-tl.md:108
- TLC-SO-VALUES-052 — Métastabilité hiérarchique (Concept), référence maths/09-values.md:31
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0102`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-074`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-052`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-074, TLC-SO-VALUES-052
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-074, TLC-SO-VALUES-052
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-074, TLC-SO-VALUES-052
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

## TLC-HR-0038

### Identité

- decision_id : `TLC-HR-0038`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0038 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-080`, `TLC-SO-VIRTUES-064`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-080`, `TLC-SO-VIRTUES-064`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: developpabilite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-080 — Développabilité (Concept), référence maths/03-huit-dimensions-de-tl.md:126
- TLC-SO-VIRTUES-064 — Développabilité (Concept), référence maths/10-virtues.md:28
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0038`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-080`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-064`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-080, TLC-SO-VIRTUES-064
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-080, TLC-SO-VIRTUES-064
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-080, TLC-SO-VIRTUES-064
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

## TLC-HR-0058

### Identité

- decision_id : `TLC-HR-0058`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0058 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-086`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-087`, `TLC-SO-VIRTUES-216`, `TLC-SO-VIRTUES-217`, `TLC-SO-VIRTUES-218`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-086`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-087`, `TLC-SO-VIRTUES-216`, `TLC-SO-VIRTUES-217`, `TLC-SO-VIRTUES-218`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: equation theoreme de necessite des vertus
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Theorem]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-086 — Équation — Théorème de nécessité des vertus (Theorem), référence maths/03-huit-dimensions-de-tl.md:150
- TLC-SO-HUIT-DIMENSIONS-DE-TL-087 — Équation — Théorème de nécessité des vertus (Theorem), référence maths/03-huit-dimensions-de-tl.md:153
- TLC-SO-VIRTUES-216 — Équation — Théorème de nécessité des Vertus (Theorem), référence maths/10-virtues.md:331
- TLC-SO-VIRTUES-217 — Équation — Théorème de nécessité des Vertus (Theorem), référence maths/10-virtues.md:334
- TLC-SO-VIRTUES-218 — Équation — Théorème de nécessité des Vertus (Theorem), référence maths/10-virtues.md:343
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0058`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-086`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-087`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-216`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-217`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-218`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-086, TLC-SO-HUIT-DIMENSIONS-DE-TL-087, TLC-SO-VIRTUES-216, TLC-SO-VIRTUES-217, TLC-SO-VIRTUES-218
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-086, TLC-SO-HUIT-DIMENSIONS-DE-TL-087, TLC-SO-VIRTUES-216, TLC-SO-VIRTUES-217, TLC-SO-VIRTUES-218
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-086, TLC-SO-HUIT-DIMENSIONS-DE-TL-087, TLC-SO-VIRTUES-216, TLC-SO-VIRTUES-217, TLC-SO-VIRTUES-218
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

## TLC-HR-0072

### Identité

- decision_id : `TLC-HR-0072`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0072 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-081`, `TLC-SO-VIRTUES-065`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-081`, `TLC-SO-VIRTUES-065`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: flexibilite contextuelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-081 — Flexibilité contextuelle (Concept), référence maths/03-huit-dimensions-de-tl.md:127
- TLC-SO-VIRTUES-065 — Flexibilité contextuelle (Concept), référence maths/10-virtues.md:29
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0072`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-081`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-065`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-081, TLC-SO-VIRTUES-065
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-081, TLC-SO-VIRTUES-065
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-081, TLC-SO-VIRTUES-065
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

## TLC-HR-0136

### Identité

- decision_id : `TLC-HR-0136`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0136 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-020`, `TLC-SO-VIRTUES-056`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-020`, `TLC-SO-VIRTUES-056`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/10-virtues.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: theoreme de necessite des vertus
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Theorem]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-020 — Théorème de nécessité des vertus (Theorem), référence maths/03-huit-dimensions-de-tl.md:148
- TLC-SO-VIRTUES-056 — Théorème de nécessité des Vertus (Theorem), référence maths/10-virtues.md:326
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0136`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-020`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VIRTUES-056`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-020, TLC-SO-VIRTUES-056
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-020, TLC-SO-VIRTUES-056
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-020, TLC-SO-VIRTUES-056
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
