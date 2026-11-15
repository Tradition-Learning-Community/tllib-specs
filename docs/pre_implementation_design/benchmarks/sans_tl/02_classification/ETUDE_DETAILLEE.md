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

| Algorithme | t=40 | t=400 | t=800 | t=3 200 |
|---|---|---|---|---|
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
