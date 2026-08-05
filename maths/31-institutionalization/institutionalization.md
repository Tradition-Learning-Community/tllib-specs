# Institutionnalisation de la tradition

## 1. Formalisation des enseignements

Le passage de l’oral à l’écrit est modélisé par

\[
\mathcal Cod_{\text{écrit}}(\mathcal{M}sg_{\text{oral}})=
\arg\min_{\mathcal{T}xt}\left(
\|\pi_{\mathcal N}(\mathcal{T}xt)-
\pi_{\mathcal N}(\mathcal{M}sg_{\text{oral}})\|^2
+\lambda\|\mathcal{T}xt-\mathcal{T}xt_{\text{ref}}\|^2\right).
\]

La codification diminue le taux de variation $\|\boldsymbol\varepsilon\|$ mais augmente la rigidité. Une Pratique codifiée est une séquence d’actions dotée d’une grammaire formelle ; sa fidélité est sa distance à la séquence canonique.

Un curriculum est un graphe orienté acyclique dont les sommets sont des jalons portant des objectifs sur les huit dimensions et dont les arcs sont les prérequis. L’efficacité se mesure par le taux de réussite et le temps moyen d’accès à la maîtrise.

## 2. Stabilisation doctrinale

Le canon est

\[
\mathcal K=\mathcal S(\mathcal W)=
\{w\in\mathcal W\mid\mathcal Aut(w)>\theta_{\text{aut}}\}.
\]

$\mathcal W$ est l’ensemble des écrits et $\mathcal Aut$ leur mesure d’authenticité.

Les dogmes forment $\mathcal Dog\subset\mathcal N_{\text{inv}}$. La distance d’une interprétation est

\[
\delta_{\text{dog}}(\mathbf X)=
\max_{d\in\mathcal Dog}\|\pi_d(\mathbf X)-d\|.
\]

L’orthodoxie exige $\delta_{\text{dog}}<\epsilon_{\text{dog}}$. Une position est déclarée hérétique si $\delta_{\text{dog}}>\epsilon_{\text{hér}}$ persiste après correction ; l’exclusion retire alors le transmetteur du graphe de transmission.

## 3. Différenciation des rôles

\[
\mathcal R=\{\text{priest},\text{doctor},\text{administrator},\ldots\},
\qquad
\phi:V_t\to\mathcal R.
\]

Chaque rôle $r$ porte des Compétences minimales $\mathbf C_r^{\min}$, des Valeurs privilégiées $\mathbf{Val}_r$ et des Vertus requises $\mathbf V_r$. L’affectation satisfait

\[
\mathbf C(v)\ge\mathbf C_{\phi(v)}^{\min},
\quad
\langle\mathbf{Val}(v),\mathbf{Val}_{\phi(v)}\rangle
\ge\theta_{\text{val}},
\quad
\|\mathbf V(v)-\mathbf V_{\phi(v)}\|\le\epsilon_{\text{vert}}.
\]

Les prêtres gardent le rite, les docteurs le sens et les administrateurs la structure. La diversité des rôles est mesurée par un indice de Shannon et doit rester équilibrée.

## 4. Bureaucratisation et capture

\[
\mathcal B=\frac{N_{\text{rules}}}{\tau_{\text{adapt}}}.
\]

$N_{\text{rules}}$ est le nombre de règles et $\tau_{\text{adapt}}$ le taux d’adaptation tel que nommé dans la source. La concentration d’autorité est

\[
G_{\mathcal A}=
\frac{\sum_{i,j}|\mathcal A_i-\mathcal A_j|}
{2n\sum_i\mathcal A_i}.
\]

Une institution échoue lorsqu’elle rigidifie ses règles, concentre le pouvoir ou oublie la finalité de la transmission.

## 5. Réforme et équilibre structure–vie

\[
\mathcal R_{\text{ref}}(\mathcal X)=\mathcal X'
\quad\text{tel que}\quad
\mathcal B'<\mathcal B,
\ G_{\mathcal A}'<G_{\mathcal A},
\ \|\pi_{\mathcal N}(\mathcal X')-
\pi_{\mathcal N}(\mathcal X_{\text{orig}})\|\le\epsilon_{\text{ref}}.
\]

Si $\mathcal B(t)>\mathcal B_{\text{crit}}$ ou $G_{\mathcal A}(t)>G_{\text{crit}}$ durablement, la source affirme la nécessité de réformes périodiques, avec

\[
T_{\text{ref}}=\frac1\lambda
\ln\!\left(\frac{\mathcal B_{\max}-\mathcal B_{\min}}
{\mathcal B_{\text{seuil}}-\mathcal B_{\min}}\right),
\]

où $\lambda$ est le taux de croissance de la bureaucratie.

L’indice de santé institutionnelle est

\[
\mathcal H_{\text{inst}}=
\frac{\mathcal V_{\text{vit}}}{\mathcal V_{\text{vit}}^{\max}}
\left(1-\frac{\mathcal B}{\mathcal B_{\max}}\right)
(1-G_{\mathcal A}),
\]

avec la condition $\mathcal H_{\text{inst}}>\theta_{\text{inst}}$.

## 6. Limites et points scientifiques non résolus

- $\mathcal{T}xt_{\text{ref}}$ est dit « éventuel » dans l’explication mais apparaît obligatoirement dans l’objectif ; le cas sans texte antérieur n’est pas défini.
- L’authenticité $\mathcal Aut$, les projections $\pi_d$ et la procédure de persistance après correction ne sont pas construites.
- Les inégalités vectorielles $\mathbf C(v)\ge\mathbf C_r^{\min}$ ne précisent pas l’ordre partiel composante par composante.
- Le chapitre appelle $\tau_{\text{adapt}}$ un taux, alors que le domaine Contexte le définit comme un produit de vitesses ; diviser le nombre de règles par ce taux rend $\mathcal B$ plus grand lorsque l’adaptation ralentit seulement si la convention inverse est retenue.
- La formule de $T_{\text{ref}}$ suppose une loi exponentielle de croissance de $\mathcal B$ qui n’est pas donnée dans le chapitre.
- $\mathcal H_{\text{inst}}$ peut être négatif si $\mathcal B>\mathcal B_{\max}$ ; aucune troncature ni plage de validité n’est indiquée.
