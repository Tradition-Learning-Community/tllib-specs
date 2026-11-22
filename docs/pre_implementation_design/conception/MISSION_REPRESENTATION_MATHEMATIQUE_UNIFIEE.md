# Mission TL — représentation mathématique unifiée, ouverte et évolutive

**Statut : étude de conception mathématique, non normative.**  
**Objet :** établir une représentation mathématique unique de la Mission, primaire et indépendante des participants, des ressources, des sources d'apprentissage, des modèles et des travaux particuliers.  
**Autorité :** le manuscrit scientifique *Tradition Learning*, puis les mathématiques et les contrats publiés dans `tllib-specs`. Ce document ne modifie ni la théorie ni les contrats normatifs.

## 1. Mission, Horizon et Périmètre

La Mission est une **entreprise orientée sur une population de référence**. Elle comporte deux aspects indissociables :

- **Entreprise orientée, ou Horizon (E)** : idéal poursuivi, éventuellement inaccessible ou encore partiellement compris ; ses propriétés et orientations peuvent être progressivement précisées ou corrigées.
- **Portée, ou Périmètre (P)** : population de référence des situations concernées par cet idéal, au sens statistique étendu aux situations possibles, futures ou non observées.

La définition conceptuelle demeure :

\[
\operatorname{Mission}=(E,P).
\]

La Mission ne se confond ni avec une solution, ni avec une famille particulière de fonctions, ni avec un ensemble exhaustif de réalisations. Une seule Mission peut admettre plusieurs formes et plusieurs réalisations différentes. Son existence n'exige pas qu'une solution soit connue.

**Primauté et indépendance :** ni Maître, ni Disciple, ni Communauté, ni les huit objets fondamentaux, ni les onze éléments d'un travail d'apprentissage ne constituent la définition mathématique de la Mission. Ces éléments peuvent être orientés par elle sans être requis pour son existence.

## 2. Objet mathématique unifié

Nous utilisons les notions existantes de **langage formel typé**, de **théorie mathématique** et de **conséquence logique**. À un état de compréhension \(t\), la Mission dispose de la formulation :

\[
\boxed{
\mathfrak m_t =
\left\langle
\mathscr L_t,\;
\operatorname{Cn}_{\mathscr L_t}
\bigl(\mathscr A_t^{P}\cup\mathscr A_t^{E}\bigr)
\right\rangle.
}
\tag{M1}
\]

| Notation | Interprétation |
|---|---|
| \(\mathfrak m_t\) | Formulation mathématique de la Mission à l'état de compréhension \(t\) |
| \(\mathscr L_t\) | Langage typé : sortes, fonctions, relations, variables et constructions nécessaires au domaine |
| \(\mathscr A_t^{P}\) | Énoncés caractérisant et délimitant la population de référence |
| \(\mathscr A_t^{E}\) | Énoncés caractérisant les propriétés et orientations actuellement connues de l'idéal |
| \(\operatorname{Cn}_{\mathscr L_t}\) | Fermeture par conséquence logique dans le système de déduction retenu |

Cette expression est **un seul objet mathématique** : les énoncés relatifs à P et à E appartiennent à une théorie commune et peuvent intervenir ensemble dans les déductions. Leur séparation d'origine conserve leur interprétation conceptuelle ; elle ne crée pas deux systèmes mathématiques indépendants.

L'opérateur \(\operatorname{Cn}\) définit un ensemble de conséquences. Il ne garantit pas que toutes ces conséquences soient calculables par un algorithme effectif. La calculabilité dépend du fragment logique et des méthodes disponibles.

La notation \(\mathfrak m_t\) représente **la formulation accessible de la Mission**, et non son identité intégrale. La Mission poursuivie peut dépasser ce qui est déjà explicité dans \(\mathscr A_t^{P}\) et \(\mathscr A_t^{E}\).

### 2.1. Incomplétude et indétermination

Pour une proposition bien formée \(\varphi\), si la théorie est cohérente et que la conséquence est entendue au sens classique :

\[
\begin{aligned}
\mathfrak m_t\models\varphi &\quad\text{: établie},\\
\mathfrak m_t\models\neg\varphi &\quad\text{: réfutée},\\
\mathfrak m_t\not\models\varphi\ \land\ \mathfrak m_t\not\models\neg\varphi
&\quad\text{: indéterminée}.
\end{aligned}
\tag{M2}
\]

Ce sont trois **statuts de connaissance**, et non l'adoption obligatoire d'une logique à trois valeurs. « Non établi » ne signifie pas « faux ». Si des axiomes contradictoires sont présents, la logique classique peut entraîner une déduction triviale de toute proposition : la cohérence doit donc être examinée.

Les propositions concernant **l'idéal** ne doivent pas être prises pour des faits déjà réalisés. Un langage adapté peut exprimer des propriétés recherchées, des relations d'admissibilité ou des orientations, sans affirmer leur satisfaction actuelle.

### 2.2. Population de référence

La population peut être exprimée par des énoncés de domaine, par exemple un prédicat \(P(s)\), avec des unités statistiques, variables, domaines de valeurs et relations pertinentes. Une énumération exhaustive n'est pas nécessaire. Les propriétés peuvent demeurer inconnues ou partiellement spécifiées.

Une source d'apprentissage est un ensemble d'observations disponibles ; elle ne définit pas automatiquement P. Le dataset, ses variables effectivement mesurées et ses distributions empiriques ne font pas partie des constituants de (M1).

## 3. Mission, modèles mathématiques et réalisations

Lorsque sa sémantique est définie, la théorie admet un ensemble de modèles mathématiques :

\[
\operatorname{Mod}(\mathfrak m_t).
\tag{M3}
\]

Un *modèle mathématique* est ici une interprétation satisfaisant les énoncés ; ce n'est pas automatiquement un modèle d'IA. Des modèles compatibles avec des propriétés encore incomplètes ne sont pas automatiquement des réalisations véritables ou suffisantes de l'entreprise.

Nous distinguons strictement :

\[
\boxed{
\text{Mission}
\ne \mathfrak m_t
\ne \operatorname{Mod}(\mathfrak m_t)
\ne \text{réalisation particulière}.
}
\tag{M4}
\]

La Mission est l'entreprise poursuivie ; \(\mathfrak m_t\) est sa formulation actuelle ; \(\operatorname{Mod}(\mathfrak m_t)\) représente ses interprétations mathématiques compatibles ; une réalisation particulière est un résultat effectivement déterminé ou accompli.

L'idéal peut admettre plusieurs réalisations pertinentes, une solution inconnue ou un horizon que l'on poursuit sans état parfait atteignable. La Mission n'est donc pas définie comme \(\arg\min L\) ni comme l'ensemble supposé connu de ses solutions.

## 4. Exemple : déterminer une relation affine

Soit la population de référence :

\[
O=[0,100].
\]

La structure recherchée est une relation affine :

\[
\exists a,b\in\mathbb R,\qquad
\forall x\in O,\ f(x)=ax+b,
\quad f:O\to\mathbb R.
\tag{M5}
\]

La formule **exprime l'allure** de la relation sans déterminer les coefficients et sans dépendre d'un dataset ni d'un modèle particulier. Elle peut appartenir à l'Horizon lorsqu'elle constitue une propriété établie de l'entreprise ; si elle est seulement une hypothèse de recherche, ce statut doit être conservé.

Une conséquence déductible de (M5) est :

\[
\forall x,y\in O,\quad
f\left(\frac{x+y}{2}\right)
=\frac{f(x)+f(y)}2.
\tag{M6}
\]

Ainsi, **la Mission peut déjà intervenir dans des calculs sans solution connue**.

Une connaissance nouvelle établissant que la relation est strictement croissante peut conduire à préciser la théorie par \(a>0\). Si des valeurs vérifiées établissent \(f(0)=3\) et \(f(10)=23\), on obtient \(a=2\), \(b=3\) et la réalisation particulière \(f(x)=2x+3\). Cette fonction n'est pas la Mission initiale. Plusieurs fonctions peuvent satisfaire l'allure affine tout en n'étant pas toutes correctes pour le phénomène réel.

## 5. Exemple : le maire et la criminalité

**P — Portée :** situations de criminalité et de sécurité publique de la ville, avec leurs variations territoriales, sociales et temporelles.

**E — Horizon :** combattre durablement la criminalité et améliorer la sécurité des habitants, en tenant compte des autres exigences applicables, sans présupposer la politique efficace.

Les réalisations pertinentes peuvent être des interventions, organisations ou **trajectoires** \(\rho\), dont plusieurs peuvent être compatibles avec la Mission. Si l'on dispose de grandeurs pertinentes et comparables — criminalité \(C(\rho)\), préjudices \(V(\rho)\), atteintes aux droits \(J(\rho)\) — on peut exprimer une relation partielle d'orientation :

\[
\rho_1\preceq_E\rho_2
\quad\Longleftarrow\quad
\begin{cases}
C(\rho_2)\le C(\rho_1),\\
V(\rho_2)\le V(\rho_1),\\
J(\rho_2)\le J(\rho_1).
\end{cases}
\tag{M7}
\]

(M7) n'est **ni une équation normative TL, ni une définition exhaustive de la sécurité** : elle illustre une relation d'orientation lorsque les trois mesures existent et que les trajectoires sont effectivement comparables. Certaines trajectoires restent incomparables. Plusieurs approches différentes peuvent contribuer à l'Horizon ; aucune solution unique n'est imposée.

## 6. Variabilité des formes mathématiques

La même construction (M1) peut exprimer des entreprises différentes :

| Entreprise | Formes mathématiques adaptées |
|---|---|
| Estimation | Fonctions, relations quantitatives, équations et propriétés de variation |
| Détection visuelle de pathologies | Situations, états et conclusions diagnostiques, relations cliniques, invariances justifiées |
| Organisation territoriale | Graphes, partitions, voisinages et propriétés relationnelles |
| Communication textuelle | Structures symboliques et relations de fidélité sémantique |
| Irrigation | États, transitions, trajectoires, contraintes physiques et orientations temporelles |

Ces formes ne constituent pas des Missions différentes au sens de la définition mathématique ; elles sont des **langages appropriés pour caractériser des Horizons différents sur leurs populations**. Aucune fonction objectif scalaire, aucune métrique universelle, aucune modalité informatique et aucun optimum connu ne sont exigés.

## 7. Compréhension évolutive de la Mission

Une Mission peut être formulée, puis comprise, précisée et corrigée progressivement. Les formulations connues peuvent être exprimées comme une famille :

\[
(\mathfrak m_t)_{t\in I}.
\tag{M8}
\]

Cette expression concerne **les états de formulation de la même entreprise lorsque leur continuité est établie** ; elle n'exige pas que les états futurs soient connus. Une révision peut enrichir, préciser, remplacer ou retirer des énoncés. L'évolution n'est donc pas nécessairement monotone : \(\mathscr A_t\subseteq\mathscr A_{t+1}\) n'est pas une condition universelle.

Lorsque \(\mathscr L_t\) change, une comparaison rigoureuse entre formulations exige une interprétation ou une traduction explicite entre langages. La proximité syntaxique ne prouve pas, à elle seule, l'identité de l'entreprise.

Distinguer :

1. **Précision de la formulation** : évolution de ce que nous savons de la même Mission.
2. **Transformation de la Mission** : changement substantiel de l'entreprise ou de sa Portée.
3. **Réalisation ou découverte** : résultat obtenu dans la poursuite de l'entreprise.

La continuité de l'entreprise ne peut pas être définie arbitrairement par un identifiant, une similarité de formules ou la simple addition de contraintes.

## 8. Calculs permis et limites

La théorie ouverte (M1) sert de référence à des opérations mathématiques **lorsqu'une interprétation et une méthode adaptée existent** :

- **Déduction** des propriétés découlant des énoncés de Portée et d'Horizon.
- **Appartenance** d'une situation à la population, lorsque les conditions suffisent à la décider.
- **Compatibilité** d'une proposition de réalisation avec les propriétés connues.
- **Comparaison partielle** de réalisations si l'Horizon définit une relation appropriée.
- **Examen de cohérence** des énoncés connus.
- **Révision** et comparaison de formulations successives.

Une formule non interprétée ou une propriété indécidable ne devient pas calculable par sa seule inscription dans la théorie. La fermeture déductive n'est pas nécessairement calculable exhaustivement. Les résultats peuvent rester indéterminés. Ces opérations sont des mathématiques générales, **pas de nouveaux opérateurs scientifiques TL**.

## 9. Concordance avec les notations et frontières du manuscrit

La théorie de référence présente une Mission pouvant dépasser les connaissances initiales du Maître et dont la solution n'est pas présupposée. Le chapitre de finalité évolutive traite de buts dynamiques, hiérarchisés et contextualisés. Notre représentation n'identifie **ni la Mission ni l'Horizon** aux régions de buts déjà notées \(\mathcal G\) dans les mathématiques téléologiques, ni aux distances de réalisation définies pour ces buts.

| Notation | Réservation |
|---|---|
| \(\mathfrak m_t\) | Formulation mathématique de la Mission à l'état de compréhension \(t\) |
| \(\mathscr L_t\), \(\mathscr A_t^P\), \(\mathscr A_t^E\) | Langage et énoncés de cette formulation |
| \(\operatorname{Cn}\), \(\operatorname{Mod}\) | Constructions de logique mathématique, non opérateurs TL |
| \(P\), \(E\) | Désignations conceptuelles locales : Portée et Horizon ; **pas** une réaffectation de \(\mathcal P\) ou \(\mathcal E\) |
| \(\mathcal M\), \(\mathcal F\), \(\mathcal G\), \(\mathcal{TLS}\) | Notations présentes dans les sources théoriques ; aucune signification nouvelle ici |

Les variables \(f,O,\rho,C,V,J\) sont locales aux exemples. Aucune nouvelle entité ni aucun neuvième objet fondamental TL n'est introduit.

## 10. Expression consolidée

**La Mission est une entreprise orientée sur une population de référence, dont la représentation mathématique est une théorie formelle ouverte et évolutive. Elle réunit les énoncés de Portée et d'Horizon dans un seul langage typé, sans présupposer la connaissance exhaustive de l'idéal, les réalisations qui le satisferont ni leur unicité.**

\[
\boxed{
\mathfrak m_t =
\left\langle
\mathscr L_t,\;
\operatorname{Cn}_{\mathscr L_t}
\bigl(\mathscr A_t^P\cup\mathscr A_t^E\bigr)
\right\rangle.
}
\]

C'est une formalisation mathématique de la conception étudiée, **pas une équation déjà publiée ou démontrée par le manuscrit TL**. Elle ne modifie ni les mathématiques normatives existantes ni les conditions scientifiques d'exécution de TL.

## Références internes

- [Mission, trois entités, huit objets et Tradition](../fondements/MISSION_ENTITES_HUIT_OBJETS_ET_TRADITION.md)
- [Constitution et frontières](CONSTITUTION_ET_FRONTIERES.md)
- [Questions ouvertes](QUESTIONS_OUVERTES.md)
- [Finalité et téléologie évolutive](../../../maths/28-finality-and-evolutionary-teleology/finality-and-evolutionary-teleology.md)
