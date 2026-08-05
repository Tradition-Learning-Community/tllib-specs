# Phase d'initiation

## 1. Reconnaissance mutuelle

La phase commence par deux scores :

\[
S_{\mathcal M}:\mathcal C_{\mathrm{asp}}\times\mathbb R_+\to[0,1],
\qquad
S_{\mathcal D}:\mathcal M\times\mathbb R_+\to[0,1].
\]

La reconnaissance est mutuelle lorsque

\[
S_{\mathcal M}(c,t)\geq\theta_{\mathcal M},
\qquad
S_{\mathcal D}(m,t)\geq\theta_{\mathcal D}.
\]

Les scores sont des agrégations pondérées :

\[
S_{\mathcal M}=\sum_{k=1}^{4}w_k\phi_k,
\qquad
w_k>0,
\qquad
\sum_{k=1}^{4}w_k=1,
\]

où les $\phi_k$ portent sur la réceptivité, le potentiel normatif, la motivation et la compatibilité axiologique ; et

\[
S_{\mathcal D}=\sum_{k=1}^{4}v_k\psi_k,
\qquad
v_k>0,
\qquad
\sum_{k=1}^{4}v_k=1,
\]

où les $\psi_k$ portent sur l'exemplarité du maître, sa compétence normative, sa bienveillance et la cohésion de sa communauté.

La motivation est représentée par un vecteur de $[0,1]^3$. La compatibilité axiologique et l'affinité sont évaluées par des similarités cosinus sur les vecteurs projetés de valeurs et sur les vecteurs de traits. L'affinité doit dépasser son seuil propre.

## 2. Réceptivité et préparation

Les quatre composantes de la réceptivité suivent

\[
\frac{dR_k}{dt}
=r_kR_k\left(1-\frac{R_k}{K_k}\right)
-\sum_{j\neq k}\alpha_{kj}R_kR_j
+\beta_kF_k(\mathcal M,\mathcal D)+\xi_k(t).
\]

Le niveau de préparation est

\[
\Pi
=\lambda\lVert R\rVert
+(1-\lambda)\frac{\lVert C_p\rVert}{\lVert C_p\rVert_{\max}}.
\]

La source impose conjointement des seuils de reconnaissance, de réceptivité, de motivation, de compatibilité axiologique et d'affinité dans son indicateur final de probation.

## 3. Confiance réciproque

Les confiances du maître et du disciple sont couplées :

\[
\begin{aligned}
\frac{dC_{\mathcal M\to\mathcal D}}{dt}
&=\alpha_1\bigl(\mathcal E_{\mathcal D}(t)-C_{\mathcal M\to\mathcal D}\bigr)
+\alpha_2\mathcal F_{\mathrm{loyalty}}(\mathcal D,t)
-\alpha_3\mathbf 1_{\{\mathrm{betrayal}\}}C_{\mathcal M\to\mathcal D},\\
\frac{dC_{\mathcal D\to\mathcal M}}{dt}
&=\beta_1\bigl(\mathcal E_{\mathcal M}(t)-C_{\mathcal D\to\mathcal M}\bigr)
+\beta_2\mathcal B_{\mathcal M}(t)
-\beta_3\mathbf 1_{\{\mathrm{abuse}\}}C_{\mathcal D\to\mathcal M}.
\end{aligned}
\]

$\mathcal E_{\mathcal D}$ et $\mathcal E_{\mathcal M}$ sont les exemplarités du disciple et du maître, $\mathcal F_{\mathrm{loyalty}}$ l'indice de loyauté et $\mathcal B_{\mathcal M}$ la bienveillance perçue. Les fonctions indicatrices modélisent les ruptures de confiance.

## 4. Contrat et opérations initiatiques

Le contrat pédagogique est le sextuplet

\[
\mathcal K
=\bigl(O_{\mathcal M},O_{\mathcal D},M,R,S,P\bigr),
\]

réunissant les objectifs du maître et du disciple, les moyens, les règles, les sanctions et les promesses. La compatibilité des objectifs exige

\[
\lVert O_{\mathcal M}-O_{\mathcal D}\rVert<\varepsilon.
\]

Le rituel d'initiation transforme

\[
\mathcal T_{\mathrm{init}}:
\mathcal D\times\mathcal C\times\mathbb R^+
\longrightarrow\mathcal D'\times\mathcal M_{\mathrm{mem}}.
\]

La phase comprend également un premier enseignement intégré, une première pratique modélisée par une réponse logistique, une évaluation initiale vectorielle et une cérémonie de validation inscrivant le disciple dans $G_t$.

## 5. Limites et points scientifiques non résolus

- La motivation est définie comme un vecteur de $[0,1]^3$, puis intervient comme terme scalaire dans le score sans opérateur d'agrégation indiqué.
- Les normes utilisées dans $\Pi$ ne sont pas définies et le cas $\lVert C_p\rVert_{\max}=0$ n'est pas traité.
- Les similarités cosinus ne sont pas définies lorsque l'un des vecteurs est nul.
- La source ne précise pas les processus générateurs des indicateurs de trahison et d'abus.
- L'évaluation initiale est donnée comme vecteur, sans espace cible ni règle d'agrégation finale.
