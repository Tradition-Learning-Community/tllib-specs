# Système de transmission en cascade

## 1. Définition

Un système de transmission en cascade est un mécanisme de propagation et de préservation par lequel un contenu vivant — message, pratique ou valeur — traverse des générations successives de Maîtres et de Disciples, en maintenant un noyau invariant tout en autorisant des adaptations contextuelles.

Il est défini comme le 12-uplet

\[
\mathcal{TC}=(\mathcal G_L,\mathcal G_D,\mathcal F,\mathcal P,
\mathcal R,\mathcal C,\mathcal A,\mathcal S,\mathcal M,
\mathcal E,\mathcal T,\mathcal V),
\]

où $\mathcal G_L$ est le graphe temporel de lignée, $\mathcal G_D$ le graphe doctrinal, $\mathcal F$ la fonction de filiation, $\mathcal P$ le processus de préservation, $\mathcal R$ le système de régulation, $\mathcal C$ le conseil des anciens, $\mathcal A$ l’architecture d’adaptation, $\mathcal S$ le spectre des seuils critiques, $\mathcal M$ les mécanismes de mesure, $\mathcal E$ l’environnement socioculturel, $\mathcal T$ la temporalité multi-échelle et $\mathcal V$ l’espace des valeurs fondatrices.

> **Convention de notation.** La source réutilise notamment $\mathcal F$ pour la filiation, la fusion et une variable de fidélité, ainsi que $\mathcal R$ pour le système et l’opérateur de régulation. Chaque occurrence conserve ici le sens défini dans sa section.

La transitivité est contrôlée : un récepteur ne devient émetteur qu’après validation. Les transformations sont locales au contexte, préservent un noyau essentiel et disposent d’une marge créative.

## 2. Axiomes

### 2.1 Conservation de l’essentiel dynamique

Pour tout $t>0$, il existe $\mathcal N^*(t)$ tel que

\[
\mu(\mathcal N^*(t))>\mu_{\min},\qquad
\forall v\in V_L,\quad
d_D(\pi_{\mathcal N}(x_v(t)),\mathcal N^*(t))<\epsilon(t),
\]

avec $\epsilon(t)=\epsilon_0e^{-\lambda t}$.

### 2.2 Adaptation nécessaire guidée

\[
\frac{d\mathcal G_D}{dt}
=\alpha(\mathcal E_{\text{context}}-\mathcal G_D)
+\beta\mathcal G_D\times(\mathcal E_{\text{context}}-\mathcal G_D)
+\gamma\nabla\mathcal C
+\delta\mathcal V(\mathcal G_D-\mathcal G_{D,\text{opt}}).
\]

### 2.3 Autorégulation collective distribuée

\[
\mathcal R(t)=\mathcal R_{\text{self}}+\mathcal R_{\text{peers}}
+\mathcal R_{\text{elders}}+\mathcal R_{\text{comm}}+\mathcal R_{\text{env}},
\]

avec $d\mathcal R/dt>0$ lorsque $d_D>\theta_{\text{alert}}$ et $\mathcal R\circ\mathcal V>\mathcal R_{\min}$.

### 2.4 Transmission fidèle-créative

\[
\frac{d\mathcal F}{dt}
=\lambda(\mathcal F_{\text{faithful}}-\mathcal F)
+\mu\mathcal F\times(\mathcal F_{\text{creative}}-\mathcal F)
+\nu\nabla\mathcal E\cdot\mathcal F
+\xi\mathcal V\cdot\mathcal F.
\]

### 2.5 Légitimité dynamique

\[
\mathcal L(\mathcal C,t)
=\mathcal L_{\text{hist}}e^{-\alpha t}
+\mathcal L_{\text{comp}}(1-e^{-\beta t})
+\mathcal L_{\text{recog}}\mathcal E(t),
\]

avec $\mathcal L(\mathcal C,t)>\mathcal L_{\min}$ pour tout $t$.

## 3. Espace de filiations et graphes

\[
\mathcal{FS}=\mathcal G_L\otimes\mathcal G_D\otimes\mathcal F
\otimes\mathcal T\otimes\mathcal V,
\qquad
g_{\mathcal{FS}}=g_L\oplus g_D\oplus d\mathcal F\oplus d\mathcal T\oplus d\mathcal V.
\]

Les graphes sont

\[
\mathcal G_L=(V_L,E_L,w_L,t_L),\qquad
w_L(e)=e^{-\lambda\operatorname{generation}(e)}\phi(t_L(e)),
\]

\[
\mathcal G_D=(V_D,E_D,w_D,\phi_D),\qquad
w_D(e)=e^{-d_D(x_{v_i},x_{v_j})}
\psi(\phi_D(v_i),\phi_D(v_j)).
\]

La superposition est

\[
\mathcal G_{\text{total}}=\mathcal G_L\cup\mathcal G_D\cup\mathcal G_{\mathcal V},
\qquad d_{\text{total}}=\min(d_L,d_D,d_{\mathcal V}).
\]

Elle fait apparaître des communautés multi-critères, des ponts adaptatifs de forte centralité d’intermédiarité et forte confiance, et des isolants dynamiques de degré faible et décroissant.

## 4. Opérateurs

### 4.1 Ramification

\[
\mathcal B:V_L\times\mathcal X_{\text{doct}}\times\mathbb R^+
\times\mathcal E\times\mathcal V
\to E_L'\times V_L'\times[0,1]_{\text{leg}},
\]

sur le domaine

\[
\{(v,x,t,\mathcal E,\mathcal V)\mid
d_D(x_v,x)>\theta_{\text{ram}}(t),\ t>t_{\text{mat}}(v),\
\mathcal E\in\mathcal E_{\text{fav}},\ \mathcal V\text{ coherent}\}.
\]

L’opérateur est non linéaire avec mémoire, contractif dans les zones stables, expansif aux frontières et préservant les valeurs.

### 4.2 Fusion

\[
\mathcal F:\mathcal P(V_L)\times\mathcal P(V_D)\times\mathbb R^+
\times\mathcal E\times\mathcal V
\to\mathcal P(V_L')\times\mathcal P(V_D')\times\mathbb R^+_{\text{syn}},
\]

\[
\frac{d\mathcal F}{dt}
=\alpha\min_{v_i\in C_1,v_j\in C_2}d_D(x_{v_i},x_{v_j})
+\beta\mathcal R_{\text{comm}}
-\gamma\operatorname{diam}(C_1\cup C_2)
+\delta\mathcal V(C_1,C_2)+\epsilon\mathcal E_{\text{conv}}.
\]

### 4.3 Préservation

\[
\mathcal P:\mathcal X_{\text{doct}}\times\mathcal N_{\text{inv}}
\times\mathbb R^+\times\mathcal E\times\mathcal V
\to\mathcal X_{\text{doct}}'\times[0,1]_{\text{fid}}
\times[0,1]_{\text{adapt}},
\]

\[
\mathcal P(x,\mathcal N,t,\mathcal E,\mathcal V)
=\pi_{\mathcal N}(x)
+\alpha(t,\mathcal E)(x-\pi_{\mathcal N}(x))
\mathbf1_{\{d_D(x,\mathcal N)<\delta_{\max}(t)\}}
+\beta(\mathcal V)\nabla\mathcal E\cdot x.
\]

### 4.4 Régulation

\[
\mathcal R:\mathcal G_{\text{total}}\times\mathcal X_{\text{doct}}
\times\mathcal S_{\text{thresh}}\times\mathcal E\times\mathcal V
\to\Delta\mathcal G_{\text{total}}\times\Delta\mathcal X_{\text{doct}}
\times\mathbb R^+_{\text{corr}},
\]

\[
\frac{d\mathcal R}{dt}
=\lambda(\mathcal X_{\text{obs}}-\mathcal X_{\text{des}})
+\mu\mathcal R\times(\mathcal X_{\text{obs}}-\mathcal X_{\text{des}})
+\nu\nabla\mathcal C+\xi\mathcal E\cdot\mathcal R
+\pi\mathcal V\cdot\mathcal R.
\]

## 5. Préservation de l’essentiel

\[
\mathcal N_{\text{inv}}(t)=\{x\in\mathcal X_{\text{doct}}\mid
\forall\tau\in[0,t],\forall v\in V_L,
d_D(\pi_{\mathcal N}(x_v(\tau)),x)<\epsilon_{\text{ess}}(\tau),
\ \mathcal V(x)>\theta_{\mathcal V}\},
\]

\[
\mathcal E_{\text{adapt}}(t)=\{x\in\mathcal X_{\text{doct}}\mid
d_D(x,\mathcal N_{\text{inv}}(t))<\delta_{\text{adapt}}(t,\mathcal E),
\ d\mathcal J/dx>0\},
\]

\[
\partial\mathcal E_{\text{adapt}}(t)=\{x\mid
d_D(x,\mathcal N_{\text{inv}}(t))=\delta_{\text{adapt}}(t,\mathcal E),
\ \|\nabla\mathcal V(x)\|<\eta_{\text{crit}}\}.
\]

Le conseil des anciens, les rituels adaptatifs et l’auto-surveillance collective sont respectivement typés par

\[
\mathcal C(t):\mathcal P(V_L)\times\mathbb R^+\times\mathcal X_{\text{doct}}
\times\mathcal E\times\mathcal V
\to\{0,1\}_{\text{val}}\times\mathbb R^+_{\text{conf}}\times\mathcal P_{\text{reco}},
\]

\[
\mathcal T_{\text{rit}}:V_L\times V_L\times\mathcal X_{\text{doct}}
\times\mathbb R^+\times\mathcal E\times\mathcal V
\to\mathcal X_{\text{doct}}'\times[0,1]_{\text{fid}}\times[0,1]_{\text{impact}},
\]

\[
\mathcal A_{\text{auto}}:V_L\times\mathcal X_{\text{doct}}
\times\mathcal N_{\text{inv}}\times\mathcal E\times\mathcal V
\to\mathbb R^+_{\text{corr}}\times\mathcal P_{\text{al}}\times\mathcal P_{\text{innov}}.
\]

## 6. Théorèmes formulés par la source

- **Conservation de l’essentiel dynamique.** Si le noyau est non vide et de mesure supérieure à $\mu_{\min}$, si la régulation est opérationnelle et complète, si le conseil est représentatif, compétent et légitime, et si les valeurs sont cohérentes et préservées, alors le noyau demeure de mesure supérieure à $\mu_{\min}$ et les valeurs restent au-dessus de $\theta_{\mathcal V}$.
- **Équilibre fidélité–adaptation–création.** Il existe un optimum $(\alpha^*,\delta^*,\gamma^*)$ maximisant
  \[
  \mathcal J=\mathcal F_{\text{fid}}(\alpha)
  +\lambda\mathcal A_{\text{adapt}}(\delta)
  +\mu\mathcal C_{\text{crea}}(\gamma)
  -\nu\mathcal R_{\text{comp}}(\alpha,\delta,\gamma),
  \]
  sous concavité des coûts et compacité de l’ensemble admissible.
- **Résilience adaptative.** Pour $\|\mathcal P\|<\epsilon$,
  \[
  \tau_{\text{rec}}<\frac1{\lambda_2(\mathcal L)}
  \left(1+\frac{\|\nabla\mathcal V\|}{\|\mathcal V\|}
  +\frac{\|\nabla\mathcal E\|}{\|\mathcal E\|}\right).
  \]

## 7. Système dynamique complet

\[
\begin{cases}
\displaystyle\frac{d\mathcal G_L}{dt}=\alpha\mathcal B(\mathcal G_L,\mathcal E,\mathcal V)-\beta\mathcal F(\mathcal G_L,\mathcal E,\mathcal V)+\gamma\mathcal R(\mathcal G_L,\mathcal E,\mathcal V)+\delta\nabla\mathcal E\cdot\mathcal G_L,\\[1em]
\displaystyle\frac{d\mathcal G_D}{dt}=-\mathcal L_D\mathcal G_D+\delta(\mathcal E_{\text{ctx}}-\mathcal G_D)+\epsilon\nabla\mathcal C+\zeta\mathcal V\cdot(\mathcal G_D-\mathcal G_{D,\text{opt}})+\eta\nabla\mathcal E\cdot\mathcal G_D,\\[1em]
\displaystyle\frac{d\mathcal F}{dt}=\theta(\mathcal G_L-\mathcal G_D)\cdot\mathcal F\cdot(1-\mathcal F)+\iota\mathcal V\cdot\mathcal F+\kappa\nabla\mathcal E\cdot\mathcal F,\\[1em]
\displaystyle\frac{dx_v}{dt}=\eta\sum_{u\in N(v)}w_{uv}(x_u-x_v)+\xi(v)(x_{\mathcal M(v)}-x_v)+\sigma dW_v+\tau\mathcal V\cdot\nabla\mathcal E\cdot x_v,\\[1em]
\displaystyle\frac{dp_i}{dt}=p_i\left(r_i-\sum_j a_{ij}p_j\right)+\mu_i\nabla\mathcal E_{\text{ctx}}+\nu_i\mathcal V\cdot p_i(1-p_i).
\end{cases}
\]

Les attracteurs nommés sont l’orthodoxie vivante stable, l’hétérodoxie créative contrôlée, le schisme constructif établi, l’orthodoxie sclérosée et l’hétérodoxie destructive. La source associe notamment $\mathcal F\approx1$ à l’orthodoxie, $\mathcal F\in(0.7,0.9)$ à l’hétérodoxie contrôlée et $\mathcal F<0.5$ au schisme constructif si $\mathcal V>\theta_{\mathcal V}$.

## 8. Métriques de santé

\[
\mathcal C_{\text{coh}}=1-\frac1{|V_L|}\sum_{v\in V_L}
d_D(x_v,\pi_{\mathcal N}(x_v))
\exp\!\left(-\lambda\frac{\|\nabla\mathcal V(x_v)\|}{\|\mathcal V(x_v)\|}\right),
\]

\[
\mathcal D_{\text{div}}=\frac1{|V_D|}\sum_{C\in\operatorname{comm}(\mathcal G_D)}|C|\log|C|
+\alpha\mathbb E[d_D(x_i,x_j)]+\beta\mathcal V_{\text{div}}(C)+\gamma\mathcal E_{\text{rich}}(C),
\]

\[
\mathcal R_{\text{res}}=\lambda_2(\mathcal L_{\text{total}})
\min_{v\in V_L}\deg(v)\,\mathcal C_{\text{coh}}
\left(1+\frac{\|\mathcal V\|}{\|\mathcal V_{\max}\|}
+\frac{\|\mathcal E\|}{\|\mathcal E_{\max}\|}\right),
\]

\[
\eta_{\text{trans}}=\frac1T\int_0^T
\frac{\sum_{v\in V_L}\mathcal F(v)e^{-\lambda\operatorname{gen}(v)}
\mathcal V(x_v)\mathcal E_{\text{qual}}(v)}
{\sum_{v\in V_L}e^{-\lambda\operatorname{gen}(v)}}\,dt,
\]

\[
\mathcal V_{\text{vit}}=\frac{d|V_L|}{dt}\mathcal C_{\text{coh}}
+\alpha\nu_{\text{innov}}+\beta\pi_{\text{perm}}
+\gamma\frac{d\mathcal V}{dt}+\delta\frac{d\mathcal E}{dt},
\]

\[
\mathcal I_{\text{imp}}=
\frac{|\partial\mathcal G_{\text{total}}\cap\mathcal E_{\text{soc}}|}
{|\partial\mathcal G_{\text{total}}|}
\mathbb E[\mathcal F(\partial\mathcal G_{\text{total}})]
\mathcal V_{\text{contrib}}(\partial\mathcal G_{\text{total}})
\mathcal E_{\text{reconn}}(\partial\mathcal G_{\text{total}}).
\]

## 9. Limites et points scientifiques non résolus

- $\mathcal F$ désigne successivement la fonction de filiation, l’opérateur de fusion et une variable dynamique de fidélité ; la source ne désambiguïse pas ces usages.
- $\mathcal G_D$ est défini comme un graphe, mais plusieurs équations lui appliquent soustraction, produit, gradient et dérivation sans définir l’espace vectoriel ou la représentation correspondante.
- La métrique $g_{\mathcal{FS}}$ additionne des métriques et des différentielles ($d\mathcal F$, $d\mathcal T$, $d\mathcal V$) sans préciser leur type tensoriel.
- Les fonctions, projections, distances, mesures, coûts, seuils et coefficients de calibration ne sont généralement pas construits. Les valeurs numériques des attracteurs sont conservées telles quelles et ne sont pas justifiées dans le chapitre.
- L’esquisse de preuve de conservation invoque une norme entre ensembles dépendant du temps et une dérivée négative sans définir cette norme ni établir les hypothèses nécessaires.
