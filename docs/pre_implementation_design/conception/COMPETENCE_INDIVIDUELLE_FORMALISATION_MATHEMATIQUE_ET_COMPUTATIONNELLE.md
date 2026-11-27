# Compétence individuelle — formalisation mathématique et computationnelle de travail

> **Statut :** étude de conception pré-implémentation, **non normative**, à confronter aux contrats applicables avant toute implémentation.
> **Date :** 27 novembre 2026.
> **Objet TL :** Compétence, considérée **individuellement** chez une unité d'apprentissage.
> **Portée :** nature de la maîtrise actualisée, représentation candidate, manifestations, cinq régressions et limites d'attribution. **Aucune API ni procédure de maturation n'est décidée.**
> **Vérification :** sources scientifiques consultées et calculs mathématiques d'illustration ; **aucune compétence TL démontrée par exécution, aucun test de conformité ni changement de code**.

## 1. Sources et statut

1. Manuscrit *Tradition Learning - main.pdf*, § 4.2.6 (« Competencies — Operational and Effective Dimension »), page imprimée 101 : aptitudes, méthodes et maîtrises concrètes permettant d'agir efficacement.
2. Manuscrit détaillé *TraditionLearning.pdf*, § 1.43.1 (« Definition and Ontological Status of Competencies », définition 1.48), pages imprimées 177–178 : Capacité actualisée et démontrable mobilisant des ressources intégrées ; actualisation, contextualisation, intégration, évolutivité, démontrabilité, reconnaissance.
3. [Mathématiques des Compétences](../../../maths/12-competencies/competencies.md), source scientifique dans ce dépôt ; [Mathématiques des Capacités](../../../maths/11-capacities/capacities.md), pour l'antériorité du potentiel et les conditions d'actualisation.
4. [Capacité individuelle — formalisation computationnelle](CAPACITE_INDIVIDUELLE_FORMALISATION_MATHEMATIQUE_ET_COMPUTATIONNELLE.md) ; [Pratique et Expérience vécue](PRATIQUE_ET_EXPERIENCE_VECUE_FORMALISATION_COMPUTATIONNELLE.md).

**Autorité :** les définitions, conditions d'existence, structures mathématiques et procédures de reconnaissance issues du manuscrit et des contrats existants ne sont **ni remplacées ni amendées**. Les constructions \(\Phi_c\), \(B_{D,\omega}\) et la caractérisation ci-dessous ne sont que des **outils de conception non normatifs**.

## 2. Acquis scientifiques : nature de la Compétence

La théorie TL définit la Compétence comme **une Capacité actualisée et démontrable** ; elle ne s'identifie ni à une tâche, ni à un modèle informatique, ni à un score. La maîtrise se manifeste dans l'action, avec une contextualisation et une intégration qui peuvent être évaluées et reconnues.

L'espace théorique est décrit par :

\[
\mathcal C_a=
\mathcal C_{\mathrm{tech}}\times
\mathcal C_{\mathrm{cog}}\times
\mathcal C_{\mathrm{soc}}\times
\mathcal C_{\mathrm{adapt}}\times
\mathcal C_{\mathrm{meta}}
\subset\mathbb R^m.
\]

Il s'agit de **la structure théorique globale**, pas de l'écriture d'une compétence atomique. La théorie expose également une relation d'actualisation entre Capacités et Compétences, ainsi que des conditions de démontrabilité et de reconnaissance que cette note ne saurait court-circuiter.

Une Compétence est **portée par D0**, non par sa Mission, son dataset, une famille de modèles ou un solveur considéré isolément. Elle peut persister même lorsque D0 n'exécute aucune action, dès lors que sa maîtrise intégrée ne s'est pas perdue ; son attribution requiert cependant des éléments de manifestation et de validation.

## 3. Nature individuelle et caractérisation mathématique proposée

### 3.1. Nature

> **Une Compétence individuelle est une maîtrise opératoire actualisée et intégrée d'une unité d'apprentissage, dont la propriété précise et la portée peuvent être caractérisées par des transformations effectivement mobilisées et leurs manifestations démontrables.**

Une **propriété atomique** désigne ici une aptitude délimitée et examinable séparément, sans supposer qu'elle est forcément une seule variable, qu'elle s'applique à toutes les tâches, ni qu'elle constitue une nouvelle catégorie scientifique TL. Une même unité peut manifester plusieurs Compétences ; une Pratique peut en solliciter plusieurs.

### 3.2. Écriture de caractérisation (proposition de conception, NON normative)

Soient :

- \(D\) : unité d'apprentissage porteuse (D0) ;
- \(c_a\) : compétence individuelle étudiée ;
- \(\omega\in\Omega_c\) : conditions pertinentes de manifestation ;
- \(B_{D,\omega}\) : comportement ou transformation **effectivement mobilisé** par l'unité sous ces conditions ;
- \(\Phi_c(B,\omega)\) : propriété mathématique spécifique (égalité, invariance, contrainte, ordre, relation probabiliste, etc.) à examiner.

Une **manifestation locale conforme à la propriété** peut être caractérisée par :

\[
\boxed{
\operatorname{Manifestation}_{D,c_a}(\omega)
\quad\Longleftrightarrow\quad
\Phi_c(B_{D,\omega},\omega).
}
\tag{C-A}
\]

Cette expression **ne transforme pas automatiquement un succès en Compétence TL établie**. Elle caractérise une manifestation. La maîtrise effective doit être établie avec une portée explicite, des observations ou preuves adaptées, l'intégration et les conditions scientifiques de validation applicables, notamment la reconnaissance prévue par la théorie.

Un comportement \(B\) n'est pas toujours une fonction de prédiction \(X\to Y\). Il peut être une transformation d'état, une procédure interactive, une relation, une politique de décision ou une autre réalisation adaptée au domaine.

### 3.3. Portée et maîtrise : les observations ne sont pas l'objet

Notons \(\Omega_c^{\mathrm{examinée}}\subseteq\Omega_c\) la portée effectivement examinée. Les manifestations permettent d'établir ou de contredire \(\Phi_c\) **dans cette portée**, mais une poignée de cas ne suffit pas à prouver sa validité sur toutes les situations possibles.

Un écart entre une manifestation et l'idéal spécifique de \(\Phi_c\) peut être quantifié avec des métriques classiques **lorsqu'elles sont pertinentes**. Ces métriques servent à évaluer une manifestation : elles ne définissent pas à elles seules la Compétence, n'imposent pas une note de 0 à 100 et ne valent pas nécessairement dans toutes les familles IA.

Un algorithme tiers peut produire une sortie conforme sans que D0 maîtrise le choix, l'adaptation ou l'exploitation de la méthode. **La présence d'un mécanisme dans une Pratique ne justifie donc pas, à elle seule, l'attribution d'une Compétence générale à D0.**

## 4. Cinq exercices : une unité D0, plusieurs Compétences candidates

Les relations suivantes ont été **résolues mathématiquement** dans l'étude ; l'exécution par une unité TL demeure **supposée**, non mesurée.

| Pratique | Relation de référence | Manifestation de compétence candidate | Ce que l'exercice ne démontre pas |
| --- | --- | --- | --- |
| P1 : prix | \(f(x)=2x+1\) | C1 : préserver l'ordre pertinent lors de l'exploitation de la relation | Maîtrise sur des données bruitées ou choix autonome d'une représentation |
| P2 : quantité quadratique | \(f(x)=3x^2\), \(x\ge0\) | C2 : restituer la courbure attendue | Maîtrise de toute non-linéarité |
| P3 : coût distance/charge | \(f(d,q)=5+2d+3q\) | C3 : distinguer des contributions additives | Capacité à reconnaître toutes les interactions réelles |
| P4 : valeur aberrante | \(f(x)=2x+1\), observation \((5,50)\) | C4 : préserver la relation malgré une perturbation non pertinente | Robustesse universelle ou choix autonome d'algorithme |
| P5 : consommation par régimes | \(f(x)=2\) si \(x<5\), sinon \(8\) | C5 : restituer une rupture de régime | Détermination exacte d'un seuil à partir des seules observations disponibles |

Il s'agit d'**aptitudes candidates distinctes**, sans obligation de les fusionner sous « capacité à apprendre des relations ». Les cinq algorithmes et les schèmes possibles ne définissent pas ces Compétences ; ils sont des moyens ou acquis impliqués dans leurs manifestations.

Quelques lois de caractérisation concrètes, **propres aux exercices** :

**C1 — ordre pertinent**, lorsque l'ordre d'entrée implique un ordre de sortie :

\[
x_1<x_2\quad\Rightarrow\quad B(x_1)\le B(x_2).
\]

Dans P2 cela est examiné sur \(x\ge0\) ; dans P3 il faut tenir l'autre variable fixe. L'ordre ne doit pas être imposé là où la relation attendue est décroissante ou non monotone.

**C2 — courbure de P2**, pour les pas admissibles \(h\) :

\[
B(x+h)-2B(x)+B(x-h)=6h^2.
\]

Le second membre exprime la référence quadratique \(3x^2\), et non une valeur universelle définissant la Compétence.

**C3 — contributions additives de P3** :

\[
B(1,1)-B(1,0)-B(0,1)+B(0,0)=0.
\]

**C5 — rupture de P5** : la différence attendue entre les régimes est \(8-2=6\). Le seuil exact **n'est pas déductible** des seuls points fournis ; \(5\) est une séparation illustrative.

## 5. Exemple intégral : Compétence C4, résistance à une observation aberrante

### 5.1. Observations

Ensemble ordinaire :

\[
O=\{(1,3),(2,5),(3,7),(4,9),(5,11)\}.
\]

Ensemble perturbé :

\[
O'=\{(1,3),(2,5),(3,7),(4,9),(5,50)\}.
\]

On **suppose ici** que la dernière observation de \(O'\) est aberrante et ne correspond pas à un changement réel du phénomène. Dans d'autres circonstances, une telle valeur pourrait être légitime et ne devrait pas être automatiquement ignorée.

Soit \(L_D\) le comportement d'apprentissage effectivement mobilisé par D0, associant aux observations une relation estimée.

La propriété atomique examinée est :

\[
\Phi_{C4}(L_D;O,O',X):
\quad L_D(O')(x)=L_D(O)(x)\quad
\text{pour les }x\in X\text{ pertinents}.
\]

Un **résidu de manifestation**, calculable sans inspecter tous les schèmes internes, est :

\[
\Delta_{C4}(x)=L_D(O')(x)-L_D(O)(x).
\]

La référence idéale sur cette perturbation particulière est \(\Delta_{C4}(x)=0\). Cela ne fixe ni seuil TL obligatoire, ni exigence d'ignorer une véritable nouvelle information.

### 5.2. Calcul des résultats

Sur les points ordinaires, la relation est \(L_D(O)(x)=2x+1\), si D0 l'a effectivement obtenue.

Pour les moindres carrés sur \(O'\), les coefficients calculés sont :

\[
L_{\mathrm{OLS}}(O')(x)=9{,}8x-14{,}6.
\]

La prédiction à \(x=6\) vaut donc :

\[
L_{\mathrm{OLS}}(O')(6)=44{,}2.
\]

Avec Theil–Sen, les pentes entre paires d'observations puis leur médiane donnent la pente \(2\), et la médiane des intercepts donne \(1\) dans cet exercice :

\[
L_{\mathrm{TS}}(O')(x)=2x+1,\qquad
L_{\mathrm{TS}}(O')(6)=13.
\]

| Relation effectivement obtenue si D0 la mobilise | Résultat \(x=6\) | Résidu par rapport à la relation ordinaire |
| --- | ---: | ---: |
| Référence \(2x+1\) | 13 | 0 |
| Moindres carrés sur \(O'\) | 44,2 | +31,2 |
| Theil–Sen sur \(O'\) | 13 | 0 |

**Interprétation :** Theil–Sen fournit une manifestation conforme à la propriété C4 dans ce cas précis. Cela **n'établit pas à lui seul une Compétence TL de D0** ; il faut examiner l'actualisation, l'intégration, l'attribution à l'unité, la portée de la maîtrise et les modalités de reconnaissance prévues par les sources scientifiques.

Si D0 reçoit **par prescription** Theil–Sen pour P4, nous observons le comportement du système équipé de cette Pratique. Nous ne pouvons pas en déduire que D0 sait lui-même identifier une valeur aberrante ou choisir une méthode robuste. Ce sont des aptitudes distinctes.

## 6. Relation à la Capacité, aux schèmes et aux autres objets

- **Capacité :** potentiel conditionnellement réalisable ; une Compétence est une maîtrise actualisée et démontrable, pas un simple potentiel. Voir [Capacité individuelle](CAPACITE_INDIVIDUELLE_FORMALISATION_MATHEMATIQUE_ET_COMPUTATIONNELLE.md).
- **Pratique :** moyen d'apprentissage configurable et réutilisable qui peut solliciter plusieurs Compétences et permettre leurs manifestations. L'identité de la Compétence ne se réduit ni au critère, ni à l'algorithme, ni au mécanisme de modification.
- **Expérience vécue :** contenus représentationnels internes acquis ou modifiés et conservés de manière intégrée. Une Compétence peut contribuer à acquérir, modifier ou exploiter des schèmes, mais elle n'est pas un schème, ni une liste de schèmes.
- **Mission :** peut mobiliser des Compétences sans leur imposer une identité ou une forme particulière.
- **Maître et Disciple :** les manifestations de M0 peuvent servir de référence à D0 ; ce dernier peut développer une maîtrise différente, potentiellement supérieure, sans copie de l'état interne du Maître.

**La généralisation, les biais, le sous-apprentissage et le surapprentissage** sont des objets d'évaluation classique qui peuvent fournir des mesures utiles **selon** la Compétence. Une seule Compétence n'est pas tenue de résoudre tous ces problèmes. Son idéal de maîtrise peut rester ouvert et jamais atteint absolument ; aucune échelle universelle 0–100 ne s'ensuit.

## 7. Décisions de conception, limites et suite autorisée

**Retenu :** une Compétence individuelle est une propriété opératoire de maîtrise actualisée de D0 ; elle peut être examinée au moyen d'une propriété \(\Phi_c\), de comportements effectivement mobilisés et d'une portée de démonstration.

**Non conclu :** qu'une réussite isolée constitue une Compétence validée ; qu'une méthode externe donne automatiquement la Compétence à D0 ; que les cinq exemples établissent des compétences TL ; que le choix d'un algorithme ou une bonne prédiction prouve une maîtrise générale indépendante de la Pratique.

**Avant l'implémentation :** vérifier les contraintes exactes de reconnaissance, d'actualisation, de domaine de validité et de conformité dans \`maths/\`, \`registry/\` et \`handoff/\`. Les espaces globaux \(\mathcal C_a\) et \(\mathcal C_p\) ont des représentations ambiantes différentes dans les sources ; **aucune application supplémentaire entre ces espaces n'est postulée ici**. Le statut des contrats peut être structurel ou conditionnellement exécutable : une déclaration ne vaut pas démonstration scientifique.

Cette note ne modifie ni le manuscrit, ni les mathématiques publiées, ni les contrats, ni le code de \`tllib\`.
