# Équité, biais et pluralité des perspectives

## 1. Définition et portée

L’équité désigne la capacité du système à distribuer justement l’accès, la reconnaissance et les bénéfices de la transmission, sans confondre justice et uniformité. La robustesse procédurale est définie par

\[
\mathcal R_{\text{proc}}=1-
\max_{j\in\mathcal J}\left|
\mathbb E_{d\in\mathbb D}[S(d,j)]-\mathbb E_{d\in\mathbb D}[S(d)]
\right|\mathcal C_{\text{trans}}\mathcal V_{\text{just}}.
\]

$S(d,j)$ est le score d’un Disciple $d$ relativement à la catégorie $j$ ; $\mathcal C_{\text{trans}}$ et $\mathcal V_{\text{just}}$ représentent transparence et justice.

## 2. Espace et mesure des biais

\[
\mathcal B_{\mathcal T}=\mathcal B_{\text{stat}}
\times\mathcal B_{\text{algo}}\times\mathcal B_{\text{cult}}
\times\mathcal B_{\text{cog}}\times\mathcal B_{\text{trad}}
\subset\mathbb R^5.
\]

\[
\beta_{\mathcal T}=\sum_{i=1}^5w_i\beta_i
+\lambda\sum_{i\ne j}\operatorname{Corr}(\beta_i,\beta_j)
+\mu\mathcal D_{\text{trad}}(\beta).
\]

La correction d’une décision $y$ conditionnée par $z$ est

\[
f_{\text{corr}}^{\mathcal T}(y,z)=y
\left(1+\alpha(z)(\mathbb E[y\mid z]-\mathbb E[y])\right)^{-1}
\mathcal F_{\text{fid}}(z)\mathcal A\text{lig}(z,\mathcal T).
\]

## 3. Optimisation sous contraintes d’équité

\[
\begin{aligned}
\min_\theta\quad&\mathbb E[\mathcal L(\theta)]
+\lambda\mathcal D_{\text{trad}}(\theta)\\
\text{s.t.}\quad&\beta_{\text{dem}}(\theta)\le\epsilon_1,
\quad\beta_{\text{opp}}(\theta)\le\epsilon_2,
\quad\beta_{\text{indiv}}(\theta)\le\epsilon_3,\\
&\mathcal R_{\text{perf}}(\theta)\ge\theta_{\min},
\quad\mathcal F_{\text{fid}}(\theta)\ge\phi_{\min}.
\end{aligned}
\]

La source donne le lagrangien

\[
\mathcal L_{\text{fair}}^{\mathcal T}(\theta,\lambda)
=\mathcal L(\theta)+\sum_{i=1}^3\lambda_i(\beta_i(\theta)-\epsilon_i)
+\mu(\mathcal R_{\text{perf}}(\theta)-\theta_{\min})
+\nu(\mathcal F_{\text{fid}}(\theta)-\phi_{\min}).
\]

## 4. Pluralité des Maîtres

Les avis sont pondérés par crédibilité historique, diversité et alignement :

\[
w_i^{\mathcal T}\propto P(M_i\mid\mathcal D)
\exp\!\left(-\lambda D_{\text{KL}}(P(\mathcal D\mid M_i)
\|P(\mathcal D\mid M_{\text{pool}}))\right)
\mathcal D_{\text{div}}(M_i)\mathcal A\text{lig}(M_i,\mathcal T).
\]

\[
\hat y_{\mathcal T}=\arg\max_y\left(
\sum_{i=1}^kw_i^{\mathcal T}P(y\mid M_i,x)
+\alpha\operatorname{Entropy}(\{P(y\mid M_i,x)\})
+\beta\mathcal A\text{lig}(y,\mathcal T)\right).
\]

La diversité cognitive et la complémentarité sont

\[
\mathcal D_{\text{cog}}^{\mathcal T}=
\frac1{\binom{k}{2}}\sum_{i<j}\left[
D_{\text{KL}}(P(y\mid M_i)\|P(y\mid M_j))
+\alpha d_{\text{persp}}(M_i,M_j)
+\beta\mathcal D_{\text{trad}}(M_i,M_j)\right],
\]

\[
\mathcal C_{\text{comp}}^{\mathcal T}=
\frac{\mathcal P_{\text{collect}}-\max_i\mathcal P_i}
{\sum_i\mathcal P_i}
\mathcal D_{\text{cog}}^{\mathcal T}
\mathcal A\text{lig}_{\text{collect}}.
\]

## 5. Responsabilité et alignement éthique

\[
\mathcal L_{\text{align}}^{\mathcal T}(\theta)
=\mathcal L_{\text{task}}(\theta)+\lambda\sum_iv_i(\theta)
+\mu\sum_jg_j(\theta)+\nu\mathcal R_{\text{eth}}(\theta)
+\xi\mathcal D_{\text{trad}}(\theta),
\]

avec les contraintes dynamiques

\[
g_j^{\mathcal T}(\theta,t)=g_j^0(\theta)
+\alpha_j(t)\frac{dg_j}{dt}
+\beta_j(t)\nabla_{\mathcal T}g_j\le0.
\]

\[
\mathcal E_{\text{align}}^{\mathcal T}=
\frac1m\sum_{j=1}^m\mathbf1_{\{g_j^{\mathcal T}(\theta)\le0\}}
\left(\frac{\partial v}{\partial\theta}\cdot
\frac{\partial\mathcal L_{\text{task}}}{\partial\theta}\right)
e^{-\lambda\|g_j^{\mathcal T}(\theta)\|}
\mathcal A\text{lig}(\theta,\mathcal T),
\]

\[
\mathcal R_{\text{resp}}^{\mathcal T}=
\frac1T\int_0^T\left\|
\frac{d\mathcal E_{\text{align}}^{\mathcal T}}{dt}\right\|
\mathbf1_{\{\mathcal E_{\text{align}}^{\mathcal T}>\theta\}}
\mathcal F_{\text{fid}}(t)\,dt.
\]

## 6. Propriété asymptotique et mesure contextuelle

Sous correction adaptative, la source affirme

\[
\beta_{\mathcal T}(t)\le\beta_0e^{-\lambda t}
+\beta_\infty^{\mathcal T},
\]

où $\beta_\infty^{\mathcal T}$ représente un biais résiduel attribué aux différences légitimes.

L’équité contextuelle est

\[
\mathcal E_{\text{ctx}}^{\mathcal T}=
\min_{c\in\mathcal C}
\frac{\mathcal P(c)}{\max_{c'}\mathcal P(c')}
\frac{\mathcal F_{\text{fid}}(c)}{\mathcal F_{\text{fid}}^{\max}}
\frac{\mathcal A\text{lig}(c,\mathcal T)}{\mathcal A\text{lig}_{\max}}.
\]

Le seuil opérationnel déclaré est $\mathcal E_{\text{ctx}}^{\mathcal T}>0.6$.

## 7. Limites et points scientifiques non résolus

- Les cinq composantes de biais, les catégories $\mathcal J$, les scores $S$, la transparence et la justice ne sont pas opérationnalisés dans le chapitre.
- $\mathcal R_{\text{proc}}$ n’est pas garanti dans $[0,1]$ : les facteurs multiplicatifs et l’écart maximal ne sont pas bornés.
- La correction $f_{\text{corr}}^{\mathcal T}$ est singulière lorsque son dénominateur s’annule ; aucune condition d’existence n’est donnée.
- Pour un problème de minimisation, les termes associés aux contraintes $\mathcal R_{\text{perf}}\ge\theta_{\min}$ et $\mathcal F_{\text{fid}}\ge\phi_{\min}$ apparaissent avec le signe $(\text{valeur}-\text{minimum})$ ; la source ne précise ni le signe des multiplicateurs ni la convention duale.
- L’entropie des avis est ajoutée dans un $\arg\max$ sans préciser si la diversité doit être récompensée ou pénalisée. La normalisation des poids $w_i^{\mathcal T}$ n’est pas fournie.
- Le biais résiduel « légitime » et les seuils $0.6$, $\epsilon_i$, $\theta_{\min}$ et $\phi_{\min}$ ne sont ni dérivés ni calibrés.
