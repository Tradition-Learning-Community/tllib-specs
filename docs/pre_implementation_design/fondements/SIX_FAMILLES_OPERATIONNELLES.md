# Six familles opérationnelles de modèles IA — cadre de référence sans TL

**Statut : classification de travail, non normative pour TL — 15 novembre 2026.**

## Objet

Cette classification est établie du point de vue du **développeur de modèles**, distinct de l'application finale. Elle décrit la **finalité principale de l'apprentissage**, et non la méthode informatique ni l'architecture. Elle est pratique, non nécessairement exclusive et non démontrée mathématiquement irréductible.

| Famille | Finalité | Exemples de modèles ou méthodes | Acquis informatiques possibles |
|---|---|---|---|
| Régression | Estimer des grandeurs | LinearRegression, Ridge, RandomForestRegressor, MLPRegressor | Coefficients, arbres, paramètres neuronaux |
| Classification | Distinguer des catégories | LogisticRegression, SVM, arbres, CNN | Frontières, conditions, paramètres, exemples supports |
| Clustering | Construire des regroupements sans classes imposées | K-Means, DBSCAN, GaussianMixture | Centres, voisinages, composantes probabilistes |
| Génération | Produire des séquences ou échantillons | n-grammes, modèles autorégressifs, VAE, diffusion | Probabilités conditionnelles, structures latentes, paramètres |
| Représentation | Apprendre une transformation/organisation de l'information | PCA, NMF, autoencodeur, contrastif | Projections, composantes, encodeurs |
| Politique de décision | Apprendre à choisir des actions selon leurs conséquences | Q-Learning, DQN, PPO, Dyna-Q | Valeurs, politiques, modèles d'environnement |

## Niveaux à ne pas confondre

- **Finalité** : les six familles ci-dessus.
- **Paradigme** : supervisé, non supervisé, auto-supervisé, par renforcement, par imitation, par préférences, etc.
- **Architecture** : linéaire, arbre, CNN, Transformer, autoencodeur, GNN, réseau récurrent, etc.
- **Mécanisme d'apprentissage** : résolution algébrique, descente de gradient, rétropropagation, partitionnement, EM, mises à jour temporelles, mémorisation d'exemples, etc.
- **Catégorie de modèle** : LLM, World Model, foundation model, multimodal, etc.

Par exemple, un Transformer peut servir à la classification, à la génération et à la représentation. Un modèle génératif autorégressif prédit des éléments successifs ; cela ne transforme pas sa finalité principale en régression. Une politique de décision peut mobiliser une fonction de valeur et des représentations apprises. Une même application peut utiliser plusieurs modèles de familles différentes.

## Cycle opérationnel et périmètre de l'étude

Nous conservons le cycle : **problème et finalité → ressources et moyens → apprentissage → acquis → évaluation/vérification → utilisation/évolution**. Le travail actuel vise **l'apprentissage et les acquis**, pas la refonte des autres activités. L'évolution d'un modèle redevient de l'apprentissage lorsqu'elle comporte une acquisition ou modification effective.

Les expériences sont réalisées **sans TL**. Elles constituent des situations de référence pour étudier ultérieurement des apprentissages appartenant aux **mêmes six familles avec TL**. **TL n'est pas une septième famille** et les familles ne définissent ni les trois entités ni les huit objets fondamentaux.

## Travaux expérimentaux détaillés

Voir [`../benchmarks/sans_tl/README.md`](../benchmarks/sans_tl/README.md), les six études détaillées et leurs chronologies. Les algorithmes étudiés par famille ont été volontairement choisis petits et suivis sur de longues suites d'observations afin d'examiner la constitution et l'évolution du contenu représentationnel, pas de mesurer une performance industrielle.
