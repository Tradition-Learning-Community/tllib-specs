# batch-005 — Revue des rapprochements candidats

État : `pending`
Décisions : 12
Catégorie de paquet : `merge_or_same_object`
Priorité maximale : `medium`

Chaque recommandation ci-dessous est candidate et non normative. Aucun choix humain n’est prérempli.

## TLC-HR-0023

### Identité

- decision_id : `TLC-HR-0023`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0023 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-047`, `TLC-SO-MESSAGE-026`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-047`, `TLC-SO-MESSAGE-026`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: contenu
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-047 — contenu (Concept), référence maths/03-huit-dimensions-de-tl.md:27
- TLC-SO-MESSAGE-026 — contenu (Concept), référence maths/07-message.md:15
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0023`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-047`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-026`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-047, TLC-SO-MESSAGE-026
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-047, TLC-SO-MESSAGE-026
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-047, TLC-SO-MESSAGE-026
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

## TLC-HR-0024

### Identité

- decision_id : `TLC-HR-0024`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0024 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-050`, `TLC-SO-MESSAGE-029`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-050`, `TLC-SO-MESSAGE-029`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: contexte
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [State]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-050 — contexte (State), référence maths/03-huit-dimensions-de-tl.md:30
- TLC-SO-MESSAGE-029 — contexte (State), référence maths/07-message.md:18
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0024`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-050`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-029`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-050, TLC-SO-MESSAGE-029
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-050, TLC-SO-MESSAGE-029
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-050, TLC-SO-MESSAGE-029
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

## TLC-HR-0026

### Identité

- decision_id : `TLC-HR-0026`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0026 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-058`, `TLC-SO-MESSAGE-069`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-058`, `TLC-SO-MESSAGE-069`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: convergence
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-058 — Convergence (Concept), référence maths/03-huit-dimensions-de-tl.md:47
- TLC-SO-MESSAGE-069 — Convergence (Concept), référence maths/07-message.md:134
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0026`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-058`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-069`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-058, TLC-SO-MESSAGE-069
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-058, TLC-SO-MESSAGE-069
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-058, TLC-SO-MESSAGE-069
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

## TLC-HR-0037

### Identité

- decision_id : `TLC-HR-0037`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0037 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-055`, `TLC-SO-MESSAGE-034`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-055`, `TLC-SO-MESSAGE-034`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: dependance contextuelle
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-055 — Dépendance contextuelle (Concept), référence maths/03-huit-dimensions-de-tl.md:37
- TLC-SO-MESSAGE-034 — Dépendance contextuelle (Concept), référence maths/07-message.md:26
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0037`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-055`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-034`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-055, TLC-SO-MESSAGE-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-055, TLC-SO-MESSAGE-034
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-055, TLC-SO-MESSAGE-034
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

## TLC-HR-0065

### Identité

- decision_id : `TLC-HR-0065`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0065 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-056`, `TLC-SO-MESSAGE-067`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-056`, `TLC-SO-MESSAGE-067`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: existence
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-056 — Existence (Concept), référence maths/03-huit-dimensions-de-tl.md:45
- TLC-SO-MESSAGE-067 — Existence (Concept), référence maths/07-message.md:132
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0065`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-056`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-067`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-056, TLC-SO-MESSAGE-067
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-056, TLC-SO-MESSAGE-067
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-056, TLC-SO-MESSAGE-067
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

## TLC-HR-0067

### Identité

- decision_id : `TLC-HR-0067`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0067 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-057`, `TLC-SO-MESSAGE-068`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-057`, `TLC-SO-MESSAGE-068`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: expression
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-057 — Expression (Concept), référence maths/03-huit-dimensions-de-tl.md:46
- TLC-SO-MESSAGE-068 — Expression (Concept), référence maths/07-message.md:133
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0067`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-057`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-068`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-057, TLC-SO-MESSAGE-068
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-057, TLC-SO-MESSAGE-068
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-057, TLC-SO-MESSAGE-068
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

## TLC-HR-0085

### Identité

- decision_id : `TLC-HR-0085`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0085 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-052`, `TLC-SO-MESSAGE-031`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-052`, `TLC-SO-MESSAGE-031`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: integrativite
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-052 — Intégrativité (Concept), référence maths/03-huit-dimensions-de-tl.md:34
- TLC-SO-MESSAGE-031 — Intégrativité (Concept), référence maths/07-message.md:23
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0085`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-052`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-031`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-052, TLC-SO-MESSAGE-031
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-052, TLC-SO-MESSAGE-031
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-052, TLC-SO-MESSAGE-031
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

## TLC-HR-0114

### Identité

- decision_id : `TLC-HR-0114`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0114 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-054`, `TLC-SO-MESSAGE-033`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-054`, `TLC-SO-MESSAGE-033`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: profondeur symbolique
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-054 — Profondeur symbolique (Concept), référence maths/03-huit-dimensions-de-tl.md:36
- TLC-SO-MESSAGE-033 — Profondeur symbolique (Concept), référence maths/07-message.md:25
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0114`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-054`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-033`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-054, TLC-SO-MESSAGE-033
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-054, TLC-SO-MESSAGE-033
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-054, TLC-SO-MESSAGE-033
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

## TLC-HR-0121

### Identité

- decision_id : `TLC-HR-0121`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0121 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-059`, `TLC-SO-MESSAGE-070`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-059`, `TLC-SO-MESSAGE-070`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: revelation
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-059 — Révélation (Concept), référence maths/03-huit-dimensions-de-tl.md:48
- TLC-SO-MESSAGE-070 — Révélation (Concept), référence maths/07-message.md:135
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0121`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-059`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-070`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-059, TLC-SO-MESSAGE-070
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-059, TLC-SO-MESSAGE-070
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-059, TLC-SO-MESSAGE-070
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

## TLC-HR-0129

### Identité

- decision_id : `TLC-HR-0129`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0129 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-049`, `TLC-SO-MESSAGE-028`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-049`, `TLC-SO-MESSAGE-028`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: structure procedurale
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-049 — structure procédurale (Concept), référence maths/03-huit-dimensions-de-tl.md:29
- TLC-SO-MESSAGE-028 — structure procédurale (Concept), référence maths/07-message.md:17
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0129`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-049`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-028`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-049, TLC-SO-MESSAGE-028
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-049, TLC-SO-MESSAGE-028
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-049, TLC-SO-MESSAGE-028
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

## TLC-HR-0139

### Identité

- decision_id : `TLC-HR-0139`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0139 ?

### Éléments concernés

- Identifiants : `TLC-SO-HUIT-DIMENSIONS-DE-TL-061`, `TLC-SO-MESSAGE-072`
- Objets : `TLC-SO-HUIT-DIMENSIONS-DE-TL-061`, `TLC-SO-MESSAGE-072`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: transformation du monde
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-HUIT-DIMENSIONS-DE-TL-061 — Transformation du monde (Concept), référence maths/03-huit-dimensions-de-tl.md:50
- TLC-SO-MESSAGE-072 — Transformation du monde (Concept), référence maths/07-message.md:137
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0139`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-061`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-072`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-061, TLC-SO-MESSAGE-072
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-061, TLC-SO-MESSAGE-072
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-HUIT-DIMENSIONS-DE-TL-061, TLC-SO-MESSAGE-072
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

## TLC-HR-0020

### Identité

- decision_id : `TLC-HR-0020`
- catégorie d’origine : `merge_or_separate`
- catégorie normalisée : `merge_or_same_object`
- justification du classement : Le candidat transversal demande de déterminer si des objets portant un nom normalisé commun désignent le même objet, un alias ou des objets distincts.
- priorité : `medium`
- portée du blocage : `blocks_feature_decomposition`

### Question à décider

Faut-il rapprocher les objets de TLC-XD-0020 ?

### Éléments concernés

- Identifiants : `TLC-SO-CAPACITIES-004`, `TLC-SO-COMPETENCIES-004`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-005`, `TLC-SO-LIVED-EXPERIENCE-004`, `TLC-SO-MESSAGE-005`, `TLC-SO-PRACTICE-004`, `TLC-SO-VALUES-004`
- Objets : `TLC-SO-CAPACITIES-004`, `TLC-SO-COMPETENCIES-004`, `TLC-SO-HUIT-DIMENSIONS-DE-TL-005`, `TLC-SO-LIVED-EXPERIENCE-004`, `TLC-SO-MESSAGE-005`, `TLC-SO-PRACTICE-004`, `TLC-SO-VALUES-004`
- Relations : aucune
- Termes : aucun
- Sources : `maths/03-huit-dimensions-de-tl.md`, `maths/07-message.md`, `maths/09-values.md`, `maths/11-capacities.md`, `maths/12-competencies.md`, `maths/13-practice.md`, `maths/14-lived-experience.md`

### Éléments de preuve

- Signal d’audit : Nom canonique normalisé commun: conditions d existence
- Type de rapprochement : same_normalized_name_across_sources
- Risque de fusion : medium
- Différences observées : {object_types: [Concept]}
- TLC-SO-CAPACITIES-004 — Conditions d’existence (Concept), référence maths/11-capacities.md:32
- TLC-SO-COMPETENCIES-004 — Conditions d’existence (Concept), référence maths/12-competencies.md:44
- TLC-SO-HUIT-DIMENSIONS-DE-TL-005 — Conditions d’existence (Concept), référence maths/03-huit-dimensions-de-tl.md:39
- TLC-SO-LIVED-EXPERIENCE-004 — Conditions d’existence (Concept), référence maths/14-lived-experience.md:30
- TLC-SO-MESSAGE-005 — Conditions d’existence (Concept), référence maths/07-message.md:28
- TLC-SO-PRACTICE-004 — Conditions d’existence (Concept), référence maths/13-practice.md:33
- TLC-SO-VALUES-004 — Conditions d’existence (Concept), référence maths/09-values.md:36
- Référence : `reports/scientific-consolidation/human-review-queue.yaml`
- Référence : `registry/scientific-objects/cross-source-duplicate-candidates.yaml#TLC-XD-0020`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-CAPACITIES-004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-COMPETENCIES-004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-HUIT-DIMENSIONS-DE-TL-005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-LIVED-EXPERIENCE-004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-MESSAGE-005`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-PRACTICE-004`
- Référence : `registry/scientific-objects/global-object-candidates.yaml#TLC-SO-VALUES-004`

### Analyse du problème

Le signal établit qu’une revue est nécessaire, mais il ne suffit pas à établir une identité scientifique, une équivalence terminologique, une correction documentaire ou une résolution. Ces conséquences exigent un jugement humain et ne peuvent pas être appliquées mécaniquement.

### Options autorisées

- `merge` — Créer ultérieurement un objet unifié après validation scientifique.
- `declare_alias` — Conserver les objets et enregistrer une équivalence de nom.
- `keep_separate` — Conserver des identités distinctes.

### Conséquences

#### `merge`

- Objets touchés : TLC-SO-CAPACITIES-004, TLC-SO-COMPETENCIES-004, TLC-SO-HUIT-DIMENSIONS-DE-TL-005, TLC-SO-LIVED-EXPERIENCE-004, TLC-SO-MESSAGE-005, TLC-SO-PRACTICE-004, TLC-SO-VALUES-004
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `declare_alias`

- Objets touchés : TLC-SO-CAPACITIES-004, TLC-SO-COMPETENCIES-004, TLC-SO-HUIT-DIMENSIONS-DE-TL-005, TLC-SO-LIVED-EXPERIENCE-004, TLC-SO-MESSAGE-005, TLC-SO-PRACTICE-004, TLC-SO-VALUES-004
- Relations touchées : aucune directement identifiée
- Termes non résolus touchés : 0
- Consolidation : l’application ultérieure devra refléter le choix ; aucun registre candidat n’est modifié pendant cette revue.
- Futur découpage fonctionnel : reste interdit tant que la revue requise n’est pas terminée.
- Extraction ciblée : non, sauf décision humaine contraire.

#### `keep_separate`

- Objets touchés : TLC-SO-CAPACITIES-004, TLC-SO-COMPETENCIES-004, TLC-SO-HUIT-DIMENSIONS-DE-TL-005, TLC-SO-LIVED-EXPERIENCE-004, TLC-SO-MESSAGE-005, TLC-SO-PRACTICE-004, TLC-SO-VALUES-004
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
