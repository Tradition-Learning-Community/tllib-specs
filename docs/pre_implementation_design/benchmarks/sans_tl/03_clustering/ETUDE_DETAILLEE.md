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
