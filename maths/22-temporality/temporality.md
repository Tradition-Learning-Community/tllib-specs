# Temporalité multi-échelle

## 1. Espace-temps évolutif

Le temps de Tradition Learning est structuré en quatre échelles continues interconnectées :

\[
\mathcal T=\mathcal T_{\text{micro}}\times\mathcal T_{\text{meso}}
\times\mathcal T_{\text{macro}}\times\mathcal T_{\text{meta}}.
\]

- $\mathcal T_{\text{micro}}$ : geste, décision et correction immédiate ;
- $\mathcal T_{\text{meso}}$ : phase d’apprentissage, compétence et maturation d’une Vertu ;
- $\mathcal T_{\text{macro}}$ : vie, carrière d’un Maître et transformation générationnelle ;
- $\mathcal T_{\text{meta}}$ : siècles, civilisations, crises et renaissances de la tradition.

Chaque niveau est annoncé isomorphe à $\mathbb R^+$. L’ensemble reçoit une structure de fibré dans laquelle chaque point du temps macro porte les temps micro et meso qui le constituent.

## 2. Métrique temporelle

\[
g_\tau=\begin{pmatrix}
\alpha_1e^{-\lambda_1t_1}&\beta_{12}&\gamma_{13}&\delta_{14}\\
\beta_{12}&\alpha_2t_2e^{-\lambda_2t_2}&\gamma_{23}&\delta_{24}\\
\gamma_{13}&\gamma_{23}&\alpha_3t_3^2&\delta_{34}\\
\delta_{14}&\delta_{24}&\delta_{34}&\alpha_4t_3^3
\end{pmatrix}.
\]

La diagonale encode des vitesses propres aux échelles ; les termes hors diagonale encodent leurs couplages. La distance temporelle est ainsi destinée à intégrer l’importance historique et le poids mnésique des événements, et non leur seule séparation chronologique.

## 3. Flux temporel héréditaire

\[
\frac{d\varphi}{d\tau}=\mathbf F_\tau(\varphi(\tau),\tau,
\nabla_\tau\mathcal V)
+\int_0^\tau K(\tau-s)\mathcal M(\varphi(s))\,ds.
\]

$\mathbf F_\tau$ est un champ non autonome, $\nabla_\tau\mathcal V$ le gradient temporel des Valeurs, $K$ un noyau de [mémoire](../23-memory/memory.md) et $\mathcal M$ l’opérateur mnésique.

## 4. Évolution multi-échelle

\[
\begin{cases}
\displaystyle\frac{\partial\mathbf X}{\partial t_1}=\epsilon_1\mathbf F_1(\mathbf X,t_1,\theta),\\[1em]
\displaystyle\frac{\partial\mathbf X}{\partial t_2}=\epsilon_2\mathbf F_2(\mathbf X,t_2,\nabla\theta),\\[1em]
\displaystyle\frac{\partial\mathbf X}{\partial t_3}=\epsilon_3\mathbf F_3(\mathbf X,t_3,\nabla^2\theta),\\[1em]
\displaystyle\frac{\partial\mathbf X}{\partial t_4}=\epsilon_4\mathbf F_4(\mathbf X,t_4,\mathcal M(\mathbf X)),
\end{cases}
\qquad
\epsilon_1\gg\epsilon_2\gg\epsilon_3\gg\epsilon_4.
\]

Les $\mathbf F_i$ sont déclarées Lipschitz. Le couplage ascendant et descendant est

\[
\mathcal C_{\text{scale}}(\mathbf X)=\sum_{i<j}\gamma_{ij}
\frac{\partial\mathbf X}{\partial t_i}\otimes
\frac{\partial\mathbf X}{\partial t_j}.
\]

## 5. Régimes

Quatre régimes sont distingués :

- **stase métastable** : $\|d\mathbf X/dt\|<\epsilon$ et parties réelles des valeurs propres négatives mais proches de zéro ;
- **régime périodique ou cyclique** : solutions périodiques ou quasi périodiques et $\operatorname{Re}(\lambda)=0$ ;
- **turbulence ou transition** : $\|d\mathbf X/dt\|>\theta_{\text{trans}}$ et $\operatorname{Re}(\lambda)>0$ ;
- **chaos structuré** : $\operatorname{Re}(\lambda)>0$ avec dimension fractale bornée.

La probabilité de transition est formulée par

\[
\mathbb P(i\to j)=
\frac{e^{-\beta\Delta E_{ij}}}{\sum_ke^{-\beta\Delta E_{ik}}}
f(\nabla_\tau\mathcal V),
\]

où $\Delta E_{ij}$ est l’écart d’énergie, $\beta$ l’inverse d’une « température sociale » et $f$ une fonction croissante du gradient temporel des Valeurs.

## 6. Limites et points scientifiques non résolus

- Dans $g_\tau$, la quatrième composante diagonale dépend de $t_3^3$ et non de $t_4$ ; cette notation est conservée sans correction.
- Aucune condition n’assure que la matrice $g_\tau$ est symétrique définie positive pour les coefficients admis.
- La structure de fibré, les espaces de $\mathbf X$ et $\theta$, les dérivées entre échelles et les fonctions $\mathbf F_i$ ne sont pas construits.
- Le facteur $f(\nabla_\tau\mathcal V)$ peut empêcher la somme des probabilités de valoir 1 ; aucune normalisation supplémentaire n’est indiquée.
- Les énergies de régime, la température sociale, les seuils et la dimension fractale critique restent indéfinis.
