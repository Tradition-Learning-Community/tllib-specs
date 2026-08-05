# Phase de validation communautaire

## 1. Système collectif

Le système de validation collective articule le système collectif de valeurs $\mathcal V_c$, la mémoire narrative $\mathcal N$, la matrice de validation $\mathcal M$ et le système de légitimation $\mathcal L$. La matrice $\mathcal M$ de ce chapitre ne désigne donc pas la mémoire ni le maître.

Pour un candidat $a$,

\[
\mathcal M(a,t)
=\frac{1}{|\mathcal A(t)|}
\sum_{a'\in\mathcal A(t)}
w(a,a',t)v(a',a,t)
+\lambda(t)r(a,t).
\]

$\mathcal A(t)$ est l'ensemble des évaluateurs, $v(a',a,t)$ leur évaluation, $w(a,a',t)$ leur poids, $r(a,t)$ la reconnaissance formelle et $\lambda(t)$ son poids.

## 2. Activation

La validation est activée par

\[
\begin{aligned}
\mathbf 1_{\mathrm{valid}}(a,t)
={}&\mathbf 1_{\{\Phi_{\mathrm{threshold}}(a,t)=1\}}
\mathbf 1_{\{\rho_{\mathrm{prep}}(a,t)\geq\rho_{\min}\}}
c_{\mathrm{conv}}(a,t)\\
&\times\mathbf 1_{\{|\mathcal A(t)|\geq Q_{\min}\}}
\mathbf 1_{\{H_{\mathrm{eval}}(t)\geq H_{\min}\}}.
\end{aligned}
\]

Les facteurs portent sur le franchissement des seuils antérieurs, la préparation, la convocation, le quorum et l'hétérogénéité des évaluateurs.

## 3. Pondération des évaluateurs

Le poids normalisé est

\[
w(a,a',t)
=\frac{
\phi_{\mathrm{eld}}(a',t)
\phi_{\mathrm{comp}}(a',t)
\phi_{\mathrm{prox}}(a,a',t)}{
\displaystyle\sum_{a''\in\mathcal A(t)}
\phi_{\mathrm{eld}}(a'',t)
\phi_{\mathrm{comp}}(a'',t)
\phi_{\mathrm{prox}}(a,a'',t)}.
\]

Les trois facteurs représentent l'ancienneté, la compétence et la proximité avec le candidat. La source rattache aussi la validation aux corrections d'équité définies dans le domaine [Équité](../21-fairness/fairness.md).

## 4. Rite, reconnaissance et légitimité

Le rite de passage peut provoquer des sauts de reconnaissance et de légitimité. La légitimité évolue selon

\[
\frac{d\mathcal L}{dt}
=\alpha_{\mathcal L}\bigl(\mathcal M(a,t)-\mathcal L\bigr)
+\beta_{\mathcal L}\bigl(\mathcal L_{\mathrm{hist}}-\mathcal L\bigr)
+\gamma_{\mathcal L}\mathcal E(t).
\]

$\mathcal L_{\mathrm{hist}}$ représente la légitimité historique et $\mathcal E(t)$ les événements affectant la légitimation. La validation finale exige simultanément le franchissement des seuils de $\mathcal M$ et de $\mathcal L$.

## 5. Limites et points scientifiques non résolus

- La formule de $\mathcal M$ divise par $|\mathcal A(t)|$ alors que l'ensemble des évaluateurs peut être vide avant l'activation.
- Le dénominateur du poids $w$ peut être nul ; aucun cas de repli n'est défini.
- $\mathbf 1_{\mathrm{valid}}$ est nommé indicateur, mais contient le facteur $c_{\mathrm{conv}}$ sans que celui-ci soit imposé comme binaire.
- Les plages de $\mathcal M$ et $\mathcal L$ ne sont pas établies ; les sauts rituels peuvent donc les faire sortir d'un intervalle supposé de scores.
- Le chapitre rappelle une dynamique de légitimité attribuée à un chapitre antérieur sans fournir ici de démonstration de stabilité.
