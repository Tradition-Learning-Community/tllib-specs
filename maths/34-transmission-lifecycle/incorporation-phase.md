# Phase d'incorporation

## 1. Retrait progressif de la guidance

La part de guidance du maître décroît selon un coefficient $\lambda(t)$. La pratique combine alors intervention du maître et activité autonome :

\[
\mathcal P_t
=\lambda(t)\mathcal P_{\mathcal M}
+\bigl(1-\lambda(t)\bigr)\mathcal P_{\mathrm{aut}}.
\]

L'indice d'autonomie proposé est

\[
\mathcal A(t)
=\frac{\lVert\mathbf C(t)-\mathbf C_{\mathrm{master}}\rVert}
{\lVert\mathbf C_{\mathrm{master}}\rVert}
\frac{V_{\mathrm{initiative}}(t)}{V_{\mathrm{initiative,max}}}
\frac{\mathcal P_{\mathrm{original}}(t)}{\mathcal P_{\mathrm{max}}}
\mathbf 1_{\{\mathcal Val_{\mathrm{independence}}>\theta_{\mathcal A}\}}.
\]

Le maître conserve un opérateur de surveillance et de correction pendant cette transition.

## 2. Incorporation des principes et des vertus

L'incorporation des vertus suit

\[
\begin{aligned}
\frac{dV_i}{dt}
={}&\alpha_i\mathcal P_{\mathrm{practice}}(t)(V_{i,\max}-V_i)
+\sum_j\beta_{ij}C_jV_i
+\gamma_i\mathbf{Val}\cdot\nabla\mathcal E_{\mathrm{moral}}\\
&-\delta_iV_i\left(1-\frac{C_i}{C_{i,\max}}\right).
\end{aligned}
\]

$\mathcal P_{\mathrm{practice}}$ est l'intensité de pratique ; le dernier terme ralentit la vertu lorsque la compétence associée reste insuffisante. L'état complet reste le système

\[
\mathbf X=(\mathbf C,\mathbf V,\mathbf{Val},\mathbf P).
\]

## 3. Pratiques

Le chapitre distingue les opérateurs de pratique technique, contextuelle, de résolution de problèmes et réflexive. Leur intensité combinée est

\[
M(t)
=w_{\mathrm{tech}}\lVert\mathcal{PT}_{\mathrm{tech}}\rVert
+w_{\mathrm{ctx}}\lVert\mathcal{PT}_{\mathrm{ctx}}\rVert
+w_{\mathrm{prob}}\lVert\mathcal{PT}_{\mathrm{prob}}\rVert
+w_{\mathrm{refl}}\lVert\mathcal{PT}_{\mathrm{refl}}\rVert.
\]

La source définit en outre une mesure de fluidité. La métacompétence évolue selon une équation dédiée et soutient l'auto-évaluation.

Le cycle réflexif enchaîne pratique, observation, évaluation et correction. L'opérateur maïeutique du maître agit sur l'identité du disciple, puis l'évolution identitaire est intégrée à la dynamique complète de $X$.

## 4. Transition

La phase s'achève au franchissement du deuxième seuil défini dans le chapitre. Le critère combine autonomie, incorporation des principes et vertus, compétence pratique et métacompétence.

## 5. Limites et points scientifiques non résolus

- Le texte annonce « trois » opérateurs de pratique mais en énumère et formalise quatre.
- $\mathcal A(t)$ n'est pas défini lorsque $\lVert\mathbf C_{\mathrm{master}}\rVert$, $V_{\mathrm{initiative,max}}$ ou $\mathcal P_{\mathrm{max}}$ est nul ; une plus grande distance à la compétence du maître augmente mécaniquement le premier facteur.
- La limite de $\lambda(t)$ est seulement donnée comme très inférieure à $1$, sans valeur terminale précise.
- Un critère utilise $\max_i C_i$ : il peut être satisfait par une seule composante de compétence, sans condition sur les autres.
- Le signe de l'opérateur maïeutique fondé sur un gradient n'est pas relié à une fonction de coût explicitement orientée.
