# Phase de guidance

## 1. Opérateur pédagogique contextualisé

La famille d'opérateurs pédagogiques est notée

\[
\Phi
=\left\{\Phi_\theta:\mathbb D\times\mathbb C\to\mathbb D
\;\middle|\;\theta\in\Theta\right\}.
\]

Le paramètre contextuel est sélectionné par

\[
\theta^*(t)
=\operatorname*{arg\,min}_{\theta\in\Theta}
\mathcal L\bigl(
\Phi_\theta(\mathbf X(t),c(t)),\mathbf X_{\mathrm{target}}
\bigr).
\]

Son adaptation est modélisée par

\[
\frac{d\theta}{dt}
=-\eta(t)\nabla_\theta
\mathcal L\bigl(
\Phi_\theta(\mathbf X(t),c(t)),\mathbf X_{\mathrm{target}}
\bigr)
+\sigma(t)\xi(t).
\]

## 2. Modes et séquence de guidance

La source distingue guidance explicite, implicite, progressive et initiatique. Leur combinaison est convexe :

\[
\Phi_{\mathrm{total}}(\mathbf X,c)
=\sum_{i\in\{\mathrm{exp},\mathrm{imp},\mathrm{prog},\mathrm{init}\}}
\alpha_i(t)\Phi_i(\mathbf X,c),
\qquad
\sum_i\alpha_i(t)=1.
\]

Les opérateurs élémentaires sont la démonstration $\mathcal D_{\mathrm{dem}}$, le questionnement $\mathcal Q$, la correction $\mathcal C$ et le silence $\mathcal S$. Une séquence type est

\[
\mathcal S\circ\mathcal C\circ\mathcal Q\circ\mathcal D_{\mathrm{dem}}.
\]

## 3. Boucle de rétroaction

Le processeur de retour est la composition hiérarchique

\[
\mathcal F
=\mathcal F_{\mathrm{perceptual}}
\circ\mathcal F_{\mathrm{evaluate}}
\circ\mathcal F_{\mathrm{integrative}}
\circ\mathcal F_{\mathrm{regulatory}}.
\]

Sa dynamique emploie un noyau causal :

\[
\mathcal F[\mathcal I_{\mathrm{ext}}](t)
=\int_{-\infty}^{t}
K(t-\tau;\mathcal R,\mathcal P)\mathcal I_{\mathrm{ext}}(\tau)\,d\tau
+\mathcal F_{\mathrm{int}}(\mathcal D).
\]

La trajectoire du disciple et le retour sont couplés sous la forme

\[
\begin{aligned}
\frac{d\mathbf X}{dt}
&=\mathcal T\bigl(\mathbf X,\mathcal F[\mathcal I_{\mathrm{ext}}]\bigr),\\
\frac{d\mathcal F}{dt}
&=\mathcal G(\mathbf X,\mathcal F,\mathcal I_{\mathrm{ext}}).
\end{aligned}
\]

Dans la version discrète, chaque état $\mathbf X_n$ produit une pratique, puis un retour et une transformation conduisant à $\mathbf X_{n+1}$. La convergence est exprimée, sous l'hypothèse d'existence d'une fonction de Lyapunov $L$, par

\[
L(\mathbf X_{n+1})
\leq L(\mathbf X_n)
-\varepsilon\lVert\mathbf X_{n+1}-\mathbf X_n\rVert^2.
\]

La source autorise plusieurs boucles de rétroaction simultanées à des échelles différentes.

## 4. Critère de fin de phase

La guidance vise le passage d'une transformation fortement commandée par le maître à une pratique progressivement autorégulée. Les seuils associés portent sur les composantes de compétence, de pratique, de vertu et de valeurs de l'état du disciple.

## 5. Limites et points scientifiques non résolus

- La famille est d'abord typée sur $\mathbb D\times\mathbb C$, alors que les équations ultérieures utilisent directement $\mathbf X$ et $c$ sans identifier formellement ces notations à $\mathbb D$ et $\mathbb C$.
- L'existence ou l'unicité de $\theta^*$ n'est pas établie.
- La combinaison dite convexe impose seulement $\sum_i\alpha_i(t)=1$ ; la non-négativité des coefficients et l'espace vectoriel nécessaire à la somme ne sont pas explicités.
- Le questionnement est formulé avec un déplacement suivant un gradient tout en étant décrit comme une réduction d'incertitude ; le signe et la fonction concernée ne sont pas justifiés.
- La condition de Lyapunov est donnée comme critère, sans fonction $L$ construite ni domaine de validité.
