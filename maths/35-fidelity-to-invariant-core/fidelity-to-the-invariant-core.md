# Fidélité au noyau invariant

## 1. Périmètre

Ce domaine ne redéfinit pas les invariants fondamentaux spécifiés dans [Invariants](../04-invariants/invariants.md). Il décrit la fidélité du nouveau maître au noyau invariant pendant la transmission secondaire : discerner le noyau et la périphérie, contrôler les variations destructrices et reconnaître les innovations qui préservent le noyau.

La source pose une tension fondamentale. Une transmission entièrement figée conduit à la sclérose ; une variation excessive conduit à la dilution. La variation peut donc être constructive, lorsqu'elle reste compatible avec le noyau, ou destructive, lorsqu'elle l'altère.

## 2. Noyau rappelé par la source

Le noyau invariant $\mathcal N_{\mathrm{inv}}$ rassemble le message fondamental, les principes cardinaux, les valeurs essentielles et les vertus fondamentales. Son identification repose sur l'universalité entre branches, le caractère fondateur, la résistance au changement historique et la reconnaissance par toutes les branches.

Le chapitre rappelle la définition

\[
\mathcal N_{\mathrm{inv}}(t)
=\left\{
x\in\mathcal X_{\mathrm{doctrinal}}
\;\middle|\;
\forall\tau\in[0,t],\;\forall v\in V_L,\;
d_D\bigl(\pi_{\mathcal N}(x_v(\tau)),x\bigr)
<\varepsilon_{\mathrm{ess}}(\tau),\;
\mathcal V(x)>\theta_{\mathcal V}
\right\}.
\]

$\mathcal X_{\mathrm{doctrinal}}$ est l'espace doctrinal, $V_L$ l'ensemble des branches de la lignée, $\pi_{\mathcal N}$ la projection sur le noyau, $d_D$ la distance doctrinale, $\varepsilon_{\mathrm{ess}}$ la tolérance d'essentialité et $\mathcal V(x)$ la valeur attribuée à $x$.

## 3. Variation générationnelle

Les sources de variation expressément retenues sont la personnalité du maître, les besoins des disciples, le contexte culturel, les nouveaux défis ainsi que les erreurs et incompréhensions. Le modèle rappelé est

\[
\mathbf X_{n+1}
=\mathbf X_n+\boldsymbol\varepsilon_n
+\mathbf C_n\bigl(\mathbf X_n-\pi_{\mathcal N}(\mathbf X_n)\bigr),
\qquad
\boldsymbol\varepsilon_n\sim\mathcal N(0,\Sigma),
\]

où $\boldsymbol\varepsilon_n$ représente la variation stochastique et $\mathbf C_n$ la correction.

## 4. Contrôle de la variation

Le nouveau maître dispose de quatre évaluations formalisées :

\[
\mathcal R_{\mathrm{art}}(\mathbf X)
=\min_{a\in\mathcal A_{\mathrm{validated}}}
\left\lVert\mathbf X-\pi_{\mathcal N}(a)\right\rVert,
\]

\[
\mathcal C_{\mathrm{cons}}(\mathbf X)
=\frac{1}{|\mathcal C_{\mathrm{elders}}|}
\sum_{c\in\mathcal C_{\mathrm{elders}}}
\left\lVert\mathbf X-\mathbf X_c\right\rVert,
\]

\[
\mathcal F_{\mathrm{comm}}(\mathbf X)=\mathcal M(\mathbf X,t),
\qquad
\mathcal A_{\mathrm{self}}(\mathbf X)=\mathcal E_{\mathrm{self}}(\mathbf X,t).
\]

Ils correspondent respectivement à la référence aux artefacts validés, à la consultation des anciens, au retour communautaire et à l'auto-évaluation réflexive. Leur combinaison est écrite

\[
\mathbf C_n
=\eta_1\mathcal R_{\mathrm{art}}
+\eta_2\mathcal C_{\mathrm{cons}}
+\eta_3\mathcal F_{\mathrm{comm}}
+\eta_4\mathcal A_{\mathrm{self}},
\qquad
\sum_i\eta_i=1.
\]

Le corpus d'artefacts, le conseil des anciens, le retour de la communauté, l'auto-évaluation et les rituels de rappel constituent les mécanismes de contrôle nommés par le texte.

## 5. Innovation fidèle

Une innovation $\delta\mathbf X$ est fidèle lorsque

\[
\left\lVert
\pi_{\mathcal N}(\mathbf X+\delta\mathbf X)
-\pi_{\mathcal N}(\mathbf X)
\right\rVert
\leq\epsilon_{\mathrm{innov}}.
\]

Une telle innovation peut être intégrée au corpus après validation communautaire. Les artefacts documentent les interprétations successives, permettent leur comparaison avec le corpus, supportent leur validation, puis l'intégration des innovations retenues.

## 6. Contraintes de fidélité du transmetteur

La fidélité est une responsabilité propre au passage du disciple au maître-relais. Parmi les conditions cumulatives de passage, la source impose une capacité de transmission au-dessus de son seuil, la validation communautaire, la disponibilité d'au moins un aspirant et l'accord explicite du maître d'origine. Le nouveau maître doit ensuite préserver le noyau tout en adaptant la transmission aux disciples et au contexte.

## 7. Limites et points scientifiques non résolus

- Le fichier source est intitulé « Fidelity to the Invariant Core », mais son titre de chapitre est « Secondary Transmission Phase » et la fidélité n'en occupe qu'une section ; le présent document conserve uniquement ce périmètre scientifique.
- Le rappel de $\mathcal N_{\mathrm{inv}}$ ne définit pas $x_v(\tau)$ ni les propriétés de la projection $\pi_{\mathcal N}$ et de la distance $d_D$.
- Dans la définition ensembliste, la même variable $x$ est comparée à toutes les projections historiques $\pi_{\mathcal N}(x_v(\tau))$ ; le statut temporel de $x$ n'est pas précisé.
- $\mathcal R_{\mathrm{art}}$ n'est pas défini lorsque $\mathcal A_{\mathrm{validated}}$ est vide, et $\mathcal C_{\mathrm{cons}}$ divise par zéro lorsque le conseil des anciens est vide.
- Les quatre termes combinés dans $\mathbf C_n$ sont respectivement des distances et des scores ; aucun espace commun ni opérateur transformant cette somme en correction d'état n'est fourni.
- Seule la somme des $\eta_i$ vaut $1$ dans la source ; leur positivité n'est pas explicitement imposée.
- Le critère d'innovation fidèle ne suffit pas, à lui seul, à construire la procédure de validation communautaire annoncée.
