# Mission TL — représentation mathématique unifiée, ouverte et évolutive

**Statut : étude de conception mathématique, non normative.**  
**Objet :** présenter une représentation mathématique unique de la Mission, indépendante des participants, des ressources, des sources d'apprentissage, des modèles et des travaux particuliers.  
**Autorité :** le manuscrit scientifique *Tradition Learning*, puis les mathématiques et les contrats publiés dans `tllib-specs`. Ce document ne modifie ni la théorie ni les contrats normatifs.

## 1. Définition fondamentale

La Mission est une entreprise orientée sur une population de référence. Elle est indépendante des moyens employés pour la poursuivre et des réalisations particulières qui pourront en résulter.

Elle possède deux constituants fondamentaux :

- **E — Entreprise orientée ou Horizon :** l'idéal poursuivi, avec ses propriétés, orientations et conditions, éventuellement incomplètement connues.
- **P — Portée ou Périmètre :** la population de référence sur laquelle porte cette entreprise, comprenant les situations pertinentes, y compris futures ou non encore observées.

La définition conceptuelle demeure :

\[
\boxed{\operatorname{Mission}=(E,P)}
\]

Cette définition n'impose ni une solution connue, ni une fonction particulière, ni un optimum unique. La Mission peut exister alors que ses réalisations demeurent inconnues.

## 2. Représentation mathématique unique

Nous utilisons une théorie formelle typée, ouverte et orientée. À un état de compréhension \(\tau\), sa représentation est :

\[
\boxed{
\mathfrak m_{\tau}
=
\left\langle
\Sigma_{\tau},
\mathscr A_{\tau}^{P},
\mathscr A_{\tau}^{E}
\right\rangle
}
\tag{M}
\]

| Notation | Signification |
|---|---|
| \(\mathfrak m_{\tau}\) | Formulation mathématique de la Mission à l'état de compréhension \(\tau\) |
| \(\Sigma_{\tau}\) | Langage mathématique typé permettant de caractériser l'entreprise |
| \(\mathscr A_{\tau}^{P}\) | Propriétés connues du Périmètre |
| \(\mathscr A_{\tau}^{E}\) | Propriétés connues de l'Horizon |
| \(\operatorname{Cn}_{\Sigma_{\tau}}\) | Fermeture par conséquence logique dans le langage et le système de déduction retenus |

C'est une seule construction mathématique, et non deux objets indépendants simplement assemblés. La distinction entre \(\mathscr A_{\tau}^{P}\) et \(\mathscr A_{\tau}^{E}\) est conservée explicitement, tandis que leur réunion permet de les exploiter conjointement dans les déductions.

Chaque énoncé garde ainsi sa signification, mais les conséquences mathématiques peuvent faire intervenir simultanément le Périmètre et l'Horizon. Lorsque le langage et le système de déduction sont fixés, cette opération s'écrit \(\\operatorname{Cn}_{\\Sigma_{\\tau}}(\\mathscr A_{\\tau}^{P}\\cup\\mathscr A_{\\tau}^{E})\).

Cette construction utilise des outils de logique mathématique existants. Elle n'introduit ni un neuvième objet fondamental TL ni une nouvelle équation de téléologie. La fermeture par conséquence logique ne garantit pas que toutes les conséquences soient calculables par un algorithme effectif ; cela dépend du fragment logique et des méthodes disponibles.

## 3. L'Horizon exprime ce qui est recherché, pas ce qui existe déjà

Considérons l'exemple d'un maire qui cherche à combattre la criminalité. Il faut distinguer :

- **La criminalité actuelle :** un fait ou un ensemble de faits relevant de la situation observée.
- **La réduction recherchée de la criminalité :** une propriété de l'Horizon.
- **Une réduction effectivement obtenue :** un résultat constaté.

Dans \(\mathscr A_{\tau}^{E}\), les expressions de l'idéal doivent donc être formulées comme des propriétés de réalisations envisagées ou de trajectoires possibles, et non comme des affirmations selon lesquelles le monde possède déjà ces propriétés.

Par exemple, une condition portant sur deux trajectoires de sécurité publique peut s'écrire :

\[
C(\rho_2)\leq C(\rho_1)
\]

lorsque \(C\), \(\rho_1\), \(\rho_2\) et les conditions de comparaison sont définis. Cette relation exprime une comparaison mathématique entre deux trajectoires. Elle n'affirme pas que la ville a effectivement suivi \(\rho_2\).

Selon la Mission, on peut employer des relations d'admissibilité, des relations d'équivalence, des contraintes, des propriétés de fonctions ou des relations d'orientation.

Aucune logique modale particulière n'est imposée à toutes les Missions. La distinction entre l'idéal et le réel est portée par la sémantique des énoncés et leur typage. Une propriété souhaitée ne doit donc pas être interprétée automatiquement comme une vérité déjà réalisée.

## 4. La connaissance incomplète est normale

La formulation de la Mission peut être partielle. Pour une proposition bien formée \(\varphi\), dans une théorie cohérente et avec une conséquence logique classique, trois situations sont possibles :

\[
\boxed{
\begin{cases}
\mathfrak m_{\tau}\models\varphi
& \text{propriété établie},\\
\mathfrak m_{\tau}\models\neg\varphi
& \text{propriété réfutée},\\
\mathfrak m_{\tau}\not\models\varphi
\ \land\
\mathfrak m_{\tau}\not\models\neg\varphi
& \text{propriété indéterminée}.
\end{cases}
}
\]

Il ne s'agit pas d'une nouvelle logique à trois valeurs : ces expressions distinguent les conséquences établies, réfutées et non décidées dans une logique classique cohérente.

Une caractéristique inconnue de la Mission n'est donc pas automatiquement considérée comme inexistante. Une Mission dont la formulation comporte des propriétés indéterminées n'est pas, pour cette seule raison, invalide.

La cohérence doit néanmoins être examinée : dans une théorie classique contradictoire, toute proposition peut être déduite.

## 5. La Mission ne se confond pas avec ses réalisations

Nous conservons quatre notions distinctes :

\[
\boxed{
\text{Mission}
\neq
\text{Formulation de Mission}
\neq
\text{Modèles mathématiques compatibles}
\neq
\text{Réalisations effectives}
}
\]

Une formulation peut admettre plusieurs modèles mathématiques. Toutefois, un modèle qui satisfait les conditions actuellement connues ne satisfait pas nécessairement l'intégralité de l'idéal, car certaines propriétés peuvent encore être inconnues.

### Exemple : relation affine

Nous voulons déterminer une relation de la forme :

\[
f(x)=ax+b,\qquad x\in O.
\]

La Mission peut exprimer cette structure sans préciser les coefficients. Plusieurs fonctions sont alors compatibles avec cette connaissance.

Si de nouvelles propriétés deviennent connues, certaines fonctions peuvent être écartées. Si une réalisation particulière est déterminée, elle ne remplace pas la Mission. Une autre réalisation peut également contribuer à l'entreprise sans créer automatiquement une nouvelle Mission.

Cette distinction vaut aussi pour les organisations, les distributions, les trajectoires et les autres formes mathématiques.

## 6. L'évolution de la Mission

Il faut distinguer deux phénomènes :

- **Évolution de la compréhension :** nous apprenons à mieux caractériser la même entreprise.
- **Évolution de l'entreprise :** son idéal ou son périmètre change effectivement.

Dans le premier cas, nous avons des formulations successives :

\[
\mathfrak m_{\tau_0},
\mathfrak m_{\tau_1},
\mathfrak m_{\tau_2},\ldots
\]

Une formulation peut être enrichie, précisée ou corrigée. Si les langages successifs diffèrent, leur comparaison exige une traduction ou une interprétation mathématique appropriée.

Nous n'imposons pas une inclusion monotone telle que :

\[
\mathscr A_{\tau_0}\subseteq\mathscr A_{\tau_1},
\]

car une compréhension nouvelle peut aussi invalider une interprétation antérieure.

La continuité de la Mission doit être préservée ou justifiée. Elle ne résulte pas de la seule ressemblance de deux formules. La Mission reste une entreprise identifiable dont la compréhension mathématique évolue, sans qu'il soit nécessaire de connaître à l'avance toutes ses formulations futures.

## 7. Une Mission peut orienter plusieurs travaux, Finalités et Tâches

Les exercices sur les parcelles illustrent qu'une même entreprise peut être abordée par plusieurs travaux.

Dans le cas des parcelles, l'entreprise considérée peut porter sur :

- l'estimation des prix ;
- l'organisation territoriale ;
- ou une entreprise plus large comprenant les deux.

Dans ce dernier cas, une seule théorie de Mission peut contenir des propriétés relatives à la valeur et à l'organisation. Les travaux d'apprentissage peuvent ensuite avoir des Finalités et des Tâches différentes.

La représentation de la Mission n'impose donc pas qu'une entreprise corresponde nécessairement à un seul travail, à une seule Finalité ou à une seule Tâche. Inversement, deux Missions distinctes peuvent utiliser la même population ou les mêmes sources.

Le découpage en Missions dépend de l'entreprise et de sa portée, et non de la classification des méthodes d'apprentissage. Lorsque plusieurs travaux partagent une Mission, ils peuvent exploiter les fragments pertinents de sa théorie sans que ces fragments deviennent automatiquement de nouvelles Missions.

## 8. Conditions d'exploitabilité mathématique

La formule (M) donne une représentation unique. Elle ne signifie toutefois pas que tous les calculs sont possibles pour toute Mission.

| Opération | Condition mathématique |
|---|---|
| Déterminer l'appartenance à \(P\) | Conditions d'appartenance suffisamment définies |
| Déduire une propriété | Règles logiques et expressions interprétables |
| Vérifier la cohérence | Fragment théorique disposant d'une procédure adaptée |
| Examiner une réalisation | Propriétés de satisfaction définies |
| Comparer deux réalisations | Relation de comparaison applicable |
| Comparer deux formulations | Langages compatibles ou interprétation entre eux |

Une réponse peut rester indéterminée.

Pour l'estimation immobilière, une invariance par rapport à un indice indirect peut être déduite si elle figure parmi les propriétés établies de l'entreprise. Pour l'irrigation, des relations entre situations et trajectoires peuvent être étudiées lorsque la dynamique pertinente est connue.

Aucune fonction de coût universelle n'est décrétée pour rendre artificiellement calculables toutes les Missions. La représentation mathématique peut donc être constituée alors que certaines propriétés ne disposent pas encore d'une procédure de décision ou de calcul.

## 9. Compatibilité avec la théorie TL

Le chapitre scientifique sur la finalité et la téléologie évolutive utilise notamment les notations :

\[
\mathcal F,\qquad
\mathcal G,\qquad
\mathcal{TLS},\qquad
d_{\mathrm{réal}}.
\]

Ces notations conservent leurs significations scientifiques. La présente représentation utilise :

\[
\mathfrak m_{\tau},\qquad
\Sigma_{\tau},\qquad
\mathscr A_{\tau}^{P},\qquad
\mathscr A_{\tau}^{E}.
\]

Nous évitons ainsi de réaffecter les symboles de l'espace des buts, de l'espace des états ou des mécanismes téléologiques. La Mission ne devient ni une région de buts, ni une distance de réalisation, ni une fonction d'optimisation.

Elle demeure conceptuellement première. Les mécanismes téléologiques existants pourront être étudiés ultérieurement dans leur relation à la Mission, mais cette relation n'est pas décrétée automatiquement par la présente formalisation.

## 10. Résultat consolidé

### Mission — représentation mathématique

\[
\boxed{
\mathfrak m_{\tau}
=
\left\langle
\Sigma_{\tau},
\left(
\mathscr A_{\tau}^{P},
\mathscr A_{\tau}^{E}
\right),
\operatorname{Cn}_{\Sigma_{\tau}}
\left(
\mathscr A_{\tau}^{P}
\cup
\mathscr A_{\tau}^{E}
\right)
\right\rangle
}
\]

La Mission est une entreprise orientée sur une population, dont les propriétés connues constituent une théorie mathématique ouverte et évolutive.

Les exigences de conception qui en résultent sont :

- **Primauté :** la Mission existe indépendamment de ses participants et de leurs travaux.
- **Unité :** E et P constituent une seule entreprise mathématiquement exprimée.
- **Ouverture :** la solution et certaines propriétés de l'idéal peuvent demeurer inconnues.
- **Pluralité :** plusieurs réalisations, Finalités et Tâches peuvent contribuer à une même Mission.
- **Évolutivité :** la compréhension peut être enrichie ou corrigée.
- **Exploitabilité :** les propriétés suffisamment définies peuvent intervenir dans des calculs mathématiques.
- **Universalité :** aucune famille de modèles d'IA, modalité ou fonction objectif n'est imposée.

### Décision de clôture

La conception mathématique de la Mission est considérée comme suffisamment consolidée pour servir de fondation à la suite du travail.

Cela signifie que la représentation proposée peut exprimer les six exercices et leurs différentes organisations en Missions et travaux. Cela ne signifie pas qu'un nouveau théorème de Tradition Learning a été démontré, ni que toutes les propriétés possibles de toute Mission ont été établies formellement.

La construction relève de la conception mathématique. Elle est présentée comme compatible avec les distinctions vérifiées dans le manuscrit, mais elle ne constitue pas encore un résultat normatif de cette théorie.

Cette étape peut donc être close. La suite du travail portera sur le **Problème**, étudié comme un concept computationnel distinct de la Mission, susceptible d'en dépendre sans se confondre avec elle.

## Références internes

- [Mission, trois entités, huit objets et Tradition](../fondements/MISSION_ENTITES_HUIT_OBJETS_ET_TRADITION.md)
- [Constitution et frontières](CONSTITUTION_ET_FRONTIERES.md)
- [Questions ouvertes](QUESTIONS_OUVERTES.md)
- [Finalité et téléologie évolutive](../../../maths/28-finality-and-evolutionary-teleology/finality-and-evolutionary-teleology.md)
