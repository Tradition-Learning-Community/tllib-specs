# Phase d'imprégnation

## 1. Immersion

L'opérateur d'immersion est

\[
\mathcal I_{\mathrm{imm}}(\mathcal D,\mathcal C_P,t)
=\mathcal D+
\sum_{c\in\mathcal C_P}\int_0^t\kappa_c(\tau)\,
\Phi_c(\mathcal D(\tau),c)\,d\tau,
\]

où $\mathcal C_P$ désigne la communauté de pratique, $\kappa_c$ un noyau de mémoire et $\Phi_c$ une influence contextuelle. Le chapitre propose l'approximation

\[
\frac{d\mathcal D}{dt}
\simeq\eta_EE(\mathcal C_P)(0-\mathcal D).
\]

L'authenticité de l'environnement est mesurée par

\[
\delta_{\mathrm{auth}}
=\max_d\min_s d_{\mathcal C_P}(d,s),
\]

avec l'exigence que $\delta_{\mathrm{auth}}$ reste sous son seuil maximal et décroisse.

## 2. Modalités d'exposition

Les modalités d'exposition sont combinées par une somme pondérée d'indicateurs. L'observation produit la trace

\[
\mathcal T_{\mathrm{obs}}(t)
=\int_0^t\mathcal O_{\mathrm{obs}}(\mathcal M,\mathcal C_P,\tau)\,d\tau.
\]

La démonstration augmente l'attention par un multiplicateur strictement supérieur à $1$. L'exposition cachée module la motivation par une fonction logistique. Pendant l'imprégnation, l'imitation différée est imposée par

\[
\mathcal I_{\mathrm{imit}}=0.
\]

## 3. Résonance sélective

Chaque objet fondamental est associé à une bande $\mathcal B_k$. Son intensité d'exposition est

\[
I_k(t)
=\left\langle
\pi_{\mathcal B_k}\bigl(\mathcal O_{\mathrm{obs}}(\mathcal D,\mathcal M,t)\bigr),
\mathbf 1
\right\rangle.
\]

Le poids de résonance de chaque bande évolue selon

\[
\frac{dw_k}{dt}
=\alpha_kI_k(t)(1-w_k)-\beta_kw_k+\gamma_k\xi_k(t).
\]

Une bande est activée si

\[
w_k>\theta_{\mathrm{act}}.
\]

La répétition est évaluée sur une fenêtre mobile par

\[
\overline I_k(t)
=\frac{1}{T}\int_{t-T}^{t}I_k(\tau)\,d\tau.
\]

## 4. Mémoires implicite et explicite

La mémoire implicite suit l'équation intégro-différentielle

\[
\frac{d\mathcal M_{\mathrm{impl}}}{dt}
=\int_0^tK_{\mathrm{impl}}(t-\tau)\,
\mathcal O_{\mathrm{obs}}(\mathcal D,\mathcal M,\tau)\,d\tau
-\lambda_{\mathrm{impl}}\mathcal M_{\mathrm{impl}},
\qquad
K_{\mathrm{impl}}(s)=\alpha_{\mathrm{impl}}e^{-\beta_{\mathrm{impl}}s}.
\]

La mémoire explicite possède sa propre équation,

\[
\frac{d\mathcal M_{\mathrm{expl}}}{dt}
=\mu(t)\mathcal E_{\mathrm{first}}(\mathcal N_{\min},\mathcal D)
-\lambda_{\mathrm{expl}}\mathcal M_{\mathrm{expl}}
+\underbrace{\text{terme de rappel}}_{\text{non défini dans la source}},
\]

puis les deux mémoires sont couplées par

\[
\frac{d\mathcal M_{\mathrm{expl}}}{dt}\ni\nu\mathcal M_{\mathrm{impl}},
\qquad
\frac{d\mathcal M_{\mathrm{impl}}}{dt}\ni\rho\mathcal M_{\mathrm{expl}}.
\]

La profondeur d'intégration évolue suivant

\[
\frac{dC}{dt}
=\kappa_1O(t)(C_{\max}-C)
\sigma(\mathcal V_{\mathrm{receptivity}}-\theta_1)
\mathbf 1_{\{\mathcal Val_{\mathrm{openness}}>\psi_1\}}.
\]

Le système complet réunit $C$, les poids $w_k$, $\mathcal M_{\mathrm{impl}}$ et $\mathcal M_{\mathrm{expl}}$. Ses conditions initiales typiques sont $C(0)=0$, $w_k(0)=w_k^0$, $\mathcal M_{\mathrm{impl}}(0)=0$ et $\mathcal M_{\mathrm{expl}}(0)=0$. La sortie exige

\[
C(T_{\mathrm{imp}})\geq C_{\mathrm{seuil}}
\qquad\text{et}\qquad
\forall k,\;w_k(T_{\mathrm{imp}})\geq w_k^{\min}.
\]

## 5. Limites et points scientifiques non résolus

- Dans l'approximation d'immersion, $0$ est déclaré état vierge et le signe est décrit comme une attraction vers le cadre communautaire ; l'équation attire pourtant $\mathcal D$ vers $0$ sans représenter séparément ce cadre.
- Pour $t<T$, la moyenne mobile requiert des valeurs sur des temps négatifs, sans convention fournie.
- Le terme « recall term » de l'équation de mémoire explicite n'est pas mathématiquement défini dans la source et n'est donc pas complété ici.
- Le système récapitulatif remplace $\mathcal O_{\mathrm{obs}}$ par $O(\tau)$ dans l'intégrale de mémoire implicite, sans identifier formellement ces deux notations.
- La condition finale porte sur toutes les bandes, tandis que le mécanisme antérieur est présenté comme une résonance sélective ; leur articulation n'est pas précisée.
