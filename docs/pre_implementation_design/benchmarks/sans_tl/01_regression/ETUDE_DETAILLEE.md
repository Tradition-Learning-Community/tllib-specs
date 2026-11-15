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
