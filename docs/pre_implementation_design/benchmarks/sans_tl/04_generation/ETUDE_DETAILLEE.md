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
