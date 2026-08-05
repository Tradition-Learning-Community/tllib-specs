# Phase d'empowerment

## 1. Diminution de la dépendance

L'indice de dépendance au maître est

\[
\Delta_{\mathcal M}(t)
=\frac{
\lVert\mathbf X(t)-\mathbf X_{\mathrm{without}}(t)\rVert}
{\lVert\mathbf X(t)\rVert}.
\]

La part de guidance décroît exponentiellement et la dynamique combine encore, pendant la transition, contribution du maître et activité autonome. Les mécanismes internes ne s'activent qu'après le franchissement de seuils de dépendance définis dans le chapitre.

## 2. Échelle d'autonomie

La source définit quatre niveaux à partir de $\Delta_{\mathcal M}$ et d'autres métriques : autonomie technique, décisionnelle, stratégique et existentielle. Le deuxième seuil du cycle correspond au passage vers une autonomie stabilisée ; l'autonomie créative est traitée ensuite comme niveau ultime.

L'autonomie ne signifie pas rupture avec la tradition : elle associe retrait de la dépendance verticale, intériorisation des critères et maintien de la fidélité au noyau.

## 3. Créativité fidèle

L'opérateur créatif est écrit

\[
\mathcal K(\mathbf X,\mathcal C)
=\mathbf X+\varepsilon\mathbf v(\mathbf X,\mathcal C).
\]

L'indice d'autonomie créative est

\[
\mathcal I_{\mathrm{crea}}(t)
=\frac{
\lVert\mathcal K(\mathbf X(t),\mathcal C(t))-\mathbf X(t)\rVert}
{\lVert\mathbf X(t)\rVert}
\left(
1-\left\lVert
\pi_{\mathcal N}(\mathcal K(\mathbf X,\mathcal C))
-\pi_{\mathcal N}(\mathbf X)
\right\rVert
\right).
\]

La source définit aussi une relation entre fidélité et innovation et un potentiel de créativité. Les opérations autorisées incluent l'analogie et la recombinaison, sous contrainte du noyau fidèle et sous validation communautaire.

Le troisième seuil exige conjointement autonomie, créativité, fidélité et reconnaissance de la capacité à transmettre.

## 4. Préparation à transmettre

La sortie transforme le disciple autonome en sujet susceptible d'occuper la fonction de maître. Elle comprend une compétence pédagogique, une autorisation communautaire et un rite de passage. Cette sortie rejoint la propagation générationnelle spécifiée dans [Propagation générationnelle](../29-generational-propagation/generational-propagation.md).

## 5. Bifurcation

L'empowerment est également représenté par un potentiel $U(\mathbf X)$ dont les minima correspondent aux attracteurs « disciple dépendant », « autonome » et « maître ». Les seuils sont les points où la topologie de $U$ change. La source emploie une bifurcation en fourche et un potentiel de Landau pour représenter le changement qualitatif, puis formule une propriété d'irréversibilité sous condition de cohérence.

## 6. Limites et points scientifiques non résolus

- L'état contrefactuel $\mathbf X_{\mathrm{without}}$ n'est pas construit ; l'indice de dépendance n'est donc pas directement calculable à partir de la seule trajectoire observée, et il n'est pas défini lorsque $\lVert\mathbf X(t)\rVert=0$.
- $\mathcal K(\mathbf X,\mathcal C)$ retourne un état transformé, alors que le texte le décrit aussi comme produisant l'innovation $\delta\mathbf X$ ; ces deux objets ne sont pas identifiés formellement.
- L'indice d'autonomie créative contient des facteurs dont la plage n'assure pas une valeur bornée ou positive.
- L'opérateur d'analogie dérive un principe par rapport à l'état sans préciser l'espace différentiel commun.
- La bifurcation en fourche et la propriété d'irréversibilité sont affirmées sans dérivation à partir de la dynamique complète du disciple.
