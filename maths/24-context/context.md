# Contexte dynamique et adaptation

## 1. Espace contextuel

\[
\mathcal C=\mathcal C_{\text{cultural}}\times
\mathcal C_{\text{social}}\times\mathcal C_{\text{institutional}}
\times\mathcal C_{\text{material}}\times\mathcal C_{\text{symbolic}}
\subset\mathbb R^m\times\mathcal M.
\]

Les facteurs décrivent respectivement Valeurs, croyances, normes et langages ; structures et rapports sociaux ; organisations, lois et procédures ; ressources, techniques et environnement physique ; mythes, récits, figures et objets symboliques. $\mathcal M$ accueille les aspects symboliques non nécessairement vectoriels. Les structures propres à la première et à la cinquième composante sont précisées dans [Culture](../25-culture/culture.md).

## 2. Métrique adaptative

\[
g_c=\sum_{i=1}^mw_i(\mathbf X,t)dx_i\otimes dx_i
+\sum_{i<j}\gamma_{ij}(\mathbf X,t)dx_i\otimes dx_j.
\]

Les $w_i\in\mathbb R^+$ pondèrent l’importance locale des dimensions ; $\gamma_{ij}$ encode leurs interactions. La distance est la longueur géodésique

\[
d_{\mathcal C}(\mathbf c_1,\mathbf c_2)=
\inf_{\gamma(0)=\mathbf c_1,\gamma(1)=\mathbf c_2}
\int_0^1\sqrt{g_c(\dot\gamma(t),\dot\gamma(t))}\,dt.
\]

Les poids évoluent selon

\[
\frac{dw_i}{dt}=\alpha_i(\mathcal E_{\text{contexte}}-w_i)
+\beta_iw_i(1-w_i)
+\gamma_i\nabla_{\mathbf X}w_i\cdot\frac{d\mathbf X}{dt}.
\]

## 3. Couplage tradition–contexte

\[
\begin{cases}
\displaystyle\frac{d\mathbf X}{dt}=\mathbf H(\mathbf X(t),\mathbf c(t),t,\nabla\mathbf c),\\[1em]
\displaystyle\frac{d\mathbf c}{dt}=\mathbf J(\mathbf c(t),\mathbf X(t),t,\nabla\mathbf X)
+\mathbf K(\mathbf c,\mathbf X)(\mathbf c_{\text{opt}}-\mathbf c).
\end{cases}
\]

$\mathbf X$ est l’état de la tradition, $\mathbf c$ celui du contexte, $\mathbf H$ et $\mathbf J$ sont déclarées Lipschitz, $\mathbf K$ est le gain de rappel vers le contexte de référence $\mathbf c_{\text{opt}}$.

La sensibilité différentielle est

\[
\mathcal S_{\text{contexte}}=
\|\nabla_{\mathbf c}\mathbf H\|
+\|\nabla_{\mathbf c}^2\mathbf H\|
+\left\|\frac{\partial\mathbf H}{\partial(\nabla\mathbf c)}\right\|.
\]

La source associe une faible sensibilité aux Principes et Valeurs fondamentales, et une sensibilité plus forte aux Pratiques et à certaines Compétences.

## 4. Adaptation optimale

\[
\mathcal A_{\text{contexte}}(\mathbf X,\mathbf c)=
\mathbf X+\alpha(\mathbf X,\mathbf c,\nabla\mathbf c)
(\mathbf X^*(\mathbf c)-\mathbf X)
+\beta(\mathbf X,\mathbf c)\nabla_{\mathbf c}\mathbf X^*.
\]

$\mathbf X^*(\mathbf c)$ est l’état contextuellement optimal ; le premier terme corrige vers cet état et le second anticipe les changements du contexte.

Si $\mathcal J(\mathbf X,\mathbf c,t)$ est strictement convexe en $\mathbf X$ et si $\nabla_{\mathbf X}\mathbf H$ est inversible, la source affirme l’existence et l’unicité d’une famille optimale telle que

\[
\frac{d\mathbf X^*}{dt}=-(\nabla_{\mathbf X}\mathbf H)^{-1}
\left(\nabla_{\mathbf c}\mathbf H\cdot\frac{d\mathbf c}{dt}
+\frac{\partial\mathbf H}{\partial t}\right).
\]

Un corollaire affirme que si $\mathcal J$ pénalise fortement l’écart aux Valeurs fondamentales, $\mathbf X^*$ reste au voisinage du noyau invariant.

## 5. Métriques

\[
\mathcal P_{\text{ctx}}(\mathbf X,\mathbf c)=
\frac{\mathcal J(\mathbf X,\mathbf c)}
{\mathcal J(\mathbf X^*(\mathbf c),\mathbf c)}\in[0,1],
\]

\[
\Delta_{\text{ctx}}(\mathbf c,\mathbf c_0)=
\frac{d_{\mathcal C}(\mathbf c,\mathbf c_0)}
{\max_{\mathbf c,\mathbf c'}d_{\mathcal C}(\mathbf c,\mathbf c')},
\]

\[
\tau_{\text{adapt}}(\mathbf c)=
\left\|\frac{d\mathbf X^*}{d\mathbf c}\right\|
\left\|\frac{d\mathbf c}{dt}\right\|.
\]

Si $\tau_{\text{adapt}}$ dépasse la capacité du système, la source identifie une crise potentielle sans fixer cette limite.

## 6. Limites et points scientifiques non résolus

- $\mathcal C$ est dite variété différentiable tout en étant incluse dans $\mathbb R^m\times\mathcal M$ avec $\mathcal M$ seulement métrique ; les conditions donnant une structure différentiable au produit ne sont pas précisées.
- Le second terme de $g_c$ n’inclut pas explicitement son symétrique $dx_j\otimes dx_i$ ; aucune condition de symétrie ou de positivité n’est donnée.
- $\mathcal E_{\text{contexte}}$ apparaît comme une même valeur d’équilibre dans toutes les équations de $w_i$, sans typage vectoriel.
- La formule de $d\mathbf X^*/dt$ est présentée comme conséquence de l’optimalité de $\mathcal J$, mais elle utilise le Jacobien de la dynamique $\mathbf H$ sans relation explicite entre $\mathbf H$ et les conditions de premier ordre de $\mathcal J$.
- Si $\mathcal J$ est une fonction de coût minimisée, le rapport $\mathcal P_{\text{ctx}}$ n’est pas nécessairement dans $[0,1]$ et peut être supérieur à 1 ; la convention d’orientation n’est pas résolue.
