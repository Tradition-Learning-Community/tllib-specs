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
