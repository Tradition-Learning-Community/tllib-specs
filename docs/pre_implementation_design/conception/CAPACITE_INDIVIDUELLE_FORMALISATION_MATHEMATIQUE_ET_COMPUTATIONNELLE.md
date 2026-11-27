# Capacité individuelle — formalisation mathématique et computationnelle de travail

> **Statut :** étude de conception pré-implémentation, **non normative**, à confronter aux contrats applicables avant toute implémentation.
> **Date :** 27 novembre 2026.
> **Objet TL :** Capacité, considérée **individuellement** chez une unité d'apprentissage (par exemple D0).
> **Portée :** définition, nature, représentation candidate, exemples calculés et limites d'attribution. **Aucun mécanisme de développement ni API n'est arrêté.**
> **Vérification :** lecture des sources scientifiques et calculs élémentaires d'exemples ; **aucun entraînement TL, test de conformité ni modification de runtime**.

## 1. Sources, autorité et frontière

1. Manuscrit principal *Tradition Learning - main.pdf*, § 4.2.5 (« Capacities — Potential and Latent Dimension »), page imprimée 101 : potentiels propres au Disciple, révélés, activés et cultivés plutôt que « créés » par transmission directe.
2. Manuscrit détaillé *TraditionLearning.pdf*, § 1.42.1 (« Definition and Ontological Status of Capacities », définition 1.41), pages imprimées 170–171 : potentiel dynamique de mobilisation des ressources, latence, activabilité, structuralité, évolutivité.
3. [Mathématiques des Capacités](../../../maths/11-capacities/capacities.md) : espace des potentiels, domaines de validité, conditions d'existence, mécanismes d'actualisation et d'évaluation.
4. [Mathématiques des Compétences](../../../maths/12-competencies/competencies.md), pour la distinction entre potentiel et actualisation.
5. [Pratique et Expérience vécue — formalisation computationnelle](PRATIQUE_ET_EXPERIENCE_VECUE_FORMALISATION_COMPUTATIONNELLE.md), pour les moyens d'apprentissage et les schèmes ; [Compétence individuelle](COMPETENCE_INDIVIDUELLE_FORMALISATION_MATHEMATIQUE_ET_COMPUTATIONNELLE.md), pour l'autre objet étudié ici.

**Autorité :** le manuscrit gouverne la théorie ; les mathématiques et contrats publiés dans \`tllib-specs\` gouvernent leurs domaines ; cette note constitue une **extension descriptive de travail** et ne modifie aucun axiome, seuil, opérateur, contrat ou classification scientifique.

## 2. Acquis scientifiques : nature de la Capacité

La théorie définit une Capacité comme un **potentiel dynamique** d'un agent individuel ou collectif, capable de mobiliser des ressources en vue de l'action ou de l'actualisation d'une Compétence, dans des conditions appropriées. Elle peut exister **sans manifestation**.

L'espace scientifique global est décrit par :

\[
\mathcal C_p=
\mathcal C_{\mathrm{inné}}\oplus
\mathcal C_{\mathrm{acquis}}\oplus
\mathcal C_{\mathrm{latent}}\oplus
\mathcal C_{\mathrm{émergent}}\subset\mathbb H.
\]

Cette expression est **celle de la théorie**. Elle ne se confond pas avec la représentation computationnelle d'**une** capacité particulière. La latence, l'activabilité, la structuralité et l'évolutivité restent des caractères scientifiques ; cette note ne les remplace pas par une performance numérique.

Une capacité appartient à une **unité d'apprentissage**, pas à un modèle informatique considéré indépendamment de cette unité. Un algorithme, un solveur, une fonction de perte ou un provider peuvent la soutenir, mais ne constituent pas automatiquement une Capacité TL.

La Mission peut solliciter une capacité sans la définir. Une capacité peut être envisagée comme **cible de développement**, sans être déclarée déjà possédée par D0. Un Maître peut manifester une capacité et favoriser les conditions de son développement chez un Disciple ; il n'en transfère pas une « copie » informatique.

## 3. Nature individuelle et caractérisation mathématique proposée

### 3.1. Nature

> **Une Capacité individuelle est une propriété opératoire potentielle d'une unité d'apprentissage, dont la réalisabilité peut être caractérisée conditionnellement à la mobilisation effective de ses moyens et dispositions, sans exiger qu'elle soit déjà manifestée.**

Le terme **atomique** signifie ici : une propriété délimitée, identifiable et examinable séparément. Il ne signifie ni « un seul nombre », ni « une seule tâche », ni « indivisible au sens mathématique ». D0 peut présenter plusieurs Capacités ; une Pratique peut en solliciter plusieurs.

### 3.2. Écriture de caractérisation (proposition de conception, NON normative)

Soient :

- \(D\) : l'unité porteuse, ici D0 ;
- \(c_p\) : une capacité individuelle étudiée ;
- \(\omega\in\Omega_c\) : une configuration de conditions pertinentes, pouvant inclure ressources, signaux, observations, Pratiques et contexte ;
- \(\mathscr B\) : un domaine de transformations ou de comportements adapté à la propriété ;
- \(\mathcal R_D(\omega)\subseteq\mathscr B\) : les transformations **effectivement accessibles** à D dans ces conditions, avec ses moyens admissibles ;
- \(\Phi_c(B,\omega)\) : la **loi, contrainte ou relation précise** qui caractérise cette propriété lorsqu'elle est réalisée par un comportement \(B\).

Une caractérisation **locale de la possibilité** s'écrit :

\[
\boxed{
\operatorname{Possible}_{D,c_p}(\omega)
\quad\Longleftrightarrow\quad
\exists B\in\mathcal R_D(\omega):\ \Phi_c(B,\omega).
}
\tag{C-P}
\]

Elle n'est **pas** une équation théorique supplémentaire de TL : c'est un outil mathématique pour raisonner sur la réalisabilité individuelle. Selon la Capacité, \(\Phi_c\) peut désigner une équation, une invariance, une condition d'ordre, une contrainte statistique ou une autre relation typée.

Une écriture équivalente, lorsque cela aide, est une **correspondance multivaluée** \(K_D:\Omega_c\rightrightarrows\mathscr B\), avec \(K_D(\omega)=\mathcal R_D(\omega)\). **La Capacité n'est pas \(K_D\)** : cette correspondance ne fait que représenter des possibilités de son porteur.

La **portée** \(\Omega_c\) doit rester explicite. Une réussite à une condition \(\omega\) ne démontre pas \(\operatorname{Possible}_{D,c_p}\) dans toutes les conditions. Inversement, l'impossibilité d'établir cette possibilité avec les moyens d'observation présents ne prouve pas l'absence de potentiel latent.

**Condition d'attribution :** \(\mathcal R_D\) ne peut pas être remplacé par « tout ce que n'importe quel logiciel externe pourrait calculer ». L'existence d'un solveur disponible ou l'existence abstraite d'une solution ne suffisent pas à attribuer une Capacité à D0. Les moyens accessibles et la mobilisation permise par la constitution réelle de D0, ainsi que les conditions scientifiques applicables, restent décisifs. Les possibilités inconnues doivent rester inconnues.

### 3.3. Ce que cette représentation n'est pas

Ce n'est ni un seuil universel, ni une note de 0 à 100, ni une taxonomie imposée, ni une nouvelle famille de modèles, ni une condition obligatoire de généralisation parfaite. Le critère concret \(\Phi_c\) relève de **la capacité particulière considérée**, pas d'une mesure commune à toutes les Capacités.

## 4. Cinq régressions, cinq propriétés candidates : une seule unité D0

Les cas ci-dessous sont des **exercices analytiques**, avec cinq Pratiques possibles pour D0. Les calculs ne prouvent ni entraînement TL exécuté ni Capacité scientifiquement établie.

| Pratique | Relation de l'exercice | Moyens envisagés | Propriété atomique candidate à examiner |
| --- | --- | --- | --- |
| P1 : prix selon \(x\) | \(f(x)=2x+1\) | Résolution algébrique | C1 : préservation d'un ordre pertinent |
| P2 : quantité selon \(x\) | \(f(x)=3x^2\), \(x\ge0\) | Gradient et erreur quadratique | C2 : préservation d'une courbure attendue |
| P3 : coût distance/charge | \(f(d,q)=5+2d+3q\) | Moindres carrés multivariés | C3 : séparation des contributions additives |
| P4 : relation avec valeur aberrante | \(f(x)=2x+1\), une observation perturbée | Estimation robuste Theil–Sen | C4 : résistance à une observation aberrante |
| P5 : consommation par régime | \(f(x)=2\) si \(x<5\), \(8\) sinon | Arbre de régression | C5 : préservation d'une rupture réelle |

Les cinq **propriétés** n'ont pas toutes la même pertinence dans chaque cas ; elles ne sont pas des types normatifs, et une même Pratique peut en solliciter plusieurs. **D0 ne possède pas automatiquement C1–C5** parce que nous avons choisi cinq méthodes appropriées.

Pour fixer \(\Phi_c\) à un niveau concret :

- **C1 — ordre**, sur un domaine orienté pertinent : \(x_1<x_2\Rightarrow B(x_1)\le B(x_2)\). Pour P3, on compare une variable en gardant l'autre fixe.
- **C2 — courbure**, avec un pas \(h\) admissible : \(B(x+h)-2B(x)+B(x-h)=6h^2\) lorsque la référence est \(3x^2\). Cette expression appartient **à l'exercice P2** ; la propriété générale ne porte pas toujours la valeur \(6h^2\).
- **C3 — séparation additive**, sur l'exercice P3 : \(B(1,1)-B(1,0)-B(0,1)+B(0,0)=0\). Elle n'autorise pas à effacer une interaction véritable dans une autre relation.
- **C4 — robustesse à une perturbation effectivement aberrante** : contrôler \(L_D(O')(x)-L_D(O)(x)\) pour les perturbations admissibles définies. La stabilité absolue n'est qu'une **référence idéale conditionnelle** : elle ne vaut pas pour des changements légitimes de la relation.
- **C5 — rupture**, sur l'exercice P5 : conserver le saut \(8-2=6\) entre les deux régimes. Les observations ne permettent pas d'identifier le seuil exact : \(5\) est une séparation illustrative entre \(4\) et \(6\).

## 5. Exemple développé — Capacité C4

Considérons :

\[
O=\{(1,3),(2,5),(3,7),(4,9),(5,11)\}
\]
\[
O'=\{(1,3),(2,5),(3,7),(4,9),(5,50)\}.
\]

Dans cet exercice, la dernière valeur de \(O'\) est supposée aberrante et la relation sous-jacente inchangée. Pour une transformation d'apprentissage \(L\) donnant une relation estimée, la propriété étudiée est la **stabilité de cette relation** face à la perturbation considérée :

\[
\Phi_{C4}(L;O,O',X)\quad:\quad
L(O')(x)=L(O)(x)\quad\text{pour tout }x\in X.
\]

**Capacité C4 de D0 :** existe-t-il, parmi les moyens qu'il peut effectivement mobiliser sous ces conditions, une transformation d'apprentissage \(L\) satisfaisant cette propriété dans la portée \(X\) considérée ?

Une méthode robuste comme Theil–Sen est **un témoin mathématique possible** : avec cet ensemble, elle restitue \(L(O')=2x+1\). Cela ne démontre **pas automatiquement** que D0 porte scientifiquement cette Capacité : il faut établir que sa mobilisation appartient réellement aux possibilités de D0, et vérifier les autres exigences TL pertinentes.

Le résultat n'est pas le schème \(2x+1\). La propriété porte sur la **possibilité de préserver la relation** quand une observation non pertinente change.

## 6. Relations aux autres objets et à l'idéal

- **Pratique :** moyen configurable de solliciter, manifester ou développer une Capacité. Une Capacité n'est pas une Pratique, et n'est pas enfermée dans une Pratique unique.
- **Expérience vécue :** schèmes acquis, modifiés et conservés de manière intégrée ; une Capacité peut contribuer à leur acquisition, transformation ou exploitation, sans se réduire à ces contenus.
- **Compétence :** maîtrise actualisée et démontrable, distincte du potentiel. Voir [l'étude jumelle](COMPETENCE_INDIVIDUELLE_FORMALISATION_MATHEMATIQUE_ET_COMPUTATIONNELLE.md).
- **Maître / Disciple :** la capacité de M0 peut être une référence et une cible pour D0, pas une installation de propriété, ni un plafond de maîtrise.
- **Mission :** peut utiliser une Capacité sans la définir.

Un idéal de réalisation d'une capacité particulière peut guider la recherche de manifestations plus larges et plus fiables. Le sous-apprentissage, le surapprentissage, les biais indésirables et la généralisation ne sont **pas quatre constituants obligatoires** de chaque Capacité ; seules les évaluations pertinentes pour \(c_p\) sont mobilisées. L'idéal n'est ni un pourcentage ni une garantie absolue.

## 7. Décisions de travail, limites et conformité future

**Retenu pour la conception :** une Capacité individuelle est un potentiel opératoire propre à l'unité ; on peut en préciser la propriété \(\Phi_c\), la portée et la réalisabilité conditionnelle. Une déclaration comme cible n'établit pas son existence. Une Capacité n'est ni un algorithme, ni une tâche, ni un schème, ni une ressource.

**Non démontré :** que C1–C5 sont scientifiquement reconnues chez D0, que \(\mathcal R_D\) est exhaustivement calculable, qu'une méthode particulière produit une transformation scientifique TL, ou qu'un indice classique mesure toute la Capacité.

**À vérifier avant implémentation :** contrats et conditions d'existence/actualisation dans \`maths/\`, \`registry/\` et \`handoff/\` ; modalités autorisées de constat et de reconnaissance ; statut exécutable, conditionnel ou seulement structurel. La relation entre les espaces théoriques \(\mathcal C_p\) et \(\mathcal C_a\), décrits dans des espaces ambiants différents, doit être laissée à la source scientifique pour toute identification formelle supplémentaire.

**Aucun** fichier scientifique normatif, contrat, algorithme TL, seuil ou API n'est modifié par cette étude.
