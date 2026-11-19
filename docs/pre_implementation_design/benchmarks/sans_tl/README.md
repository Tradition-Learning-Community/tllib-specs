# Benchmarks de pré-implémentation — Six familles **sans TL**

## Nature et portée

Ces six expériences **synthétiques**, exécutées le 15 novembre 2026, observent de petits modèles sur de longues suites d'observations. Elles examinent l'évolution interne des contenus représentationnels acquis, parfois au moyen de sondes sur des entrées contrôlées. Les mesures de contraste, probabilités, valeurs Q, activations et paramètres **ne constituent pas un comptage direct des schèmes**.

Les benchmarks sont des **références de recherche préparatoire**, et non des tests de conformité `tllib-specs`, des résultats de production, des performances validées de TL ou des preuves de formation d'une Tradition.

## Index des six familles

| Famille | Observations | Modèles | Documents détaillés |
|---|---:|---|---|
| [Régression](01_regression/ETUDE_DETAILLEE.md) | 1 600 | RLS, arbre, petit réseau | Étude, chronologie, provenance |
| [Classification](02_classification/ETUDE_DETAILLEE.md) | 3 200 | logistique, BernoulliNB, arbre, MLP | Étude, chronologie, provenance |
| [Clustering](03_clustering/ETUDE_DETAILLEE.md) | 3 200 | K-Means, MiniBatch, GMM, DBSCAN | Étude, chronologie, provenance |
| [Génération](04_generation/ETUDE_DETAILLEE.md) | 3 200 séquences | unigramme, bi-/tri-/4-gramme, petit réseau | Étude, chronologie, provenance |
| [Représentation](05_representation/ETUDE_DETAILLEE.md) | 3 200 images | PCA, IncrementalPCA, NMF, autoencodeur, contrastif | Étude, chronologie, provenance |
| [Politique de décision](06_politique_decision/ETUDE_DETAILLEE.md) | 3 200 transitions | Q-Learning, Expected SARSA, Dyna-Q, DQN | Étude, chronologie, provenance |

Le fichier [`ETUDE_COMPLETE_SIX_FAMILLES_SANS_TL.md`](ETUDE_COMPLETE_SIX_FAMILLES_SANS_TL.md) conserve **le document intégral d'origine** des six familles. Chaque sous-dossier comprend ses fichiers `ETUDE_DETAILLEE.md`, `CHRONOLOGIE_COMPLETE.md` et `FICHIERS_ORIGINAUX_SHA256.md` **sans modification de contenu**.

## Données, programmes, checkpoints et limites de reproduction

Les fichiers bruts et exécutables ont été conservés **séparément**, dans l'archive `ETUDE_SIX_FAMILLES_SANS_TL.zip` construite précédemment (91 fichiers). **Seuls les fichiers Markdown sont placés dans ce dépôt**. Les inventaires SHA-256 permettent de vérifier l'identité des originaux lorsqu'ils sont disponibles, mais ne permettent pas à eux seuls de les recréer. Pour une reproduction, l'archive de données et scripts reste nécessaire ; son dépôt dans `tllib-specs` n'est ni effectué ni revendiqué ici.

La régression disposait initialement de son script et d'un JSON de résultats, sans jeu de données séparé ; ce script régénère le jeu synthétique à partir de la graine fixée. Pour les autres familles, se reporter à l'inventaire conservé.

## Méthode de comparaison future

Le périmètre de ces expériences demeure *sans TL*. Si une comparaison avec TL est entreprise, conserver autant que possible les mêmes données, architectures élémentaires, critères de mesure, points d'observation et traces ; distinguer les modifications du système informatique, les phénomènes TL scientifiquement définis et les hypothèses non testées.
