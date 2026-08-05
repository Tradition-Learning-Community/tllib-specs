# Finalité et téléologie évolutive

## 1. Espace des buts

La finalité est un but qui oriente le système tout en évoluant avec le contexte et le chemin parcouru. L’espace des finalités est

\[
\mathcal F=\{\mathcal G\subset\mathcal{TLS}\mid
\mathcal G\text{ est une sous-variété régulière de dimension }d\}
\times\mathbb R^+_{\text{priority}}\times\mathcal C_{\text{evolution}}.
\]

Un but $\mathcal G$ est une région de l’espace d’état, muni d’une priorité dynamique et d’un contexte de validité. Les buts immédiats, intermédiaires et ultimes sont hiérarchisés par

\[
\mathcal G_{\text{imm}}\subset\mathcal G_{\text{int}}
\subset\mathcal G_{\text{ult}}.
\]

## 2. Réalisation et attracteurs

\[
d_{\text{réal}}(\mathbf X,\mathcal G,t)=
\inf_{y\in\mathcal G}\left(\|\mathbf X-y\|
+\alpha(t)d_{\text{temp}}(t)
+\beta(t)d_{\text{ctx}}(\mathbf X,\mathbf c(t))\right).
\]

Cette distance combine écart à la cible, délai temporel et inadéquation contextuelle. L’ensemble des attracteurs finaux dynamiques est

\[
\mathcal A_{\text{fin}}(t)=\{\mathbf X\in\mathcal{TLS}\mid
\lim_{\tau\to\infty}\varphi(\tau,\mathbf X)\in\mathcal G(t),
\ \mathcal P_{\text{prés}}(\mathbf X)>\theta\}.
\]

La condition $\mathcal P_{\text{prés}}>\theta$ impose la préservation de l’essentiel.

## 3. Axiomes

- **Hiérarchie.** L’atteinte successive des buts inférieurs contribue à la convergence vers le but ultime.
- **Plasticité téléologique.** $\mathcal G(t+1)=\mathcal U(\mathcal G(t),\mathbf c(t))$ et $\mathcal U$ préserve le noyau invariant.
- **Attraction.** Tout $\mathbf X_0$ dans le bassin $B_{\text{att}}(t)$ converge vers $\mathcal A_{\text{fin}}(t)$.
- **Préservation.** Toute poursuite d’un but maintient $\mathcal P_{\text{prés}}(\mathbf X)>\theta$ sur l’attracteur.

L’opérateur de mise à jour est typé par

\[
\mathcal U:\mathcal F\times\mathcal C\times\mathbb R^+\to\mathcal F,
\]

avec, pour tout $y\in\mathcal G'=\mathcal U(\mathcal G,\mathbf c,t)$,

\[
\|\pi_{\mathcal N}(y)-\pi_{\mathcal N}(\mathcal G)\|<\epsilon.
\]

## 4. Optimisation finalisée

\[
\mathcal J(\mathbf X,u,t)=\int_0^TL(\mathbf X(s),u(s),s,\mathcal G(s))\,ds
+\Phi(\mathbf X(T),\mathcal G(T))
+\Psi(\mathcal P_{\text{prés}}).
\]

$L$ est le coût instantané, $\Phi$ le coût terminal et $\Psi$ la pénalité de perte de l’essentiel. Le système hamiltonien donné est

\[
\begin{cases}
\dot{\mathbf X}=\nabla_pH(\mathbf X,p,u,\mathcal G),\\
\dot p=-\nabla_xH(\mathbf X,p,u,\mathcal G),\\
\dot{\mathcal G}=\nabla_{\mathcal G}H(\mathbf X,p,u,\mathcal G),\\
H=p\cdot\mathbf F(\mathbf X,u)-L(\mathbf X,u,\mathcal G)
+\lambda\cdot\mathcal P_{\text{prés}}.
\end{cases}
\]

La trajectoire optimale satisfait aussi

\[
\frac{\partial V}{\partial t}+\min_u
\left[L(\mathbf X,u,t,\mathcal G)
+\nabla_{\mathbf X}V\cdot\mathbf F(\mathbf X,u)\right]=0.
\]

## 5. Auto-finalisation

\[
\frac{d\mathcal G}{dt}=\alpha_{\mathcal G}(\mathcal G_{\text{ém}}-\mathcal G)
+\beta_{\mathcal G}\nabla_{\mathbf X}\mathcal J\cdot\mathcal G
+\gamma_{\mathcal G}\nabla_{\mathbf c}\mathcal G\cdot\frac{d\mathbf c}{dt}.
\]

$\mathcal G_{\text{ém}}$ est un but issu de la dynamique interne, proposé par la source comme le centre de gravité de l’attracteur courant. Les deux autres termes adaptent le but au coût et au contexte.

Le système état–but–commande est

\[
\begin{cases}
\dot{\mathbf X}=\mathbf F(\mathbf X,u,t),\\
\dot{\mathcal G}=\alpha(\mathcal G_{\text{ém}}-\mathcal G)
+\beta\nabla_{\mathbf X}\mathcal J\cdot\mathcal G
+\gamma\nabla_{\mathbf c}\mathcal G\cdot\dot{\mathbf c},\\
u(t)=\arg\min_u[L(\mathbf X,u,t,\mathcal G)
+\lambda\|\mathbf X-\mathbf X^*(\mathcal G)\|^2].
\end{cases}
\]

## 6. Théorèmes formulés par la source

- **Convergence téléologique.** Si $\mathcal J$ est strictement convexe en $\mathbf X$ avec minimum global unique, si la dynamique d’état contracte exponentiellement vers ce minimum et si $\mathcal U$ contracte l’espace des buts, alors $(\mathbf X,\mathcal G)$ converge exponentiellement vers un point fixe $(\mathbf X^*,\mathcal G^*)$.
- **Préservation de l’essentiel.** Si l’attracteur satisfait $\mathcal P_{\text{prés}}>\theta$ et si $\mathcal U$ préserve le noyau, toute trajectoire admissible reste dans cette région. La source attribue le caractère répulsif de la frontière à $\Psi$.
- **Convergence contextuelle.** Sous convexité adaptative de $\mathcal J$ et régularité de $\mathbf F$,
  \[
  \lim_{t\to\infty}d_{\text{réal}}(\mathbf X(t),\mathcal G^*)=0.
  \]

## 7. Métriques

\[
\lambda_{\text{tél}}=\lim_{t\to\infty}\frac1t
\ln d_{\text{réal}},
\qquad
\eta_{\text{tél}}=\frac1T\int_0^Te^{-\rho t}\mathcal J(\mathbf X,u,t)\,dt,
\]

\[
\mathcal R_{\text{tél}}(t)=
e^{-d_{\text{réal}}(\mathbf X(t),\mathcal G(t),t)}.
\]

## 8. Limites et points scientifiques non résolus

- L’ensemble de toutes les sous-variétés régulières de $\mathcal{TLS}$ est déclaré variété de buts, finie ou infinie dimensionnelle, sans atlas ni métrique construits.
- L’inclusion des buts immédiats, intermédiaires et ultimes est présentée comme une inclusion ensembliste et comme une relation d’étapes ; l’équivalence entre ces deux sens n’est pas établie.
- $\pi_{\mathcal N}(\mathcal G)$ applique une projection à un ensemble sans définir l’image ensembliste ni la norme utilisée.
- Le signe $+\lambda\mathcal P_{\text{prés}}$ dans un Hamiltonien contenant $-L$ et le terme $+\Psi(\mathcal P_{\text{prés}})$ décrit comme pénalité ne permettent pas de déterminer si une meilleure préservation augmente ou diminue le coût.
- La « vitesse de convergence » $\lambda_{\text{tél}}$ est négative en cas de décroissance exponentielle de la distance ; la convention de signe n’est pas commentée.
- Les preuves ne montrent pas que la simple pénalité $\Psi$ rend la frontière $\mathcal P_{\text{prés}}=\theta$ répulsive.
