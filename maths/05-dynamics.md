# Équations dynamiques (Dynamics)

## 1. Introduction

Les entités fondamentales de Tradition Learning — Maître, Disciple, Communauté — ne sont pas statiques. Leur évolution temporelle est régie par des systèmes d’équations différentielles stochastiques (EDS) couplées, qui traduisent l’interaction entre processus internes (affinement, maturation) et influences externes (relations, environnement, aléas). Ce chapitre rassemble les principales équations dynamiques présentées dans les fichiers précédents, afin d’offrir une vision synthétique des mécanismes en jeu.

## 2. Équations du Maître

Le Maître $\mathcal{M} = (\mathcal{K},\nu,\mathcal{E},\mathcal{P},\mathcal{A},\mathcal{R},\mathcal{S})$ évolue selon les équations suivantes.

### 2.1 Évolution de la connaissance $\mathcal{K}$

\[
\begin{aligned}
d\mathcal{K}(t) =&\ \underbrace{\alpha\cdot\nabla_{\mathcal{K}}R(\mathcal{K},\nu)}_{\text{affinement interne}}\,dt \\
&+ \underbrace{\beta\cdot\mathbb{E}_{\mathcal{D}\sim\mu_t}[\delta\mathcal{K}_{\mathrm{ped}}(\mathcal{D})]}_{\text{rétroaction pédagogique}}\,dt \\
&+ \underbrace{\gamma\cdot I_{\mathrm{ext}}(t)}_{\text{apport externe}}\,dt + \underbrace{\sigma_{\mathcal{K}}\,dW_{\mathcal{K}}(t)}_{\text{bruit exploratoire}}
\end{aligned}
\]

- $\nabla_{\mathcal{K}}R$ : gradient de la fonctionnelle de cohérence $R$ (alignement connaissance‑valeurs).
- $\delta\mathcal{K}_{\mathrm{ped}}(\mathcal{D})$ : mise à jour due à l’enseignement du Disciple $\mathcal{D}$.
- $I_{\mathrm{ext}}$ : entrées externes (autres Maîtres, expériences, lectures).
- $W_{\mathcal{K}}$ : processus de Wiener (exploration aléatoire).

### 2.2 Dynamique de l’exemplarité $\mathcal{E}$

\[
\frac{d^2\mathcal{E}}{dt^2} + \zeta\frac{d\mathcal{E}}{dt} + \omega_0^2\mathcal{E} = F_{\mathrm{contexte}}(t) + \eta_{\mathcal{E}}(t)
\]

- $\zeta$ : coefficient d’amortissement éthique (résilience).
- $\omega_0$ : fréquence propre du noyau éthique (stabilité du système de valeurs).
- $F_{\mathrm{contexte}}$ : défis contextuels (perturbations éthiques).
- $\eta_{\mathcal{E}}$ : bruit coloré (fluctuations morales).

### 2.3 Dynamique du système de valeurs $\nu$

\[
\frac{\partial\rho(\sigma,t)}{\partial t} = D\Delta_{\nu}\rho(\sigma,t) - \nabla_{\nu}\cdot\big(\rho(\sigma,t)\vec{v}(\sigma,t)\big)
\]

- $\rho(\sigma,t)$ : densité de probabilité d’activation du simplexe $\sigma$.
- $\Delta_{\nu}$ : laplacien combinatoire sur le complexe simplicial.
- $\vec{v}$ : champ de dérive (raffinement délibéré).
- $D$ : coefficient de diffusion (évolution spontanée).

### 2.4 Évolution de l’autorité $\mathcal{A}$

\[
\frac{d\mathcal{A}}{dt} = \lambda_{\mathcal{A}}(\mathcal{E}(t)-\mathcal{A}(t)) + \mu_{\mathcal{A}}\frac{d\bar{\mathcal{Q}}}{dt} + \nu_{\mathcal{A}}\frac{d\mathcal{S}}{dt} + \xi_{\mathcal{A}}(t)
\]

- $\bar{\mathcal{Q}}$ : qualité moyenne des Disciples.
- $\mathcal{S}$ : statut symbolique.
- $\xi_{\mathcal{A}}$ : sauts de Poisson (changements soudains de réputation).

## 3. Équations du Disciple

Le Disciple $\mathcal{D} = (\mathcal{S}_0,\mathcal{P},\mathcal{R},\mathcal{T},\mathcal{F},\mathcal{G},\mathcal{A},\mathcal{C})$ évolue selon les équations suivantes.

### 3.1 Évolution par trajectoire $\mathcal{T}$

\[
\begin{aligned}
d\mathcal{P}(t) =&\ \underbrace{\nabla_{\mathcal{P}}U(\mathcal{P},\mathcal{M})}_{\text{potentiel de guidage}}\,dt \\
&+ \underbrace{\Gamma(\mathcal{P})\circ(\mathcal{M}-\Pi_{\mathcal{M}}(\mathcal{P}))}_{\text{attraction vers le Maître}}\,dt \\
&+ \underbrace{D\Delta_{\mathcal{P}}\mathcal{P}}_{\text{diffusion exploratoire}}\,dt + \underbrace{\sigma_{\mathcal{P}}(\mathcal{P})\,dW_{\mathcal{P}}(t)}_{\text{fluctuations aléatoires}}
\end{aligned}
\]

- $U$ : potentiel de guidage (incorpore l’état cible du Maître et les buts intrinsèques).
- $\Gamma$ : tenseur de couplage adaptatif (modulation de l’attraction selon la maturité).
- $D\Delta_{\mathcal{P}}$ : diffusion exploratoire.
- $W_{\mathcal{P}}$ : bruit blanc cylindrique (variabilité cognitive, éclairs de compréhension).

### 3.2 Dynamique de génération d’identité $\mathcal{G}$

\[
\frac{\partial\mathcal{I}}{\partial t} = \underbrace{\alpha\Delta\mathcal{I}}_{\text{diffusion}} + \underbrace{\beta\mathcal{I}(1-\mathcal{I})(\mathcal{I}-\theta)}_{\text{cristallisation}} + \underbrace{\gamma(\mathcal{M}_{\mathcal{I}}-\mathcal{I})}_{\text{influence du Maître}} + \eta_{\mathcal{I}}(t)
\]

- $\alpha\Delta\mathcal{I}$ : propagation de l’identité.
- $\beta\mathcal{I}(1-\mathcal{I})(\mathcal{I}-\theta)$ : terme de seuil (équation de Fisher‑KPP), $\theta$ seuil critique.
- $\gamma(\mathcal{M}_{\mathcal{I}}-\mathcal{I})$ : attraction vers l’identité du Maître.
- $\eta_{\mathcal{I}}$ : bruit (fluctuations identitaires).

### 3.3 Évolution de la réceptivité $\mathcal{R}$

\[
\frac{d\mathcal{R}_k}{dt} = r_k\mathcal{R}_k\left(1-\frac{\mathcal{R}_k}{K_k}\right) - \sum_{j\neq k}\alpha_{kj}\mathcal{R}_k\mathcal{R}_j + \beta_k\mathcal{F}_k(\mathcal{M},\mathcal{D}) + \xi_k(t)
\]

- Compétition de type Lotka‑Volterra entre bandes de réceptivité.
- $r_k$ : taux de croissance intrinsèque.
- $K_k$ : capacité de charge (réceptivité maximale soutenable).
- $\alpha_{kj}$ : coefficients de compétition.
- $\beta_k\mathcal{F}_k$ : modulation par le Maître.
- $\xi_k$ : sauts de Poisson (changements attentionnels soudains).

### 3.4 Traitement du feedback $\mathcal{F}$

\[
\mathcal{F}[\mathcal{I}_{\mathrm{ext}}](t) = \int_{-\infty}^t K(t-\tau;\mathcal{R},\mathcal{P})\cdot\mathcal{I}_{\mathrm{ext}}(\tau)\,d\tau + \mathcal{F}_{\mathrm{int}}(\mathcal{D})
\]
avec noyau multi‑exponentiel
\[
K(t) = \sum_{m=1}^{M} A_m e^{-\lambda_m t}\cos(\omega_m t+\phi_m)
\]
(intégration multi‑échelle des retours).

## 4. Équations de la Communauté

La Communauté $\mathcal{C} = (\mathcal{A},\mathcal{R},\mathcal{V}_c,\mathcal{N},\mathcal{T},\mathcal{M},\mathcal{E},\mathcal{G})$ évolue selon le système couplé suivant.

### 4.1 Système d’évolution couplé

\[
\begin{cases}
\displaystyle\frac{d\mathcal{A}}{dt} = F_A(\mathcal{A},\mathcal{R},\mathcal{V}_c) + \sigma_A dW_A(t)\\[1.2em]
\displaystyle\frac{d\mathcal{R}}{dt} = L\mathcal{R} + B(\mathcal{A},\mathcal{V}_c) + \sigma_R dW_R(t)\\[1.2em]
\displaystyle\frac{d\mathcal{V}_c}{dt} = -\alpha(\mathcal{V}_c-\mathcal{V}_{\mathrm{consensus}}) + \beta\nabla\mathcal{N} + \sigma_V dW_V(t)\\[1.2em]
\displaystyle\frac{d\mathcal{N}}{dt} = \mathcal{T}(\mathcal{A},\mathcal{E}_{\mathrm{exp}}) - \gamma\mathcal{N} + \sigma_N dW_N(t)\\[1.2em]
\displaystyle\frac{d\mathcal{I}_{\mathrm{coll}}}{dt} = \mathcal{G}(\mathcal{A},\mathcal{V}_c,\mathcal{N}) + \sigma_I dW_I(t)
\end{cases}
\]

- $F_A$ : flux démographiques (recrutements, départs, transitions de rôles).
- $L$ : laplacien du graphe relationnel (diffusion des influences).
- $B$ : co‑évolution réseau‑attributs.
- $\mathcal{V}_{\mathrm{consensus}}$ : vecteur de consensus (dynamique des valeurs).
- $\mathcal{T}(\mathcal{A},\mathcal{E}_{\mathrm{exp}})$ : intégration des nouvelles expériences dans la mémoire.
- $\mathcal{G}$ : génération d’identité collective.
- Les $dW_i$ sont des bruits corrélés (fluctuations environnementales).

### 4.2 Interactions avec le Maître et le Disciple

Les dynamiques communautaires sont modulées par des opérateurs d’interaction :
\[
\begin{aligned}
\frac{d\mathcal{A}}{dt} &\ni I_{\mathcal{M}\to\mathcal{C}}(\mathcal{M},\mathcal{A}) + I_{\mathcal{D}\to\mathcal{C}}(\mathcal{D},\mathcal{A})\\
\frac{d\mathcal{R}}{dt} &\ni J_{\mathcal{M}\to\mathcal{C}}(\mathcal{M},\mathcal{R}) + J_{\mathcal{D}\to\mathcal{C}}(\mathcal{D},\mathcal{R})\\
\frac{d\mathcal{V}_c}{dt} &\ni K_{\mathcal{M}\to\mathcal{C}}(\mathcal{M},\mathcal{V}_c) + K_{\mathcal{D}\to\mathcal{C}}(\mathcal{D},\mathcal{V}_c)
\end{aligned}
\]

### 4.3 Contraintes de viabilité

La dynamique doit respecter des bornes structurelles :
- $|\mathcal{A}(t)| \ge N_{\min}$ (taille minimale).
- $\lambda_2(L(\mathcal{R}(t))) \ge \lambda_{\min}$ (connectivité).
- $\|\mathcal{V}_c(t) - \mathcal{V}_{\mathrm{core}}\| \le \Delta_{\max}$ (cohérence des valeurs).
- $\int_0^t \|\mathcal{N}(\tau) - \mathcal{N}_{\mathrm{essentiel}}\| d\tau \le M_{\max}$ (conservation de la mémoire).

Le non‑respect de ces contraintes annonce l’effondrement ou la pathologie de la communauté.

## 5. Remarques sur les couplages

Les trois systèmes sont en interaction :
- Le Maître influence le Disciple (guidage, exemplarité) et la Communauté (légitimation).
- Le Disciple influence le Maître (feedback pédagogique) et la Communauté (renouvellement).
- La Communauté influence le Maître (autorité) et le Disciple (validation sociale).

La dynamique globale est donc un système couplé de grande dimension dont l’étude analytique est complexe, mais qui peut être abordée par des méthodes numériques (discrétisation, simulation d’EDS, analyse de stabilité).

---

*Ce fichier rassemble les principales équations dynamiques. Pour les dérivations détaillées et les propriétés mathématiques (convergence, stabilité, bifurcations), se reporter aux fichiers respectifs des entités.*