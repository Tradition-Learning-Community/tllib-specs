# Cohorte : espace des traits, architecture et dynamique

## 1. Périmètre

Une cohorte n’est pas une simple collection de Disciples. Elle est un collectif structuré dans lequel les relations entre pairs, la composition typologique et la topologie du réseau produisent des propriétés propres : cohésion, diversité, intelligence collective, synergie, robustesse et capacité de régénération.

## 2. Espace des traits disciplinaires

Chaque Disciple est représenté par un vecteur de douze traits, regroupés en quatre familles :

| Famille | Traits |
|---|---|
| cognitive | analytique, intuitif, créatif |
| affective | réceptif, résilient, empathique |
| comportementale | discipliné, explorateur, collaboratif |
| motivationnelle | intrinsèque, extrinsèque, transcendant |

La source définit l’espace des traits par

\[
\mathcal{T} = \mathcal{T}_{\text{cog}} \otimes \mathcal{T}_{\text{aff}} \otimes \mathcal{T}_{\text{beh}} \otimes \mathcal{T}_{\text{mot}} \cong \mathbb{R}^{12},
\]

avec

\[
\begin{aligned}
\mathcal{T}_{\text{cog}} &= \operatorname{span}\{\tau_1^{\text{analytical}},\tau_2^{\text{intuitive}},\tau_3^{\text{creative}}\},\\
\mathcal{T}_{\text{aff}} &= \operatorname{span}\{\tau_4^{\text{receptive}},\tau_5^{\text{resilient}},\tau_6^{\text{empathic}}\},\\
\mathcal{T}_{\text{beh}} &= \operatorname{span}\{\tau_7^{\text{disciplined}},\tau_8^{\text{explorer}},\tau_9^{\text{collaborative}}\},\\
\mathcal{T}_{\text{mot}} &= \operatorname{span}\{\tau_{10}^{\text{intrinsic}},\tau_{11}^{\text{extrinsic}},\tau_{12}^{\text{transcendent}}\}.
\end{aligned}
\]

Les bases sont déclarées orthonormales, $\langle\tau_i,\tau_j\rangle=\delta_{ij}$, et la distance est

\[
d_{\mathcal{T}}(\vec t,\vec t')=\sqrt{\sum_{i=1}^{12}(t_i-t_i')^2}.
\]

Un Disciple $\mathcal D$ possède un profil $\vec t(\mathcal D)\in\mathcal T$ dont chaque coordonnée $t_i$ appartient à $[0,1]$ — ou, selon la formulation ouverte de la source, à un intervalle continu.

## 3. Typologie

Six types sont présentés comme des attracteurs, non comme des classes rigides : Analyst, Intuitive, Pragmatic, Emotive, Willful et Visionary. Un profil réel peut être hybride :

\[
\mathcal{D}_{\text{hybrid}}=\sum_{i=1}^{6}\alpha_i\mathcal{D}_{T_i},
\qquad \sum_i\alpha_i=1,\quad \alpha_i\ge 0,
\]

où $\mathcal D_{T_i}$ est le vecteur représentatif du type pur $i$. La source indique que les coefficients peuvent être obtenus par projection ou apprentissage supervisé, sans fixer de procédure.

Deux mesures comparent les profils :

\[
d_{\text{euclid}}(\mathcal D_1,\mathcal D_2)
=\sqrt{\sum_{i=1}^{12}(t_{1i}-t_{2i})^2},
\]

\[
\operatorname{sim}_{\text{cos}}(\mathcal D_1,\mathcal D_2)
=\frac{\langle\vec t_1,\vec t_2\rangle}{\|\vec t_1\|\,\|\vec t_2\|}.
\]

La distance typologique est donnée par

\[
d_{\text{type}}(T_i,T_j)=\inf_\gamma\int_0^1
\sqrt{g(\dot\gamma(t),\dot\gamma(t))}\,dt
+\lambda\,\|\Phi^{-1}(T_i)-\Phi^{-1}(T_j)\|,
\]

où $\gamma$ est une géodésique dans l’espace des types et $\Phi:\mathcal T\to\mathcal M_{\text{types}}$ l’application de classification.

Pour $\mathcal C=\{\mathcal D_1,\ldots,\mathcal D_n\}$, l’indice de diversité est

\[
H_{\text{type}}(\mathcal C)
=-\sum_{i=1}^{6}p_i\log p_i
+\alpha\,\mathbb E\!\left[d_{\text{type}}(\mathcal D_i,\mathcal D_j)\right],
\]

où $p_i$ est la proportion du type $i$ et $\alpha>0$ un coefficient de calibration.

## 4. Définition algébrique et topologie

Une cohorte est le quintuple

\[
\mathcal C=(D,R,\circ,\sim,G),
\]

où $D\subset\mathbb D$ est l’ensemble des Disciples, $R\subseteq D\times D$ une relation d’apprentissage, $\circ:D\times D\to D$ une opération de collaboration, $\sim$ une relation d’équivalence d’affinité, de niveau ou de rôle, et $G=(V,E,w)$ un graphe valué. $(D,\circ)$ est un magma, en général non associatif, et $\sim$ partitionne $D$ en classes d’affinité.

Dans $G$, $V=D$, $E\subseteq V\times V$ et $w:E\to\mathbb R^+$ mesure l’intensité relationnelle. Si $A$ est la matrice d’adjacence pondérée :

- $\deg(v)=\sum_u A_{vu}$ ;
- $L=D-A$, avec ici $D=\operatorname{diag}(\deg(v))$ ;
- $\lambda_2(L)>0$ est la condition de non-fragmentation ;
- le diamètre vaut $\operatorname{diam}(G)=\max_{u,v}d(u,v)$.

La cohésion combine connectivité spectrale et diversité typologique :

\[
\kappa(\mathcal C)=\frac{\lambda_2(L)}{\lambda_n(L)}
\cdot\frac1{|D|}\sum_{i=1}^{6}p_i(1-p_i),
\]

avec une zone optimale $[\kappa_{\min},\kappa_{\max}]$.

## 5. Dynamiques

La distribution $P(\vec t,t)$ des profils suit l’équation de Fokker–Planck

\[
\frac{\partial P}{\partial t}
=-\nabla\cdot[\vec F(\vec t)P]
+\frac12\nabla^2[\Sigma(\vec t)P],
\]

avec

\[
\vec F(\vec t)
=\alpha(\vec\mu_{\mathcal M}-\vec t)
+\beta\,\mathbb E_{\text{pair}}[\vec t_{\text{pair}}-\vec t].
\]

$\vec\mu_{\mathcal M}$ est le profil du Maître ; le premier terme attire vers ce profil, le second vers les pairs ; $\Sigma$ représente les fluctuations et explorations individuelles, généralement anisotropes.

Sous des conditions de régularité et de bornitude, et lorsque la contribution des pairs est symétrique,

\[
P_\infty(\vec t)\propto
\exp\!\left(-\frac{2}{\sigma^2}V(\vec t)\right),
\qquad
V(\vec t)=\frac\alpha2\|\vec t-\vec\mu_{\mathcal M}\|^2.
\]

Une influence dominante des pairs peut provoquer une bifurcation et une polarisation en sous-groupes ; la source renvoie à une condition sur les valeurs propres du système linéarisé sans la donner.

Les proportions typologiques évoluent selon

\[
\frac{dp_i}{dt}
=\alpha_i p_i(1-p_i)+\sum_{j\ne i}\beta_{ij}p_j
-\gamma_i p_i+\eta_i(t),
\]

où $\alpha_i$ est le taux d’auto-renforcement, $\beta_{ij}$ le taux de conversion de $j$ vers $i$, $\gamma_i$ le taux de perte et $\eta_i$ le bruit de recrutement ou de départ. La stabilité des points fixes $\mathbf p^*$ s’analyse par le Jacobien.

## 6. Propriétés émergentes et santé

L’intelligence collective est définie par

\[
I_{\text{coll}}(\mathcal C)
=\sum_{i=1}^{6}\omega_i p_i
+\alpha\kappa(\mathcal C)
+\beta H_{\text{type}}(D)
+\gamma\mathbb E[d_{\text{type}}],
\]

et la synergie par

\[
S(\mathcal C)=I_{\text{coll}}(\mathcal C)
-\sum_{i=1}^{6}p_iI_{\text{indiv}}(T_i).
\]

La source affirme que $S(\mathcal C)>0$ apparaît si et seulement si

\[
H_{\text{type}}(D)>H_{\text{crit}},\qquad
\kappa_{\min}<\kappa(\mathcal C)<\kappa_{\max},\qquad
\mathbb E[\text{complementarity}]>\theta_{\text{comp}}.
\]

La robustesse est mesurée par

\[
R(\mathcal C)=\min_{\Delta\mathbf p}
\left\|\frac{\partial I_{\text{coll}}}{\partial\mathbf p}\right\|^{-1}
+\lambda\rho(\nabla^2I_{\text{coll}}),
\]

où $\rho$ est le rayon spectral du Hessien.

La probabilité de formation d’un lien entre types et l’efficacité de l’interaction sont

\[
P(A_{ij}=1\mid \operatorname{type}_i=T_k,\operatorname{type}_j=T_l)
=\frac{\exp(\theta_{kl})}{1+\exp(\theta_{kl})},
\]

\[
\eta_{kl}(P)=\eta_{\text{base}}(P)
+\alpha_{kl}d_{\text{type}}(T_k,T_l)
+\beta_{kl}\operatorname{comp}(T_k,T_l).
\]

La matrice de performance est $\mathcal P=\Theta\circ\mathcal H$. L’indice de santé est

\[
H_{\text{health}}(\mathcal C)
=\kappa(\mathcal C)H_{\text{type}}(D)
\mathbb E[\eta_{kl}]S(\mathcal C).
\]

Les alertes explicites sont : $H_{\text{type}}<H_{\min}$, $\kappa<\kappa_{\min}$, $\kappa>\kappa_{\max}$ ou $S(\mathcal C)<0$.

## 7. Théorèmes formulés par la source

- **Convergence sous guidage.** Sous régularité et bruit borné, la distribution des profils converge vers une distribution stationnaire centrée sur $\vec\mu_{\mathcal M}$. Des interactions symétriques et une diversité initiale non nulle permettent plusieurs équilibres typologiques.
- **Stabilité d’une configuration.** $(\mathbf p^*,A^*)$ est asymptotiquement stable si le Jacobien de la composition a ses valeurs propres à partie réelle négative, si $\lambda_2(L)>0$ et si $H_{\text{type}}$ reste dans une zone de stabilité.
- **Émergence de l’intelligence collective.** Sous les trois conditions d’émergence ci-dessus, la synergie croît avec la diversité jusqu’à un optimum puis décroît.

## 8. Limites et points scientifiques non résolus

- Le produit tensoriel de quatre espaces tridimensionnels a dimension $3^4=81$, alors que la source l’identifie à $\mathbb R^{12}$. Cette incohérence est conservée sans correction.
- Les centres des six types, l’application $\Phi$, sa préimage, la métrique $g$ de l’espace des types et la méthode d’estimation des $\alpha_i$ ne sont pas spécifiés.
- L’équation de Fokker–Planck ne précise pas la nature tensorielle de $\Sigma$ ni les conditions aux limites ; le seuil spectral de bifurcation n’est pas donné.
- Les coefficients, seuils et intervalles optimaux sont laissés à calibrer. $H_{\text{health}}$ n’est pas normalisé dans la source malgré l’interprétation « proche de 1 ».
- Dans $H_{\text{type}}$, la distance est écrite entre $\mathcal D_i$ et $\mathcal D_j$ alors que $d_{\text{type}}$ est défini sur les types $T_i,T_j$.
