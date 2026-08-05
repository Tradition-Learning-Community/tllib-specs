# Propagation générationnelle et qualité de réplication

## 1. Seuil de transmission secondaire

Le passage du Disciple au transmetteur exige le seuil de maîtrise transmissionnelle

\[
\mathcal T_3=\left\{(\mathbf C,\mathbf V,\mathbf{Val},\mathbf P)\ \middle|\
\begin{array}{l}
\sum_iw_iC_i\ge\theta_3\land V_{\text{trans}}\ge\phi_3
\land\|\mathbf{Val}-\mathbf{Val}_{\text{master}}\|\le\delta_3\\
\land\mu_{\mathbf P}(\mathbf P_{\text{ped}})\ge\omega_3
\land\mathcal F_{\text{trans}}>\theta_{\mathcal F}
\end{array}\right\}.
\]

Il combine Compétences techniques, Vertu de transmission, alignement des Valeurs, Pratique pédagogique et fidélité. Le changement de statut est accompagné par le Maître et validé par la Communauté.

## 2. Variations entre générations

La variation du contenu dans la lignée suit

\[
\frac{dx_v}{dt}=\eta\sum_{u\in N(v)}w_{uv}(x_u-x_v)
+\xi(v)(x_{\mathcal M(v)}-x_v)+\sigma dW_v(t)
+\tau\mathcal V\cdot\nabla\mathcal E\cdot x_v.
\]

Le bruit $\sigma dW_v$ représente les variations aléatoires ; le dernier terme les adaptations contextuelles délibérées.

Une mutation constructive appartient à

\[
\mathcal D_{\text{constructive}}=\{x\in\mathcal X_{\text{doct}}\mid
d_D(x,\mathcal N_{\text{inv}})\in(0,\delta_{\text{innov}}],
\ d\mathcal J/dx>0,
\ \mathcal V(x)>\theta_{\mathcal V},
\ \mathcal E(x)\in\mathcal E_{\text{fav}}\},
\]

tandis qu’une mutation destructive appartient à

\[
\mathcal D_{\text{destructive}}=\{x\in\mathcal X_{\text{doct}}\mid
d_D(x,\mathcal N_{\text{inv}})>\delta_{\text{rupture}},
\ d\mathcal J/dx<0,
\ \mathcal V(x)<\theta_{\mathcal V}
\text{ ou }\mathcal E(x)\notin\mathcal E_{\text{fav}}\}.
\]

L’enveloppe des innovations admises est

\[
\mathcal E_{\text{adapt}}(t)=\{x\in\mathcal X_{\text{doct}}\mid
d_D(x,\mathcal N_{\text{inv}}(t))<\delta_{\text{adapt}}(t,\mathcal E),
\ d\mathcal J/dx>0\}.
\]

## 3. Qualité de réplication

\[
Q_{\text{rép}}(t)=\frac1{|\mathcal N_{\text{inv}}|}
\sum_{x\in\mathcal N_{\text{inv}}}\omega_x
\left(1-\frac{\delta_x(t)}{\delta_x^{\max}}\right)e^{-\lambda t}.
\]

$\delta_x(t)$ est l’écart générationnel de la composante $x$, $\delta_x^{\max}$ l’écart toléré et $\omega_x$ son importance relative.

L’érosion moyenne du Message est modélisée par

\[
\|\mathbf M_n-\mathbf M_0\|
\approx\|\mathbf M_0\|(1-e^{-nd}),
\]

\[
d=(1-Q_{\text{rép}})(1-\mathcal R_{\text{auto}})
(1+\kappa\|\nabla\mathcal E\|).
\]

La correction collective doit rapprocher tout $x$ destructif du noyau :

\[
\mathcal R_{\text{correctif}}:
\mathcal D_{\text{destructive}}\times\mathcal C\times\mathcal E\times\mathcal V
\to\mathcal X_{\text{doct}}'\times[0,1]_{\text{efficiency}},
\]

\[
\|\mathcal R_{\text{correctif}}(x)-\pi_{\mathcal N}(x)\|
<\|x-\pi_{\mathcal N}(x)\|,
\quad
\mathcal V(\mathcal R_{\text{correctif}}(x))>\mathcal V(x).
\]

## 4. Graphe générationnel

\[
G_t=(V_t,E_t,w),
\]

où les sommets sont les transmetteurs reconnus, les arcs $u\to v$ les formations de transmetteur et $w(u\to v)\in[0,1]$ la qualité. Les propriétés suivies sont degrés entrant et sortant, densité

\[
\rho_t=\frac{|E_t|}{|V_t|(|V_t|-1)},
\]

composantes connexes, centralités, clustering, diamètre, modularité et éventuelle loi $P(k)\propto k^{-\gamma}$.

## 5. Taux de reproduction

\[
R(t)=\frac{\text{nombre de nouveaux transmetteurs formés entre }t
\text{ et }t+\Delta t}
{\text{nombre de transmetteurs à }t}.
\]

$R>1$ indique l’expansion, $R=1$ la stabilité fragile et $R<1$ le déclin. La source propose

\[
R_c=1+\frac{\sigma_R^2}{\mathbb E[R]}f(\rho,\kappa),
\]

comme seuil critique dépendant de la variance, de la densité et de la cohésion.

## 6. Diversification générationnelle

Les branches peuvent se spécialiser tant que

\[
\max_i d_D(x_i,\mathcal N_{\text{inv}})<\delta_{\text{rupture}}.
\]

L’émergence d’une école suit différenciation, stabilisation, reconnaissance, autonomisation et dialogue inter-écoles. Une diversité harmonieuse exige reconnaissance mutuelle, noyau commun, échanges inter-écoles et arbitrage légitime.

## 7. Limites et points scientifiques non résolus

- $Q_{\text{rép}}$ divise par le cardinal du noyau, alors que $\mathcal N_{\text{inv}}$ est ailleurs un sous-ensemble potentiellement continu ; aucune mesure de remplacement n’est donnée.
- Le facteur $e^{-\lambda t}$ fait décroître la qualité de réplication avec le temps même si tous les écarts sont nuls ; cette conséquence n’est pas discutée.
- Le taux $d$ dépend de $Q_{\text{rép}}(t)$ et du contexte, mais est utilisé comme constante par génération dans la loi d’érosion.
- La source affirme que le seuil $R_c$ rend l’extinction « irréversible » ou sa probabilité nulle, sans définir le processus de branchement, $f(\rho,\kappa)$ ni les hypothèses probabilistes.
- Les arcs orientés rendent les « composantes connexes » ambiguës : faible ou forte connexité n’est pas précisée.
- Les seuils de mutation, de fidélité et de reproduction ne sont pas calibrés.
