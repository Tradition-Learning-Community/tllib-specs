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
| 550 | 1,19 | 1,89 | −2,00 |+| 800 | 1,56 | 2,30 | −2,00 |
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

Nous examinons ensuite, à humidité et maturité fixées, le changement des valeurs d'action lorsque seul le marqueur varie :

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
