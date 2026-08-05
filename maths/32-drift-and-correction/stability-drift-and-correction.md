# Stabilité, dérive et correction

## 1. Identification du noyau et de la périphérie

Pour chaque élément $e$ de la tradition,

\[
\kappa(e)=\frac15(\kappa_{\text{uni}}(e)
+\kappa_{\text{fond}}(e)+\kappa_{\text{res}}(e)
+\kappa_{\text{rec}}(e)+\kappa_{\text{supp}}(e)).
\]

$\kappa_{\text{uni}}$ mesure la présence dans les branches et les époques, $\kappa_{\text{fond}}$ la centralité dans le graphe de dépendances, $\kappa_{\text{rec}}$ la reconnaissance communautaire et $\kappa_{\text{supp}}$ l’effet d’une suppression simulée. La résistance au changement est

\[
\kappa_{\text{res}}(e)=1-
\frac{\|\Delta e\|}{\|\Delta e\|_{\max}}.
\]

L’axiome d’appartenance pose $e$ dans le noyau si $\kappa(e)>\kappa_{\min}$, et dans la périphérie sinon. Ce score sert ici au diagnostic de fidélité ; il ne remplace pas les invariants fondamentaux de [04-invariants](../04-invariants/invariants.md).

## 2. Renforcement et cristallisation

L’incorporation par répétition suit

\[
\mathcal I_{\text{inc}}(n)=
\mathcal I_{\text{inc}}^{\max}(1-e^{-\lambda n}).
\]

La pression vers l’écriture est

\[
p_{\text{écrit}}(t)=\sigma\!\left(
\alpha_1(N(t)-N_c)+\alpha_2d_{\max}(t)
+\alpha_3\delta_{\text{doct}}(t)
+\alpha_4(T_{\max}-T_{\text{témoins}}(t))
+\alpha_5P_{\text{ext}}(t)\right).
\]

$N$ est le nombre de Disciples, $d_{\max}$ la distance maximale au centre, $\delta_{\text{doct}}$ la divergence doctrinale, $T_{\text{témoins}}$ le nombre de témoins directs vivants et $P_{\text{ext}}$ la pression extérieure.

## 3. Indices de dérive

### 3.1 Dogmatisation

\[
\Delta_{\text{dog}}=1-
\frac{\|\boldsymbol\varepsilon\|}{\|\boldsymbol\varepsilon\|_0}
\frac{\mathcal A_{\text{adapt}}}{\mathcal A_{\text{adapt}}^0}.
\]

Une valeur proche de 1 est interprétée comme une forte rigidification des Principes.

### 3.2 Rigidité institutionnelle

\[
I_{\text{rig}}=
\frac{N_{\text{rules}}}{N_{\text{rules}}^0}
\frac{\tau_{\text{decision}}}{\tau_{\text{decision}}^0}
(1-\mathcal A_{\text{adapt}}).
\]

### 3.3 Perte d’intensité de mission

\[
\mathcal I_{\text{mis}}=
\frac{\mathcal V_{\text{vit}}}{\mathcal V_{\text{vit}}^{\max}}
\frac{\mathcal F_{\text{eng}}}{\mathcal F_{\text{eng}}^{\max}}
\frac{\mathcal J_{\text{joy}}}{\mathcal J_{\text{joy}}^{\max}}.
\]

$\mathcal F_{\text{eng}}$ est la fraction engagée de la Communauté et $\mathcal J_{\text{joy}}$ un indice d’enquête.

## 4. Rupture et schisme

\[
\mathcal S_{\text{rupture}}=
\left\{(v,x,t,\mathcal E,\mathcal V)\ \middle|\
\begin{array}{l}
d_D(x,\mathcal N_{\text{inv}})>\delta_{\text{rupture}},\\
|\{u\in V_L\mid d_D(x_u,x)<\epsilon\}|>N_{\text{crit}},\\
\mathcal V(x)<\theta_{\mathcal V},\\
\mathcal E_{\text{support}}(x)>\mathcal E_{\min}
\end{array}\right\}.
\]

La rupture exige donc une divergence doctrinale, une masse critique de soutien, une dégradation des Valeurs et un environnement suffisamment porteur. La source distingue schismes doctrinal, institutionnel, culturel et personnel, sans leur attribuer d’équations séparées.

## 5. Réforme et réinitialisation de mission

Le cycle de réforme comporte diagnostic, proclamation, résistance, expansion et institutionnalisation ; le chapitre déclare qu’un modèle détaillé dépasse sa synthèse.

Une réinitialisation est

\[
\mathcal R_{\text{reset}}:\mathcal X\to\mathcal X'
\]

telle que

\[
\|\pi_{\mathcal N}(\mathcal X')-
\pi_{\mathcal N}(\mathcal X_{\text{orig}})\|
<\varepsilon_{\text{reset}},
\quad
\mathcal V_{\text{vit}}'>\mathcal V_{\text{vit}},
\quad
\mathcal B'<\mathcal B.
\]

La continuité du reset est

\[
\mathcal C_{\text{cont}}=1-
\frac{\|\pi_{\mathcal N}(\mathcal X')-
\pi_{\mathcal N}(\mathcal X)\|}
{\|\pi_{\mathcal N}(\mathcal X)\|},
\]

avec $\mathcal C_{\text{cont}}>\mathcal C_{\min}$ et augmentation de vitalité.

## 6. Limites et points scientifiques non résolus

- Les cinq composantes de $\kappa(e)$ sont moyennées sans vérifier qu’elles sont toutes normalisées dans $[0,1]$ ; le test de suppression simulée n’est pas défini.
- La formule source de l’efficacité mnésique d’un rituel divise par $\|\mathcal X-\mathcal X\|=0$ ; elle est donc indéfinie et n’est pas reprise comme métrique valide.
- $\Delta_{\text{dog}}$ et $I_{\text{rig}}$ ne sont pas bornés sans hypothèses sur les ratios et sur $\mathcal A_{\text{adapt}}$.
- La probabilité $p_{\text{écrit}}$ suppose des variables commensurables après pondération, mais les unités et calibrations ne sont pas données.
- Les quatre conditions de $\mathcal S_{\text{rupture}}$ sont simultanées, alors que la partie conceptuelle décrit plusieurs voies de schisme ; leur articulation n’est pas résolue.
- Le chapitre reconnaît explicitement qu’il ne fournit pas de modèle mathématique détaillé du cycle de réforme.
