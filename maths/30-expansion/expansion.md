# Expansion géographique, culturelle et polycentrique

## 1. Nœuds d’expansion

Un nœud d’expansion peut être un transmetteur exceptionnel, une communauté formatrice, un lieu stratégique ou un moment historique favorable. Il combine degré sortant élevé, qualité des transmissions, rayonnement géographique, centralité d’intermédiarité et innovation contrôlée.

Ces nœuds appartiennent au graphe générationnel $G_t$ défini dans [Propagation générationnelle](../29-generational-propagation/generational-propagation.md), sans redéfinir ici la qualité de réplication ni le seuil $R$.

## 2. Contagion spatiale

Soit $\rho(\mathbf r,t)$ la densité d’adhérents ou de communautés :

\[
\frac{\partial\rho}{\partial t}=D\nabla^2\rho
+\gamma\rho\Phi(\mathbf r,t)-\mu\rho,
\]

où $D$ est la mobilité, $\mu$ le taux de perte et

\[
\Phi(\mathbf r,t)=\frac1{N(\mathbf r,t)}
\sum_{i\in\operatorname{comm}(\mathbf r,t)}
\mathcal E_{\text{comm}}^{(i)}
\]

le rayonnement moyen local. Dans l’approximation d’un front d’onde,

\[
v\approx2\sqrt{D(\gamma\Phi-\mu)},
\]

et l’expansion exige $\gamma\Phi>\mu$.

## 3. Traduction et adaptation

\[
\mathcal T_{\text{trad}}(\mathcal{M}sg,\mathcal C_1,\mathcal C_2)
=\mathcal{M}sg',
\quad
\pi_{\mathcal N}(\mathcal{M}sg')=
\pi_{\mathcal N}(\mathcal{M}sg).
\]

\[
Q_{\text{trad}}=1-
\frac{\|\mathcal{M}sg'-\mathcal{M}sg\|}{\|\mathcal{M}sg\|}
-\lambda d_{\mathcal C}(\mathcal C_2,\mathcal C_1).
\]

La traduction requiert un transmetteur bilingue culturellement et compétent relativement au noyau, avec $\kappa_{\text{trad}}>\kappa_{\min}$.

L’adaptation d’une Pratique est

\[
\mathcal A_{\text{adapt}}(\mathcal{PR},\mathcal C)=
\arg\min_{\mathcal{PR}'}\left(
\|\pi_{\mathcal N}(\mathcal{PR}')-
\pi_{\mathcal N}(\mathcal{PR})\|^2
+\lambda\|\mathcal{PR}'-\mathcal{PR}_{\mathcal C}^*\|^2\right).
\]

Elle est dite possible si et seulement si la distance entre le noyau de la Pratique et les contraintes du contexte est inférieure à $\delta_{\text{adapt}}$.

## 4. Résistance et greffe culturelle

\[
\frac{\partial\rho}{\partial t}=D\nabla^2\rho
+\gamma\rho\Phi\left(1-\frac\rho{\rho_{\max}}\right)
-\mu\rho-\beta R\rho,
\]

\[
R=R_{\text{cult}}+R_{\text{soc}}+R_{\text{pol}}+R_{\text{eco}}.
\]

La compatibilité de greffe est

\[
\chi(\mathcal C_{\text{target}},\mathcal T)=
\frac1{|\mathcal N_{\text{inv}}|}
\sum_{n\in\mathcal N_{\text{inv}}}
\max_{c\in\mathcal C_{\text{target}}}\operatorname{sim}(n,c).
\]

La probabilité de pénétration initiale est déclarée proportionnelle à $\chi$ et $v_{\text{loc}}\approx v_0\chi$.

La réinterprétation locale vérifie

\[
\mathcal R_{\text{interp}}(\mathcal{M}sg,\mathcal C,\mathcal H_{\text{loc}})
=\mathcal{M}sg+\epsilon(\mathcal C,\mathcal H_{\text{loc}}),
\]

\[
\|\pi_{\mathcal N}(\mathcal{M}sg')-
\pi_{\mathcal N}(\mathcal{M}sg)\|\le\delta_{\text{interp}}.
\]

## 5. Polycentrisme et écoles

\[
H_{\text{cent}}=\sum_{v\in V_t}
\left(\frac{c(v)}{\sum_uc(u)}\right)^2.
\]

Le système est polycentrique si $H_{\text{cent}}<\theta_{\text{cent}}$. Une école est une communauté du graphe, caractérisée par son interprétation moyenne $\bar{\mathbf X}_E$ et

\[
d_E=\|\pi_{\mathcal N}(\bar{\mathbf X}_E)-\mathbf X_{\mathcal N}\|.
\]

La diversification stable exige, pour toutes écoles $E_i,E_j$,

\[
d_{\text{int}}(E_i,E_j)\le D_{\max},
\qquad
\frac1K\sum_id_{E_i}\le\Delta_{\text{avg}}.
\]

## 6. Limites et points scientifiques non résolus

- $\Phi$ dépend de $N(\mathbf r,t)$ sans règle lorsque aucune communauté n’est présente ; sa régularité nécessaire au front d’onde n’est pas donnée.
- $Q_{\text{trad}}$ pénalise simultanément l’écart du Message traduit et la distance des contextes, sans normalisation ; il n’est pas garanti dans $[0,1]$.
- La faisabilité « si et seulement si » de l’adaptation ne définit pas la distance entre un noyau de Pratique et des contraintes contextuelles.
- $\chi$ suppose le noyau fini et une similarité entre objets doctrinaux et culturels ; ni la mesure ni la similarité ne sont construites.
- Le modèle de résistance est une extension logistique du premier modèle de contagion, mais la relation entre les deux équations et leurs domaines de validité n’est pas explicitée.
- Les seuils de polycentrisme et de diversité stable ne sont pas calibrés, et le théorème ne fournit pas de preuve de suffisance pour éviter le schisme.
