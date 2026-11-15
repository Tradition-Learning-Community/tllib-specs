# Tradition Learning — Étude expérimentale intégrale des six familles de modèles IA, sans TL

**Document de conservation détaillé — 15 novembre 2026**

Ce document réunit, **sans réduction à une simple synthèse**, les six études expérimentales de cette discussion. Pour chaque famille, il décrit le problème commun, les algorithmes, les observations successives, les contenus représentationnels acquis ou modifiés, les sondes internes, les interprétations défendables et les limites. Après chaque étude figurent **toutes les lignes et toutes les colonnes de la chronologie enregistrée**.

Les expériences et la théorie scientifique de TL doivent rester distinctes : **aucune expérience ci-dessous ne contient un opérateur Tradition Learning**. Les mêmes données et programmes peuvent servir plus tard comme témoins techniques, sans inventer de transformation TL.

**Règle d’étude des schèmes :** un schème est le contenu représentationnel interne acquis ou modifié pendant l'apprentissage et susceptible de contribuer au fonctionnement du modèle. Il ne se réduit ni à un poids, ni à une activation, ni à une coordonnée latente, ni à une sortie, ni à la seule différence entre deux instants. À chaque instant, nous observons le répertoire de relations disponibles, y compris celles qui persistent et celles dont l'influence diminue.

**Portée :** les formulations des problèmes, ressources et technologies ne sont ici que des conditions de départ. Le sujet est **l'acquisition et l'évolution interne**. L'évaluation et l'inférence servent parfois de sondes, mais n'ont pas été réinterprétées comme apprentissage.

**Fichiers associés :** l’archive `ETUDE_SIX_FAMILLES_SANS_TL.zip` contient exactement six dossiers de famille, chacun avec `ETUDE_DETAILLEE.md`, `CHRONOLOGIE_COMPLETE.md`, les copies originales des scripts et données, les archives ZIP originales lorsqu'elles existaient, les checkpoints, les manifestes et l’inventaire SHA-256. Le document présent couvre le texte et les tableaux ; les JSON, NPZ et PT conservent les états bruts complets sans perte.

---


---

<!-- DÉBUT 01_regression -->

# 1/6 — Régression : observation prolongée des acquis internes, sans TL

**Statut : expérience synthétique exécutée, fichiers originaux conservés.**  
**Problème :** apprendre à estimer le prix fictif d'une parcelle.  
**Périmètre :** le fonctionnement de l'apprentissage et l'évolution des contenus représentationnels, pas la préparation métier des ressources, le déploiement, ni Tradition Learning.

## 1. Pourquoi cette expérience

La régression est l'apprentissage d'une relation permettant d'estimer une grandeur numérique. Notre première observation élémentaire (le coefficient d'une droite variant sur quelques exemples) a établi qu'une relation peut apparaître, être renforcée par répétition, puis corrigée par une observation contradictoire. Nous voulons examiner la même chose sur **une longue suite de 1 600 observations**, avec plusieurs algorithmes simples et l'ensemble des contenus présents à chaque contrôle.

Le terme *schème* désigne ici un **contenu représentationnel interne acquis ou modifié** : une association, régularité, relation conditionnelle ou abstraction susceptible de contribuer au fonctionnement du modèle. Il ne désigne ni une ligne de données, ni un coefficient isolé, ni une cellule d'arbre, ni l'activation d'un neurone, ni la sortie.

Les trois modèles reçoivent **exactement les mêmes entrées dans le même ordre**. Les mesures de contraste permettent d'inférer quelles relations ils exploitent ; elles ne sont pas des comptages directs de schèmes. Le maintien d'une sensibilité interne n'établit pas qu'un schème isolable a survécu à l'identique.

## 2. Construction scientifique de l'expérience

Chaque parcelle fictive est décrite par :

- **A :** niveau de superficie (1, 2, 3 ou 4) ;
- **R :** accès routier (0 ou 1) ;
- **P :** indice indirect (0 ou 1), initialement confondu avec R ;
- **y :** prix en milliers USD, avec bruit aléatoire.

**Générateur synthétique réel du script :**

```text
A ∈ {1,2,3,4}, R ∈ {0,1}
P = R pour les observations 1..300
P devient aléatoire indépendant pour 301..1600
y = 4 + 3 A + 5 R + 3 A R + bruit gaussien (écart-type 0,8)
```

Il n'y a **aucun effet propre de P** sur le prix généré. En revanche, l'effet de la route dépend de la superficie par l'interaction A·R. Par exemple, le supplément dû à la route est de 8 milliers USD lorsque A=1 et de 17 milliers USD lorsque A=4. Ce générateur n'est pas une vérité sur l'immobilier réel ; il sert à tester des mécanismes de ML sur des observations contrôlées.

**Graine :** `20261115`.  **États :** après 40, 100, 300, 500, 900 et 1 600 observations.

## 3. Les trois algorithmes réellement employés

### 3.1. Régression linéaire par moindres carrés récursifs (RLS)

La méthode apprend quatre coefficients : intercept et contributions de A, R, P. L'apprentissage procède par mise à jour séquentielle de l'estimation et de la covariance associée (initialisée à 1000·I dans le code). Elle ne possède **pas** de terme A·R. Elle ne pourra donc pas représenter directement le fait que l'avantage de la route diffère entre petites et grandes parcelles.

- **État informatique acquis :** vecteur de coefficients, état de covariance récursive.
- **Contenus représentationnels étudiés :** association superficie–prix ; association accès–prix ; éventuelle association indice–prix ; contribution moyenne de la route.
- **Ambiguïté initiale :** lorsque R et P coïncident parfaitement, aucune observation ne permet de leur attribuer des effets distincts de manière fiable ; la méthode peut répartir la contribution entre les deux.

### 3.2. Arbre CART de régression

Arbre de profondeur maximale 3, avec un minimum de 8 observations par feuille. Il est **réentraîné sur toutes les observations accumulées** à chaque point de contrôle. Les divisions choisies peuvent porter sur la superficie, l'accès ou l'indice indirect selon les réductions d'erreur disponibles.

- **État informatique acquis :** seuils, caractéristiques divisées, valeurs de feuilles, chemins.
- **Contenus étudiés :** conditions locales, régimes de prix selon superficie et accès, interaction représentée par des régions distinctes.
- **Limite :** une division alternative sur deux caractéristiques confondues ne constitue pas automatiquement une découverte ; des règles différentes peuvent effectuer la même séparation sur les observations disponibles.

### 3.3. Petit réseau neuronal MLP

Structure : **3 entrées → 8 unités cachées `tanh` → 1 estimation**, avec optimisation Adam (taux 0,02). Les paramètres sont conservés d'un checkpoint à l'autre ; le réseau effectue 500 mises à jour en lot complet sur toutes les données accumulées au point de contrôle. Les entrées de superficie sont normalisées selon une transformation fixe et la sortie est ramenée en milliers USD.

- **États conservés :** paramètres, activations cachées pour des observations fixes, sensibilités à chaque caractéristique.
- **Contenus étudiés :** combinaisons non linéaires, effets contextuels de la route, réponses internes à l'indice P.
- **Précaution :** les 8 activations cachées ne représentent pas nécessairement 8 schèmes indépendants.

Ces méthodes ne reçoivent pas les mêmes budgets de calcul ni les mêmes règles de mise à jour. Leur comparaison porte sur les **contenus et trajectoires observables**, pas sur une mesure normalisée de vitesse ou d'efficacité.

## 4. Le déroulement : t = 40, 100, 300, 500, 900, 1 600

### 4.1. Premières 300 observations : apparition et coexistence de relations ambiguës

L'accès routier R et l'indice indirect P sont alors identiques dans toutes les observations. Il est possible de constater un effet lié à cette paire, mais pas de savoir, uniquement à partir de ces observations, lequel des deux est pertinent.

- **Après 40 observations :** la régression linéaire attribue déjà une contribution positive à R et P. L'arbre retient des divisions qui expriment des effets de superficie et d'accès. Le MLP réagit aux trois caractéristiques.
- **Après 100 observations :** dans la trace conservée, l'arbre sélectionne l'indice indirect pour une de ses séparations, alors qu'il l'avait traité autrement à 40 observations. Ce changement ne signifie pas que le modèle ait découvert la causalité ; R et P sont encore confondus.
- **Après 300 observations :** le réseau et la régression linéaire continuent à exploiter l'indice indirect. Certaines règles de l'arbre recourent de nouveau à R.

Les schèmes ne sont pas seulement les relations incorrectes. À chacun de ces instants, les modèles disposent aussi d'acquis relatifs à la taille, aux variations de prix et, selon leurs structures, aux interactions. Nous conservons l'intégralité de ces contenus accessibles par sondes et structures.

### 4.2. Après 300 observations : nouvelles combinaisons et différenciation

De nouvelles parcelles présentent R≠P. Elles rendent observables des situations jusque-là absentes : route présente sans indicateur ; indicateur présent sans route.

Ces nouvelles observations obligent progressivement les modèles à réviser l'attribution de l'effet au prix. Ce qui varie n'est pas seulement un coefficient, mais le **rôle que différentes relations jouent dans la prédiction**.

| Observations | Influence absolue moyenne de P — RLS | Arbre | MLP |
|---:|---:|---:|---:|
| 40 | 6,706 | 0,000 | 5,443 |
| 100 | 6,350 | 12,818 | 5,004 |
| 300 | 6,282 | 0,000 | 4,624 |
| 500 | 0,239 | 0,000 | 0,127 |
| 900 | 0,047 | 0,000 | 0,102 |
| 1 600 | 0,110 | 0,000 | 0,072 |

Les valeurs sont en milliers USD de contraste conditionnel, calculées sur des sondes fixes dans le script. Elles **ne sont ni des paramètres, ni une mesure du nombre de schèmes**. Les colonnes sont ici une observation des changements de contribution au fonctionnement. La ligne de l'arbre à 100 observations illustre le caractère parfois abrupt des effets des partitions.

### 4.3. Qu'est-ce qui est appris, et pas seulement abandonné ?

Dans ce scénario, la vraie relation comporte un terme d'interaction A·R. L'effet de la route diffère entre petite et grande parcelle.

| Modèle à 1 600 observations | Différence due à R pour A=1 | Différence due à R pour A=4 |
|---|---:|---:|
| Générateur synthétique | 8,0 | 17,0 |
| Régression linéaire sans interaction | 12,4 | 12,4 |
| Arbre CART | 8,1 | 17,1 |
| MLP | 8,2 | 17,1 |

La régression linéaire ne peut apprendre que l'effet moyen prévu par sa classe de fonctions. L'arbre et le MLP apprennent à différencier l'effet de la route selon la superficie : une **relation composée** devient exploitable.

Les contenus présents à la fin comprennent donc des associations de taille, un effet de route et, pour les modèles suffisamment expressifs, une interaction. L'affaiblissement de P et l'acquisition de l'interaction se déroulent simultanément.

## 5. Le phénomène interne le plus instructif : utiliser moins sans tout effacer

Pour le MLP, des sondes fixent la superficie et la route, puis changent uniquement P. Elles mesurent une différence dans la couche cachée et une différence dans l'estimation finale.

| Mesure | Après 300 observations | Après 1 600 observations |
|---|---:|---:|
| Différence moyenne entre activations cachées | 1,110 | 0,929 |
| Effet de P sur les estimations finales, kUSD | 4,624 | 0,072 |

La sensibilité des unités cachées à P demeure perceptible alors que l'effet sur la sortie devient faible. Il existe donc un **décalage entre l'information exprimée dans une transformation interne et son influence sur le résultat**.

On ne peut pas en déduire qu'un schème isolable de l'indice P a été parfaitement conservé : cela demanderait des interventions causales et une étude plus détaillée de l'identité des contenus. On peut seulement établir la persistance de la sensibilité interne et la forte diminution de son effet final.

## 6. Répertoire représentationnel à examiner à chaque instant

Nous ne limitons pas les schèmes aux différences entre deux checkpoints. Il faut examiner au même moment :

- la relation superficie–prix ;
- la relation route–prix ;
- la relation P–prix lorsqu'elle est présente ;
- les interactions conditionnelles entre A et R ;
- la stabilité ou l'instabilité des distinctions selon les contextes ;
- les réponses cachées du réseau à des perturbations fixes ;
- les régions et chemins de décision de l'arbre ;
- les limites de ce que chaque modèle peut représenter.

Une corrélation peut être acquise et utilisée sans être causale. L'optimisation d'un prix estimé ne prouve pas une compréhension des facteurs immobiliers. Une amélioration de prédiction ne permet pas de dénombrer les schèmes.

## 7. Protocole reproductible, données et fichiers

- `experiment_regression_schemes.py` : **script source original** contenant générateur, RLS, CART, MLP, sondes et checkpoints ; lancer avec `python experiment_regression_schemes.py` dans un environnement avec NumPy, scikit-learn et PyTorch.
- `experiment_regression_schemes_results.json` : résultats et états détaillés originaux.
- `CHRONOLOGIE_COMPLETE.md` : toutes les mesures exposées par checkpoint, extraites directement du JSON.
- `FICHIERS_ORIGINAUX_SHA256.txt` : vérification de conservation des fichiers.

**Important :** l'expérience de régression ne disposait pas d'un fichier NPZ ni d'une archive d'origine. Les 1 600 observations sont générées par le script original avec la graine fixe `20261115`. Un sous-fichier de données peut être produit secondairement pour archivage, mais ne doit pas être présenté comme un original existant lors de l'exécution initiale.

## 8. Résultats et limites à conserver

1. Les mêmes observations peuvent conduire à des contenus représentationnels différents selon les mécanismes utilisés.
2. Des associations initialement indiscernables peuvent se différencier avec de nouvelles combinaisons d'observations.
3. Une représentation interne peut continuer à réagir à une caractéristique alors que celle-ci ne contribue presque plus à la prédiction.
4. Des relations composées peuvent apparaître dans certains modèles et rester irréprésentables dans d'autres.
5. Une modification de support informatique n'est ni la définition ni le comptage d'un schème.
6. L'expérience est synthétique, à graine fixe, non répétée sur plusieurs graines, et n'implémente **aucune opération TL**.

Le programme et le JSON complets constituent les enregistrements détaillés de l'expérience, au-delà des exemples commentés ici.


---

# Chronologie complète des six contrôles — Régression

**Mesures transcrites directement du JSON original** `originaux/experiment_regression_schemes_results.json`.

Ce tableau présente chaque modèle à chaque instant. Les structures d’arbres complètes, coefficients et sondes cachées supplémentaires sont conservés dans le JSON original.

| t | phase | RLS_area_if_no_road | RLS_area_if_road | RLS_road_at_small | RLS_road_at_large | RLS_proxy_effect | Tree_area_if_no_road | Tree_area_if_road | Tree_road_at_small | Tree_road_at_large | Tree_proxy_effect | TinyMLP_area_if_no_road | TinyMLP_area_if_road | TinyMLP_road_at_small | TinyMLP_road_at_large | TinyMLP_proxy_effect | mlp_hidden_proxy_abs_mean_all_contexts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | ambiguous | 13.526 | 13.526 | 6.706 | 6.706 | 6.706 | 4.688 | 10.466 | 9.38 | 15.158 | 0.0 | 7.979 | 13.398 | 7.783 | 13.203 | 7.686 | 1.104 |
| 100 | ambiguous | 13.31 | 13.31 | 6.35 | 6.35 | 6.35 | 8.532 | 8.532 | 0.0 | 0.0 | 11.373 | 8.55 | 13.454 | 8.476 | 13.38 | 7.11 | 1.11 |
| 300 | ambiguous | 13.532 | 13.532 | 6.282 | 6.282 | 6.282 | 8.965 | 17.862 | 8.249 | 17.146 | 0.0 | 8.932 | 13.312 | 8.833 | 13.213 | 6.628 | 1.11 |
| 500 | disambiguation | 13.564 | 13.564 | 12.244 | 12.244 | 0.239 | 9.077 | 17.796 | 8.268 | 16.987 | 0.0 | 9.051 | 17.36 | 8.384 | 16.693 | 0.226 | 0.959 |
| 900 | disambiguation | 13.402 | 13.402 | 12.44 | 12.44 | 0.047 | 9.121 | 17.815 | 8.297 | 16.991 | 0.0 | 9.099 | 17.679 | 8.367 | 16.947 | 0.224 | 0.945 |
| 1600 | disambiguation | 13.493 | 13.493 | 12.419 | 12.419 | 0.11 | 9.017 | 17.981 | 8.109 | 17.073 | 0.0 | 9.021 | 17.904 | 8.183 | 17.066 | 0.204 | 0.929 |

## Descriptions des branches, paramètres et réponses internes, contrôle par contrôle

### Après 40 observations (ambiguous)

**linear_coeff** :

```json
[
  -0.387,
  4.509,
  6.706,
  6.706
]
```

**tree_splits** :

```json
[
  2,
  1,
  0
]
```

**tree_depth** :

```json
2
```

**tree_leaves** :

```json
4
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50",
  "road > 0.50 & area <= 2.50",
  "road > 0.50 & area > 2.50",
  "road > 0.50 & area > 2.50"
]
```

**mlp_hidden_road_difference** :

```json
1.227
```

**mlp_hidden_proxy_difference** :

```json
1.023
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.125,
  -0.759,
  0.568,
  0.404,
  0.325,
  -0.426,
  0.264,
  -0.546
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 6.706,
  "Tree": 0.0,
  "TinyMLP": 5.443
}
```

### Après 100 observations (ambiguous)

**linear_coeff** :

```json
[
  0.316,
  4.437,
  6.35,
  6.35
]
```

**tree_splits** :

```json
[
  6,
  0,
  1
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "proxy <= 0.50 & area <= 2.50 & area > 1.50",
  "proxy > 0.50 & area <= 2.50 & area > 1.50",
  "proxy <= 0.50 & area > 2.50 & area > 3.50",
  "proxy > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.251
```

**mlp_hidden_proxy_difference** :

```json
1.051
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.097,
  -0.814,
  0.557,
  0.399,
  0.096,
  -0.433,
  0.309,
  -0.524
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 6.35,
  "Tree": 12.818,
  "TinyMLP": 5.004
}
```

### Après 300 observations (ambiguous)

**linear_coeff** :

```json
[
  0.164,
  4.511,
  6.282,
  6.282
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.264
```

**mlp_hidden_proxy_difference** :

```json
1.057
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.072,
  -0.816,
  0.551,
  0.417,
  -0.005,
  -0.414,
  0.343,
  -0.513
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 6.282,
  "Tree": 0.0,
  "TinyMLP": 4.624
}
```

### Après 500 observations (disambiguation)

**linear_coeff** :

```json
[
  0.226,
  4.521,
  12.244,
  0.239
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.438
```

**mlp_hidden_proxy_difference** :

```json
0.996
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.013,
  -0.854,
  0.49,
  0.258,
  0.155,
  -0.507,
  0.539,
  -0.608
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 0.239,
  "Tree": 0.0,
  "TinyMLP": 0.127
}
```

### Après 900 observations (disambiguation)

**linear_coeff** :

```json
[
  0.374,
  4.467,
  12.44,
  0.047
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.501
```

**mlp_hidden_proxy_difference** :

```json
0.966
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.046,
  -0.864,
  0.542,
  0.317,
  0.037,
  -0.512,
  0.565,
  -0.575
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 0.047,
  "Tree": 0.0,
  "TinyMLP": 0.102
}
```

### Après 1600 observations (disambiguation)

**linear_coeff** :

```json
[
  0.289,
  4.498,
  12.419,
  0.11
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.55
```

**mlp_hidden_proxy_difference** :

```json
0.948
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.099,
  -0.87,
  0.578,
  0.289,
  0.013,
  -0.528,
  0.586,
  -0.582
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 0.11,
  "Tree": 0.0,
  "TinyMLP": 0.072
}
```


<!-- FIN 01_regression -->



---

<!-- DÉBUT 02_classification -->

# 2/6 — Classification : acquisition, coexistence et réorganisation des schèmes, sans TL

**Statut : étude expérimentale exécutée ; fichiers originaux conservés.**  
**Problème :** classer de petites images de 7 × 7 pixels représentant des traits horizontaux ou verticaux.  
**Périmètre :** apprentissage interne sur 3 200 observations, avec un indice trompeur et des sondes constantes. Aucune opération Tradition Learning.

## 1. Position du problème et définition opérationnelle

La classification consiste à apprendre des distinctions entre catégories. Notre exemple minimal est une image de 49 pixels :

- Classe 0 : trait **horizontal** ;
- Classe 1 : trait **vertical**.

Chaque image présente de légères variations de position et un bruit de pixels. Un **petit repère en haut à gauche** est artificiellement associé à l'orientation dans les 400 premières observations ; après cette phase, le repère devient indépendant de l'orientation. Les modèles ne connaissent pas cette règle cachée.

Ces images sont pédagogiques : elles ne représentent pas des maladies oculaires et n'ont aucune validité diagnostique. Elles permettent d'observer les mêmes phénomènes d'apprentissage sur une structure assez petite pour examiner les 49 entrées et toutes les couches d'un réseau.

Le schème est un **contenu représentationnel interne** acquis ou modifié, par exemple une régularité sur l'orientation, la position, les combinaisons de pixels, la présence du repère ou leurs relations. Ni un pixel brut, ni une activation, ni une règle d'arbre isolée ne deviennent automatiquement un schème.

Au lieu de ne regarder que les schèmes qui changent, nous suivons les distinctions simultanément présentes, stables ou instables, à chaque instant et à chaque niveau.

## 2. Séquence de données et observations

- **Entraînement :** 3 200 images binaires 7×7, dans un ordre conservé.
- **Contrôle :** 600 images de vérification séparées ; 8 images fixes de sondage à variations maîtrisées.
- **Graine :** `20261115`.
- **Points de contrôle :** t = 0, 40, 120, 300, 400, 550, 800, 1 200, 2 000, 3 200.
- **Changement de distribution :** avant t=401, repère et orientation coïncident selon la règle de génération ; ensuite le repère ne constitue plus un indice fiable.

Les sondes contrôlées examinent séparément trois différences : changement d'orientation, présence du repère, déplacement de position du trait. Ces sondes sont des outils d'observation du comportement et des représentations ; elles ne sont **pas** une identification exhaustive de tous les schèmes.

## 3. Les quatre algorithmes comparés

### 3.1. Régression logistique par SGD, incrémentale

Le classifieur reçoit directement les 49 pixels, calcule un score et ajuste des coefficients pour mieux distinguer les catégories. L'état appris associe une contribution statistique aux entrées, mais la relation acquise ne se réduit pas à un poids particulier.

Le dispositif suit simultanément l'influence de l'orientation, du repère et les estimations sur les images fixes ; les coefficients complets sont conservés dans le résultat original.

### 3.2. Bernoulli Naive Bayes

Pour chaque classe, Naive Bayes conserve des estimations de la probabilité d'apparition de chaque pixel, avec lissage. Les observations ajoutent progressivement des comptages qui modifient les distributions conditionnelles.

Le modèle exprime donc plusieurs associations en parallèle, y compris celles relatives au repère et aux régions traversées par le trait. L'hypothèse d'indépendance conditionnelle des pixels limite la manière dont il combine leurs relations.

### 3.3. Arbre CART de profondeur limitée

L'arbre apprend des divisions sur la valeur des pixels afin de séparer les classes. Dans le protocole, il est **reconstruit sur toutes les données déjà vues** à chaque point de contrôle. Les premières divisions peuvent sélectionner un pixel trompeur si celui-ci sépare parfaitement les observations initiales.

La transformation de l'arbre concerne les chemins, les seuils et les régions de décision. Les changements de divisions ne signifient pas nécessairement la disparition des informations auparavant exploitées, ni la création d'un schème unique pour chaque nœud.

### 3.4. Réseau MLP de taille pédagogique

Architecture : **49 → 12 → 6 → 1**. On conserve les réponses des 12 unités de la première couche cachée et des 6 unités de la seconde, ainsi que les différences entre leurs activations pour les images de contrôle.

Les contenus représentationnels peuvent être distribués, superposés ou mobilisés différemment suivant la couche. Les activations enregistrées renseignent sur les distinctions exprimées, **sans équivalence activation = schème**.

## 4. Le déroulement de l'apprentissage

### t = 0 : état avant apprentissage

Le classifieur incrémental et Naive Bayes n'ont pas encore estimé les relations à partir des données. Le réseau possède des activations issues de ses poids initialisés aléatoirement : ce sont des calculs internes, **pas des schèmes acquis grâce à cet entraînement**.

### t = 40 : premières associations

L'orientation et le repère sont tous les deux présents dans les exemples. La régression logistique est plus sensible au repère qu'à l'orientation sur les sondes (0,104 contre 0,045). Naive Bayes commence à estimer une forte association entre repère et catégorie. L'arbre peut privilégier immédiatement le repère. Le réseau exprime déjà plusieurs différences entre images.

### t = 120 et 300 : renforcement et coexistence

Le repère demeure fortement corrélé à la catégorie, tout comme les pixels dessinant les traits. Le modèle peut exploiter simultanément ces deux ensembles de relations.

Dans le MLP, la première couche exprime une différence d'orientation importante à t=120 (norme ~5,44) et une différence relative au repère (~0,82). La seconde exprime fortement l'orientation (~4,85) et devient beaucoup moins sensible au repère (~0,05). Les niveaux internes n'effectuent donc pas exactement les mêmes distinctions.

### t = 400 : le repère est encore entièrement corrélé

Pour la logistique, le contraste d'orientation est ~0,368 et celui du repère ~0,402. Naive Bayes estime encore presque une probabilité 1 du repère dans une classe et presque 0 dans l'autre. L'arbre utilise le repère en première division.

Cette situation ne prouve pas que le modèle a découvert une règle fiable sur les images : les données ne contiennent pas encore les contre-exemples nécessaires.

### t = 550, 800 et 1 200 : différenciation progressive

Les nouvelles images contredisent la corrélation entre repère et orientation. La logistique revoit progressivement l'influence du repère à ~0,283 puis ~0,152 et ~0,063, pendant que l'orientation devient plus influente (~0,502, ~0,647 et ~0,766).

Naive Bayes actualise **toutes** les probabilités des pixels, pas uniquement celle du repère. L'arbre reconstruit son organisation ; certaines divisions changent. Les couches du MLP continuent à exprimer des différences d'orientation, de repère et de position, mais celles-ci se propagent différemment vers la sortie.

### t = 2 000 et 3 200 : maintien de distinctions, réduction d'autres influences

La logistique produit un contraste d'orientation ~0,94 et de repère ~0,00075 à t=3200. L'arbre final utilise des pixels des régions où les traits sont observables, et non le marqueur comme première décision. Naive Bayes conserve néanmoins dans ses statistiques la contribution des anciennes observations : l'association du repère diminue mais ses fréquences ne deviennent pas nécessairement identiques. Le réseau exprime encore le repère dans une couche sans que cette variation commande la catégorie finale.

## 5. Comparaison détaillée des sensibilités aux différents instants

**Notation dans le tableau :** `orientation / repère`, variations observées sur les sondes de contrôle. Les chiffres ne représentent ni des poids ni des quantités de schèmes.

| Algorithme | t=40 | t=400 | t=800 | t=3 200 |+|---|---|---|---|---|
| Logistique | 0,05 / 0,10 | 0,37 / 0,40 | 0,65 / 0,15 | 0,94 / 0,00 |
| Bernoulli Naive Bayes | 0,42 / 0,47 | 0,39 / 0,61 | 0,93 / 0,06 | 0,97 / 0,01 |
| Arbre CART | 0,00 / 1,00 | 0,00 / 1,00 | 0,60 / 0,30 | 0,91 / 0,00 |
| Petit MLP | 0,51 / 0,48 | 1,00 / 0,00 | 1,00 / 0,00 | 1,00 / 0,00 |

Le tableau exhaustif, notamment les états t=0, 120, 300, 550, 1 200 et 2 000, figure dans `CHRONOLOGIE_COMPLETE.md` ; les valeurs non arrondies sont dans le CSV et le JSON conservés.

### L'association du repère selon Naive Bayes

| Observations | P(repère présent \| verticale) | P(repère présent \| horizontale) |
|---:|---:|---:|
| 40 | 0,96154 | 0,05556 |
| 120 | 0,98246 | 0,01493 |
| 400 | 0,99459 | 0,00457 |
| 550 | 0,84906 | 0,10727 |
| 800 | 0,73522 | 0,20482 |
| 1 200 | 0,67361 | 0,32962 |
| 2 000 | 0,59495 | 0,38955 |
| 3 200 | 0,55137 | 0,44227 |

La distribution conditionnelle conserve l'historique de toutes les observations ; une faible différence peut persister sans être déterminante pour la classification finale. Il serait incorrect de dire que le modèle a effacé toute relation avec le repère.

## 6. Les niveaux internes du MLP : inventaire des distinctions simultanées

Nous avons mesuré la différence d'activation induite par un changement contrôlé, d'abord dans la première couche cachée (12 dimensions), puis dans la deuxième (6 dimensions).

| Observations | Couche 1 — orientation | Couche 1 — repère | Couche 2 — orientation | Couche 2 — repère |
|---:|---:|---:|---:|---:|
| 0 | 0,60 | 0,26 | 0,20 | 0,08 |
| 40 | 2,88 | 1,12 | 2,94 | 1,80 |
| 120 | 5,44 | 0,82 | 4,85 | 0,05 |
| 400 | 5,79 | 0,92 | 4,89 | 0,01 |
| 800 | 5,87 | 0,51 | 4,89 | 0,004 |
| 3 200 | 5,56 | 0,48 | 4,88 | 0,002 |

L'orientation, la position du trait et le repère peuvent être exprimés simultanément. À t=3 200, la première couche continue à réagir au repère, tandis que la deuxième et la décision finale y réagissent très peu.

Ces distances ne sont **pas** comparables entre couches comme une quantité unique d'information : les dimensions et les transformations diffèrent. Elles ne prouvent pas qu'un schème « repère » serait isolé dans un neurone. Des régularités peuvent être combinées ou distribuées entre de nombreux éléments.

## 7. Relations apprises, corrigées, maintenues et non identifiables

Nous distinguons :

- **contenu utile acquis :** différenciation entre configurations horizontales et verticales ;
- **contenu trompeur initial :** association du marqueur avec la classe ;
- **contenu toujours exprimé :** certaines réponses cachées au marqueur, même lorsqu'il n'influence presque plus le résultat ;
- **autres contenus potentiels :** sensibilité aux positions, configurations locales de pixels, bruit, combinaisons de régions ;
- **contenu non déductible de nos sondes :** tous les motifs réellement représentés au-delà des huit images fixes.

Une étiquette ne signifie pas que le modèle possède une compréhension générale de ce qu'est un « trait ». Une classification correcte sur un contrôle donné n'identifie pas l'organisation causale de l'information utilisée. L'analyse interne exige les paramètres, distributions et activations complets, pas seulement les sorties.

## 8. Les fichiers originaux de l'expérience

- `experiment_classification_schemes.py` : code complet générant et entraînant les quatre modèles ;
- `experiment_classification_schemes_dataset.npz` : 3 200 observations, 600 vérifications, images de sondage ;
- `experiment_classification_schemes_results.json` : états, distributions, divisions et activations aux checkpoints ;
- `experiment_classification_schemes_summary.csv` : trajectoires comparatives ;
- `experiment_classification_schemes_manifest.json` : graine, configuration, versions, empreintes ;
- `classification_run_log.txt` : trace d'exécution existante dans l'environnement, conservée comme pièce complémentaire ;
- `CHRONOLOGIE_COMPLETE.md` : transcription complète des indicateurs publiés par checkpoint.

Exécution : `python experiment_classification_schemes.py`. Dépendances exactes et limites dans le manifeste/code. Les résultats peuvent varier suivant l'environnement.

## 9. Ce que l'étude établit et ce qu'elle n'établit pas

1. Les modèles confrontés aux mêmes observations peuvent développer des contenus internes différents.
2. Les régularités pertinentes et trompeuses peuvent être apprises en parallèle.
3. Une sensibilité d'une couche peut persister alors qu'elle est atténuée plus loin.
4. Le choix des structures (logistique, probabiliste, arbre, neurones) modifie la manière d'acquérir et de maintenir les relations.
5. Les sondes documentent des distinctions ; elles ne dénombrent pas les schèmes et ne les localisent pas automatiquement.
6. Une seule simulation ne prouve pas la généralité statistique des trajectoires.
7. **Aucune opération TL** n'intervient dans l'apprentissage.

La totalité des états numériques et des observations est conservée dans les fichiers originaux, sans réduction au présent exposé.


---

# Chronologie complète des indicateurs — 02_classification

**Tableau directement extrait du CSV expérimental original, sans recalcul ni interpolation.**

- Fichier original : `originaux/experiment_classification_schemes_summary.csv`.
- Lignes expérimentales : **10**.
- Colonnes conservées : **17**.
- Les chiffres sont des mesures ou paramètres du protocole, **pas des dénombrements de schèmes**.
- La totalité des états multidimensionnels, au-delà des indicateurs de ce tableau, est conservée dans le JSON/NPZ originaux.

| t | SGD_logistic_orientation | SGD_logistic_marker | SGD_logistic_accuracy | Bernoulli_NB_orientation | Bernoulli_NB_marker | Bernoulli_NB_accuracy | CART_tree_orientation | CART_tree_marker | CART_tree_accuracy | Tiny_MLP_orientation | Tiny_MLP_marker | Tiny_MLP_accuracy | MLP_hidden_1_orientation | MLP_hidden_1_marker | MLP_hidden_2_orientation | MLP_hidden_2_marker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | — | — | — | — | — | — | — | — | — | 0.01609 | 0.00555 | 0.54333 | 0.60294 | 0.25921 | 0.20025 | 0.07625 |
| 40 | 0.04532 | 0.10437 | 0.57167 | 0.4223 | 0.4744 | 0.77167 | 0.0 | 1.0 | 0.53 | 0.51164 | 0.48435 | 0.85667 | 2.88039 | 1.11743 | 2.94186 | 1.7971 |
| 120 | 0.26233 | 0.2138 | 0.67667 | 0.64433 | 0.35537 | 0.71167 | 0.0 | 1.0 | 0.53 | 0.99852 | 0.00011 | 0.88833 | 5.44446 | 0.81637 | 4.85272 | 0.04532 |
| 300 | 0.37721 | 0.35129 | 0.65667 | 0.51663 | 0.48326 | 0.65667 | 0.0 | 1.0 | 0.53 | 0.99919 | 1e-05 | 0.89 | 6.02943 | 0.69004 | 4.89332 | 0.00423 |
| 400 | 0.36756 | 0.40246 | 0.63833 | 0.38919 | 0.6107 | 0.66 | 0.0 | 1.0 | 0.53 | 0.9995 | 1e-05 | 0.89667 | 5.78922 | 0.9188 | 4.88639 | 0.0114 |
| 550 | 0.50158 | 0.28304 | 0.82833 | 0.87766 | 0.11626 | 0.93 | 0.59217 | 0.38628 | 0.665 | 0.9994 | 1e-05 | 0.96833 | 6.01539 | 0.56318 | 4.89236 | 0.00596 |
| 800 | 0.64653 | 0.15231 | 0.965 | 0.93165 | 0.05599 | 0.97333 | 0.59944 | 0.30379 | 0.82167 | 0.99964 | 0.0 | 0.98333 | 5.86711 | 0.50993 | 4.89357 | 0.00413 |
| 1200 | 0.76589 | 0.06269 | 0.98 | 0.95282 | 0.02858 | 0.98333 | 0.72241 | 0.10703 | 0.82667 | 0.99968 | 0.0 | 0.99167 | 5.70679 | 0.46514 | 4.88637 | 0.00507 |
| 2000 | 0.88115 | 0.01948 | 0.97833 | 0.96221 | 0.01466 | 0.98333 | 0.91429 | 0.0 | 0.90333 | 0.99979 | 0.0 | 0.99167 | 5.61225 | 0.43961 | 4.88053 | 0.00468 |
| 3200 | 0.94019 | 0.00075 | 0.97667 | 0.96511 | 0.0074 | 0.98333 | 0.90797 | 0.0 | 0.91833 | 0.99984 | 0.0 | 0.99167 | 5.56419 | 0.48095 | 4.87789 | 0.0018 |


<!-- FIN 02_classification -->



---

<!-- DÉBUT 03_clustering -->

# 3/6 — Clustering : évolution des organisations acquises, sans TL

**Statut : expérience synthétique exécutée ; originaux conservés.**  
**Problème :** découvrir des regroupements dans un ensemble de parcelles fictives, sans étiquettes de groupe fournies aux algorithmes.  
**Données :** 3 200 observations, 3 caractéristiques, 4 algorithmes, 10 checkpoints.  
**Objet :** comprendre tous les contenus organisationnels acquis aux différents instants, pas seulement les changements du nombre de groupes.

## 1. Différence essentielle avec la classification

Le clustering recherche une organisation des observations sans recevoir une classe-cible connue pour chaque observation. Ses résultats peuvent prendre la forme de centres, densités, paramètres de distributions, régions ou relations de voisinage.

Le schème désigne ici, dans notre langage de travail, une régularité ou relation interne **acquise ou modifiée** susceptible d'aider le modèle à organiser les observations. Il ne devient pas automatiquement équivalent à un centroïde, une composante gaussienne, un point central ou une étiquette de groupe.

Il faut aussi reconnaître une différence importante entre les méthodes : certaines déterminent un état à appliquer à de nouveaux exemples ; d'autres, comme DBSCAN dans l'implémentation utilisée, déterminent principalement une organisation sur les observations vues, sans méthode `predict` standard.

## 2. Scénario expérimental

Le générateur fournit 3 200 observations synthétiques avec les coordonnées :

- `geometry_x` et `geometry_y` : structure géométrique formant deux régions sous-jacentes ;
- `spurious_indicator_z` : indice indirect corrélé à la région pendant les 400 premières observations, puis généré indépendamment.

Quelques observations sont atypiques. Aucune étiquette des régions sous-jacentes n'est utilisée lors du `fit`. Les étiquettes éventuellement conservées dans le NPZ servent uniquement à l'audit postérieur, et ne doivent pas être interprétées comme des informations transmises aux algorithmes.

**Graine :** 20261115. **Checkpoints :** 80, 160, 280, 400, 560, 800, 1 200, 1 800, 2 400, 3 200.

Le script conserve des sondes spatiales fixes : points au centre des régions, au voisinage des frontières, et points dont les coordonnées X, Y restent constantes tandis que Z change. Ces sondes permettent d'observer l'influence de Z mais **ne définissent pas un nombre de schèmes**.

## 3. Méthodes et véritables mécanismes d'apprentissage

### 3.1. K-Means

Le modèle dispose de deux centres initiaux qu'il réajuste en alternant l'affectation aux centres les plus proches et le recalcul des centres. À chaque checkpoint, une nouvelle instance de K-Means est ajustée sur le préfixe complet des observations.

**États et relations conservés :** centres XYZ, affectations, distances aux centres, effectifs, moyennes et covariances des groupes calculés pour l'étude, inertie et sondes. K-Means ne « connaît » pas le sens métier des groupes ; il optimise un critère géométrique.

### 3.2. MiniBatch K-Means

Même famille de représentations par centres, mais apprentissage par lots de **40 observations** : `partial_fit` modifie progressivement les centres, sans repartir d'une initialisation neuve à chaque checkpoint.

Les centres intermédiaires expriment une organisation acquise au fil des lots, pouvant être proche de l'organisation de K-Means complet sans partager exactement le même parcours.

### 3.3. Mélange gaussien par EM

Deux composantes probabilistes, ajustées par l'algorithme Expectation–Maximization sur les observations cumulées. L'état appris comporte : poids de chaque composante, moyennes, matrices de covariance et responsabilités probabilistes.

Cela permet d'observer non seulement la séparation des centres, mais **les dispersions et les relations entre les variables à l'intérieur de chaque composante**. Les assignations ne sont pas nécessairement exclusives dans le calcul probabiliste ; les responsabilités peuvent être graduelles.

### 3.4. DBSCAN

Regroupe les observations selon la densité de leurs voisinages et leur connexité. Son état enregistré comporte labels, exemples centraux, bruit, points périphériques et voisinages de sondes. Le modèle ne détermine pas un ensemble de deux centres.

Le nombre de points centraux peut croître mécaniquement avec la taille de l'échantillon à `eps` et `min_samples` fixés. Cela n'est pas un indicateur universel de maturation d'un contenu représentationnel.

## 4. Trajectoire temporelle — les observations ne restent pas statistiquement semblables

Pendant les 400 premières observations, l'indice Z aide fortement à distinguer les deux régions. Par la suite, cet effet diminue.

| Observations cumulées | Corrélation observée entre X et Z |
|---:|---:|
| 80 | 0,924 |
| 160 | 0,895 |
| 280 | 0,913 |
| 400 | 0,900 |
| 560 | 0,706 |
| 800 | 0,472 |
| 1 200 | 0,319 |
| 1 800 | 0,214 |
| 2 400 | 0,147 |
| 3 200 | 0,113 |

Cette corrélation décrit le jeu de données ; ce n'est pas une observation directe d'un schème. Son intérêt est de confronter le changement de données aux **structures effectivement acquises par les algorithmes**.

## 5. K-Means : suivre simultanément la séparation X, Y et Z

Les deux centres apprennent des organisations dans les trois dimensions. Aux deux checkpoints suivants, les valeurs enregistrées sont approximativement :

| Instant | Centre gauche (X,Y,Z) | Centre droit (X,Y,Z) |
|---|---|---|
| 400 | (−2,29 ; −0,22 ; −1,25) | (2,22 ; 0,32 ; 1,30) |
| 3 200 | (−2,27 ; −0,22 ; −0,13) | (2,30 ; 0,29 ; 0,13) |

Il y a simultanément :

- **Maintien** de la distinction selon X ;
- **Maintien** d'une différence moyenne selon Y ;
- **Affaiblissement** de la séparation selon Z ;
- **Évolution** des distances, régions de proximité et appartenances possibles.

L'écart des centres selon Z passe d'environ 2,59 à 80 observations à 2,545 à 400, 1,880 à 560, 1,243 à 800, puis 0,259 à 3 200.

Pour les sondes où X et Y sont fixés, le changement de Z provoque un changement de groupe dans environ **60 %** des comparaisons à 400 observations et **13,3 %** à 3 200 observations. Ces pourcentages caractérisent les sondes choisies, pas une propriété universelle de l'espace.

L'étude interne ne porte donc pas uniquement sur « Z est abandonné » : elle inclut la géométrie persistante selon X et Y, la dispersion des observations et le système de proximités tout entier.

## 6. MiniBatch K-Means : acquisition progressive par lots

Le modèle rencontre les données dans l'ordre et actualise les centres avec des minibatches de 40 observations. Les coordonnées approchent finalement celles de K-Means complet :

| Méthode à 3 200 observations | Centre gauche (X,Z) | Centre droit (X,Z) |
|---|---|---|
| K-Means | (−2,27 ; −0,13) | (2,30 ; 0,13) |
| MiniBatch K-Means | (−2,27 ; −0,13) | (2,29 ; 0,13) |

Deux mécanismes informatiques distincts peuvent donc aboutir à une organisation très voisine. Cela ne veut pas dire qu'ils ont effectué les mêmes opérations ni appris exactement les mêmes représentations intermédiaires.

Les acquisitions concernent des centres évolutifs, mais aussi leurs relations avec les points observés. La proximité finale ne suffit pas à reconstruire leur trajectoire : c'est pourquoi les checkpoints sont conservés.

## 7. Gaussian Mixture : apparition et transformation de distributions entières

Dans un mélange gaussien, les relations acquises portent sur les composantes, leurs moyennes, leurs covariances et la manière dont chaque observation s'y rattache probabilistiquement.

Pendant la phase initiale, Z est relativement homogène au sein de chaque région. Après t=400, chaque région accueille une gamme bien plus large de valeurs de Z.

| Observations | Écart des moyennes selon Z | Variance Z moyenne des composantes |
|---:|---:|---:|
| 80 | 2,588 | 0,240 |
| 400 | 2,545 | 0,235 |
| 560 | 1,880 | 0,725 |
| 800 | 1,243 | 1,110 |
| 1 200 | 0,800 | 1,210 |
| 1 800 | 0,525 | 1,295 |
| 2 400 | 0,340 | 1,260 |
| 3 200 | 0,259 | 1,245 |

Ces deux colonnes n'ont pas la même dimension physique. La comparaison porte sur **leurs trajectoires**, pas sur une valeur commune.

Le modèle représente en parallèle : la différence spatiale entre régions, l'incertitude d'appartenance des points proches des frontières, la distribution de Z au sein de chaque région et les relations de covariance entre caractéristiques.

Si une distribution s'élargit, cela ne signifie pas nécessairement qu'un schème aurait été créé ou détruit ; cela atteste la modification d'un contenu probabiliste appris.

## 8. DBSCAN : stabilité des groupes et transformation des voisinages

| Observations | Groupes trouvés | Exemples centraux | Points considérés comme bruit |
|---:|---:|---:|---:|
| 80 | 2 | 56 | 6 |
| 400 | 2 | 382 | 7 |
| 800 | 2 | 727 | 29 |
| 1 800 | 2 | 1 718 | 29 |
| 3 200 | 2 | 3 109 | 35 |

Dans ce scénario, DBSCAN conserve **deux groupes** à ces instants. Pourtant, les voisinages denses s'étendent, des points changent de statut (central, périphérique, bruit) et de nouvelles régions de l'espace sont couvertes.

Pour une sonde située dans la région géométrique gauche, avec Z=0, le nombre de points centraux présents dans son voisinage de rayon fixé passe de **5 à t=400** à **327 à t=3 200**. Ce décompte croît notamment parce que le nombre total d'observations augmente. Il ne s'agit donc pas d'une échelle de richesse représentationnelle.

Les consultations des points de sonde ne sont pas une méthode `predict` standard fournie par DBSCAN. Les états des 3 200 observations comprennent les appartenances complètes et leurs voisinages, non seulement le nombre de groupes.

## 9. Inventaire des organisations à observer à chaque instant

| Aspect du contenu organisationnel | K-Means / MiniBatch | Mélange gaussien | DBSCAN |
|---|---|---|---|
| Régions géométriques | centres, distances, affectations | moyennes, responsabilités | composantes denses et connexité |
| Relations entre variables | positions relatives des centres | matrices de covariance | géométrie des voisinages |
| Dispersion au sein de groupes | statistiques calculables sur les groupes | modélisée dans chaque composante | distribution des points centraux/périphériques |
| Cas atypiques | affectés au centre le plus proche | probabilités d'appartenance éventuellement faibles | points éventuellement déclarés bruit |
| Dynamique d'apprentissage | refit complet ou actualisation par lots | estimations EM sur préfixes | refit des zones de densité |

Le mot « schème » ne sert pas à renommer mécaniquement chacune de ces structures. C'est l'acquisition de **contenus de relation et d'organisation** que nous étudions, en conservant la possibilité qu'ils soient distribués ou non isolables.

## 10. Fichiers, reproduction et précautions

**Originaux à conserver inchangés :**

- `experiment_clustering_schemes.py` : code complet ;
- `experiment_clustering_schemes_dataset.npz` : observations et sondes exactes ;
- `experiment_clustering_schemes_results.json` : états internes cumulés, tous les centres, covariances, affectations, exemples centraux et sondes ;
- `experiment_clustering_schemes_summary.csv` : 40 états, 4 algorithmes × 10 checkpoints ;
- `experiment_clustering_schemes_manifest.json` : versions et empreintes ;
- `experiment_clustering_schemes_README.md` : notice technique originale ;
- `experiment_clustering_schemes_package.zip` : **archive originale**, également conservée intacte.

Reproduction : `python experiment_clustering_schemes.py`, avec NumPy et scikit-learn. Les versions exactes sont dans le manifeste. Les résultats décrivent une simulation à une graine, pas une validation répliquée sur plusieurs jeux de données.

**Précautions scientifiques :** K-Means et Gaussian Mixture sont paramétrés pour rechercher deux groupes ; retrouver deux groupes ne prouve pas qu'ils auraient découvert librement le nombre véritable. Une structure qui converge n'implique pas une signification métier valide. Aucun mécanisme Tradition Learning n'a été ajouté.

Les indicateurs de **tous les instants et de tous les algorithmes** figurent dans `CHRONOLOGIE_COMPLETE.md`, et les états sans perte dans le JSON original.


---

# Chronologie complète des indicateurs — 03_clustering

**Tableau directement extrait du CSV expérimental original, sans recalcul ni interpolation.**

- Fichier original : `originaux/experiment_clustering_schemes_summary.csv`.
- Lignes expérimentales : **40**.
- Colonnes conservées : **12**.
- Les chiffres sont des mesures ou paramètres du protocole, **pas des dénombrements de schèmes**.
- La totalité des états multidimensionnels, au-delà des indicateurs de ce tableau, est conservée dans le JSON/NPZ originaux.

| n | algorithm | observed_correlation_geometry_x_spurious_z | ari_audit_not_used_in_fit | cluster_count | contrast_z | centroid_difference_z | inertia | probe_component_entropy | noise_fraction | core_fraction | probe_center_core_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80 | KMeans_refit | 0.9240708315755822 | 1.0 | 2 | 0.6 | 2.587701062024558 | 66.7235593015761 | — | — | — | — |
| 80 | MiniBatchKMeans_incremental | 0.9240708315755822 | 1.0 | 2 | 0.6 | 2.587701062024557 | 66.7235593015761 | — | — | — | — |
| 80 | GaussianMixture_EM | 0.9240708315755822 | 1.0 | 2 | 0.49393061395842647 | 2.587701062024519 | — | 0.05529467715114658 | — | — | — |
| 80 | DBSCAN | 0.9240708315755822 | 1.0 | 2 | — | — | — | — | 0.075 | 0.7 | 0 |
| 160 | KMeans_refit | 0.8951971165022868 | 1.0 | 2 | 0.6 | 2.581461254284704 | 145.7685811343945 | — | — | — | — |
| 160 | MiniBatchKMeans_incremental | 0.8951971165022868 | 1.0 | 2 | 0.6 | 2.581461254284704 | 145.7685811343945 | — | — | — | — |
| 160 | GaussianMixture_EM | 0.8951971165022868 | 1.0 | 2 | 0.5789832976252293 | 2.581461373276259 | — | 0.0646295451378875 | — | — | — |
| 160 | DBSCAN | 0.8951971165022868 | 1.0 | 2 | — | — | — | — | 0.03125 | 0.88125 | 0 |
| 280 | KMeans_refit | 0.912638054502137 | 1.0 | 2 | 0.6 | 2.593752881076689 | 235.87706024732108 | — | — | — | — |
| 280 | MiniBatchKMeans_incremental | 0.912638054502137 | 1.0 | 2 | 0.6 | 2.5937528810766883 | 235.87706024732103 | — | — | — | — |
| 280 | GaussianMixture_EM | 0.912638054502137 | 1.0 | 2 | 0.599833033787037 | 2.5937529069027843 | — | 0.054620410386997366 | — | — | — |
| 280 | DBSCAN | 0.912638054502137 | 1.0 | 2 | — | — | — | — | 0.017857142857142856 | 0.9321428571428572 | 0 |
| 400 | KMeans_refit | 0.8999870552892796 | 1.0 | 2 | 0.6 | 2.5454042802424954 | 366.67276216084815 | — | — | — | — |
| 400 | MiniBatchKMeans_incremental | 0.8999870552892796 | 1.0 | 2 | 0.6 | 2.5454042802424945 | 366.67276216084815 | — | — | — | — |
| 400 | GaussianMixture_EM | 0.8999870552892796 | 1.0 | 2 | 0.5999886005679652 | 2.5454043205546193 | — | 0.041875391646407 | — | — | — |
| 400 | DBSCAN | 0.8999870552892796 | 1.0 | 2 | — | — | — | — | 0.0175 | 0.955 | 0 |
| 560 | KMeans_refit | 0.7060329270491088 | 1.0 | 2 | 0.6 | 1.8837968845015394 | 796.4413194967319 | — | — | — | — |
| 560 | MiniBatchKMeans_incremental | 0.7060329270491088 | 1.0 | 2 | 0.6 | 1.8837968845015394 | 796.4413194967319 | — | — | — | — |
| 560 | GaussianMixture_EM | 0.7060329270491088 | 1.0 | 2 | 0.3474156317414881 | 1.8837965565165584 | — | 0.12193557611666711 | — | — | — |
| 560 | DBSCAN | 0.7060329270491088 | 0.996054095124525 | 2 | — | — | — | — | 0.039285714285714285 | 0.8928571428571429 | 0 |
| 800 | KMeans_refit | 0.47170015347992816 | 1.0 | 2 | 0.4666666666666667 | 1.2430864516996714 | 1485.915748900854 | — | — | — | — |
| 800 | MiniBatchKMeans_incremental | 0.47170015347992816 | 1.0 | 2 | 0.4666666666666667 | 1.2430864516996714 | 1485.915748900854 | — | — | — | — |
| 800 | GaussianMixture_EM | 0.47170015347992816 | 1.0 | 2 | 0.20197641603901986 | 1.243078789674931 | — | 0.1328293977501028 | — | — | — |
| 800 | DBSCAN | 0.47170015347992816 | 0.9869825963299762 | 2 | — | — | — | — | 0.03625 | 0.90875 | 0 |
| 1200 | KMeans_refit | 0.3192390749125099 | 1.0 | 2 | 0.2 | 0.7940453311413849 | 2327.882175286745 | — | — | — | — |
| 1200 | MiniBatchKMeans_incremental | 0.3192390749125099 | 1.0 | 2 | 0.2 | 0.7976619599639037 | 2327.908450809987 | — | — | — | — |
| 1200 | GaussianMixture_EM | 0.3192390749125099 | 1.0 | 2 | 0.11610575583983664 | 0.7955584568167198 | — | 0.14154979205623539 | — | — | — |
| 1200 | DBSCAN | 0.3192390749125099 | 0.9864063771447085 | 2 | — | — | — | — | 0.021666666666666667 | 0.9408333333333333 | 0 |
| 1800 | KMeans_refit | 0.21444973805856882 | 1.0 | 2 | 0.2 | 0.5242881913611928 | 3675.882981429054 | — | — | — | — |
| 1800 | MiniBatchKMeans_incremental | 0.21444973805856882 | 1.0 | 2 | 0.2 | 0.5267486094207634 | 3675.9003995546473 | — | — | — | — |
| 1800 | GaussianMixture_EM | 0.21444973805856882 | 1.0 | 2 | 0.05949351240663483 | 0.5249559080706652 | — | 0.14076805452684918 | — | — | — |
| 1800 | DBSCAN | 0.21444973805856882 | 0.9741635657242954 | 2 | — | — | — | — | 0.01611111111111111 | 0.9544444444444444 | 0 |
| 2400 | KMeans_refit | 0.14689495298252847 | 1.0 | 2 | 0.2 | 0.3428782967423884 | 4798.033625090826 | — | — | — | — |
| 2400 | MiniBatchKMeans_incremental | 0.14689495298252847 | 1.0 | 2 | 0.2 | 0.34471855557367265 | 4798.046557730569 | — | — | — | — |
| 2400 | GaussianMixture_EM | 0.14689495298252847 | 1.0 | 2 | 0.033099025514345154 | 0.34316354612669686 | — | 0.14690535306001706 | — | — | — |
| 2400 | DBSCAN | 0.14689495298252847 | 0.9714823936230174 | 2 | — | — | — | — | 0.012083333333333333 | 0.9620833333333333 | 0 |
| 3200 | KMeans_refit | 0.11337896197454622 | 1.0 | 2 | 0.13333333333333333 | 0.25929229252299524 | 6337.569433091272 | — | — | — | — |
| 3200 | MiniBatchKMeans_incremental | 0.11337896197454622 | 1.0 | 2 | 0.13333333333333333 | 0.2606449969573449 | 6337.579089271852 | — | — | — | — |
| 3200 | GaussianMixture_EM | 0.11337896197454622 | 1.0 | 2 | 0.020491957463274178 | 0.25907007997571163 | — | 0.14952729006263613 | — | — | — |
| 3200 | DBSCAN | 0.11337896197454622 | 0.9692533524626229 | 2 | — | — | — | — | 0.0109375 | 0.9715625 | 0 |


<!-- FIN 03_clustering -->



---

<!-- DÉBUT 04_generation -->

# 4/6 — Génération : acquisition de régularités de séquence, sans TL

**Statut : expérience exécutée ; fichiers originaux et checkpoints conservés.**  
**Problème :** apprendre à générer des séquences de quatre tokens dans un langage artificiel élémentaire.  
**Données :** 3 200 séquences d'entraînement, 600 séquences distinctes de vérification ; 5 modèles ; 11 états.  
**Périmètre :** observer l'apprentissage interne, la formation des régularités de séquence et leurs combinaisons, sans introduire Tradition Learning.

## 1. Pourquoi le langage artificiel est un bon cas pédagogique

La génération consiste à apprendre des régularités qui permettent de produire de nouveaux échantillons ou séquences. Un modèle génératif n'est pas nécessairement un LLM : même un modèle de Markov à n-grammes apprend des distributions qui servent à produire des séquences.

Le cas volontairement minimal rend visibles les distributions conditionnelles, leurs évolutions, les limites de la longueur du contexte et les représentations d'un petit réseau neuronal. Le schème désigne ici un **contenu représentationnel acquis ou modifié**, pouvant concerner une relation conditionnelle, la structure de la séquence, une association animal–action, une dépendance au lieu ou une combinaison de plusieurs facteurs.

Un mot, un compteur de fréquence, une probabilité finale ou une activation n'est pas automatiquement un schème. Une sortie générée n'est pas elle-même une acquisition durable si le modèle n'apprend pas pendant sa production.

## 2. Un seul problème et les mêmes données pour cinq modèles

Chaque séquence d'entraînement comporte exactement quatre tokens :

```text
ANIMAL → LIEU → COULEUR → ACTION
```

Exemples pédagogiques :

```text
chat   → jardin → bleu  → grimpe
chien  → jardin → rouge → court
chat   → maison → rouge → dort
chien  → maison → bleu  → dort
```

**Règle synthétique de production des séquences :**

- chat dans la maison : `dort` est généralement attendu ;
- chien dans la maison : `dort` est généralement attendu ;
- chat dans le jardin : `grimpe` est généralement attendu ;
- chien dans le jardin : `court` est généralement attendu.

L'action principale est choisie dans environ 90 % des cas, mais d'autres actions sont possibles. Les modèles apprennent donc des régularités probabilistes, non un ensemble de règles nécessairement déterministes.

Pendant les **400 premières séquences**, la couleur accompagne l'animal (chat/bleu, chien/rouge). Après la 400e, elle est indépendante. Des combinaisons initialement absentes peuvent alors apparaître, notamment « chat, jardin, rouge ».

**États observés :** 0, 40, 120, 280, 400, 560, 800, 1 200, 1 800, 2 400, 3 200. **Graine :** 20261115.

Le jeu conserve huit contextes de contrôle : toutes les combinaisons entre les deux animaux, les deux lieux et les deux couleurs. Nous étudions les trois actions sur ces contextes et, pour le réseau, les activations à plusieurs niveaux.

## 3. Les cinq méthodes de génération

### 3.1. Unigramme

Apprend la fréquence générale des tokens, sans tenir compte du contexte. Il peut apprendre qu'un token d'action est fréquent, mais ne peut pas acquérir directement une relation conditionnelle du type « ce chat dans ce lieu réalise telle action ».

### 3.2. Bigramme

Apprend les fréquences et probabilités du prochain token conditionnellement au **token immédiatement précédent**. Au moment de générer l'action, le dernier token est la couleur. Le modèle peut acquérir une association couleur–action, mais il n'a plus directement accès au lieu et à l'animal précédents.

### 3.3. Trigramme

Apprend des continuations conditionnées par les **deux derniers tokens**. Au moment de générer l'action, il voit le lieu et la couleur, mais pas directement l'animal. Il peut donc représenter une distinction associée au lieu, sans reproduire automatiquement toutes les dépendances animal–action.

### 3.4. 4-gramme

Le modèle reçoit les **trois tokens précédents**, donc l'animal, le lieu et la couleur. Il peut apprendre des distributions différentes pour chaque contexte précis. Il ne généralise cependant pas automatiquement d'un contexte jamais rencontré à un autre par une représentation partagée : avec lissage additif, un contexte absent fournit une distribution par défaut, et non une connaissance spécifique acquise.

### 3.5. Petit réseau neuronal génératif

Architecture : trois tokens de contexte → embeddings de **dimension 8** → couche cachée **16 unités** → probabilités sur **11 tokens**. Optimisation numérique pour prédire le prochain token. Les embeddings, transformations cachées et sorties sont enregistrés aux onze états.

Le réseau peut partager des représentations entre différents contextes grâce à ses paramètres communs, sans que chaque dimension d'embedding ou chaque neurone corresponde à un schème distinct.

Les n-grammes utilisent des comptages avec lissage additif ; le réseau ajuste ses paramètres. Ce ne sont pas des trajectoires équivalentes en nombre de calculs.

## 4. Ce qui se forme successivement dans les modèles

### t=0 : absence d'acquis issus du jeu

Les n-grammes ne disposent pas encore de statistiques apprises. Les distributions uniformes initiales proviennent du lissage et ne doivent pas être présentées comme des régularités découvertes.

Le réseau peut produire des activations à partir de son initialisation aléatoire. Ce ne sont pas des schèmes issus du jeu d'apprentissage.

### t=40, 120 et 280 : plusieurs régularités coexistent

Les fréquences générales des tokens se forment. Les n-grammes plus longs accumulent aussi des relations entre les contextes et les continuations. Le réseau apprend simultanément la structure des séquences, les associations liées au lieu, à l'animal et, dans les premières données, à la couleur.

Nous ne suivons pas uniquement l'association trompeuse : le vocabulaire, l'ordre des catégories de tokens, les fréquences des actions et les régularités entre animal–lieu–action constituent simultanément la matière représentationnelle étudiée.

### t=400 : certains contextes sont encore absents

Pour le 4-gramme, « chat, jardin, rouge » n'a jamais été rencontré puisque les chats portent encore systématiquement le marqueur bleu. Le modèle n'a pas appris une distribution spécifique à cette combinaison.

Un contraste élevé entre contextes peut donc provenir non seulement d'une association trompeuse acquise, mais aussi de **l'absence totale d'observations** pour certains contextes et de l'effet du lissage.

### t=560, 800 et au-delà : nouveaux contextes, nouvelles distributions

Les marqueurs deviennent indépendants et les combinaisons auparavant absentes apparaissent. Le 4-gramme peut désormais apprendre leurs fréquences spécifiques. Les modèles utilisant un contexte plus court révisent aussi les distributions qu'ils possèdent déjà.

### Exemple détaillé : « chat, jardin, rouge » pour le 4-gramme

| Instant | État du contexte | Probabilité conditionnelle de `grimpe` parmi les trois actions |
|---|---|---:|
| 0 | Pas d'exemple | Non acquise (distribution de lissage) |
| 40 | Contexte absent | Distribution par défaut |
| 400 | Contexte encore absent | Distribution par défaut |
| 560 | Combinaison rencontrée | 83,0 % |
| 800 | Association consolidée | 89,4 % |
| 3 200 | Relation toujours représentée | 87,0 % |

Cette régularité peut apparaître alors que d'autres relations, telles que les contextes de la maison et la structure du langage, sont déjà représentées depuis de nombreux instants. Il n'y a **pas un schème unique qui évoluerait en remplacement de tous les autres**.

## 5. Comparaison finale de ce que le contexte permet de représenter

Les contrastes sont des **distances de variation totale moyennes** entre distributions d'actions obtenues en faisant varier un seul facteur dans huit contextes fixes. Ils ne représentent pas une quantité de schèmes.

| Modèle | Variation due à l'animal | Variation due au lieu | Variation due à la couleur |
|---|---:|---:|---:|
| Unigramme | 0 | 0 | 0 |
| Bigramme | 0 | 0 | 0,037 |
| Trigramme | 0 | 0,835 | 0,033 |
| 4-gramme | 0,431 | 0,836 | 0,013 |
| Petit réseau | 0,453 | 0,823 | 0,007 |

Ces résultats montrent que les contenus accessibles dépendent des contextes consultés. Un bigramme ne dispose pas du mécanisme pour exploiter directement l'animal présent trois tokens plus tôt. Un 4-gramme peut distinguer des contextes complets, mais n'utilise pas nécessairement une abstraction partagée. Un réseau peut apprendre des représentations communes à plusieurs situations.

## 6. Évolution de l'association trompeuse avec la couleur

| Séquences | Bigramme | Trigramme | 4-gramme | Réseau neuronal |
|---:|---:|---:|---:|---:|
| 400 | 0,430629 | 0,447775 | 0,578056 | 0,182974 |
| 560 | 0,310709 | 0,318928 | 0,071158 | 0,084497 |
| 800 | 0,215596 | 0,219177 | 0,024795 | 0,013652 |
| 1 200 | 0,132695 | 0,133324 | 0,014136 | 0,028672 |
| 2 400 | 0,052314 | 0,048731 | 0,015190 | 0,009004 |
| 3 200 | 0,036890 | 0,033491 | 0,013396 | 0,007076 |

Mesure : variation de la distribution des actions lorsqu'on change la couleur sans changer l'animal et le lieu.

La relation couleur–action, initialement utile aux modèles à contexte court parce que la couleur informe sur l'animal, devient moins pertinente. Dans les modèles à contexte long, les valeurs du début reflètent aussi la non-observation de certaines combinaisons : les étiqueter toutes comme « faux schèmes » serait excessif.

D'autres contenus subsistent à tous ces instants : relations entre lieux et actions, différences entre animaux, probabilités générales et structures de séquence.

## 7. Étudier plusieurs niveaux internes du réseau neuronal

L'observation est faite aux niveaux : **embeddings**, **couche cachée** et **distribution de sortie**.

- Les embeddings codent les tokens dans un espace appris ; une coordonnée n'est pas nécessairement un schème.
- La couche cachée combine les représentations de trois tokens ; certaines différences de contextes y sont exprimées.
- La sortie fournit des probabilités de continuations ; ce ne sont pas les schèmes eux-mêmes.

Une comparaison contrôle l'animal et le lieu, puis modifie seulement la couleur :

| Séquences | Distance moyenne des activations cachées | Influence sur la distribution des actions |
|---:|---:|---:|
| 40 | 1,356 | 0,060 |
| 400 | 1,665 | 0,183 |
| 800 | 0,758 | 0,014 |
| 3 200 | 0,646 | 0,007 |

La couleur continue à provoquer des différences dans les transformations internes même lorsque son influence sur les actions diminue fortement. Ces deux mesures sont de nature différente et ne peuvent pas être comparées directement comme si elles partageaient une échelle de concepts.

### Évolution non monotone

La probabilité moyenne de l'action dominante dans les contextes de contrôle varie pendant l'apprentissage : elle était d'environ 94,9 % à 800 observations, 84,6 % à 1 200, et 87,1 % à 3 200. Une propriété peut donc fluctuer sans que le modèle ait globalement « oublié » sa structure.

## 8. Productions de séquences : seulement un contrôle de l'exploitation

Exemples de générations enregistrées dans l'étude :

- À 400 séquences : `chat — maison — bleu — dort` ; `chien — jardin — rouge — court`.
- À 3 200 séquences : `chien — maison — rouge — dort` ; `chat — maison — bleu — dort` ; `chat — jardin — rouge — grimpe`.

Cette dernière combinaison était absente pendant la phase initiale. Le modèle peut ensuite la produire grâce aux distributions ou représentations apprises. Cela démontre une **capacité de combinaison**, pas l'apparition automatique d'un nouveau schème pendant l'acte de génération.

Les sorties servent ici au contrôle ; notre étude porte sur le mécanisme d'apprentissage et ses états internes.

## 9. Fichiers et reproductibilité

Conserver sans modification :

- `experiment_generation_schemes.py` : générateur, modèles à n-grammes, réseau et sondes ;
- `experiment_generation_schemes_dataset.npz` : 3 200 séquences et 600 séquences de vérification ;
- `experiment_generation_schemes_results.json` : distributions, paramètres, états de sondes, sorties à 11 instants ;
- `experiment_generation_schemes_summary.csv` : 55 lignes, cinq modèles × onze instants ;
- `experiment_generation_schemes_manifest.json` : versions et empreintes ;
- `experiment_generation_schemes_README.md` : notice de l'exécution ;
- `experiment_generation_schemes_states/neural_after_*.pt` : **onze checkpoints complets** des paramètres neuronaux ;
- `experiment_generation_schemes_package.zip` : archive ZIP originale ;
- `generation_run_stdout.txt` : trace d'exécution supplémentaire lorsqu'elle existe.

La reproduction utilise Python, NumPy et PyTorch (voir script et README pour les détails). Les données, états et checkpoints sont conservés tels quels ; nos sondes ne forment pas une preuve exhaustive des contenus acquis.

## 10. Enseignements et limites

Le même jeu peut conduire à des contenus locaux, contextuels ou distribués, selon le mécanisme d'acquisition. Plusieurs relations se forment simultanément, certaines persistent, d'autres se rééquilibrent. Un même modèle peut conserver une réponse interne à une caractéristique sans l'utiliser sensiblement dans ses continuations. Les sorties générées et l'état représenté ne sont pas identiques. Aucun de ces mécanismes n'appartient à TL dans cette expérience.

`CHRONOLOGIE_COMPLETE.md` et les fichiers JSON/NPZ/PT donnent l'intégralité des mesures et états originaux pour une exploitation future.


---

# Chronologie complète des indicateurs — 04_generation

**Tableau directement extrait du CSV expérimental original, sans recalcul ni interpolation.**

- Fichier original : `originaux/experiment_generation_schemes_summary.csv`.
- Lignes expérimentales : **55**.
- Colonnes conservées : **10**.
- Les chiffres sont des mesures ou paramètres du protocole, **pas des dénombrements de schèmes**.
- La totalité des états multidimensionnels, au-delà des indicateurs de ce tableau, est conservée dans le JSON/NPZ originaux.

| observations | model | animal_TV_mean | place_TV_mean | badge_TV_mean | mean_p_main_given_action_token | action_token_mass_mean | hidden_badge_l2_mean | hidden_animal_l2_mean | hidden_place_l2_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | unigram | 0.0 | 0.0 | 0.0 | 0.333333 | 0.272727 | — | — | — |
| 0 | bigram | 0.0 | 0.0 | 0.0 | 0.333333 | 0.272727 | — | — | — |
| 0 | trigram | 0.0 | 0.0 | 0.0 | 0.333333 | 0.272727 | — | — | — |
| 0 | 4gram | 0.0 | 0.0 | 0.0 | 0.333333 | 0.272727 | — | — | — |
| 0 | neural | 0.107806 | 0.04838 | 0.083584 | 0.317178 | 0.314402 | 1.311657 | 1.457512 | 1.423977 |
| 40 | unigram | 0.0 | 0.0 | 0.0 | 0.373494 | 0.201946 | — | — | — |
| 40 | bigram | 0.0 | 0.0 | 0.418605 | 0.372093 | 0.843137 | — | — | — |
| 40 | trigram | 0.0 | 0.788003 | 0.49086 | 0.649056 | 0.739211 | — | — | — |
| 40 | 4gram | 0.520986 | 0.394002 | 0.520986 | 0.593826 | 0.505969 | — | — | — |
| 40 | neural | 0.18906 | 0.060191 | 0.059878 | 0.391419 | 0.404458 | 1.356176 | 1.658792 | 1.387959 |
| 120 | unigram | 0.0 | 0.0 | 0.0 | 0.372428 | 0.200661 | — | — | — |
| 120 | bigram | 0.0 | 0.0 | 0.436181 | 0.372279 | 0.938874 | — | — | — |
| 120 | trigram | 0.0 | 0.851981 | 0.451816 | 0.677411 | 0.885826 | — | — | — |
| 120 | 4gram | 0.555714 | 0.425991 | 0.555714 | 0.611191 | 0.579276 | — | — | — |
| 120 | neural | 0.210092 | 0.16667 | 0.074309 | 0.480542 | 0.687502 | 1.326203 | 1.837047 | 1.379514 |
| 280 | unigram | 0.0 | 0.0 | 0.0 | 0.375666 | 0.200285 | — | — | — |
| 280 | bigram | 0.0 | 0.0 | 0.425719 | 0.375618 | 0.972445 | — | — | — |
| 280 | trigram | 0.0 | 0.88455 | 0.445144 | 0.700678 | 0.946677 | — | — | — |
| 280 | 4gram | 0.582096 | 0.442275 | 0.582096 | 0.624381 | 0.609702 | — | — | — |
| 280 | neural | 0.278883 | 0.397695 | 0.165486 | 0.650669 | 0.947215 | 1.170249 | 2.1644 | 1.872913 |
| 400 | unigram | 0.0 | 0.0 | 0.0 | 0.371108 | 0.200199 | — | — | — |
| 400 | bigram | 0.0 | 0.0 | 0.430629 | 0.371001 | 0.980519 | — | — | — |
| 400 | trigram | 0.0 | 0.875918 | 0.447775 | 0.693197 | 0.962007 | — | — | — |
| 400 | 4gram | 0.578056 | 0.437959 | 0.578056 | 0.622361 | 0.617367 | — | — | — |
| 400 | neural | 0.398143 | 0.741 | 0.182974 | 0.809146 | 0.970319 | 1.665348 | 2.334435 | 2.879117 |
| 560 | unigram | 0.0 | 0.0 | 0.0 | 0.370882 | 0.200143 | — | — | — |
| 560 | bigram | 0.0 | 0.0 | 0.310709 | 0.370794 | 0.985989 | — | — | — |
| 560 | trigram | 0.0 | 0.860127 | 0.318928 | 0.690125 | 0.972471 | — | — | — |
| 560 | 4gram | 0.438674 | 0.848243 | 0.071158 | 0.887871 | 0.909751 | — | — | — |
| 560 | neural | 0.444602 | 0.86401 | 0.084497 | 0.888467 | 0.982368 | 1.493492 | 2.412822 | 3.623253 |
| 800 | unigram | 0.0 | 0.0 | 0.0 | 0.371491 | 0.2001 | — | — | — |
| 800 | bigram | 0.0 | 0.0 | 0.215596 | 0.371575 | 0.990127 | — | — | — |
| 800 | trigram | 0.0 | 0.859767 | 0.219177 | 0.690777 | 0.980475 | — | — | — |
| 800 | 4gram | 0.443723 | 0.859823 | 0.024795 | 0.903685 | 0.953837 | — | — | — |
| 800 | neural | 0.454101 | 0.935827 | 0.013652 | 0.948735 | 0.991013 | 0.75763 | 2.235023 | 4.293669 |
| 1200 | unigram | 0.0 | 0.0 | 0.0 | 0.370787 | 0.200067 | — | — | — |
| 1200 | bigram | 0.0 | 0.0 | 0.132695 | 0.370764 | 0.993393 | — | — | — |
| 1200 | trigram | 0.0 | 0.839458 | 0.133324 | 0.68443 | 0.986897 | — | — | — |
| 1200 | 4gram | 0.429663 | 0.845625 | 0.014136 | 0.890674 | 0.972233 | — | — | — |
| 1200 | neural | 0.370106 | 0.80501 | 0.028672 | 0.845977 | 0.989954 | 0.822343 | 2.127185 | 4.106955 |
| 1800 | unigram | 0.0 | 0.0 | 0.0 | 0.370386 | 0.200044 | — | — | — |
| 1800 | bigram | 0.0 | 0.0 | 0.080604 | 0.3704 | 0.995581 | — | — | — |
| 1800 | trigram | 0.0 | 0.834669 | 0.07754 | 0.68168 | 0.991207 | — | — | — |
| 1800 | 4gram | 0.423793 | 0.832649 | 0.013104 | 0.88716 | 0.982166 | — | — | — |
| 1800 | neural | 0.444257 | 0.863459 | 0.009256 | 0.912595 | 0.99443 | 0.856927 | 2.390072 | 4.308172 |
| 2400 | unigram | 0.0 | 0.0 | 0.0 | 0.369561 | 0.200033 | — | — | — |
| 2400 | bigram | 0.0 | 0.0 | 0.052314 | 0.369593 | 0.99668 | — | — | — |
| 2400 | trigram | 0.0 | 0.832238 | 0.048731 | 0.680992 | 0.993387 | — | — | — |
| 2400 | 4gram | 0.419505 | 0.830308 | 0.01519 | 0.885443 | 0.986767 | — | — | — |
| 2400 | neural | 0.410882 | 0.825037 | 0.009004 | 0.881865 | 0.996116 | 0.699715 | 2.211857 | 4.173462 |
| 3200 | unigram | 0.0 | 0.0 | 0.0 | 0.370295 | 0.200025 | — | — | — |
| 3200 | bigram | 0.0 | 0.0 | 0.03689 | 0.370335 | 0.997507 | — | — | — |
| 3200 | trigram | 0.0 | 0.834964 | 0.033491 | 0.681722 | 0.995026 | — | — | — |
| 3200 | 4gram | 0.430632 | 0.835971 | 0.013396 | 0.88967 | 0.990086 | — | — | — |
| 3200 | neural | 0.452647 | 0.822731 | 0.007076 | 0.87075 | 0.996326 | 0.646181 | 2.142515 | 4.298746 |


<!-- FIN 04_generation -->



---

<!-- DÉBUT 05_representation -->

# 5/6 — Apprentissage de représentations : évolution des espaces et contenus internes, sans TL

**Statut : expérience exécutée, données et originaux conservés.**  
**Problème :** apprendre des représentations de petites images, sans étiquettes de catégorie fournies aux algorithmes.  
**Données :** exactement les 3 200 images 7×7 de l'expérience 2/6, mais sans exploiter leurs étiquettes ; 5 méthodes ; 10 checkpoints.  
**Périmètre :** processus d'acquisition des transformations internes et des contenus représentationnels, sans TL.

## 1. Une distinction décisive : représentation et schème

La famille opérationnelle « Représentation » rassemble les modèles dont la finalité est d'apprendre une transformation ou un espace dans lequel l'information devient exploitable. Le **schème**, dans notre vocabulaire de travail, est un **contenu représentationnel interne acquis ou modifié**, quelle que soit la famille : régression, classification, clustering, génération, représentation ou décision.

Un embedding calculé pour une image n'est pas nécessairement un nouveau schème ; un vecteur latent n'est pas un inventaire de schèmes ; une composante de PCA n'est pas automatiquement un schème isolé. Les contenus peuvent être répartis entre coordonnées, composantes, paramètres et transformations.

La question examinée est donc : **quels types de relations le modèle acquiert-il et comment leur expression interne se transforme-t-elle au fil des observations, à différents niveaux ?**

## 2. Les mêmes images que dans la classification, mais sans cible de classe

Le jeu de 3 200 images binaires 7×7 contient :

- un trait horizontal ou vertical ;
- des variations de position ;
- du bruit de fond ;
- un marqueur de coin temporairement associé à l'orientation pendant les 400 premières observations, puis indépendant.

Les algorithmes de cette expérience ne reçoivent pas les classes « horizontal » et « vertical » comme cibles. Les catégories sont seulement utiles pour **les analyses a posteriori**, et non pour guider l'entraînement.

**Checkpoints :** 0, 40, 120, 300, 400, 550, 800, 1 200, 2 000, 3 200. **Graine :** 20261115.

Les sondes sont des images de contrôle fixes modifiant séparément l'orientation, la position et le marqueur. Pour chaque méthode, on peut observer les différences entre représentations obtenues pour ces images ; cela n'est pas un nombre de schèmes.

## 3. Les cinq algorithmes et ce qu'ils déterminent

### 3.1. PCA : 49 → 4 composantes

PCA apprend des directions de plus grande variance, par décomposition matricielle. Il conserve les composantes, les moyennes et informations de projection. À chaque checkpoint, PCA est recalculé sur toutes les images accumulées : ce n'est pas une unique instance modifiée automatiquement avec chaque nouvel exemple.

**Contenus étudiés :** directions de variation, relations entre pixels, expression de l'orientation, position et marqueur dans la projection. Une composante peut mélanger plusieurs régularités.

### 3.2. IncrementalPCA : 49 → 4 composantes

Même finalité de projection par composantes, mais actualisée progressivement sur des lots de 40 observations. Les directions apprises peuvent suivre une trajectoire différente de PCA complet et converger vers une organisation proche.

### 3.3. NMF : 49 → 4 composantes non négatives

La factorisation non négative apprend une représentation additive des images. Des combinaisons de composantes peuvent reconstruire des portions de traits et différentes structures spatiales. Elle ne garantit pas qu'une composante corresponde exclusivement à un type de trait, à une catégorie ou à un schème identifié.

NMF est réajusté sur le préfixe complet de données à chaque checkpoint.

### 3.4. Autoencodeur : 49 → 16 → 4 → 16 → 49

L'encodeur transforme l'image en un code latent de dimension 4. Le décodeur tente de reconstruire les 49 pixels. L'erreur de reconstruction guide l'optimisation des paramètres.

**À observer :** premières activations cachées, code latent, couches de décodage, qualité de reconstruction et réponses aux différences d'orientation, de marqueur et de position. Les contenus représentés à une couche peuvent être atténués ou réorganisés dans la suivante.

### 3.5. Encodeur contrastif : 49 → 16 → 4

Un modèle contrastif apprend des représentations rapprochant différentes vues du même exemple et éloignant certaines représentations d'exemples distincts. Dans notre expérience, les transformations utilisées modifient légèrement le bruit et **rendent la présence du marqueur aléatoire**.

Cette intervention expérimentale guide l'invariance recherchée : si le marqueur devient non pertinent pour rapprocher deux vues, le code final peut apprendre à lui être peu sensible. Cela ne prouve pas que le modèle a spontanément découvert une vérité générale sur le marqueur.

## 4. Suivre ce qui est représenté à chaque instant

Avant apprentissage, PCA, IncrementalPCA et NMF ne disposent pas de composantes déterminées. Les réseaux calculent des activations initiales, mais celles-ci ne constituent pas des schèmes acquis par ce jeu.

Pour les neuf checkpoints après initialisation, nous enregistrons les contrastes de représentation pour trois modifications contrôlées : **orientation, marqueur, position**. Les distances sont propres aux espaces de chaque modèle : elles ne sont pas directement comparables entre algorithmes comme une mesure commune de richesse conceptuelle.

### Premiers et derniers checkpoints

| Méthode | Observations | Contraste orientation | Contraste marqueur | Contraste position |
|---|---:|---:|---:|---:|
| PCA | 40 | 1,814 | 0,590 | 1,505 |
| PCA | 3 200 | 2,439 | 0,032 | 1,529 |
| IncrementalPCA | 40 | 1,814 | 0,590 | 1,505 |
| IncrementalPCA | 3 200 | 2,431 | 0,060 | 1,528 |
| NMF | 40 | 0,568 | 0,133 | 0,380 |
| NMF | 3 200 | 0,069 | 0,040 | 0,197 |
| Autoencodeur | 40 | 0,096 | 0,025 | 0,209 |
| Autoencodeur | 3 200 | 0,109 | 0,128 | 0,992 |
| Contrastif | 40 | 1,178 | 0,349 | 0,764 |
| Contrastif | 3 200 | 1,452 | 0,011 | 1,247 |

La différence de comportement est importante : PCA finit avec une forte sensibilité à l'orientation et à la position, faible au marqueur ; l'autoencodeur finit très sensible à la position et encore sensible au marqueur ; le contrastif apprend à réduire fortement l'influence du marqueur. NMF exprime autrement les relations, avec des échelles et contenus de représentation différents.

**Les mêmes données ne conduisent pas à une représentation unique**, parce que les objectifs de projection, reconstruction ou contraste sont distincts.

## 5. PCA et IncrementalPCA : évolution des directions

Pour PCA, les distances mesurées sur nos sondes restent approximativement :

| Observations | Orientation | Marqueur | Position |
|---:|---:|---:|---:|
| 40 | 1,814 | 0,590 | 1,505 |
| 400 | 2,499 | 0,244 | 1,485 |
| 800 | 2,432 | 0,124 | 1,513 |
| 1 200 | 2,427 | 0,086 | 1,520 |
| 2 000 | 2,452 | 0,038 | 1,526 |
| 3 200 | 2,439 | 0,032 | 1,529 |

Les distinctions d'orientation et de position restent exprimées, tandis que celle du marqueur diminue fortement. Cela n'implique ni que PCA a identifié une notion « orientation » au sens humain, ni qu'une composante unique constitue un schème stable.

IncrementalPCA intègre les observations par lots. Les résultats finaux sont proches de PCA complet, mais les opérations informatiques de mise à jour sont différentes. On conserve donc à la fois l'organisation acquise et sa trajectoire d'observation.

## 6. NMF : des parties additives et des combinaisons

Les composantes non négatives peuvent exprimer des motifs spatiaux et des parties d'images combinables. Le modèle apprend des représentations adaptées à la reconstruction additive, pas à la discrimination supervisée des deux orientations.

Le contraste d'orientation mesuré sur les quatre coordonnées de NMF passe de 0,568 à t=40 à 0,069 à t=3200, alors que l'erreur moyenne de reconstruction de vérification diminue de 0,0736 à 0,0669.

Cela montre que le modèle peut **mieux représenter globalement les images selon son critère**, tout en distinguant moins fortement une caractéristique qui nous intéresse dans un autre usage. Ce n'est pas la preuve que l'orientation a disparu de toute l'information représentée.

## 7. Autoencodeur : différences selon les niveaux internes

L'autoencodeur possède plusieurs transformations internes. Nous avons comparé les distinctions exprimées dans la première couche cachée et dans le code latent.

| Niveau | Observations | Orientation | Marqueur | Position |
|---|---:|---:|---:|---:|
| Première couche cachée | 400 | 0,710 | 0,324 | 0,827 |
| Code latent | 400 | 0,182 | 0,096 | 0,226 |
| Première couche cachée | 3 200 | 0,644 | 0,339 | 1,570 |
| Code latent | 3 200 | 0,109 | 0,128 | 0,992 |

La position devient particulièrement représentée dans le code latent. La première couche continue à réagir aussi à l'orientation et au marqueur. Le contenu ne peut donc être déduit uniquement de la sortie du code latent, et encore moins de la qualité finale de reconstruction.

**Erreur de reconstruction mesurée :**

| Observations | Erreur MSE de reconstruction |
|---:|---:|
| 40 | 0,2401 |
| 120 | 0,2220 |
| 300 | 0,1929 |
| 400 | 0,1736 |
| 550 | 0,1480 |
| 800 | 0,1243 |
| 1 200 | 0,1089 |
| 2 000 | 0,1022 |
| 3 200 | 0,0961 |

La diminution de l'erreur constitue une indication de l'amélioration de reconstruction, non une identification des schèmes responsables ni une preuve de pertinence pour une autre tâche.

## 8. Contrastif : acquisition d'invariances orientées par l'objectif

Les transformations de données encouragent le modèle à ne pas faire dépendre son code final du repère. Nous comparons la sensibilité du code à l'orientation et au marqueur :

| Observations | Contraste d'orientation | Contraste du marqueur |
|---:|---:|---:|
| 40 | 1,178 | 0,349 |
| 400 | 1,476 | 0,058 |
| 800 | 1,350 | 0,045 |
| 1 200 | 1,323 | 0,027 |
| 2 000 | 1,472 | 0,019 |
| 3 200 | 1,452 | 0,011 |

Au dernier checkpoint, la **première couche cachée** conserve un contraste au marqueur d'environ 0,295 tandis que le **code final** présente environ 0,011. L'expression d'une caractéristique peut ainsi persister à un niveau et être fortement atténuée au niveau suivant.

Cette invariance n'est pas une vérité automatiquement découverte par l'IA : elle est favorisée par notre choix de transformations. Selon la tâche, rendre un modèle invariant à une caractéristique peut être souhaitable ou dangereux.

## 9. Identité des schèmes et changement de coordonnées

Deux représentations peuvent encoder des distinctions semblables dans des bases ou orientations différentes. Des dimensions latentes peuvent permuter, changer de signe ou se réorganiser sans que le contenu exploitable soit modifié de manière équivalente.

Il faut donc éviter de suivre « le schème numéro 1 » en regardant simplement la première coordonnée d'un vecteur. Le protocole conserve les composantes et paramètres, mais examine également les relations entre images de contrôle.

La sensibilité à une propriété ne démontre pas que cette propriété est utilisée causalement pour une autre tâche. La reconstruction et le contraste sont les objectifs de ces modèles ; nous n'avons pas transformé artificiellement cette famille en classification.

## 10. Répertoire de fichiers originaux

- `experiment_representation_schemes.py` : protocole complet, cinq méthodes et sondes ;
- `experiment_representation_schemes_dataset.npz` : images utilisées (partagées logiquement avec la classification) ;
- `experiment_representation_schemes_results.json` : composantes, codes, états et activations aux dix instants ;
- `experiment_representation_schemes_summary.csv` : les 45 états entraînés, 5 méthodes × 9 checkpoints après initialisation ;
- `experiment_representation_schemes_trajectories.png` : graphique original ;
- `experiment_representation_schemes_manifest.json` : versions, paramètres, empreintes ;
- `experiment_representation_schemes_README.md` : notice technique d'origine ;
- `experiment_representation_schemes_package.zip` : archive originale complète.

La conservation comprend également `CHRONOLOGIE_COMPLETE.md`, construit à partir du CSV existant, sans remplacer les résultats originaux.

**Reproduction :** utiliser le script Python et les dépendances indiquées dans la notice originale. Les méthodes ne suivent pas un budget de calcul strictement identique ; PCA/NMF sont recalculés sur préfixes, IncrementalPCA est incrémental, et les réseaux sont entraînés numériquement.

## 11. Ce qui est établi, sans TL

Plusieurs formes de représentation peuvent se développer à partir des mêmes observations. Une représentation adaptée à la variance, à la reconstruction ou au contraste n'est pas nécessairement adaptée à un autre objectif. Des contenus peuvent coexister, être réorganisés ou devenir moins importants à certains niveaux, sans disparaître des autres. Aucune couche, dimension, activation ou composante ne définit automatiquement un schème. La notion transversale de schème ne doit pas être confondue avec la famille opérationnelle Représentation.

Il s'agit d'une seule expérience synthétique à graine fixe. Aucun opérateur TL n'y est introduit.


---

# Chronologie complète des indicateurs — 05_representation

**Tableau directement extrait du CSV expérimental original, sans recalcul ni interpolation.**

- Fichier original : `originaux/experiment_representation_schemes_summary.csv`.
- Lignes expérimentales : **45**.
- Colonnes conservées : **9**.
- Les chiffres sont des mesures ou paramètres du protocole, **pas des dénombrements de schèmes**.
- La totalité des états multidimensionnels, au-delà des indicateurs de ce tableau, est conservée dans le JSON/NPZ originaux.

| checkpoint | model | orientation_contrast | marker_contrast | position_contrast | orientation_fraction | validation_reconstruction_mse | stage_steps | probe_geometry_stability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | PCA | 1.814481 | 0.589794 | 1.504952 | 0.75469 | 0.064016 | 40 | — |
| 40 | IncrementalPCA | 1.814481 | 0.589794 | 1.504952 | 0.75469 | 0.064016 | 1 | — |
| 40 | NMF | 0.567809 | 0.132684 | 0.380001 | 0.810584 | 0.073578 | 40 | — |
| 40 | Autoencoder | 0.096025 | 0.025433 | 0.20922 | 0.790602 | 0.240091 | 2 | — |
| 40 | Contrastive | 1.177554 | 0.348715 | 0.764361 | 0.771525 | — | 2 | — |
| 120 | PCA | 2.487718 | 0.133098 | 1.489427 | 0.949215 | 0.055016 | 120 | 0.846659 |
| 120 | IncrementalPCA | 2.373392 | 0.139151 | 1.491937 | 0.944617 | 0.05468 | 3 | 0.957831 |
| 120 | NMF | 0.857378 | 0.119393 | 0.34547 | 0.877767 | 0.069875 | 120 | 0.760263 |
| 120 | Autoencoder | 0.138935 | 0.046107 | 0.215112 | 0.750829 | 0.222041 | 6 | 0.805692 |
| 120 | Contrastive | 1.678091 | 0.253478 | 1.212958 | 0.868771 | — | 6 | 0.918993 |
| 300 | PCA | 2.530581 | 0.309549 | 1.457355 | 0.891009 | 0.054106 | 300 | 0.872946 |
| 300 | IncrementalPCA | 2.441434 | 0.18561 | 1.531767 | 0.929346 | 0.05344 | 8 | 0.936473 |
| 300 | NMF | 0.700431 | 0.051147 | 0.253316 | 0.931947 | 0.06771 | 300 | 0.47619 |
| 300 | Autoencoder | 0.175219 | 0.078527 | 0.227771 | 0.69053 | 0.192908 | 12 | 0.877395 |
| 300 | Contrastive | 1.426431 | 0.10064 | 1.115627 | 0.934096 | — | 12 | 0.971538 |
| 400 | PCA | 2.499126 | 0.244188 | 1.485255 | 0.910988 | 0.053398 | 400 | 0.972485 |
| 400 | IncrementalPCA | 2.433819 | 0.188502 | 1.517569 | 0.928116 | 0.053169 | 11 | 0.989595 |
| 400 | NMF | 0.717665 | 0.102889 | 0.124176 | 0.87461 | 0.067449 | 400 | 0.677066 |
| 400 | Autoencoder | 0.181767 | 0.096311 | 0.225523 | 0.653655 | 0.173588 | 16 | 0.982485 |
| 400 | Contrastive | 1.476172 | 0.057539 | 1.11453 | 0.962484 | — | 16 | 0.989053 |
| 550 | PCA | 2.432349 | 0.181248 | 1.522983 | 0.930652 | 0.052849 | 550 | 0.956058 |
| 550 | IncrementalPCA | 2.402884 | 0.174476 | 1.531399 | 0.932304 | 0.052892 | 15 | 0.983023 |
| 550 | NMF | 0.666958 | 0.088064 | 0.224636 | 0.883362 | 0.067377 | 550 | 0.874111 |
| 550 | Autoencoder | 0.158524 | 0.111961 | 0.206274 | 0.586074 | 0.147973 | 22 | 0.976464 |
| 550 | Contrastive | 1.495724 | 0.046139 | 1.152954 | 0.970076 | — | 22 | 0.967707 |
| 800 | PCA | 2.431842 | 0.123524 | 1.513463 | 0.951661 | 0.052522 | 800 | 0.974808 |
| 800 | IncrementalPCA | 2.414535 | 0.142345 | 1.517182 | 0.944329 | 0.052632 | 22 | 0.997809 |
| 800 | NMF | 0.456672 | 0.050686 | 0.2978 | 0.900098 | 0.067065 | 800 | 0.619595 |
| 800 | Autoencoder | 0.101483 | 0.106189 | 0.186437 | 0.488668 | 0.124281 | 30 | 0.945265 |
| 800 | Contrastive | 1.350133 | 0.045104 | 1.079791 | 0.967673 | — | 30 | 0.952381 |
| 1200 | PCA | 2.426981 | 0.08606 | 1.523875 | 0.965755 | 0.052345 | 1200 | 0.967141 |
| 1200 | IncrementalPCA | 2.414472 | 0.116244 | 1.519499 | 0.954067 | 0.052444 | 32 | 0.978094 |
| 1200 | NMF | 0.369129 | 0.057485 | 0.247593 | 0.865253 | 0.066391 | 1200 | 0.973727 |
| 1200 | Autoencoder | 0.05221 | 0.081038 | 0.210265 | 0.391827 | 0.108933 | 44 | 0.847838 |
| 1200 | Contrastive | 1.32331 | 0.026826 | 1.106621 | 0.980131 | — | 44 | 0.897646 |
| 2000 | PCA | 2.451768 | 0.038209 | 1.529093 | 0.984655 | 0.052257 | 2000 | 0.979737 |
| 2000 | IncrementalPCA | 2.437866 | 0.075793 | 1.525825 | 0.969848 | 0.052313 | 52 | 0.991785 |
| 2000 | NMF | 0.408336 | 0.052745 | 0.170676 | 0.885606 | 0.067166 | 2000 | 0.524904 |
| 2000 | Autoencoder | 0.119568 | 0.090287 | 0.621557 | 0.569764 | 0.102235 | 70 | 0.764094 |
| 2000 | Contrastive | 1.472298 | 0.018587 | 1.11288 | 0.987533 | — | 70 | 0.910783 |
| 3200 | PCA | 2.438507 | 0.031563 | 1.528766 | 0.987222 | 0.05229 | 3200 | 0.94414 |
| 3200 | IncrementalPCA | 2.430839 | 0.059534 | 1.527668 | 0.976094 | 0.052312 | 82 | 0.974261 |
| 3200 | NMF | 0.069065 | 0.040494 | 0.196538 | 0.630389 | 0.066918 | 3200 | 0.440066 |
| 3200 | Autoencoder | 0.109253 | 0.128015 | 0.992118 | 0.460463 | 0.096097 | 108 | 0.798577 |
| 3200 | Contrastive | 1.451677 | 0.011029 | 1.247005 | 0.99246 | — | 108 | 0.932129 |


<!-- FIN 05_representation -->



---

<!-- DÉBUT 06_politique_decision -->

# 6/6 — Politique de décision : acquisition de relations entre situations, actions et conséquences, sans TL

**Statut : expérience exécutée, plusieurs ressources de l'expérience conservées.**  
**Problème :** apprendre à choisir des actions dans un minuscule environnement fictif d'irrigation et de récolte.  
**Données :** 3 200 transitions d'expérience communes ; 4 algorithmes ; 10 checkpoints.  
**Périmètre :** uniquement l'évolution de l'apprentissage interne, sans TL et sans valider une application agronomique.

## 1. Le sens de cette sixième famille

Une politique de décision cherche à choisir des actions à partir de situations et de conséquences. Les contenus appris peuvent exprimer non seulement une correspondance entrée–sortie, mais des relations temporelles : une action coûteuse maintenant peut préparer un résultat positif plus tard.

Le terme de travail *schème* désigne ici **le contenu représentationnel interne acquis ou modifié** relativement aux situations, actions, transitions et conséquences. Une cellule Q, une récompense, un neurone ou un état brut n'est pas automatiquement un schème.

Les quatre modèles reçoivent **exactement le même journal d'interactions**, recueilli par une politique exploratoire fixe. Nous comparons donc les apprentissages sur une expérience commune, mais non leurs capacités à explorer individuellement l'environnement ni leurs budgets de calcul.

## 2. Environnement élémentaire et conditions

Trois bits d'observation :

- `dry` : 0 = sol humide, 1 = sol sec ;
- `mature` : 0 = culture en croissance, 1 = culture mûre ;
- `marker` : indice indirect, 0 ou 1, sans influence sur la dynamique physique ni les récompenses.

Il existe donc **8 états observables**. Trois actions : **attendre** (0), **irriguer** (1), **récolter** (2), soit 24 couples état-action possibles.

### Conséquences de l'environnement synthétique

| Situation/action | Transition et récompense |
|---|---|
| Sol sec, en croissance ; attendre | Reste sec/en croissance ; −0,25 |
| Sol sec, en croissance ; irriguer | Devient humide, même maturité ; −0,20 |
| Sol humide, en croissance ; attendre | Devient mûr et sec ; +0,15 |
| Mûre, sol sec ; récolter | Fin de l'épisode ; +1,50 |
| Mûre, sol humide ; récolter | Fin de l'épisode ; +5,00 |
| Récolter avant maturité | Fin de l'épisode ; −2,00 |
| Mûre ; attendre | Reste mûre, devient sèche ; −0,50 |
| Toute irrigation | Coût −0,20, rend le sol humide sans changer la maturité |

Le facteur d'actualisation `gamma` vaut **0,92**. Ce sont des règles inventées pour l'expérience, **pas une modélisation agronomique scientifique**.

Pendant les 400 premières transitions, `marker == dry` dans les observations, ce qui confond les deux caractéristiques. Après la 400e, le marqueur devient indépendant. Il n'affecte jamais la croissance, les récompenses ou les transitions physiques.

L'ordre des **3 200 transitions** est fixé ; la politique de collecte choisit uniformément les actions, indépendamment des quatre apprenants. **Checkpoints :** 0, 40, 120, 300, 400, 550, 800, 1 200, 2 000, 3 200.

## 3. Les quatre algorithmes réellement employés

### 3.1. Q-Learning tabulaire

Apprend une valeur pour chaque couple état-action par mises à jour temporelles exploitant la récompense immédiate et le maximum des valeurs futures estimées. Taux d'apprentissage **0,18**. L'état interne est une table **8×3** et un historique de ses transformations.

Il peut apprendre l'intérêt différé d'irriguer sans attribuer une valeur positive à l'action dès la première interaction. Les valeurs ne sont pas de simples récompenses immédiates.

### 3.2. Expected SARSA tabulaire

Apprend également des valeurs état-action, mais utilise l'espérance du retour suivant sous une politique cible **ε-greedy**, ε=0,15. Taux d'apprentissage **0,18**.

**Précaution :** les transitions sont collectées par une politique exploratoire uniforme, différente de la politique cible. C'est une utilisation *off-policy* de mises à jour Expected SARSA, **pas** une expérience SARSA ordinaire strictement on-policy.

### 3.3. Dyna-Q

Conserve une table de valeurs et construit un **modèle empirique des transitions observées**, avec leurs fréquences et récompenses. Après chaque transition réelle, il effectue **cinq mises à jour simulées** de planification à partir de ce modèle.

Il représente ainsi deux types distincts de contenus internes : relations de transition entre états et conséquences, et estimations de retours futurs pour les actions. Son budget d'apprentissage inclut des mises à jour supplémentaires : on ne doit pas le comparer aux autres en « temps de calcul identique ».

### 3.4. Petit DQN neuronal

Architecture : **3 entrées → 12 unités cachées `tanh` → 8 unités cachées `tanh` → 3 valeurs Q**. Entraînement par rejeu d'expériences, perte Huber (`smooth-L1`) et réseau cible.

Les activations des deux couches cachées et les 8×3 valeurs prédites sont conservées aux dix checkpoints, ainsi que les paramètres neuronaux complets. Les représentations intermédiaires peuvent exprimer des distinctions dont l'effet sur les valeurs Q est faible.

## 4. Trajectoire d'un état : sec, en croissance, marqueur présent

Nous examinons simultanément les valeurs de trois actions apprises par Q-Learning, et pas seulement l'action qui devient finalement préférée.

| Transitions cumulées | Attendre | Irriguer | Récolter |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 40 | −0,04 | −0,01 | −1,26 |
| 120 | 0,04 | 0,65 | −1,39 |
| 300 | 0,76 | 1,59 | −1,94 |
| 400 | 1,59 | 2,31 | −1,99 |
| 550 | 1,19 | 1,89 | −2,00 |
| 800 | 1,56 | 2,30 | −2,00 |
| 1 200 | 2,38 | 3,30 | −2,00 |
| 2 000 | 3,09 | 3,65 | −2,00 |
| 3 200 | 3,12 | 3,66 | −2,00 |

Ces valeurs représentent le **retour futur actualisé estimé**. L'irrigation coûte −0,20 immédiatement mais peut devenir positive si elle prépare la maturité et une bonne récolte.

À 40 transitions, l'échec d'une récolte prématurée est déjà représenté dans une valeur négative. À 120, l'estimation de l'irrigation devient positive. Entre 400 et 550, certaines valeurs diminuent. L'apprentissage n'est pas monotone. À 3 200, l'irrigation devient plus favorable que l'attente dans cet état.

Les contenus représentationnels étudiés concernent plusieurs relations coexistantes : coût immédiat, croissance, humidité, maturité, pénalité de récolte prématurée, bénéfice futur, possibilité de retarder une action. Une valeur Q n'est qu'une représentation numérique de ces conséquences estimées dans une situation donnée.

## 5. Le répertoire des actions au dernier instant

Au terme des 3 200 transitions, on obtient avec le DQN, en fixant le marqueur à zéro :

| Situation | Attendre | Irriguer | Récolter |
|---|---:|---:|---:|
| Humide, en croissance | 4,20 | 3,66 | −2,00 |
| Humide, mûre | 3,56 | 4,40 | 5,00 |
| Sec, en croissance | 3,12 | 3,67 | −2,00 |
| Sec, mûre | 3,55 | 4,40 | 1,50 |

Cette configuration représente plusieurs relations articulées. Selon la maturité et l'humidité, attendre, irriguer et récolter peuvent devenir préférables. Ce ne sont pas quatre « schèmes » indépendants : chaque valeur peut dépendre des mêmes règles d'environnement, et certaines relations sont réparties entre plusieurs états et actions.

Les valeurs ont été arrondies. Le contenu informatique complet 8×3 et les réponses internes des couches sont dans les résultats originaux.

## 6. Ambiguïté puis différenciation de l'indice indirect

Jusqu'à t=400, l'indice `marker` vaut toujours la même chose que `dry`. Les 4 combinaisons où il les contredit **n'ont pas été observées**. Pour les méthodes tabulaires, leurs entrées sont des valeurs initiales par défaut, et non des acquis. La forte différence entre ces états et les états rencontrés ne prouve donc pas, à elle seule, l'apprentissage d'un faux schème.

Après l'arrivée des observations où marqueur et humidité sont indépendants, les 8 états et les 24 couples état-action sont présents dès t=550.

Nous examinons ensuite, à humidité et maturité fixées, le changement des valeurs d'action lorsque seul le marqueur varie :+
| Transitions | Q-Learning | Expected SARSA | Dyna-Q | DQN |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0,229 |
| 40 | 0,976 | 0,964 | 1,752 | 0,306 |
| 120 | 1,811 | 1,750 | 5,549 | 0,596 |
| 300 | 3,882 | 3,595 | 6,131 | 0,792 |
| 400 | 4,702 | 4,284 | 6,131 | 1,002 |
| 550 | 1,569 | 1,437 | 0,070 | 0,421 |
| 800 | 0,479 | 0,441 | 0 | 0,056 |
| 1 200 | 0,207 | 0,191 | 0 | 0,029 |
| 2 000 | 0,015 | 0,017 | 0 | 0,016 |
| 3 200 | 0 | 0 | 0 | 0,008 |

La colonne Dyna-Q change rapidement, mais Dyna-Q effectue également cinq mises à jour simulées par transition réelle. Ces contrastes sont des mesures de comportement des fonctions apprises, pas un comptage de schèmes.

### Trois relations dans le même DQN

| Transitions | Contraste humidité | Contraste maturité | Contraste marqueur |
|---:|---:|---:|---:|
| 40 | 0,12 | 0,22 | 0,31 |
| 400 | 1,52 | 6,01 | 1,00 |
| 550 | 2,72 | 5,60 | 0,42 |
| 800 | 2,31 | 5,34 | 0,06 |
| 1 200 | 2,29 | 5,33 | 0,03 |
| 3 200 | 2,29 | 5,34 | 0,008 |

Le modèle devient fortement sensible à l'humidité et à la maturité en même temps que sa sensibilité au marqueur diminue. **L'absence d'effet final du marqueur ne signifie pas l'absence de contenus internes relatifs à celui-ci.**

## 7. Inspecter les deux couches cachées du DQN

Une sonde garde humidité et maturité fixes et ne modifie que `marker`.

| Checkpoint | Première couche, 12 dimensions | Deuxième couche, 8 dimensions | Différence des valeurs Q |
|---:|---:|---:|---:|
| 0 | 1,045 | 0,534 | 0,229 |
| 40 | 1,069 | 0,580 | 0,306 |
| 400 | 1,115 | 0,991 | 1,002 |
| 550 | 0,837 | 0,428 | 0,421 |
| 800 | 0,717 | 0,083 | 0,056 |
| 1 200 | 0,698 | 0,070 | 0,029 |
| 2 000 | 0,678 | 0,074 | 0,016 |
| 3 200 | 0,664 | 0,080 | 0,008 |

Les échelles et dimensions des couches sont différentes. Le contraste de couche 1 reste sensible au marqueur à la fin alors que le vecteur d'action n'en dépend presque plus. Ce sont des sensibilités observées, **pas** la preuve qu'un schème unique aurait été conservé, modifié ou effacé.

À t=0, les activations proviennent de l'initialisation aléatoire et ne doivent pas être présentées comme des acquis.

## 8. Dyna-Q et l'acquisition de contenus de dynamique

Dyna-Q apprend non seulement les valeurs des actions, mais un modèle empirique des transitions rencontrées. Celui-ci comprend des effectifs de transitions et des informations de récompense.

- Après 400 transitions : **12 couples état-action rencontrés** sur 24.
- Après 550 transitions : **24 couples rencontrés** sur 24.

Pour l'action `irriguer` dans l'état sol sec, culture en croissance, marqueur présent, observée 151 fois au terme de l'expérience :

| État suivant observé | Occurrences |
|---|---:|
| Sol humide, culture en croissance, marqueur absent | 90 |
| Sol humide, culture en croissance, marqueur présent | 61 |

Ces effectifs distinguent la dynamique physique (irriguer rend humide) de la variation du marqueur. Le modèle peut ensuite utiliser ces transitions pour ses propres mises à jour simulées de valeurs Q.

Le contenu dynamique empirique est différent de l'estimation de valeur d'une action. Ils se combinent dans l'algorithme, sans constituer automatiquement de nouveaux objets scientifiques.

## 9. Ce qui est observable à chacun des dix instants

- Tables **8×3 complètes** des trois méthodes tabulaires ;
- Valeurs **8×3 prédites** par DQN ;
- Activations **8×12 et 8×8** de ses deux couches cachées ;
- Paramètres du réseau à chaque checkpoint ;
- Modèle empirique complet des transitions de Dyna-Q ;
- Visites des états et couples état-action ;
- Sondes de contraste sur humidité, maturité, marqueur ;
- Préférences d'action et comparaison diagnostique avec la politique optimale du simulateur (sans que cette solution soit fournie aux apprenants).

La comparaison avec l'optimum connu est **un contrôle postérieur**, non le schème ni la cible directement transmise au modèle.

## 10. Fichiers conservés : expérience principale et version complémentaire

**Expérience principale (`politique_decision_6e`) :**

- `experiment_policy_schemes.py` ;
- `dataset_policy.npz` ;
- `results_policy.json` ;
- `dqn_checkpoint_parameters.npz` ;
- `summary_policy.csv` ;
- `cue_q.png` ;
- `action_agreement.png` ;
- `manifest_policy.json` ;
- `README.md` ;
- archive originale `experience_politique_decision_sans_TL.zip`.

**Une autre réalisation présente dans les fichiers initiaux** est conservée comme ressource complémentaire, sans être silencieusement fusionnée avec la principale : `politique_decision_experiment/` et son archive originale `experiment_decision_schemes_package.zip`. Elle comprend programme, tests, checkpoints `.pt`, résultats, trajectoires et manifeste distincts. Ces deux ensembles ne doivent pas être présentés comme une seule et même exécution.

Lancer le script principal avec les dépendances NumPy, PyTorch et matplotlib (voir son README pour la syntaxe et les options). Les résultats reposent sur un scénario synthétique à une graine, sans validation répliquée sur de nombreux environnements.

## 11. Ce que cette famille apporte à l'étude des schèmes

Les contenus appris peuvent relier plusieurs moments : une action actuelle, un état futur et des conséquences différées. Plusieurs relations coexistent et peuvent se réorganiser pendant les mises à jour. Les représentations d'une même situation peuvent être explicites dans des tables, distribuées dans un réseau ou liées à un modèle empirique de transitions. Une différence entre couches n'est pas automatiquement une différence de schèmes identifiés.

L'étude est **sans TL** et ne prétend pas que les signaux de récompense équivalent aux objets scientifiques de TL.


---

# Chronologie complète des indicateurs — 06_politique_decision

**Tableau directement extrait du CSV expérimental original, sans recalcul ni interpolation.**

- Fichier original : `originaux/politique_decision_6e/summary_policy.csv`.
- Lignes expérimentales : **40**.
- Colonnes conservées : **15**.
- Les chiffres sont des mesures ou paramètres du protocole, **pas des dénombrements de schèmes**.
- La totalité des états multidimensionnels, au-delà des indicateurs de ce tableau, est conservée dans le JSON/NPZ originaux.

| n | algorithm | visited_sa | visited_states | probe_cue_q | probe_dry_q | probe_stage_q | probe_cue_policy_switch | probe_action_agreement | dqn_hidden1_cue | dqn_hidden2_cue | dqn_hidden1_dry | dqn_hidden2_dry | dqn_hidden1_mature | dqn_hidden2_mature |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | q_learning | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.25 | — | — | — | — | — | — |
| 0 | expected_sarsa | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.25 | — | — | — | — | — | — |
| 0 | dyna_q | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.25 | — | — | — | — | — | — |
| 0 | dqn | 0 | 0 | 0.22891848906874657 | 0.13777199760079384 | 0.11320328339934349 | 1.0 | 0.375 | 1.045381486415863 | 0.5336105078458786 | 0.9053685367107391 | 0.2620239183306694 | 0.9515268206596375 | 0.32446859031915665 |
| 40 | q_learning | 10 | 4 | 0.9758571107882738 | 0.9758571107882738 | 0.9512087293730545 | 0.5 | 0.375 | — | — | — | — | — | — |
| 40 | expected_sarsa | 10 | 4 | 0.9644080700351965 | 0.9644080700351965 | 0.9461992291479352 | 0.5 | 0.375 | — | — | — | — | — | — |
| 40 | dyna_q | 10 | 4 | 1.7518879343656573 | 1.7518879343656573 | 1.5826507574579478 | 0.5 | 0.375 | — | — | — | — | — | — |
| 40 | dqn | 10 | 4 | 0.3062616363167763 | 0.1236866693943739 | 0.22109554335474968 | 1.0 | 0.375 | 1.0694327354431152 | 0.5795987844467163 | 0.9098556041717529 | 0.27747658640146255 | 1.0157891511917114 | 0.4014598950743675 |
| 120 | q_learning | 12 | 4 | 1.8114020076482213 | 1.8114020076482213 | 1.633963195147458 | 0.75 | 0.5 | — | — | — | — | — | — |
| 120 | expected_sarsa | 12 | 4 | 1.7500050769255266 | 1.7500050769255266 | 1.6224914280992588 | 0.75 | 0.5 | — | — | — | — | — | — |
| 120 | dyna_q | 12 | 4 | 5.5485138957681155 | 5.5485138957681155 | 2.733301410147687 | 0.75 | 0.625 | — | — | — | — | — | — |
| 120 | dqn | 12 | 4 | 0.5959267765283585 | 0.13187988474965096 | 3.27730393409729 | 0.0 | 0.5 | 0.990655392408371 | 0.7459638565778732 | 1.0036019533872604 | 0.2981385514140129 | 1.7073693871498108 | 2.733223080635071 |
| 300 | q_learning | 12 | 4 | 3.8821297572142344 | 3.8821297572142344 | 2.621742437839443 | 0.75 | 0.625 | — | — | — | — | — | — |
| 300 | expected_sarsa | 12 | 4 | 3.594899707604571 | 3.5948997076045703 | 2.6492297053710714 | 0.75 | 0.625 | — | — | — | — | — | — |
| 300 | dyna_q | 12 | 4 | 6.130750707834045 | 6.130750707834045 | 2.667817724796723 | 0.75 | 0.625 | — | — | — | — | — | — |
| 300 | dqn | 12 | 4 | 0.7918976992368698 | 1.3183757662773132 | 5.0829532742500305 | 0.5 | 0.75 | 1.1246625036001205 | 0.8691537231206894 | 1.226586937904358 | 1.066492773592472 | 1.9458024203777313 | 2.765559494495392 |
| 400 | q_learning | 12 | 4 | 4.702335525652632 | 4.702335525652632 | 2.6506924358255066 | 0.75 | 0.625 | — | — | — | — | — | — |
| 400 | expected_sarsa | 12 | 4 | 4.284409054852617 | 4.284409054852617 | 2.7044389278583587 | 0.75 | 0.625 | — | — | — | — | — | — |
| 400 | dyna_q | 12 | 4 | 6.13075613875345 | 6.13075613875345 | 2.6678166505171355 | 0.75 | 0.625 | — | — | — | — | — | — |
| 400 | dqn | 12 | 4 | 1.002158299088478 | 1.5201693177223206 | 6.009479522705078 | 0.75 | 0.625 | 1.114838793873787 | 0.991037130355835 | 1.2437284886837006 | 1.0814609974622726 | 1.9330981075763702 | 2.6759426295757294 |
| 550 | q_learning | 24 | 8 | 1.568637984838889 | 2.103228329244073 | 4.3959935014619145 | 0.0 | 1.0 | — | — | — | — | — | — |
| 550 | expected_sarsa | 24 | 8 | 1.4373160649927974 | 2.110302031352079 | 4.441939630083341 | 0.0 | 1.0 | — | — | — | — | — | — |
| 550 | dyna_q | 24 | 8 | 0.07011026073493713 | 2.332129095291423 | 5.356372444898214 | 0.0 | 1.0 | — | — | — | — | — | — |
| 550 | dqn | 24 | 8 | 0.42055803537368774 | 2.722467541694641 | 5.601041674613953 | 0.25 | 0.875 | 0.8366140425205231 | 0.4275369718670845 | 1.6479130387306213 | 1.8467912375926971 | 1.8848530650138855 | 2.419685423374176 |
| 800 | q_learning | 24 | 8 | 0.47870536320843743 | 2.4538648502042806 | 5.370934221629081 | 0.0 | 1.0 | — | — | — | — | — | — |
| 800 | expected_sarsa | 24 | 8 | 0.4414176698931713 | 2.589899710854146 | 5.48323888404441 | 0.0 | 1.0 | — | — | — | — | — | — |
| 800 | dyna_q | 24 | 8 | 7.163392765144793e-06 | 2.2894327967385224 | 5.335638454290064 | 0.0 | 1.0 | — | — | — | — | — | — |
| 800 | dqn | 24 | 8 | 0.056360999122262 | 2.3056159615516663 | 5.337212145328522 | 0.0 | 1.0 | 0.71693916618824 | 0.08299498446285725 | 1.6517598628997803 | 1.6343635618686676 | 1.8076601326465607 | 2.3691859543323517 |
| 1200 | q_learning | 24 | 8 | 0.20696917794903014 | 2.5269524182351537 | 5.413212708978905 | 0.0 | 1.0 | — | — | — | — | — | — |
| 1200 | expected_sarsa | 24 | 8 | 0.19133696219386773 | 2.740328319743534 | 5.56502451170688 | 0.0 | 1.0 | — | — | — | — | — | — |
| 1200 | dyna_q | 24 | 8 | 7.505218918220334e-12 | 2.2894064000104906 | 5.335633300581769 | 0.0 | 1.0 | — | — | — | — | — | — |
| 1200 | dqn | 24 | 8 | 0.029175989096984267 | 2.2848903238773346 | 5.332870244979858 | 0.0 | 1.0 | 0.6979962736368179 | 0.0702848145738244 | 1.6593849658966064 | 1.6273311376571655 | 1.8086354732513428 | 2.367343097925186 |
| 2000 | q_learning | 24 | 8 | 0.015246691590431597 | 2.29815584382495 | 5.336747795791692 | 0.0 | 1.0 | — | — | — | — | — | — |
| 2000 | expected_sarsa | 24 | 8 | 0.01705733047976244 | 2.557051266035783 | 5.475022727583241 | 0.0 | 1.0 | — | — | — | — | — | — |
| 2000 | dyna_q | 24 | 8 | 0.0 | 2.2894064 | 5.335633300580483 | 0.0 | 1.0 | — | — | — | — | — | — |
| 2000 | dqn | 24 | 8 | 0.015841172426007688 | 2.289578139781952 | 5.337635338306427 | 0.0 | 1.0 | 0.6783413141965866 | 0.07436661515384912 | 1.6682486832141876 | 1.6393876373767853 | 1.8069307208061218 | 2.367175906896591 |
| 3200 | q_learning | 24 | 8 | 0.0002820587440444026 | 2.289463004628396 | 5.335640717350124 | 0.0 | 1.0 | — | — | — | — | — | — |
| 3200 | expected_sarsa | 24 | 8 | 0.0003704563597041247 | 2.545809329577452 | 5.472915719571544 | 0.0 | 1.0 | — | — | — | — | — | — |
| 3200 | dyna_q | 24 | 8 | 0.0 | 2.2894064 | 5.335633300580483 | 0.0 | 1.0 | — | — | — | — | — | — |
| 3200 | dqn | 24 | 8 | 0.007953224936500192 | 2.2896987795829773 | 5.335875153541565 | 0.0 | 1.0 | 0.6638982146978378 | 0.08048141980543733 | 1.67202627658844 | 1.643662005662918 | 1.8041361272335052 | 2.3670795559883118 |


<!-- FIN 06_politique_decision -->

