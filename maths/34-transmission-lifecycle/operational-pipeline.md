# Pipeline opérationnel de la transmission

## 1. Périmètre

Le pipeline décrit le passage d'un aspirant à un maître-relais. Il articule l'admission, l'imprégnation, l'apprentissage actif, l'épreuve communautaire et l'autorisation de transmettre. Les formalismes propres à chaque phase sont détaillés dans les documents associés de ce domaine.

## 2. Admission

L'opérateur d'admission est

\[
\mathcal A_{\mathrm{adm}}:\mathcal C_{\mathrm{asp}}\times\mathbb R_+
\longrightarrow \mathcal D\cup\{\varnothing\}.
\]

L'aspirant est admis lorsque

\[
\Phi_{\mathrm{selection}}(c,t)\geq\theta_{\mathrm{adm}},
\]

avec

\[
\Phi_{\mathrm{selection}}(a,t)
=w_1\lVert\mathbf C_p(a)\rVert
+w_2\mathcal R(a,t)
+w_3\mathcal Mot(a,t)
+w_4\mathcal Val_{\mathrm{init}}(a).
\]

$\mathbf C_p$ est le vecteur de capacités de l'aspirant, $\mathcal R$ sa réceptivité, $\mathcal Mot$ sa motivation et $\mathcal Val_{\mathrm{init}}$ son alignement initial avec les valeurs fondamentales.

## 3. Imprégnation et apprentissage actif

Pendant l'imprégnation, l'état $X$ évolue selon

\[
\frac{d\mathbf X}{dt}
=\alpha_{\mathrm{imp}}\,
\mathcal O_{\mathrm{obs}}(\mathcal M,\mathcal C,t)
\bigl(\mathbf X_{\mathcal M}-\mathbf X\bigr),
\qquad 0\leq t\leq T_{\mathrm{imp}}.
\]

L'apprentissage actif est présenté sous la forme générale

\[
\frac{d\mathbf X}{dt}
=\mathcal F_{\mathrm{phase}}(\mathbf X,\mathcal M,\mathcal C,t)
+\text{bruit et correction}.
\]

La source subdivise cette étape en trois dynamiques :

\[
\frac{dC}{dt}
=\kappa_2P(t)\sqrt{C(C_{\max}-C)}\,
\mathcal V_{\mathrm{perseverance}}
\exp\!\left(
-\frac{\lVert\mathcal Val-\mathcal Val_{\mathcal M}\rVert^2}{2\tau^2}
\right),
\]

\[
\frac{dC}{dt}
=\kappa_3M(t)\frac{C}{1+C}
\exp\!\left(-\frac{(C-C_{\mathrm{opt}})^2}{2\sigma^2}\right)
\mathcal P_{\mathrm{fluid}},
\]

\[
\frac{dC}{dt}
=\kappa_4J(t)\log(1+C)\Phi(\mathcal V,\mathcal Val)
\bigl(1+\alpha\lVert\nabla\mathcal E_{\mathrm{context}}\rVert\bigr).
\]

Elles correspondent respectivement à l'imitation, à la maîtrise technique et au jugement contextuel. Les opérateurs propres à ces transformations sont spécifiés dans [Guidance Phase](guidance-phase.md), [Incorporation Phase](incorporation-phase.md) et [Integration Phase](integration-phase.md).

## 4. Épreuve et validation communautaire

La probabilité de réussite de l'épreuve, pour un environnement $e$, est

\[
\mathbb P(\mathrm{success}\mid X,e)
=\sigma\!\left(
\beta_1\Phi_1(X)+\beta_2\Phi_2(X)+\beta_3\Phi_3(X)-\gamma_e
\right).
\]

La validation collective est agrégée par

\[
V_{\mathrm{coll}}
=\frac{1}{|\mathcal C|}\sum_{c\in\mathcal C}
\mathrm{rec}(c,\mathcal D,t).
\]

Le disciple est prêt lorsque

\[
V_{\mathrm{coll}}>\theta_{\mathrm{val}}
\qquad\text{et}\qquad
\Phi_3(X)\geq\Theta_3.
\]

## 5. Sortie et relais

La sortie du pipeline est donnée par

\[
\mathcal R_{\mathrm{init}}(\mathcal D,\mathcal C,t)
=\bigl(\mathcal M_{\mathrm{relais}},S_{\mathrm{trans}},A_{\mathrm{trans}}\bigr),
\]

où $\mathcal M_{\mathrm{relais}}$ est le maître-relais, $S_{\mathrm{trans}}$ le statut de transmission et $A_{\mathrm{trans}}$ l'autorité correspondante. Le maître-relais rejoint le graphe de lignée $G_t$.

La composition globale est résumée par trois opérateurs :

\[
\mathcal E_{\mathrm{entry}}(a,t)
=\mathcal A_{\mathrm{adm}}(a,t)
\circ\mathcal O_{\mathrm{obs}}(a,\mathcal M,t),
\qquad
\mathcal R_{\mathrm{init}}.
\]

La transformation intermédiaire est donnée dans la source par un système couplé sur $\mathbf C$, $\mathbf V$, $\mathbf{Val}$ et $\mathbf P$, avec des termes laissés sous la forme $\dots$ ; ceux-ci ne sont pas complétés ici.

## 6. Automate explicite de la source

Le chapitre formalise explicitement le pipeline par l'automate fini

\[
\mathcal A=(S,\Sigma,\delta,s_0,S_F),
\]

dont les états sont aspirant, imprégnation, apprentissage actif, épreuve, transmission et sortie. Une transition de retour est expressément donnée :

\[
\delta(s_3,\mathrm{failure})=s_2.
\]

Cette transition représente le retour de l'épreuve vers l'apprentissage actif après un échec.

## 7. Limites et points scientifiques non résolus

- Les espaces de $C_p$, $R$, $\mathrm{Mot}$ et $\mathrm{Val}_{\mathrm{init}}$ ne sont pas typés dans la somme définissant $\Phi_{\mathrm{selection}}$.
- Les fonctions $\mathcal F_{\mathrm{phase}}$, $\mathrm{rec}$, $\Phi_1$, $\Phi_2$ et $\Phi_3$ ne sont pas construites dans ce chapitre.
- L'écriture $\mathcal A_{\mathrm{adm}}(a,t)\circ\mathcal O_{\mathrm{obs}}(a,\mathcal M,t)$ compose des sorties sans typer cette composition.
- La source présente d'abord quatre grandes étapes, puis développe sept phases nommées ; elle ne donne pas une bijection formelle complète entre ces deux découpages.
- L'automate énumère ses états, mais ne fournit pas l'ensemble complet des symboles de $\Sigma$ ni toutes les valeurs de $\delta$.
