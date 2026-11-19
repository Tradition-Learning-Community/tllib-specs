# Parcelles immobilières — Six exercices IA et leurs onze éléments

**Étude préparatoire sans Tradition Learning (TL) — non normative.**  
**19 novembre 2026.**  
**Statut :** exercices proposés ; aucun modèle immobilier de ce document n'a été entraîné ni évalué ici.

## Objet et conventions

Ce document décrit **six travaux d'apprentissage distincts**, réalisés à partir d'une même base illustrative de parcelles, avec pour chacun : **un énoncé métier, un énoncé développeur, les onze éléments** répartis entre les trois phases, ainsi que les schèmes à examiner. La **Mission TL n'est pas introduite** dans ces exercices : elle ne se substitue ni au Problème, ni à la Finalité, ni à la Tâche.

Les onze éléments sont des responsabilités analytiques, **pas onze classes Python ni onze opérations strictement séquentielles**. Le modèle est constitué dès l'initialisation ; la phase dite « après apprentissage » considère son état résultant. L'Évaluation peut intervenir à divers moments et conduire à d'autres apprentissages.

### Jeu de données commun

Supposons `parcelles.csv` contenant **10 000 observations fictives** :

| Colonne | Exemple | Signification |
|---|---|---|
| `superficie_m2` | `450` | Superficie du terrain |
| `commune` | `Kampemba` | Commune |
| `quartier` | `Bel-Air` | Quartier |
| `acces_route` | `asphaltee` | Type d'accès |
| `distance_centre_km` | `8.5` | Distance au centre |
| `eau`, `electricite` | `oui`, `oui` | Disponibilité des services |
| `usage` | `residentiel` | Type d'utilisation |
| `topographie` | `plat` | Relief |
| `prix_usd` | `38000` | Prix observé |
| `date_observation` | `2026-06-15` | Date d'observation |

C'est une **base hypothétique**, pas un jeu de données collecté. Les six exercices utilisent la même base de départ mais pas nécessairement les mêmes colonnes ou cibles. La politique de décision exige en plus des transitions d'environnement et des retours, absents de ce tableau. Prétraitements, seuils et éventuelles normalisations sont ajustés sur l'entraînement seulement pour éviter les fuites d'information.

---

## 1. Régression — Estimer le prix d'une parcelle

**Énoncé métier.** Estimer le prix d'une parcelle à partir de ses caractéristiques connues.

**Énoncé développeur.** Entraîner un modèle de régression supervisée pour prédire `prix_usd` à partir des variables descriptives, sans utiliser le prix de la nouvelle parcelle dans ses entrées.

### Phase 1 — Avant l'apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 1 | **Problème** | Le prix d'une parcelle nouvellement considérée n'est pas connu. | Estimer une variable réelle `y=prix_usd` depuis des variables numériques et catégorielles `X`. |
| 2 | **Finalité** | Obtenir une estimation de prix exploitable dans le contexte immobilier étudié. | Construire une fonction `f(X) -> y_hat`, applicable à de nouvelles parcelles. |
| 3 | **Tâche** | Estimation du prix. | Régression supervisée. |
| 4 | **Ressources** | Ordinateur, logiciels et moyens de calcul. | Python, pandas, NumPy, scikit-learn, CPU, RAM. |
| 5 | **Sources d'apprentissage** | Caractéristiques et prix observés des parcelles. | `X` = colonnes descriptives ; `y = prix_usd` ; découpage temporel train/test si pertinent. |

### Phase 2 — Constitution et apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 6 | **Configuration** | Choisir un estimateur capable de tenir compte de plusieurs caractéristiques et de leurs interactions. | `HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, loss='squared_error', random_state=42)` avec prétraitement adéquat des catégories. |
| 7 | **Algorithme d'apprentissage** | Apprendre à estimer les prix à partir des observations. | Gradient boosting d'arbres avec `model.fit(X_train, y_train)`. |
| 8 | **Critère d'apprentissage** | Réduire les écarts entre prix estimés et prix observés. | Perte quadratique (`squared_error`). |
| 9 | **Mécanisme de modification** | Corriger progressivement les estimations. | Construction successive des arbres qui améliorent la prédiction du modèle courant. |

### Phase 3 — Modèle et évaluation

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 10 | **Modèle** | Estimateur capable de donner un prix pour une nouvelle parcelle. | Estimateur ajusté avec ensemble d'arbres ; `model.predict(X_new)`. |
| 11 | **Évaluation** | Vérifier les écarts de prix selon les types et localisations de parcelles. | `mean_absolute_error`, `root_mean_squared_error`, résidus par commune, test temporel. |

**Schèmes à examiner :** relations superficie–prix, effets de la route et du quartier, interactions, associations trompeuses. Ces contenus ne correspondent pas nécessairement à des arbres ou nœuds individuels.

---

## 2. Classification — Parcelle chère ou peu chère

**Énoncé métier.** Déterminer si une parcelle est chère ou peu chère selon une convention de classement explicitée.

**Énoncé développeur.** Prédire une étiquette binaire dérivée des prix historiques, à partir des caractéristiques de la parcelle. Pour l'exercice, le seuil correspond à la **médiane du prix sur l'ensemble d'entraînement**, et non à une définition universelle de « chère ».

### Phase 1 — Avant l'apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 1 | **Problème** | La catégorie de prix d'une nouvelle parcelle n'est pas connue. | Classer une observation selon `prix_usd > mediane_train`, sans utiliser son prix comme entrée. |
| 2 | **Finalité** | Distinguer les deux catégories de prix. | Obtenir `f(X) -> {0,1}` et, si possible, des probabilités de classe. |
| 3 | **Tâche** | Catégorisation binaire. | Classification supervisée. |
| 4 | **Ressources** | Ordinateur et logiciel d'analyse. | Python, scikit-learn, pandas, CPU. |
| 5 | **Sources d'apprentissage** | Caractéristiques et prix connus pour catégoriser les parcelles. | `X` descriptif ; `y_class=(prix_usd > mediane_train).astype(int)` ; seuil défini sur train uniquement. |

### Phase 2 — Constitution et apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 6 | **Configuration** | Choisir un système de classement à plusieurs arbres. | `RandomForestClassifier(n_estimators=200, min_samples_leaf=5, criterion='gini', random_state=42)` ; encodage des catégories. |
| 7 | **Algorithme d'apprentissage** | Apprendre à distinguer les catégories. | Construction de forêt par `model.fit(X_train, y_class_train)`. |
| 8 | **Critère d'apprentissage** | Former des divisions séparant les classes. | Impureté de Gini, utilisée pour sélectionner les divisions. |
| 9 | **Mécanisme de modification** | Construire les règles de classification. | Création des nœuds, seuils et feuilles de chaque arbre. |

### Phase 3 — Modèle et évaluation

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 10 | **Modèle** | Classifieur distinguant chère et peu chère. | Forêt ajustée ; `predict`, `predict_proba`. |
| 11 | **Évaluation** | Examiner les erreurs de classement selon les quartiers. | Matrice de confusion, `balanced_accuracy_score`, précision, rappel et analyse par sous-groupes. |

**Schèmes à examiner :** régularités discriminantes, combinaisons de caractéristiques, dépendances trompeuses ; le seuil choisi reste une convention de l'expérience.

---

## 3. Clustering — Regrouper les parcelles similaires

**Énoncé métier.** Découvrir des ensembles de parcelles présentant des caractéristiques semblables, sans catégories imposées à l'avance.

**Énoncé développeur.** Appliquer `KMeans` à une représentation numérique des attributs immobiliers afin d'apprendre des centres et des affectations de groupes.

### Phase 1 — Avant l'apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 1 | **Problème** | Les regroupements naturels de parcelles sont inconnus. | Rechercher une organisation dans l'espace des caractéristiques. |
| 2 | **Finalité** | Obtenir des groupes descriptifs pour examiner les ressemblances. | Produire une partition exploitable et ses centres. |
| 3 | **Tâche** | Regroupement. | Clustering non supervisé. |
| 4 | **Ressources** | Poste de calcul et outils statistiques. | Python, NumPy, scikit-learn, CPU, RAM. |
| 5 | **Sources d'apprentissage** | Caractéristiques descriptives sans classes. | `X_cluster` encodé/standardisé ; `prix_usd` exclu ici du `fit` et réservé à l'analyse. |

### Phase 2 — Constitution et apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 6 | **Configuration** | Chercher initialement quatre groupes, à titre d'hypothèse. | `KMeans(n_clusters=4, n_init=10, random_state=42)` sur variables prétraitées. |
| 7 | **Algorithme d'apprentissage** | Organiser les parcelles par proximité. | Algorithme de Lloyd avec `fit(X_cluster)`. |
| 8 | **Critère d'apprentissage** | Réduire la dispersion à l'intérieur des groupes. | Inertie, somme des distances quadratiques aux centres. |
| 9 | **Mécanisme de modification** | Réajuster les groupes successivement. | Affectation au centre le plus proche, puis recalcul des centres. |

### Phase 3 — Modèle et évaluation

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 10 | **Modèle** | Groupes de parcelles et leurs profils. | `KMeans` ajusté : `cluster_centers_`, `labels_`, `predict`. |
| 11 | **Évaluation** | Vérifier la différenciation et la pertinence des groupes. | Inertie, `silhouette_score`, stabilité et caractérisation des groupes, y compris par prix non utilisé pendant l'apprentissage. |

**Schèmes à examiner :** régularités de proximité et d'organisation ; un centre n'est pas automatiquement un schème individuel.

---

## 4. Génération — Produire des parcelles synthétiques

**Énoncé métier.** Produire des descriptions nouvelles et plausibles de parcelles présentant des combinaisons de caractéristiques et de prix synthétiques.

**Énoncé développeur.** Entraîner un modèle génératif sur des enregistrements immobiliers tabulaires mixtes afin d'en échantillonner de nouveaux, sans les présenter comme des parcelles réelles.

### Phase 1 — Avant l'apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 1 | **Problème** | Les combinaisons plausibles de caractéristiques ne sont pas entièrement connues. | Modéliser une distribution jointe sur variables numériques et catégorielles. |
| 2 | **Finalité** | Produire des exemples immobiliers synthétiques variés et cohérents. | Générer de nouveaux enregistrements tabulaires valides. |
| 3 | **Tâche** | Génération. | Modélisation générative tabulaire. |
| 4 | **Ressources** | Moyens de calcul et de stockage. | Python, PyTorch, pandas, NumPy, CPU ou GPU. |
| 5 | **Sources d'apprentissage** | Enregistrements historiques avec caractéristiques et prix. | Table mixte comprenant éventuellement `prix_usd`, encodée/normalisée ; séparation train/test. |

### Phase 2 — Constitution et apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 6 | **Configuration** | Constituer un générateur de parcelles. | VAE tabulaire : encodeur, `mu`/`logvar`, latent `z`, décodeur à sorties numériques et catégorielles, optimiseur Adam. |
| 7 | **Algorithme d'apprentissage** | Apprendre les combinaisons observées et pouvoir en produire d'autres. | VAE entraîné par réparamétrisation, rétropropagation et `optimizer.step()`. |
| 8 | **Critère d'apprentissage** | Favoriser fidélité des données et possibilité de génération. | Reconstruction numérique + entropie croisée catégorielle + divergence KL, pondérations explicites. |
| 9 | **Mécanisme de modification** | Ajuster les relations apprises par le générateur. | `loss.backward()` et actualisation des paramètres de l'encodeur/décodeur par Adam. |

### Phase 3 — Modèle et évaluation

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 10 | **Modèle** | Générateur de nouvelles parcelles synthétiques. | VAE ajusté ; `z -> decoder(z)` puis décodage des colonnes. |
| 11 | **Évaluation** | Examiner plausibilité, diversité et incohérences. | Comparaison distributions marginales/conjointes, validation des contraintes, duplication, mémorisation. |

**Schèmes à examiner :** relations entre localisation, superficie, équipements, usage et prix. Les enregistrements produits ne sont pas des transactions réelles.

---

## 5. Représentation — Décrire les parcelles dans un espace réduit

**Énoncé métier.** Obtenir une description compacte des principales différences entre parcelles pour faciliter leur analyse.

**Énoncé développeur.** Apprendre une projection de leurs caractéristiques descriptives vers trois dimensions, puis l'appliquer à de nouveaux enregistrements.

### Phase 1 — Avant l'apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 1 | **Problème** | Les nombreuses caractéristiques sont difficiles à analyser simultanément. | Représenter les caractéristiques dans un espace réduit. |
| 2 | **Finalité** | Conserver des différences importantes dans une représentation compacte. | Produire trois coordonnées conservant une part importante de la variance. |
| 3 | **Tâche** | Représentation des parcelles. | Réduction de dimension / apprentissage de représentation. |
| 4 | **Ressources** | Ordinateur et outils numériques. | Python, NumPy, scikit-learn, CPU/RAM. |
| 5 | **Sources d'apprentissage** | Caractéristiques descriptives des parcelles. | Matrice `X_repr` encodée et standardisée sans `prix_usd` dans cette variante. |

### Phase 2 — Constitution et apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 6 | **Configuration** | Choisir une représentation en trois dimensions. | `PCA(n_components=3)` avec prétraitement ajusté sur train. |
| 7 | **Algorithme d'apprentissage** | Déterminer les principales variations des parcelles. | ACP par SVD, `pca.fit(X_train_transformed)`. |
| 8 | **Critère d'apprentissage** | Préserver la variance dominante. | Maximisation de la variance projetée sous orthogonalité. |
| 9 | **Mécanisme de modification** | Construire les axes de représentation. | Décomposition numérique et calcul des composantes, sans mise à jour Adam. |

### Phase 3 — Modèle et évaluation

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 10 | **Modèle** | Transformation donnant trois coordonnées par parcelle. | PCA ajustée, `components_`, `mean_`, `transform(X_new)`. |
| 11 | **Évaluation** | Vérifier ce qui est conservé et perdu. | `explained_variance_ratio_`, reconstruction inverse et stabilité sur contrôle. |

**Schèmes à examiner :** régularités statistiques de la projection ; les trois composantes ne sont pas nécessairement trois schèmes distincts.

---

## 6. Politique de décision — Acheter, attendre ou renoncer

**Énoncé métier.** Selon la situation d'une parcelle et ses évolutions possibles, choisir une action : acheter, attendre ou renoncer.

**Énoncé développeur.** Apprendre une politique de décision séquentielle dans un environnement simulé qui utilise les parcelles pour initialiser des états, mais fournit **en plus** transitions et récompenses. **Le fichier statique `parcelles.csv` ne contient pas ces expériences.**

### Phase 1 — Avant l'apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 1 | **Problème** | Les conséquences futures d'actions immobilières sont incertaines. | Apprendre à choisir des actions dans un processus de décision séquentiel. |
| 2 | **Finalité** | Disposer d'une capacité de choix adaptée à plusieurs situations. | Obtenir une politique fondée sur une estimation de `Q(s,a)` dans l'environnement défini. |
| 3 | **Tâche** | Choix séquentiel d'actions. | Politique de décision par renforcement. |
| 4 | **Ressources** | Ordinateur et environnement d'expérimentation. | Python, PyTorch, Gymnasium, CPU/GPU, simulateur explicite. |
| 5 | **Sources d'apprentissage** | Caractéristiques de parcelles et expériences état–action–conséquence. | `parcelles.csv` pour des états initiaux ; transitions `(s,a,r,s_next,terminated)` fournies par simulateur **à concevoir/justifier**. |

### Phase 2 — Constitution et apprentissage

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 6 | **Configuration** | Définir situations, actions et conséquences simulées. | Actions `acheter`, `attendre`, `renoncer`, DQN, buffer de rejeu, réseau cible, epsilon-greedy, `gamma`, Adam. |
| 7 | **Algorithme d'apprentissage** | Expérimenter des décisions successives et en tirer des acquis. | DQN : interaction, échantillonnage d'expériences, cibles TD, mise à jour du réseau. |
| 8 | **Critère d'apprentissage** | Ajuster les estimations des conséquences d'actions. | `torch.nn.SmoothL1Loss()` entre `Q(s,a)` et la cible de Bellman. |
| 9 | **Mécanisme de modification** | Actualiser les valeurs associées aux décisions. | `loss.backward()`, `optimizer.step()` et synchronisation du réseau cible. |

### Phase 3 — Modèle et évaluation

| N° | Élément | Métier | Développeur IA |
|---:|---|---|---|
| 10 | **Modèle** | Système sélectionnant une action en situation. | Réseau Q entraîné et règle `argmax_a Q(s,a)`. |
| 11 | **Évaluation** | Examiner les conséquences sur différents scénarios. | Retours cumulés, comparaisons à politiques de référence, robustesse en simulation. |

**Schèmes à examiner :** relations état–action–conséquence, effets différés et régularités de décision ; leur pertinence réelle dépend de la validité du simulateur.

---

## Comparaison des six cas

| Famille | Algorithme | Critère | Modèle résultat | Sortie |
|---|---|---|---|---|
| Régression | Gradient boosting | Erreur quadratique | Ensemble d'arbres | Prix estimé |
| Classification | Random Forest | Gini | Forêt de classification | Classe / probabilité |
| Clustering | K-Means | Inertie | Centres et groupes | Affectation |
| Génération | VAE | Reconstruction + KL | Générateur tabulaire | Parcelle synthétique |
| Représentation | PCA/SVD | Variance conservée | Projection | Vecteur réduit |
| Politique de décision | DQN | Erreur TD | Réseau Q / politique | Action |

## Limites et suite expérimentale

1. Les six exercices sont des **propositions de travail sans TL**, pas six expériences immobilières exécutées. Aucun résultat numérique ou apprentissage constaté n'est revendiqué.
2. Le seuil médian, les quatre clusters, les trois composantes et les hyperparamètres sont des **choix d'exercice**, non des seuils scientifiques universels.
3. Le sixième cas nécessite des informations de transition, des récompenses et une dynamique d'environnement supplémentaires ; il serait incorrect de prétendre les lire dans le CSV statique.
4. Les schèmes restent un **concept de travail** pour étudier les contenus représentationnels internes constitutifs des modèles ; ils ne sont pas un neuvième objet TL ni automatiquement identiques aux poids, arbres, centres ou composantes.
5. Le même Problème ou les mêmes données n'impliquent pas la même Finalité, le même Critère, le même modèle ni les mêmes schèmes. Les différences doivent être examinées par des expériences contrôlées.
6. La séparation entre **constitution**, **exécution**, **apprentissage effectivement observé** et **évaluation** doit être conservée.
7. Ce document ne formule ni Mission TL, ni définition des entités/objets TL, ni contrat scientifique ou API `tllib`.

### Références du dépôt (branche documentaire)

- [`fondements/SIX_FAMILLES_OPERATIONNELLES.md`](../fondements/SIX_FAMILLES_OPERATIONNELLES.md)
- [`fondements/SCHEMES_NOTES_DE_TRAVAIL.md`](../fondements/SCHEMES_NOTES_DE_TRAVAIL.md)
- [`benchmarks/sans_tl/README.md`](../benchmarks/sans_tl/README.md)
- [`conception/CONSTITUTION_ET_FRONTIERES.md`](CONSTITUTION_ET_FRONTIERES.md)

**Chemin de dépôt :** `docs/pre_implementation_design/conception/EXERCICES_PARCELLES_SIX_FAMILLES_11_ELEMENTS.md`.
