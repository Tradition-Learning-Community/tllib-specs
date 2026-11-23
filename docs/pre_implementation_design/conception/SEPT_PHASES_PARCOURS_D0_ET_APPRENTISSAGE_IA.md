# Tradition Learning — Parcours de D0 sur les sept phases et articulation avec l'apprentissage IA classique

> **Statut :** note de conception pré-implémentation — proposition de design, non normative.  
> **Produit :** `tllib` (Tradition Learning Library).  
> **Périmètre :** un système TL minimal avec M0, D0, C0 et une expérience de régression numérique.  
> **Date :** 23 novembre 2026.  
> **Implémentation et tests :** aucun changement de code ni test de conformité exécuté dans le cadre de cette note.  
> **Autorité :** manuscrit scientifique pour la théorie ; snapshot épinglé de `tllib-specs` pour les contrats ; code et documentation de `tllib` pour l'état du produit.

## Sommaire

1. [Objet et limites](#1-objet-et-limites)
2. [Sources et hiérarchie d'autorité](#2-sources-et-hiérarchie-dautorité)
3. [Modèle scientifique commun : 3 entités, 8 objets, 7 phases](#3-modèle-scientifique-commun--3-entités-8-objets-7-phases)
4. [Constitution du système TL minimal](#4-constitution-du-système-tl-minimal)
5. [L'apprentissage IA classique demeure pleinement opérationnel](#5-lapprentissage-ia-classique-demeure-pleinement-opérationnel)
6. [Un seul parcours articulé pour D0](#6-un-seul-parcours-articulé-pour-d0)
7. [Conception par phase](#7-conception-par-phase)
8. [Articulation des huit objets sur l'ensemble du parcours](#8-articulation-des-huit-objets-sur-lensemble-du-parcours)
9. [Continuité, bifurcations et issues défavorables](#9-continuité-bifurcations-et-issues-défavorables)
10. [Responsabilités de tllib et interfaces à concevoir](#10-responsabilités-de-tllib-et-interfaces-à-concevoir)
11. [Frontières des contrats et de l'exécution scientifique](#11-frontières-des-contrats-et-de-lexécution-scientifique)
12. [Plan de conformité et d'expérimentation](#12-plan-de-conformité-et-dexpérimentation)
13. [Décisions retenues, non-décisions et prochains travaux](#13-décisions-retenues-non-décisions-et-prochains-travaux)
14. [Références](#14-références)

---

## 1. Objet et limites

### 1.1. Objectif

Décrire **un seul parcours continu du Disciple D0**, depuis sa candidature à l'Initiation jusqu'à la possibilité d'Autonomisation, afin de préparer le design opérationnel de `tllib`. La note doit aider à déterminer :

- ce que le développeur fournit et ce qui peut rester ouvert ;
- quelles relations existent entre M0, D0 et C0 ;
- comment les huit objets fondamentaux sont mobilisés, conservés, mis en relation et éventuellement transformés ;
- comment les mécanismes des sept phases sont déclenchés, reliés et suivis ;
- comment une opération d'apprentissage IA classique continue de fonctionner **sans être assimilée à une opération TL** ;
- comment traiter admissions refusées, mesures indisponibles, retours en arrière, erreurs, évaluations non concluantes, changements de Maître et continuation autonome ;
- quelles données, conditions, providers, opérations et preuves seront nécessaires dans `tllib`.

Le document est un **design d'articulation pré-implémentation**. Ce n'est ni une nouvelle définition scientifique de TL, ni un contrat de substitution à `tllib-specs`, ni une API déjà disponible, ni un compte rendu de tests exécutés.

### 1.2. Invariants de conception

1. **Trois entités fondamentales :** Maître, Disciple, Communauté. Une Cohorte regroupe des Disciples et ne crée pas une quatrième entité.
2. **Huit objets fondamentaux :** Message, Principes, Valeurs, Vertus, Capacités, Compétences, Pratique, Expérience vécue. Chacun conserve sa fonction scientifique et ses relations.
3. **Sept phases :** Initiation, Imprégnation, Guidage, Incorporation, Intégration, Validation, Autonomisation. Elles décrivent le cheminement scientifique, non des types d'objets ni sept appels obligatoirement séquentiels.
4. **Un même D0 persiste** à travers le temps, les tentatives, les interruptions et les réorientations. Ses transformations ne créent pas nécessairement un nouvel acteur informatique.
5. **Une Tradition** est un héritage vivant, intégré, évolutif et transmissible ; elle n'est pas réductible à la solution du Problème, au modèle `w`, à ses poids ou à un checkpoint.
6. **Une opération informatique n'est pas une preuve de transformation TL.** Enregistrer une exposition, exécuter SGD ou sauvegarder un modèle ne démontre pas, à eux seuls, l'Imprégnation, l'Incorporation, l'Intégration ou la Validation.
7. **Aucune science inventée :** seuils, domaines, équations, métriques, normalisations, fonctions de rappel et transitions non spécifiées restent sous l'autorité scientifique de la source ou d'un provider explicitement requis.
8. **Le système reste ouvert :** arrivée/départ de participants, plusieurs Maîtres, cohortes, branches, générations et continuation sans solutions connues à l'avance.

### 1.3. Trois résultats à ne jamais confondre

| Résultat | Sens dans `tllib` | Ne prouve pas à lui seul |
|---|---|---|
| Système constitué | Relations, rôles, ressources et conditions représentés | Qu'une opération scientifique est exécutable |
| Opération exécutée | Une fonction informatique ou scientifique a effectivement produit un résultat | Un apprentissage du Disciple ni une Tradition développée, sans mesure pertinente |
| Transformation scientifique constatée | Un résultat conforme à un mécanisme TL et à ses critères applicables | Une nouvelle Tradition reconnue ou une promotion de rôle automatique |

---

## 2. Sources et hiérarchie d'autorité

| Niveau | Source | Utilisation dans cette note |
|---|---|---|
| Fondements théoriques | `Tradition Learning - main.pdf` (148 pages) | Entités, objets, relations, fondation générale de TL |
| Développement théorique du parcours | `TraditionLearning.pdf` (748 pages), notamment chapitres 14–22 et 15–21 pour les sept phases | Mécanismes détaillés du parcours et de sa continuation |
| Contrats logiciels | `Tradition-Learning-Community/tllib-specs`, révision `07439babd59c657354e3200ed24c55e2e3eeb72c` | Obligations, limites, statuts d'exécution et acceptations TLC-FC |
| Produit | `Tradition-Learning-Community/tllib`, branche `main`, `README.md`, `docs/v1/` et `specs.lock.json` | Architecture C++20, runtime, providers, APIs, état de développement |

La première version PDF est utilisée comme manuscrit de référence pour les fondements ; le volume étendu contient les chapitres détaillant explicitement les sept phases. Ces fichiers **n'ont pas une pagination ni un périmètre identiques**. Leurs formulations ne sont ni fusionnées ni corrigées silencieusement. En cas de différence ayant un effet logiciel, l'implémentation suit le handoff épinglé de `tllib-specs` et préserve les points non résolus.

Les détails des équations ne sont pas recopiés intégralement ici : le présent document renvoie aux sources et ne se substitue pas à elles.

---

## 3. Modèle scientifique commun : 3 entités, 8 objets, 7 phases

### 3.1. Les entités et leurs rôles dans le cas minimal

- **M0 — Maître initial.** Il occupe ce rôle uniquement si les conditions TL le permettent. Il peut sélectionner, transmettre, guider, évaluer, réguler, puis se retirer progressivement. Il **n'est pas obligé de connaître la solution finale** du Problème.
- **D0 — aspirant puis Disciple si admis.** Il reçoit, pratique, découvre, développe des acquis et peut contribuer. Son modèle numérique ou son algorithme n'est **pas automatiquement** l'entité Disciple : le système TL doit constituer ce rôle et relier les ressources effectivement utilisées.
- **C0 — Communauté initiale.** Elle participe aux relations, à la mémoire, à la régulation, à la reconnaissance et éventuellement aux filiations. Sa présence structurelle ne garantit pas que le quorum d'une Validation collective soit satisfait.

La distinction **identité scientifique / rôle scientifique / ressource informatique** est obligatoire. Une ressource peut soutenir plusieurs rôles ; le logiciel ne déduit pas le rôle d'une classe ML, d'une instance `torch.nn.Module` ou d'un fichier de poids.

### 3.2. Les huit objets, patrimoine mobilisé et transformé

| Objet | Identité scientifique dans le parcours | Limite de l'exemple |
|---|---|---|
| Message | Contenu porteur de sens transmis, reçu et éventuellement transformé | Le texte d'un prompt ou d'une consigne n'est pas automatiquement tout le Message TL |
| Principes | Structures et invariants pertinents pour les activités | Une règle numérique candidate n'est pas automatiquement un Principe de la Tradition |
| Valeurs | Orientations axiologiques du système et de ses membres | Ne pas les remplacer par un coefficient de perte |
| Vertus | Dispositions développées selon les dynamiques TL | Une hausse d'accuracy n'est pas une mesure directe de Vertu |
| Capacités | Potentiel scientifiquement caractérisé du Disciple | Ne pas les assimiler aux capacités mémoire/GPU |
| Compétences | Acquis effectifs contextualisés et évaluables | Une bonne prédiction ponctuelle n'est pas toute la Compétence |
| Pratique | Objet relatif à l'activité exercée et à sa dynamique | Ce n'est pas la phase de Guidage ni uniquement une boucle `fit()` |
| Expérience vécue | Traces et intégration scientifique des situations rencontrées | Un journal d'exécution ou un checkpoint n'en démontre pas à lui seul l'existence TL |

Le terme de travail **schème** peut désigner un contenu représentationnel interne acquis ou modifié par un modèle IA. Il n'est **pas un neuvième objet TL**. Il ne faut pas non plus le confondre avec des poids, paramètres, features, activations ou états. Le document ne présume aucune méthode universelle pour identifier un schème dans une ressource ML.

### 3.3. Les phases : le chemin, non le bagage

Les sept phases nomment des dynamiques scientifiques. Le Guidage est une **phase** où M0 conduit D0 ; la Pratique est un **objet** susceptible d'être mobilisé pendant le Guidage, l'Incorporation et d'autres phases.

La relation d'Incorporation

\[
\mathcal P_t = \lambda(t)\mathcal P_{\mathcal M} + (1-\lambda(t))\mathcal P_{\mathrm{aut}}
\]

combine **deux contributions à la Pratique** ; elle ne met pas « Guidage + Pratique » au même niveau ontologique. Son exécution suppose les opérandes compatibles et le coefficient prévus au contrat, sans emprunter le taux d'apprentissage de SGD.

### 3.4. Parcours et automate : ne pas écraser la théorie

Le manuscrit étendu décrit aussi **quatre grandes étapes** du pipeline et les **sept phases détaillées**. Le contrat `operational-pipeline.md` conserve un automate fini plus synthétique (aspirant, Imprégnation, apprentissage actif, épreuve, transmission, sortie), dont **toutes les transitions ne sont pas spécifiées**. Il indique explicitement un retour après échec d'épreuve :

\[
\delta(s_3,\mathrm{failure})=s_2.
\]

La conception doit donc :

- prendre en charge ce qui est réellement spécifié ;
- ne pas inventer de bijection complète entre les quatre grandes étapes, les états de l'automate et les sept phases ;
- autoriser les interactions, retours, reprises et simultanéités définies ;
- ne pas imposer un ordonnanceur global obligeant tous les Disciples à suivre des niveaux synchronisés.

---

## 4. Constitution du système TL minimal

Les six responsabilités de constitution, sans leur imposer un ordre strict, sont :

1. **Définir Mission et Problème.** Ici, Mission de développement d'aptitudes de découverte/exploitation de relations numériques ; Problème d'étude : apprendre une relation numérique à partir de quelques observations. La Mission reste un concept computationnel potentiellement ouvert.
2. **Inventorier les Ressources.** Échantillons, modèle linéaire, algorithme SGD, environnement de calcul, observables, éventuelles représentations scientifiques et mécanismes de persistance.
3. **Constituer les rôles initiaux.** M0, C0 et D0 en tant que **candidat** ; ne pas faire apparaître artificiellement la relation de disciple admis avant décision d'Initiation.
4. **Associer les Capacités.** Établir les capacités scientifiques et les capacités informatiques disponibles, sans les confondre.
5. **Vérifier les conditions scientifiques.** Contrats applicables, préconditions, représentations, providers, seuils fournis et types compatibles.
6. **Mettre à disposition.** Exposer le système constitué à travers les surfaces du produit ; une opération indisponible reste explicitement indisponible.

### 4.1. État initial *décrit*, non présumé rempli

| Élément | Présent dans le scénario | Non établi au départ |
|---|---|---|
| Candidat D0 | Identité et ressources associables | Admission et états scientifiques complets |
| M0 | Rôle de référence supposé dans notre scénario | Compétences/paramètres TL mesurés numériquement |
| C0 | Communauté initiale | Jury, quorum et scores de légitimité |
| ML | Modèle, observations, SGD, calcul reproductible | Généralisation prouvée |
| TL | Schéma scientifique et contrats disponibles | Valeurs numériques de résonance, mémoire, cohérence, autonomie, etc. |

---

## 5. L'apprentissage IA classique demeure pleinement opérationnel

### 5.1. Modèle et objectif informatique

Le cas est volontairement simple et ne constitue **pas** une définition de TL limitée à la régression, à ML ou au supervisé.

\[
\widehat y=wx,\qquad w_0=0
\]

Pour chaque observation `(x,y)` :

\[
L_{\mathrm{ML}}(w;x,y)=\frac12(wx-y)^2,
\quad
w_{n+1}=w_n-\eta(wx-y)x,
\quad
\eta=0{,}1.
\]

La fonction de perte est **informatique**, pas la mesure universelle d'une phase TL ni la fonction de coût scientifique d'un opérateur de Guidage.

### 5.2. Données et trace entièrement reproductible

**Apprentissage :** alternance de `(1,2)` et `(2,4)` pendant huit mises à jour.  
**Observation de contrôle :** `(3,6)`, qui n'intervient pas dans les huit mises à jour.  
**Observation additionnelle illustrative :** `(4,8)` lors de la réflexion sur l'Autonomisation.

| n | Entrée | Résultat attendu | `w_n` après mise à jour | Placement illustratif dans le parcours |
|---:|---:|---:|---:|---|
| 0 | — | — | 0 | Constitution |
| 1 | 1 | 2 | 0,20000000 | Première Pratique possible durant l'Initiation |
| 2 | 2 | 4 | 0,92000000 | Pratique accompagnée pendant le Guidage |
| 3 | 1 | 2 | 1,02800000 | Pratique pendant l'Incorporation |
| 4 | 2 | 4 | 1,41680000 | Pratique pendant l'Incorporation |
| 5 | 1 | 2 | 1,47512000 | Pratique pendant l'Incorporation |
| 6 | 2 | 4 | 1,68507200 | Pratique pendant l'Incorporation |
| 7 | 1 | 2 | 1,71656480 | Activité informatique pendant l'Intégration |
| 8 | 2 | 4 | 1,82993888 | Activité informatique pendant l'Intégration |

À l'issue :

\[
\widehat y(3)=5{,}48981664,
\qquad |6-\widehat y(3)|=0{,}51018336.
\]

Sur `x=4`, le modèle produit `7,31975552`. Si `y=8` est donné comme nouvelle référence, l'erreur absolue est `0,68024448`.

Ces nombres **sont démontrables par l'algorithme SGD indiqué**. Ils ne démontrent ni une résonance TL, ni une nouvelle Vertu, ni une reconnaissance communautaire, ni l'autonomie de D0.

### 5.3. Principes d'interopérabilité

- L'entraînement classique continue avec les outils et frameworks appropriés : boucles ML, autograd, NumPy, PyTorch, TensorFlow ou autres, selon l'application.
- `tllib` ne devient pas un framework généraliste concurrent de ces outils et ne réimplémente pas les tenseurs ou optimiseurs déjà éprouvés sans nécessité propre à TL.
- La ressource ML peut exposer ses observations, modifications, résultats et capacités à un système TL **par des interfaces explicites** ; ce lien ne transforme pas automatiquement l'optimiseur en Maître ou le modèle en Disciple.
- Un modèle peut aussi ne pas avoir d'équivalent direct de `w` (segmentation, génération, décision, simulation, modèle multimodal) ; l'architecture TL ne doit pas dépendre de cette simplification.
- Les transformations internes éventuelles de schèmes sont à étudier sans confondre état informatique, développement de D0 et formation d'une Tradition.

### 5.4. Deux chronologies reliées, mais non identiques

**Chronologie informatique :** observations → prédiction → perte → gradient → mise à jour des paramètres → mesures ML.  
**Chronologie TL :** relations entre entités → mobilisation des objets → opérations scientifiques applicables → résultats et régulations → acquis et continuation.

Un même événement informatique peut être une preuve ou une ressource pour plusieurs opérations scientifiques, mais **ne vaut pas leur exécution**.

---

## 6. Un seul parcours articulé pour D0

### 6.1. Scénario favorable conditionnel

```text
Système TL constitué (M0, C0, candidat D0 ; ressources ML disponibles)
   |
   +-- Initiation : examen réciproque, admission si conditions satisfaites
   |       \-- première Pratique possible : w0 -> w1 = 0,2
   |
   +-- Imprégnation : observation, exposition, résonance et mémoire
   |       \-- w peut rester à 0,2 : aucune mise à jour ML obligatoire
   |
   +-- Guidage : interventions M0, réception par D0, feedback
   |       \-- mise à jour ML illustrative : w1 -> w2 = 0,92
   |
   +-- Incorporation : Pratiques et réflexion de D0
   |       \-- mises à jour ML n=3..6 : w6 = 1,685072
   |
   +-- Intégration : synthèse des acquis et cohérence
   |       \-- activité ML n=7..8 : w8 = 1,82993888
   |
   +-- Validation : C0 évalue et reconnaît si conditions remplies
   |       \-- contrôle ML sur (3,6), sans admission TL automatique
   |
   +-- Autonomisation : D0 poursuit, peut découvrir, innover, transmettre
           \-- nouveau cas (4,8), aucune promotion automatique

Les branches d'échec, d'ajournement et de retour demeurent possibles.
```

Cette distribution des opérations SGD est une **mise en scène pédagogique**. Elle n'est pas une exigence scientifique de phase ni une prescription d'implémentation. Le scénario favorable suppose des résultats TL supplémentaires **non chiffrés ici**.

### 6.2. Ce que doit conserver un système vivant

- D0 conserve une identité propre malgré plusieurs tentatives et relations ;
- M0 et C0 restent identifiables, avec leurs interventions et leurs effets propres ;
- les huit objets et leurs relations ne sont pas recréés artificiellement à chaque phase ;
- les nouveaux acquis, contenus et relations peuvent apparaître au fil du parcours ;
- les traces ML et les résultats TL sont distingués mais reliables par leur provenance ;
- le système peut continuer après la septième phase, avec ou sans nouvelle transmission.

---

## 7. Conception par phase

Chaque sous-section distingue **mécanisme scientifique**, **illustration ML**, **responsabilité logicielle** et **issues alternatives**. Les éléments proposés pour la traçabilité sont des exigences de design, pas une nomenclature normative de nouveaux objets TL.

### 7.1. Initiation — Établissement de la relation scientifique

**Mécanismes sources.** Reconnaissance réciproque, réceptivité et préparation, affinité, confiance, probation, contrat pédagogique, premiers enseignements et Pratiques, évaluation initiale, admission et inscription dans les relations de filiation. Référence : `initiation-phase.md`, manuscrit étendu ch. 15.

**Chronologie de D0.** Le candidat D0 rencontre M0 et évalue à son tour M0. Une première Pratique supervisée peut produire la mise à jour `w0=0` vers `w1=0,2`. Ce calcul ne fournit aucun seuil TL d'admission. Pour notre trajectoire favorable, on suppose les conditions d'admission satisfaites et la relation reconnue.

**Objets mobilisables.** Message, Principes, Valeurs, Capacités, premières Compétences, Pratique et Expérience vécue, selon les contenus effectivement présents ; pas d'hypothèse d'évolution systématique des huit objets.

**Responsabilités pré-implémentation.**

- Représenter le candidat **avant** son admission et rattacher toute tentative à son identité continue.
- Relier scores, conditions, résultats et décisions à M0, D0, C0 et à leurs sources.
- Ne valider l'entrée et les inscriptions relationnelles que sur une décision scientifiquement autorisée.
- Préserver l'historique des tentatives et les motifs/résultats lorsqu'ils sont disponibles.

**Issues et reprises.** Admission ; évaluation incomplète ; probation/préparation complémentaire ; renoncement ; refus de M0 ; refus de D0 ; réorientation ; nouveau cycle de candidature. Un seuil non atteint **n'implique pas à lui seul** une exclusion définitive. Le moteur n'invente ni seuil, ni agrégation manquante.

**Critère de preuve.** Une admission constatée doit être traçable à des conditions satisfaites et aux effets autorisés ; `w=0,2` n'en est pas la preuve.

### 7.2. Imprégnation — Exposition, résonance et mémoire

**Mécanismes sources.** Immersion dans le cadre de Pratique, observation et démonstration, exposition sélective, huit bandes de résonance associées aux objets fondamentaux, mémoire implicite/explicite et dynamique d'Imprégnation. Référence : `impregnation-phase.md`, manuscrit étendu ch. 16.

Pour chaque bande `k`, la dynamique de résonance est :

\[
\frac{dw_k}{dt}=\alpha_k I_k(t)(1-w_k)-\beta_k w_k+\gamma_k\xi_k(t).
\]

**Important :** `w_k` désigne ici des poids de résonance TL, **pas** le coefficient `w` de régression. Une bande activée satisfait une condition stricte `w_k > θ_act` lorsque les opérandes applicables sont fournis.

**Chronologie de D0.** M0 rend observable la prédiction `ŷ(2)=0,4` et l'observation `y=4`. D0 peut être exposé à la situation **sans corriger immédiatement le modèle** : `w` reste `0,2`.

**Responsabilités pré-implémentation.**

- Conserver la source d'exposition, son contexte, son temps, les objets/bandes référencés et les mesures disponibles.
- Séparer les événements enregistrés des états scientifiques effectivement calculés.
- Préserver la mémoire implicite et explicite comme mécanismes scientifiques distincts des logs et checkpoints.
- Prendre en charge les besoins d'historique pour les noyaux temporels, sans construire arbitrairement les fonctions non fournies.

**Issues et reprises.** Exposition faible ; absence d'exposition ; répétition ; oubli ; résonance sélective ; mémoire non calculable ; interruption. La condition finale du chapitre exige également **toutes** les bandes au-delà de leurs seuils minimaux, tandis que la résonance est présentée comme sélective : le contrat de garde `...-052` conserve cette tension **sans la résoudre**.

**Critère de preuve.** Une exposition ou un fichier de logs n'est pas une Imprégnation scientifiquement exécutée.

### 7.3. Guidage — Transformation par interventions de M0

**Mécanismes sources.** Famille des opérateurs pédagogiques `Φ_θ`, sélection contextualisée, modes explicite/implicite/progressif/initiatique, démonstration, questionnement, correction, silence, processeur de feedback `F`, générateur de trajectoire `T`, boucles locales. Référence : `guidance-phase.md`, manuscrit étendu ch. 17.

**Chronologie de D0.** M0 intervient à partir de la prédiction `0,4` pour `(2,4)`. D0 reçoit, traite ou ne traite pas cette intervention. Une mise à jour SGD ultérieure produit `w2=0,92` ; **elle ne prouve pas** à elle seule l'effet de l'opérateur `Φ_θ`.

**Responsabilités pré-implémentation.**

- Conserver les références à l'intervention, au mode, aux opérateurs applicables, au contexte et à la réception par D0.
- Séparer **intervention émise**, **intervention reçue**, **feedback disponible**, **transformation scientifique constatée** et **mise à jour informatique**.
- Prendre en charge plusieurs boucles simultanées lorsque les contrats l'autorisent.
- Ne pas convertir un `optimizer.step()` en opération `Φ_θ` par défaut.

**Issues et reprises.** Intervention non reçue ; compréhension partielle ; réponse rejetée ; correction erronée ; silence intentionnel ; résultat non concluant ; initiative de D0 ; adaptation du Guidage ; indisponibilité de M0. Aucune progression ne doit être attribuée par simple ordre reçu.

**Critère de preuve.** La relation scientifique entre intervention, retour et évolution doit être établie par les mécanismes exécutables, pas déduite d'une baisse de perte ML.

### 7.4. Incorporation — Pratique et réflexion de D0

**Mécanismes sources.** Retrait progressif des interventions directes, Pratique autonome, incorporation des Principes et des Vertus, formes technique/contextuelle/résolution de problèmes/réflexive de la Pratique, fluidité, métacompétence et auto-évaluation. Référence : `incorporation-phase.md`, manuscrit étendu ch. 18.

Le contrat présente deux contributions **à la Pratique** :

\[
\mathcal P_t=\lambda(t)\mathcal P_{\mathcal M}+(1-\lambda(t))\mathcal P_{\mathrm{aut}}.
\]

Cette écriture ne signifie pas que l'objet Pratique et la phase Guidage sont sur le même plan. Le `λ(t)` scientifique n'est pas `η=0,1` de SGD.

**Chronologie de D0.** D0 effectue quatre mises à jour classiques supplémentaires, de `w2=0,92` à `w6=1,685072`, avec une supervision éventuellement moins directe. Les activités pertinentes de réflexion et d'auto-correction doivent être **observées ou exécutées comme telles** ; les itérations ne les créent pas implicitement.

**Responsabilités pré-implémentation.**

- Représenter la Pratique, son contexte, son résultat et ses éventuelles corrections.
- Préserver les contributions sous influence du Maître et autonomes selon leurs contrats.
- Relier des activités à leurs implications scientifiques **uniquement lorsque déterminables**.
- Permettre que D0 continue son activité tout en ayant encore besoin de M0.

**Issues et reprises.** Répétition sans amélioration ; mauvaise auto-évaluation ; incapacité à se corriger ; transfert raté dans un contexte nouveau ; Pratique incorrecte ; reprise du Guidage ; changement de méthode ML. Le franchissement du seuil d'Incorporation n'est **pas** un nombre d'epochs.

**Critère de preuve.** Une boucle d'entraînement autonome n'est pas automatiquement l'autonomie scientifique ni l'Incorporation des Vertus.

### 7.5. Intégration — Cohérence et identité émergente

**Mécanismes sources.** Générateur d'identité `G`, contrôleur de cohérence, alignement entre dimensions scientifiques, indices de cohérence, corrections, crises et bifurcations identitaires. Référence : `integration-phase.md`, manuscrit étendu ch. 19.

Un état particulier étudié par la théorie est `X=(C,V,Val,P,I)` : il comprend notamment Compétences, Vertus, Valeurs, Capacités et identité. **Il ne remplace pas les huit objets fondamentaux** et ne signifie pas que l'identité en devient un neuvième.

**Chronologie de D0.** Les mises à jour classiques `n=7,8` produisent `w8=1,82993888`. D0 peut cependant être compétent sur cette prédiction tout en présentant une incohérence parmi ses acquis, ses Principes, ses Valeurs ou sa Pratique. La réussite informatique ne produit pas une identité TL.

**Responsabilités pré-implémentation.**

- Conserver l'identité continue de D0 et distinguer son identité scientifique émergente de l'identifiant informatique.
- Relier les éléments d'alignement, mesures, alertes et corrections disponibles.
- Exiger la compatibilité des espaces pour les calculs vectoriels ; préserver les cas de dénominateur nul.
- Garder l'historique des incohérences, corrections et bifurcations si celles-ci sont établies.

**Issues et reprises.** Cohérence incomplète ; compétences sans alignement démontré ; mesures impossibles ; contradictions ; crises ; régulation et réorganisation. La source présente des signes opposés pour certaines corrections et des critères de fin divergents (seuil 2 versus 3) : ne pas trancher dans le code.

**Critère de preuve.** Un checkpoint avec `w8` ne contient pas automatiquement l'identité scientifique de D0.

### 7.6. Validation — Évaluation et reconnaissance par C0

**Mécanismes sources.** Activation conditionnelle de la validation, matrice collective `\mathcal M`, pondération des évaluateurs, système de légitimation `\mathcal L`, feedback multisource, éventuels rites de passage et régulation communautaire. Référence : `validation-phase.md`, manuscrit étendu ch. 20.

La condition finale exige conjointement :

\[
\mathcal M(a,t)\geq\theta_M
\quad\land\quad
\mathcal L(a,t)\geq\theta_L.
\]

**Chronologie de D0.** Sur `(3,6)`, le modèle prédit `5,48981664` (erreur absolue `0,51018336`). C'est un **résultat ML utilisable comme élément d'évaluation**, pas un verdict TL. Même avec un seul Disciple, C0 ne dispose pas nécessairement d'un ensemble d'évaluateurs satisfaisant le quorum.

**Responsabilités pré-implémentation.**

- Distinguer demande, préparation, convocation, activation effective, collecte d'évaluations, agrégation, décision, reconnaissance, légitimation et statut.
- Conserver les évaluations contradictoires et la provenance des critères/poids.
- Refuser le calcul d'une moyenne sur ensemble vide et d'un poids normalisé à dénominateur nul.
- Respecter les seuils fournis, sans en inventer ni fusionner `\mathcal M` et `\mathcal L`.

**Issues et reprises.** Quorum insuffisant ; évaluations divergentes ; demande ajournée ; réexamen ; score favorable sans légitimité suffisante ; refus ; retrait de candidature ; reconnaissance partielle. Ces issues sont des possibilités de gestion tant qu'elles ne sont pas associées à des opérateurs scientifiques définis.

**Critère de preuve.** D0 n'est pas promu Maître-relais sur la seule base de `w8` ou d'une accuracy élevée.

### 7.7. Autonomisation — Émancipation, créativité et préparation à transmettre

**Mécanismes sources.** Diminution de la dépendance envers M0, quatre niveaux d'autonomie, mécanismes internes d'autorégulation, créativité fidèle, innovations sous contraintes des invariants, préparation à la maîtrise transmissive. Référence : `empowerment-phase.md`, manuscrit étendu ch. 21.

L'indice de dépendance fait appel à un contrefactuel :

\[
\Delta_{\mathcal M}(t)=
\frac{\|X(t)-X_{\mathrm{without}}(t)\|}{\|X(t)\|}.
\]

Le contrefactuel `X_without` **n'est pas obtenu en désactivant arbitrairement les callbacks du modèle** et ne peut pas être présumé disponible. Sa construction et le cas de norme nulle constituent des frontières explicites.

**Chronologie de D0.** D0 examine un nouveau cas `(4,8)`. Le modèle actuel prédit `7,31975552`. D0 peut poursuivre l'apprentissage, remettre en question sa méthode, proposer une nouvelle représentation ou rechercher la règle `y=2x`. L'hypothèse `w=2` est une **solution candidate informatique**, non une innovation TL validée.

**Responsabilités pré-implémentation.**

- Permettre le fonctionnement de D0 sans sollicitation permanente de M0.
- Préserver la filiation tout en faisant évoluer la dépendance et les relations.
- Distinguer proposition nouvelle, examen de fidélité, reconnaissance par C0 et éventuelle contribution à la Tradition.
- Représenter la préparation à la transmission sans transformer automatiquement D0 en Maître.
- Articuler une éventuelle transition scientifique autorisée avec la propagation générationnelle et de nouveaux Disciples.

**Issues et reprises.** Autonomie partielle ; dépendance persistante ; retrait prématuré de M0 ; interruption ; innovation incorrecte ; innovation non reconnue ; Disciple autonome mais non autorisé à transmettre ; Maître-relais reconnu. La transmission secondaire du manuscrit (ch. 22) prolonge le cycle **après** l'Autonomisation, sans constituer une huitième phase parmi les sept examinées ici.

**Critère de preuve.** Capacité de `fit()` à continuer sans appel humain ≠ indice scientifique d'Autonomisation.

---

## 8. Articulation des huit objets sur l'ensemble du parcours

Les phases ne possèdent **pas** chacune une copie indépendante des huit objets. Les mêmes identités scientifiques et leurs relations persistent ou évoluent selon les transformations permises.

| Objet | Initiation / Imprégnation | Guidage / Incorporation | Intégration / Validation / Autonomisation |
|---|---|---|---|
| Message | Contenu initial, réception, exposition | Transmission et appropriation éventuelle | Cohérence du sens, fidélité et transmission possible |
| Principes | Premiers contenus, exposition | Application guidée puis exercée | Alignement, maintien/variation admissible, mobilisation autonome |
| Valeurs | Compatibilité initiale, exposition | Orientation de la Pratique et des transformations | Cohérence, appréciation collective, innovation fidèle |
| Vertus | Potentiel et dispositions observables lorsqu'établies | Développement par les mécanismes de Pratique | Stabilité, alignement, évaluation et transmission |
| Capacités | Évaluation initiale, réceptivité liée au contexte | Activation et développement selon la théorie | Mobilisation autonome et potentiel transmissif |
| Compétences | Premières observations | Développement et consolidation | Cohérence, évaluation contextualisée, autonomie |
| Pratique | Première pratique ; observation de celle de M0 | Exercices, feedback, pratique autonome, réflexion | Vérification, activité indépendante, pratique transmissive |
| Expérience vécue | Premières situations et expositions | Accumulation et intégration des situations exercées | Identité, mémoire, jugement et transmission |

**Cette table est une cartographie fonctionnelle**, pas une matrice de dérivées, une liste de seuils, ni l'affirmation que tous les objets se modifient à chaque phase. Leur existence et leur contenu peuvent apparaître de manière différée.

---

## 9. Continuité, bifurcations et issues défavorables

### 9.1. Une tentative n'est pas une entité TL

Pour suivre une admission ou une validation répétée, le produit peut avoir besoin de **dossiers, événements, tentatives, preuves et décisions**. Ce sont des structures logicielles de traçabilité ; elles ne créent pas de nouvelles entités fondamentales ni de nouveaux objets scientifiques.

### 9.2. Branches à prendre en compte

| Situation | Comportement de conception | Ce qui est interdit |
|---|---|---|
| Candidat non admis | Conserver la tentative ; nouvelle évaluation ou clôture si autorisée | Créer un Disciple admis fictif |
| Admission mutuellement refusée | Conserver les deux positions | Forcer la relation Maître–Disciple |
| Exposition sans résonance calculable | Enregistrer l'exposition et la frontière scientifique | Déclarer une Imprégnation terminée |
| Intervention non reçue | Conserver l'intervention sans effet attribué | Déduire une transformation du seul envoi |
| Pratique répétée sans progrès | Poursuivre, réguler ou réorienter si autorisé | Inventer une augmentation de Compétence |
| Incohérence d'acquis | Garder le diagnostic et les corrections fondées | Remplacer par `loss_ML` |
| Jury absent/quorum non atteint | Reporter ou maintenir non résolue la Validation | Inventer des évaluateurs |
| Reconnaissance non obtenue | Conserver acquis et décision ; permettre les suites autorisées | Effacer l'histoire du Disciple |
| M0 indisponible | Conserver D0, ses acquis, sa filiation et les possibilités de continuation | Détruire automatiquement le système |
| D0 autonome non transmetteur | Poursuivre sans promotion | Accorder automatiquement le rôle de Maître |
| Innovation non reconnue | Garder la proposition et l'examen | La convertir en Tradition validée |

### 9.3. Temporalisations simultanées

- Une activité informatique peut se poursuivre pendant l'Intégration ou la Validation.
- Un Disciple peut recevoir du Guidage tout en exerçant une Pratique progressivement autonome.
- La Communauté et les autres participants peuvent continuer leurs propres activités.
- La filiation représente une ascendance scientifique, **pas** des promotions synchronisées par générations de modèles.

Toute logique d'enchaînement doit respecter les conditions de la source, sans ajout d'une machine à états parallèle non spécifiée.

---

## 10. Responsabilités de tllib et interfaces à concevoir

### 10.1. Ne pas créer un second moteur TL

L'architecture produit vérifiée reste :

- **Noyau scientifique unique C++20** et surfaces publiques C++/Python reposant sur ce moteur ;
- **runtime explicite**, registry TLC-FC et dispatch conditionné par versions, opérandes et capacités ;
- **providers explicites** pour les calculs scientifiques ou accès externes requis ;
- **interopérabilité numérique** avec les outils usuels (ex. NumPy et DLPack lorsque appropriés), sans nouveau ndarray généraliste ;
- **tests de conformité** et diagnostic structuré, fondés sur le snapshot verrouillé `tllib-specs`.

L'état du dépôt consulté est **V1 en développement** : les fondations techniques existent, les fonctionnalités scientifiques des domaines ne sont pas annoncées comme toutes implémentées ou validées. Ce document ne suppose pas l'existence d'une API `SystemTL.run_all_phases()` ou similaire.

### 10.2. Responsabilités à raccorder à l'existant

| Responsabilité | Entrées/relations pertinentes | Sorties/effets à distinguer |
|---|---|---|
| Constitution | Mission, Problème, ressources, rôles, Capacités, conditions | Système structuré, non preuve d'apprentissage |
| Entités et relations | M0, D0, C0 ; rôles et temporalité | Relations scientifiques et filiation autorisées |
| Huit objets | Identités, contenus, relations et transformations applicables | Acquis et effets TL, sans typage réducteur ML |
| Exécution des phases | Opération TLC-FC, version, contexte, opérandes et provider requis | Résultat exécutable / structure / frontière non résolue |
| Apprentissage externe | Données, modèle, algorithme, métriques | États et résultats ML, distincts des états TL |
| Suivi historique | Opération, phase concernée, acteurs, objet, ressource, source, temps | Traçabilité et continuation sans nouvelle science |
| Évaluation / reconnaissance | Preuves, jugements, communauté, conditions | Évaluation, légitimité et rôle distincts |
| Continuation | Ressources et relations nouvelles, décisions scientifiques | Nouvelles activités, relais, cohortes, branches et générations |

**Remarque :** cette table attribue des responsabilités, **pas des classes, modules ou méthodes déjà décidés**. Réutiliser les types `Result/Error`, `ExecutionContext`, registry, providers, conventions et tests réellement existants.

### 10.3. Enregistrement de provenance : proposition de design

Pour chaque opération examinée dans le prototype, conserver au minimum, lorsque disponibles :

- référence du système et du Disciple D0, de M0/C0 s'ils interviennent ;
- mécanisme scientifique et TLC-FC de provenance, phase(s) concernée(s) ;
- objets mobilisés et références à leurs états scientifiques, sans les réduire à des tags ;
- identifiant de ressource informatique et version d'état ML, s'ils existent ;
- contexte d'exécution, temporalité et paramètres réellement fournis ;
- mode de support (`structural_only`, `conditionally_executable`, etc.) et providers explicitement résolus ;
- résultat calculé, statut de disponibilité, diagnostic structuré et preuve/test correspondant ;
- origine des décisions : Maître, Disciple, Communauté, provider ou calcul.

Aucun champ proposé ici ne constitue une nouvelle dimension scientifique obligatoire. **Le schéma exact devra être décidé à partir des formats partagés existants**, pas dupliqué dans chaque domaine.

### 10.4. Relation à l'apprentissage IA classique : adaptateurs, pas substitution

L'application reste propriétaire du problème métier et de sa mécanique ML. L'interface avec `tllib` doit permettre de rattacher, selon le cas :

- les données présentées et observations réellement effectuées ;
- les opérations d'entraînement, d'inférence et d'évaluation ;
- les changements d'état des ressources numériques ;
- les interventions de M0 et activités effectives de D0 ;
- les résultats scientifiques TL lorsque les mécanismes sont disponibles.

Exemple conceptuel, **non API** :

```text
application ML : observe (2,4) -> predict 0,4 -> SGD -> w=0,92
              |                 |                |
              +---- preuves/ressources utilisables par une activité TL

système TL    : M0 intervient -> D0 reçoit -> feedback/trajet scientifique éventuel
              |                               |
              +---- opérateurs TLC-FC et providers applicables

runtime       : confronte contrats + opérandes + capacité + provenance
              -> résultat conforme OU frontière déclarée
```

**Ne pas réaliser un couplage implicite** du type `loss.backward()` = Guidage, `optimizer.step()` = Incorporation, `validate()` = Validation communautaire ou `model.eval()` = Intégration.

### 10.5. Continuer après la septième phase

L'Autonomisation n'arrête pas le système TL. Selon les conditions applicables : D0 peut poursuivre une Mission ouverte, découvrir une solution, produire des contributions, aider un autre participant, recevoir un nouveau Guidage ou devenir Maître-relais. Une nouvelle Cohorte et une génération de filiation peuvent se former. Cela constitue une **continuation interne du système**, à distinguer de la réutilisation externe d'une Tradition par un développeur et de la reprise technique d'un système déjà créé.

---

## 11. Frontières des contrats et de l'exécution scientifique

### 11.1. Règle commune

Les handoffs de `tllib-specs` distinguent des mécanismes **exécutables**, **conditionnellement exécutables** et **structurels seulement**. La présence d'une formule ou d'un descripteur ne rend pas automatiquement toute la phase exécutable. Les packages mentionnés ci-dessous sont rattachés au snapshot `07439bab...` de `specs.lock.json` ; consulter leurs `contract.json`, `manifest.json`, `acceptance.json`, `traceability.json` avant toute implémentation.

### 11.2. Points d'appui vérifiés

| Phase | Contrats TLC-FC vérifiés ou clés | Frontières à respecter |
|---|---|---|
| Initiation | `maths/34-transmission-lifecycle/initiation-phase.md` et handoffs correspondants | Agrégations/dénominations scientifiques incomplètes ; admission seulement si conditions prouvées |
| Imprégnation | `...-043` dynamique des poids de résonance (**structurel**) ; `...-044` activation d'une bande (**conditionnel**) ; `...-052` garde sélective/toutes bandes (**structurel**) | Ne pas fournir `θ_act`, `I_k` ou les paramètres de résonance manquants |
| Guidage | `...-053` famille de `Φ` (**structurel**) ; `...-061` feedback/noyau causal (**structurel**, provider requis) ; `...-067` conditions de sortie (**structurel**) | Ne pas inventer le solveur d'argmin, le noyau causal ni les seuils |
| Incorporation | `...-068` combinaison de Pratiques (**conditionnel**) ; `...-070` indice d'autonomie (**conditionnel**) ; `...-073` dynamique des Vertus (**structurel**) ; `...-079` sortie (**structurel**) | Compatibilité des représentations, domaines définis, coefficient `λ(t)` fourni |
| Intégration | `...-081` générateur identitaire ; `...-085` garde de gradient ; `...-086` garde de cohérence ; `...-089` divergences de seuil (**structurels**) | Ne pas corriger arbitrairement les signes, espaces ou critères de sortie |
| Validation | `...-091` matrice (**conditionnel**) ; `...-094` poids normalisés (**conditionnel**) ; `...-098` prédicat final (**conditionnel**) | Évaluateurs non vides, dénominateurs valides, seuils M et L fournis séparément |
| Autonomisation | `...-100` garde contrefactuelle (**structurel**) ; `...-103` indice créatif (**conditionnel**) ; `...-107` préparation transmissive (**structurel**) ; `...-108` relais générationnel (**structurel**) | Ne pas construire `X_without`, le noyau invariant ou la promotion de rôle par défaut |

Les abréviations `...-NNN` renvoient à `TLC-FC-34-TRANSMISSION-LIFECYCLE-NNN` ; les statuts ci-dessus concernent **ces fonctionnalités**, non une certification de toute la phase.

### 11.3. Ambiguïtés scientifiques conservées, non corrigées

- Imprégnation : résonance sélective versus condition finale portant sur toutes les bandes.
- Guidage : typages `D,C` et `X,c`, existence de l'argmin, combinaison dite convexe, critère de convergence conditionnel.
- Incorporation : domaines de l'indice d'autonomie, valeur terminale de `λ(t)`, critère portant sur `max_i C_i`, opérateur maïeutique.
- Intégration : singularité par inverse de distance, signes contradictoires de gradients correctifs, compatibilité des espaces, seuil 2 versus seuil 3.
- Validation : ensemble d'évaluateurs vide, dénominateur de pondération nul, indicateur de convocation non garanti binaire, plages de reconnaissance/légitimité.
- Autonomisation : état contrefactuel, norme nulle, distinction innovation/état transformé, propriétés de bifurcation non dérivées intégralement.

**Ne pas modifier `tllib-specs` ni les manuscrits pour livrer cet exemple.** Une anomalie précise peut être signalée via la procédure appropriée ; elle n'autorise pas un comportement ad hoc dans `tllib`.

---

## 12. Plan de conformité et d'expérimentation

### 12.1. Tests informatiques classiques, déterministes

À exécuter sur la ressource de régression indépendamment de TL :

1. Avec `w0=0`, `(1,2)`, `(2,4)` alternés huit fois et `η=0,1`, obtenir la série de paramètres du §5.2.
2. Vérifier `w8=1,82993888` avec une tolérance numérique déclarée pour le backend utilisé.
3. Vérifier `ŷ(3)=5,48981664` et l'erreur absolue `0,51018336`.
4. Vérifier que l'observation de contrôle `(3,6)` n'est pas introduite implicitement dans l'entraînement.
5. Vérifier les résultats distincts des mises à jour et des seules prédictions.

### 12.2. Tests de structure et de relations TL

- Identité de D0 préservée entre candidature, éventuelle admission, sept phases, interruption et continuation.
- M0 et C0 conservent des rôles distincts ; aucune ressource ML ne devient automatiquement Maître/Disciple/Communauté.
- Les huit objets restent identifiables et leurs fonctions ne sont pas remplacées par des hyperparamètres.
- Plusieurs tentatives d'Initiation/Validation peuvent être conservées sans effacer les précédentes.
- Les phases peuvent se recouvrir et évoluer selon les conditions autorisées ; aucune synchronisation obligatoire par cohortes/générations.
- Les nouveaux contenus et acquis peuvent apparaître après la constitution initiale.

### 12.3. Tests des frontières d'exécution scientifiques

- Un descripteur `structural_only` n'annonce pas un opérateur scientifique exécuté.
- Un contrat conditionnel sans opérande/provider requis produit un résultat indisponible ou une erreur structurée conforme, sans valeur fictive.
- Les dépendances de mémoire, résonance, cohérence, légitimation et autonomie ne sont pas remplacées par des variables ML homonymes.
- Les divisions par zéro, représentations incompatibles et conditions non résolues sont traitées selon les acceptations publiées.
- Le prédicat de Validation n'est pas réduit à une performance ML ; les conditions M et L restent conjointes.
- La promotion Maître-relais ne découle pas de la seule fin d'un entraînement ou d'un signal logiciel arbitraire.
- La parité C++/Python est vérifiée pour les opérations réellement exposées, sans seconde logique scientifique Python.

### 12.4. Tests de parcours et cas défavorables

| Scénario | Résultat acceptable à démontrer |
|---|---|
| D0 non admis | Candidat conservé ; aucune phase aval déclarée accomplie fictivement |
| D0 admis, résonance indisponible | Expositions conservées ; statut scientifique non usurpé |
| M0 intervient, D0 ne reçoit pas | Aucune transformation inférée de l'envoi seul |
| D0 termine SGD, états TL incomplets | Résultat ML conservé ; pas de Validation/Autonomisation automatique |
| Jury insuffisant | Aucun calcul collectif fictif ; données de convocation conservées |
| D0 autonome sans autorisation de transmettre | Continuation possible sans Maître-relais |
| M0 disparaît | D0 et ses ressources persistent ; liens historiques conservés |
| D0 propose une variation de modèle | Proposition traçable ; Tradition non altérée sans examen autorisé |

### 12.5. Critères de livraison du prototype

Le prototype sera considéré comme **techniquement utile**, et non scientifiquement complet, s'il peut :

1. constituer le cas M0–D0–C0 et relier la ressource ML sans confondre les rôles ;
2. reproduire la trace SGD ;
3. lier les opérations/événements aux sept phases sans imposer une progression scientifique fictive ;
4. représenter les huit objets et leurs relations selon les contrats structurels concernés ;
5. exécuter seulement les TLC-FC effectivement disponibles avec préconditions remplies ;
6. conserver et rapporter les opérations non disponibles et les issues défavorables ;
7. préserver la possibilité de continuer D0 au-delà de l'Autonomisation.

Il ne sera déclaré **parcours scientifique TL intégralement exécuté** que si tous les mécanismes nécessaires sont devenus exécutables dans les conditions scientifiques et logicielles requises et si les preuves correspondantes existent.

---

## 13. Décisions retenues, non-décisions et prochains travaux

### 13.1. Décisions de conception retenues

1. Un système TL minimal peut être constitué avec **M0, D0 candidat et C0**, puis évoluer sans recréation artificielle par phase.
2. Les huit objets scientifiques **traversent les sept phases**, conservent leurs identités et leurs relations.
3. La Pratique est un objet fondamental ; le Guidage et l'Incorporation sont des phases. Les expressions de combinaison portent sur des **contributions à la Pratique**, pas sur une somme ontologique phase+objet.
4. L'apprentissage IA classique reste complet, reproductible et éventuellement indépendant dans ses opérations numériques ; TL lui apporte **un système scientifique distinct** de transmission, transformation, mémoire, régulation et continuation, sans remplacement de l'optimiseur.
5. Les états scientifiques TL et les états de ressources ML sont reliés par des références de provenance, **pas assimilés**.
6. Les échecs, reprises, refus, reports, innovations non reconnues et continuations doivent être représentables.
7. La Tradition est distincte d'un modèle obtenu ; la formation de nouvelles Traditions/contributions ne se déduit pas d'un checkpoint.
8. L'architecture existante C++20/runtime/providers/API/interop/conformité reste l'autorité produit ; aucun second moteur n'est justifié par ce document.

### 13.2. Non-décisions explicites

- Aucun nouveau type scientifique, neuvième objet ou quatrième entité n'est proposé.
- Aucun seuil, métrique, opérateur, état terminal scientifique ou équation supplémentaire n'est défini.
- Aucune API publique, classe C++, signature Python, format de sérialisation ou nouveau backend n'est arrêté ici.
- Aucun provider implicite n'est introduit ; aucun `autograd`/SGD ne se substitue par défaut à un mécanisme TL.
- Aucun découpage rigide ne remplace le pipeline/automate partiellement spécifiés.
- Aucune modification du manuscrit ou de `tllib-specs` n'est envisagée pour cette activité ordinaire de développement.

### 13.3. Prochains travaux opérationnels recommandés

1. Inventorier **à l'échelle des fonctionnalités nécessaires à ce seul cas** les headers, interfaces runtime, providers, types communs, bindings et tests réels de `tllib` ; ne pas refaire un audit global des 36 domaines.
2. Établir la matrice `cas D0 -> TLC-FC -> acceptation -> exécutable/conditionnel/structurel -> preuve`, selon le snapshot épinglé.
3. Implémenter d'abord le **raccordement sûr** d'un cas de régression externe et d'un système TL structurellement constitué, sans simuler les mécanismes non exécutables.
4. Ajouter les tests de trace ML, de parité C++/Python, de non-confusion des rôles et de frontières scientifiques.
5. Développer progressivement les opérations TLC-FC disponibles, leurs providers explicites et leurs acceptations, sans réécrire la théorie.
6. Étendre ensuite l'expérience à d'autres tâches (classification, segmentation, génération, décision, simulation) **pour éprouver les invariants universels**, sans redéfinir TL autour de la régression.

---

## 14. Références

### 14.1. Manuscrits du projet

- **`Tradition Learning - main.pdf`**, *Tradition Learning: A Framework for Low-Data Environments and Bias Mitigation*, édition scientifique 2025, 148 pages : fondements de la théorie, entités, objets et relations.
- **`TraditionLearning.pdf`**, même projet, version étendue de 748 pages : chapitre 14 (pipeline), chapitre 15 (Initiation), 16 (Imprégnation), 17 (Guidage), 18 (Incorporation), 19 (Intégration), 20 (Validation), 21 (Autonomisation), 22 (transmission secondaire).

### 14.2. Sources normatives épinglées

Base : [`tllib-specs` à la révision 07439bab...](https://github.com/Tradition-Learning-Community/tllib-specs/tree/07439babd59c657354e3200ed24c55e2e3eeb72c).

- [`operational-pipeline.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/operational-pipeline.md)
- [`initiation-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/initiation-phase.md)
- [`impregnation-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/impregnation-phase.md)
- [`guidance-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/guidance-phase.md)
- [`incorporation-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/incorporation-phase.md)
- [`integration-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/integration-phase.md)
- [`validation-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/validation-phase.md)
- [`empowerment-phase.md`](https://github.com/Tradition-Learning-Community/tllib-specs/blob/07439babd59c657354e3200ed24c55e2e3eeb72c/maths/34-transmission-lifecycle/empowerment-phase.md)
- [`handoff/features/`](https://github.com/Tradition-Learning-Community/tllib-specs/tree/07439babd59c657354e3200ed24c55e2e3eeb72c/handoff/features) : `manifest.json`, `contract.json`, `acceptance.json`, `traceability.json` par TLC-FC.

### 14.3. Documentation du produit

- [`tllib/README.md`](https://github.com/Tradition-Learning-Community/tllib/blob/main/README.md)
- [`tllib/docs/v1/PRODUCT-CONTRACT.md`](https://github.com/Tradition-Learning-Community/tllib/blob/main/docs/v1/PRODUCT-CONTRACT.md)
- [`tllib/docs/v1/ARCHITECTURE.md`](https://github.com/Tradition-Learning-Community/tllib/blob/main/docs/v1/ARCHITECTURE.md)
- [`tllib/docs/v1/FOUNDATION-BEFORE-DOMAINS.md`](https://github.com/Tradition-Learning-Community/tllib/blob/main/docs/v1/FOUNDATION-BEFORE-DOMAINS.md)
- [`tllib/specs.lock.json`](https://github.com/Tradition-Learning-Community/tllib/blob/main/specs.lock.json)

**Règle de maintenance :** après évolution de `specs.lock.json`, revalider les références, les statuts d'exécution et la matrice de conformité de ce document avant tout usage comme base d'implémentation.