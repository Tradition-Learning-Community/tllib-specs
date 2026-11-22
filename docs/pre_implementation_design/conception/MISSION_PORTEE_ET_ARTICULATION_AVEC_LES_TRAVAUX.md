# Mission TL — portée et articulation avec les travaux

**Synthèse de conception complémentaire — 22 novembre 2026**  
**Statut :** documentation préparatoire non normative. Cette note complète la [représentation mathématique unifiée de la Mission](MISSION_REPRESENTATION_MATHEMATIQUE_UNIFIEE.md) ; elle ne modifie ni le manuscrit théorique ni les contrats de `tllib-specs`.

## 1. Définition conceptuelle retenue

La Mission est une **entreprise orientée sur une population de référence**. Elle peut précéder la connaissance de sa solution, rester ouverte et recevoir plusieurs réalisations et contributions. Celui qui la porte peut ignorer la voie qui permettra de l'accomplir ; les travaux peuvent contribuer progressivement à mieux la comprendre.

Nous retenons la distinction conceptuelle :

\[
\boxed{\operatorname{Mission}=(E,P)}
\]

- **E — Entreprise orientée / Horizon :** ce qui est poursuivi, avec des orientations, propriétés et exigences qui peuvent être encore partiellement inconnues.
- **P — Portée / Périmètre :** la population de référence à laquelle s'applique l'entreprise.

Cette définition de conception ne doit pas être attribuée comme une équation normative déjà publiée dans le manuscrit. E n'est ni une solution, ni une fonction de perte, ni une liste fermée de buts. P n'est ni le dataset, ni une liste de variables, ni la totalité du contexte mobilisable. La Mission ne se confond pas avec une Finalité de travail, une Tâche, une méthode, un modèle ou la Tradition.

Le chapitre 4.1 du manuscrit *Tradition Learning - main.pdf* (page imprimée 99) présente un Maître porteur d'une Mission qui peut être accomplie grâce à des contributions dépassant sa connaissance initiale. La Mission primaire reste distincte de son porteur : elle ne contient pas constitutivement le Maître, le Disciple, la Communauté ni les huit objets fondamentaux.

## 2. La Portée désigne une population, pas un inventaire de variables

La population est constituée des **unités ou situations visées par l'entreprise**, selon des conditions d'appartenance. Selon la Mission, une unité peut être une parcelle, une image, un événement, une configuration, une situation de décision ou une trajectoire. Il faut préciser le type d'unité : des « parcelles » et des « décisions relatives aux parcelles à un instant » ne sont pas automatiquement le même type de population.

Une caractérisation mathématique possible est :

\[
P=\{u\in\mathscr U\mid\chi_P(u)\},
\]

où \(\mathscr U\) est un univers typé et \(\chi_P\) une condition d'appartenance. Cette écriture illustre la délimitation ; elle ne prescrit ni un univers exhaustivement énuméré ni un prédicat toujours calculable.

**La Portée ne requiert pas d'inventorier toutes les propriétés de ses membres.** Une parcelle peut appartenir à la population sans que soient connues la météo, la géologie, l'histoire juridique, toutes les valeurs possibles ou les influences politiques qui pourront être pertinentes dans certains travaux.

Il faut distinguer :

| Concept | Question à laquelle il répond |
|---|---|
| Portée P | Sur quelles unités ou situations l'entreprise s'applique-t-elle ? |
| Variable / observable | Quelle propriété peut-on examiner d'une unité ou situation ? |
| Contexte | Quelles conditions extérieures ou environnantes interviennent dans un travail ou dans la poursuite de l'entreprise ? |
| Source d'information | Où et comment obtient-on des observations ? |
| Échantillon / dataset | Quels cas et quelles mesures sont effectivement disponibles ? |
| Ressource | Quels moyens matériels, logiciels, humains ou environnementaux sont mobilisables ? |

Une population peut conserver une définition d'appartenance stable alors que ses membres réels évoluent. L'apparition d'une nouvelle parcelle qui satisfait déjà les conditions de P ne constitue pas, en soi, une nouvelle Mission. Inversement, modifier les conditions constitutives d'appartenance peut changer P, même si le dataset reste identique.

Aucune cardinalité particulière n'est imposée à la famille des variables possibles : elle peut être finie, très grande ou infinie. Le point déterminant est de ne pas confondre les observables et la population.

## 3. Variables, contexte et travaux particuliers

Pour un travail d'apprentissage ou d'étude \(i\), l'accès aux informations peut être représenté par une application d'observation locale au travail :

\[
h_i:P\times K_i\rightharpoonup X_i.
\]

- P reste la population de la Mission ;
- \(K_i\) désigne les conditions contextuelles nécessaires aux observations de ce travail ;
- \(X_i\) est son espace d'informations, distinct de P ;
- \(\rightharpoonup\) autorise des observations partielles, manquantes ou indisponibles.

Ce schéma est une représentation mathématique auxiliaire ordinaire, pas un nouvel objet scientifique TL. Il ne suppose pas que toutes les Tâches observent les mêmes variables ni que toutes les observations appartiennent à un tableau unique.

**Exemple immobilier.** Une Mission concerne les parcelles d'une zone et l'amélioration des connaissances et décisions pertinentes à leur sujet.

- Un travail d'estimation peut utiliser la superficie, l'accès routier, les ventes comparables et la localisation.
- Un travail de décision peut aussi utiliser le prix, la météo, le risque d'inondation, les taux, les conditions politiques et la réglementation.

La météo et l'état politique peuvent être des informations contextuelles utiles sans devenir automatiquement des unités supplémentaires de la population immobilière. S'ils servent effectivement à définir les situations visées — par exemple, uniquement les situations d'inondation pendant une période déterminée —, ils peuvent aussi intervenir dans la condition d'appartenance à P. Ce rôle doit être justifié ; le nom d'une variable ne suffit pas.

Deux travaux peuvent donc utiliser des applications d'observation différentes alors que leur population est la même. Inversement, deux Missions peuvent partager exactement le même dataset sans partager le même E.

## 4. Dans quelles circonstances la Mission change-t-elle ?

| Événement | Analyse |
|---|---|
| Ajouter la météo dans un algorithme | Ne change pas, à lui seul, E ou P. |
| Ajouter des variables politiques, économiques ou techniques | N'impose aucune nouvelle Mission. |
| Changer de méthode ou de modèle | Ne change pas, à lui seul, E ou P. |
| Créer un travail supplémentaire sous le même Horizon | N'impose aucune nouvelle Mission. |
| Observer de nouvelles unités qui satisfont déjà les conditions de P | Augmente les observations ou l'extension constatée ; ne change pas nécessairement la définition de P. |
| Découvrir qu'une description antérieure de P ou E était incomplète | Peut conduire à préciser la même Mission. |
| Étendre délibérément la population à un domaine jusque-là exclu | Peut modifier substantiellement P. |
| Remplacer l'entreprise poursuivie par une autre | Peut constituer une nouvelle Mission. |

La continuité d'une Mission ne se déduit pas d'un simple test sur les noms de variables. Elle doit être appréciée et justifiée à partir de la continuité de E et de P. Aucun seuil, distance ou invariant universel n'est décrété ici.

## 5. Mission, Problème, Finalité, Tâche et onze éléments

La Mission ne doit pas absorber l'anatomie des travaux d'apprentissage.

- Un **Problème** exprime les inconnues, relations ou conditions computationnelles à examiner. Il est distinct de l'entreprise globale, d'un manque présumé de données et d'une Tâche prédéfinie.
- Une **Finalité de travail** caractérise le résultat, les propriétés ou le progrès recherchés dans ce travail.
- Une **Tâche** caractérise la nature de l'activité : régression, classification, clustering, génération, représentation, décision, etc.

La Finalité n'est pas systématiquement la fonction de perte.

Les onze éléments retenus pour décrire un travail d'apprentissage IA — qui ne sont pas les onze éléments fondamentaux de TL — sont :

| N° | Élément du travail | Rôle |
|---:|---|---|
| 1 | Problème | Inconnues et relations à déterminer ou examiner. |
| 2 | Finalité | Résultat, propriétés ou progrès recherchés dans le travail. |
| 3 | Tâche | Nature du traitement entrepris. |
| 4 | Ressources | Moyens matériels, logiciels ou environnementaux mobilisables. |
| 5 | Sources d'apprentissage | Observations, expériences, flux, exemples ou interactions disponibles. |
| 6 | Configuration | Conditions initiales et choix de constitution de la méthode. |
| 7 | Algorithme d'apprentissage | Processus effectif d'apprentissage. |
| 8 | Critère d'apprentissage | Conditions ou objectifs guidant ce processus. |
| 9 | Mécanisme de modification | Modifications effectives des structures ou états. |
| 10 | Modèle | Résultat informatique ou état exploitable. |
| 11 | Évaluation | Vérifications, sondes et comparaisons pertinentes. |

Un même travail peut combiner plusieurs Tâches ou méthodes. Une Mission peut orienter plusieurs travaux ; plusieurs Missions peuvent partager des Sources, Ressources ou travaux connexes. Ni la correspondance un travail–une Mission, ni la correspondance une Tâche–une Mission n'est obligatoire.

## 6. Six travaux immobiliers : deux organisations possibles

Le document [EXERCICES_PARCELLES_SIX_FAMILLES_11_ELEMENTS.md](EXERCICES_PARCELLES_SIX_FAMILLES_11_ELEMENTS.md) décrit six travaux distincts à partir d'une base illustrative commune de **10 000 observations fictives**. La source commune ne fixe pas le nombre de Missions.

| Travail | Problème / Finalité particulière | Famille de Tâche |
|---|---|---|
| 1 | Estimer le prix des parcelles | Régression |
| 2 | Distinguer des catégories de prix construites pour l'exercice | Classification |
| 3 | Découvrir des groupes descriptifs de parcelles | Clustering |
| 4 | Produire des descriptions immobilières synthétiques plausibles | Génération |
| 5 | Construire une représentation compacte des parcelles | Représentation |
| 6 | Choisir d'acheter, attendre ou renoncer dans un simulateur défini | Politique de décision |

Le travail de décision emploie en plus un environnement de transitions et des conséquences simulées ; le tableau immobilier statique ne constitue pas, à lui seul, une source complète pour cet apprentissage.

Deux organisations sont scientifiquement possibles :

**Organisation A — Six Missions.** Le développeur distingue six entreprises, chacune avec son propre E et, le cas échéant, son P. Elles peuvent partager la population des parcelles et certaines sources sans être identiques. Une Mission particulière peut elle-même accueillir d'autres travaux.

**Organisation B — Une Mission.** Le développeur poursuit une entreprise plus générale, par exemple comprendre et exploiter les propriétés et évolutions des parcelles dans le périmètre immobilier retenu. Les six travaux ont leurs Problèmes, Finalités et Tâches particuliers, sans redéfinir à chaque fois la population ou l'Horizon général. La Mission unique ne se définit pas comme la somme des six fonctions de perte.

Dans les deux organisations, le choix doit être justifié par le sens de E et les conditions d'appartenance à P, pas par le nombre d'algorithmes ou de colonnes.

## 7. Ne pas confondre les six travaux immobiliers et les six expériences historiques

Les expériences documentées dans [ETUDE_COMPLETE_SIX_FAMILLES_SANS_TL.md](../benchmarks/sans_tl/ETUDE_COMPLETE_SIX_FAMILLES_SANS_TL.md) constituent un autre corpus : estimation de prix fictifs, classification d'images 7 × 7, géométrie, séquences artificielles, représentation des mêmes images et irrigation fictive. Elles n'utilisent pas une population unique de parcelles pour les six familles. Classification et représentation y partagent effectivement les images, avec des Finalités différentes.

Regrouper toutes ces études historiques sous une Mission unique demanderait une entreprise et une Portée plus larges, explicitement justifiées. Les résultats de ces expériences restent des observations sans TL : leur relecture au moyen de la Mission n'atteste pas qu'une Mission ait guidé les apprentissages déjà exécutés.

## 8. Frontières avec la théorie TL et statut de cette note

TL comprend trois entités — Maître, Disciple, Communauté — et huit objets fondamentaux — Message, Principes, Valeurs, Vertus, Capacités, Compétences, Pratique et Expérience vécue. Leur anatomie, leurs relations et leurs mathématiques ne sont pas remplacées par la représentation de Mission.

La Tradition est un héritage vivant, intégré, évolutif et transmissible. Elle ne se confond ni avec la Mission, ni avec une solution, un dataset, des poids, des schèmes ou une collection d'artefacts. Les schèmes demeurent un terme de travail pour les contenus représentationnels acquis ou modifiés dans un modèle ; ils ne deviennent pas un neuvième objet TL.

Les mathématiques du contexte dynamique et de la finalité/téléologie évolutive conservent leurs domaines propres. Cette note n'assimile ni le contexte à P, ni un but téléologique à E sans relation scientifique établie.

La Mission peut être conceptuellement première, mais une opération de TL ne devient scientifique et exécutable que dans les conditions prévues par les contrats concernés. Une structure constituée, une opération exécutable, un apprentissage constaté et un développement de Tradition sont quatre états de justification différents.

### Décisions de conception retenues

1. La Mission est une entreprise orientée sur une population de référence : (E, P).
2. P délimite les unités ou situations visées, non le nombre ou la liste des variables disponibles.
3. Les variables, contextes et sources sont déterminés selon les travaux ; leur évolution ne redéfinit pas automatiquement la Mission.
4. L'appartenance d'une nouvelle unité à une population déjà définie ne signifie pas nécessairement que P a été modifié.
5. L'Horizon ne se confond ni avec le fait actuel, ni avec une solution unique, ni avec la Finalité et le critère d'un travail.
6. Une Mission peut accueillir plusieurs Problèmes, Finalités, Tâches et réalisations ; plusieurs Missions peuvent partager des données et ressources.
7. Les formulations de Mission peuvent évoluer ; leur continuité exige une justification, non un seuil inventé.
8. Les déductions et vérifications mathématiques sont conditionnelles aux propriétés correctement définies.
9. Les expériences antérieures sans TL demeurent des témoins, et non des preuves de transformation TL.
10. Cette note est un résultat de conception argumenté, non une nouvelle loi TL déjà démontrée dans les sources normatives.

**Définition consolidée de la Portée :** *la population de référence à laquelle s'applique l'entreprise orientée, délimitée par des conditions d'appartenance pertinentes, sans obligation d'énumérer les propriétés, observations ou variables qui pourront servir à sa poursuite.*

**Définition consolidée de la Mission :** *une entreprise orientée sur une population de référence, susceptible de demeurer ouverte, d'être progressivement mieux comprise et de recevoir plusieurs réalisations et contributions sans être identifiée à l'une d'entre elles.*

## Références internes

- [Représentation mathématique unifiée de la Mission](MISSION_REPRESENTATION_MATHEMATIQUE_UNIFIEE.md).
- [Mission, entités, huit objets et Tradition](../fondements/MISSION_ENTITES_HUIT_OBJETS_ET_TRADITION.md).
- [Six travaux immobiliers et onze éléments](EXERCICES_PARCELLES_SIX_FAMILLES_11_ELEMENTS.md).
- [Six expériences historiques sans TL](../benchmarks/sans_tl/README.md).
- [Constitution et frontières](CONSTITUTION_ET_FRONTIERES.md).
- [Questions ouvertes](QUESTIONS_OUVERTES.md).
- [Contexte dynamique](../../../maths/24-context/context.md).
- [Finalité et téléologie évolutive](../../../maths/28-finality-and-evolutionary-teleology/finality-and-evolutionary-teleology.md).
