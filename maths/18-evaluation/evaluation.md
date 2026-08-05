# Évaluation multidimensionnelle et multi-source

## 1. Périmètre et architecture

L’évaluation mesure la progression individuelle et collective, croise plusieurs points de vue et produit l’information utilisée par la [régulation](../19-regulation/regulation.md). Elle appartient au système conjoint

\[
\mathcal{ER}=(\mathcal M,\mathcal E,\mathcal R,\mathcal A,
\mathcal S,\mathcal T,\mathcal C,\mathcal I,\mathcal P,
\mathcal V,\mathcal D,\mathcal F).
\]

Dans le périmètre de l’évaluation :

- $\mathcal M=\mathcal M_t\times\mathcal M_c\times\mathcal M_e\times\mathcal M_r$ est l’espace des métriques ;
- $\mathcal E=\mathcal E_{\text{mentor}}\times\mathcal E_{\text{peers}}\times\mathcal E_{\text{self}}\times\mathcal E_{\text{community}}$ regroupe les sources ;
- $\mathcal A=\mathcal A_{\text{weighting}}\times\mathcal A_{\text{fusion}}\times\mathcal A_{\text{confidence}}$ agrège les évaluations ;
- $\mathcal S=\mathcal S_{\text{zones}}\times\mathcal S_{\text{transitions}}\times\mathcal S_{\text{alerts}}$ définit zones et seuils ;
- $\mathcal C$ porte les contextes de cohorte, de communauté et de temps ;
- $\mathcal V$ impose éthique, équité et bienveillance.

Le domaine de validité est

\[
\mathcal U_{\mathcal{ER}}=\{(d,t,c)\in\mathbb D\times\mathbb R^+\times\mathbb C\mid
\operatorname{confidence}(d,t)>\theta_c,
\mathcal T_{\text{transparency}}(c,t)>\theta_t,
\mathcal B(c,t)>\theta_b,
\mathcal V(c)\in\mathcal V_{\text{admissible}}\}.
\]

Les sources doivent chacune dépasser $\theta_{\text{reliability}}$ ; la confiance moyenne, la transparence et la bienveillance doivent également dépasser leurs seuils respectifs.

## 2. Métriques de progression

### 2.1 Espace technique

\[
\mathcal M_t=\{m_{t,i}=f_{t,i}(\mathbf C)\mid i=1..k_t\},
\qquad f_{t,i}:\mathcal C\to\mathbb R\text{ Lipschitz}.
\]

\[
m_{t,1}=\|\mathbf C_{\text{technical}}\circ\mathbf W_{\text{technical}}\|,
\]

\[
m_{t,2}=\frac1T\int_0^T\sigma(\|d\mathbf C/dt\|)
\mathbf1_{\{\|d^2\mathbf C/dt^2\|<\epsilon\}}\,dt,
\]

\[
m_{t,3}=\frac{\mathbf C\cdot\mathbf C_{\text{reference}}}
{\|\mathbf C\|\|\mathbf C_{\text{reference}}\|}
\exp\!\left(-\frac{\|\mathcal E_{\text{context}}-\mathcal E_{\text{optimal}}\|^2}{2\tau^2}\right).
\]

### 2.2 Espace contextuel

\[
\mathcal M_c=\{m_{c,j}=f_{c,j}(\mathbf C,\mathbf V,\mathbf{Val},
\mathcal E_{\text{context}})\mid j=1..k_c\}.
\]

\[
m_{c,1}=\mathbb E_{\mathcal E}[\|\mathbf C(\mathcal E)
-\mathbf C_{\text{optimal}}(\mathcal E)\|w(\mathcal E)],
\]

\[
m_{c,2}=\frac{\mathbf V_{\text{prudence}}\cdot\mathbf C_{\text{analysis}}}
{\|\mathbf V_{\text{prudence}}\|\|\mathbf C_{\text{analysis}}\|}
\sigma(\mathbf{Val}_{\text{wisdom}}),
\]

\[
m_{c,3}=\frac{\sum w_i\operatorname{resolution}_i}
{\sum w_i\operatorname{complexity}_i}\tanh(\mathcal P_{\text{innovation}}).
\]

### 2.3 Espace éthique

\[
\mathcal M_e=\{m_{e,k}=f_{e,k}(\mathbf V,\mathbf{Val},
\mathbf{Actions},\mathbf{Decisions})\mid k=1..k_e\}.
\]

\[
m_{e,1}=1-\frac{\|\mathbf{Actions}-\pi_{\mathbf{Val}}(\mathbf{Actions})\|_{\mathbf W}}
{\|\mathbf{Actions}\|}
\exp\!\left(-\frac{\|\nabla\mathbf V\|^2}{2\sigma^2}\right),
\]

\[
m_{e,2}=\frac{\mathbf{Val}\cdot\mathbf{Decisions}}
{\|\mathbf{Val}\|\|\mathbf{Decisions}\|}
+\alpha\|\nabla_{\mathcal E}(\mathbf{Val}\cdot\mathbf{Decisions})\|,
\]

\[
m_{e,3}=\frac1T\int_0^T
\exp\!\left(-\frac{\|\mathbf V(t)-\mathbf V(t+\Delta t)\|^2}{2\sigma^2}\right)
\mathbf1_{\{\|d\mathbf{Val}/dt\|<\eta\}}\,dt.
\]

### 2.4 Indice intégré

\[
\mathcal I_{\text{progression}}(d,t)
=\sum_{i\in\{t,c,e,r\}}w_i(d,t)\mathcal N_i\!\left(
\frac1{k_i}\sum_{j=1}^{k_i}
\frac{m_{i,j}-m_{i,j,\min}}{m_{i,j,\max}-m_{i,j,\min}}\right)
+\sum_{(i,j)\in I}\gamma_{i,j}(d,t)\Psi(m_i,m_j),
\]

\[
\Psi(m_i,m_j)=m_im_j
\exp\!\left(-\frac{(m_i-\mu_i)^2+(m_j-\mu_j)^2}{2\sigma_{ij}^2}\right),
\]

\[
\frac{dw_i}{dt}=\kappa_i(\operatorname{importance}_i(t)-w_i)
+\lambda_i\frac{\partial\mathcal J}{\partial w_i}
+\mu_i\mathcal E_{\text{context}}(t)(w_{i,\text{opt}}-w_i).
\]

## 3. Zones et transitions

Les zones sont définies par $\|\mathcal M(d,t)\|$ : émergence sous $\theta_1$, structuration entre $\theta_1$ et $\theta_2$, intégration entre $\theta_2$ et $\theta_3$, maîtrise au-dessus de $\theta_3$, avec

\[
\begin{aligned}
\theta_1(t)&=\mathbb E[\|\mathcal M_{\text{novice}}(t)\|]
(1+\alpha\mathcal E_{\text{stimulant}}(t)),\\
\theta_2(t)&=\mathbb E[\|\mathcal M_{\text{competent}}(t)\|]
\sigma(\mathcal P_{\text{fluid}}(t)),\\
\theta_3(t)&=\mathbb E[\|\mathcal M_{\text{advanced}}(t)\|]
\tanh(\mathcal V_{\text{coherence}}(t)).
\end{aligned}
\]

\[
\mathbb P(i\to i+1\mid t)=\sigma\!\left(
\beta_i(\|\mathcal M(d,t)\|-\theta_i(t))
+\alpha_i\frac{d\|\mathcal M\|}{dt}
+\gamma_i\mathcal V_{\text{preparation}}(t)\right).
\]

## 4. Sources d’évaluation

### 4.1 Mentor

\[
\mathcal E_{\text{mentor}}(d,t)=\mathbf W_m(d,t)\cdot
\Phi_m(\mathbf X(d,t),\mathcal E_{\text{context}}(t))+b_m(t)+\epsilon_m(d,t),
\]

où $\Phi_m$ réunit distance à la compétence de référence, alignement des Vertus et Valeurs, perspective longitudinale et potentiel d’évolution. Les poids apprennent selon

\[
\frac{d\mathbf W_m}{dt}=\eta_m(\mathcal E_{\text{truth}}-\mathcal E_{\text{mentor}})
\Phi_m^\top+\lambda_m(\mathbf W_{m,\text{opt}}-\mathbf W_m).
\]

### 4.2 Pairs

\[
\mathcal E_{\text{peers}}(d,t)=\frac1{|P_d(t)|}\sum_{p\in P_d(t)}
\mathbf W_p(d,p,t)\cdot\Psi_p(\mathbf X(d,t),\mathbf{Interactions}(d,p,t),
\mathcal E_{\text{context}}(t))+b_p(t)+\epsilon_p(d,t),
\]

\[
P_d(t)=\{p\in\mathbb D\mid\operatorname{affinity}(d,p,t)>\theta_{\text{aff}},
\operatorname{exposure}(d,p,t)>\theta_{\text{exp}},
\operatorname{competence}(p,t)>\theta_{\text{comp}}\}.
\]

$\Psi_p$ porte sur contribution coopérative, qualité du retour, fiabilité, soutien émotionnel et apprentissage mutuel.

### 4.3 Auto-évaluation

\[
\mathcal E_{\text{self}}(d,t)=\mathbf W_a(d,t)\cdot
\Gamma_a(\mathbf X_{\text{perceived}},\mathbf X_{\text{real}},
\mathcal M_{\text{awareness}})+b_a(t)+\epsilon_a(d,t),
\]

où $\Gamma_a$ mesure les écarts de compétences, Vertus, jugement, conscience des limites et autocorrection. Le biais est

\[
\epsilon_a=\alpha\operatorname{overconfidence}
+\beta\operatorname{excessive\_modesty}
+\gamma\operatorname{cognitive\_blindness}
+\delta\mathcal E_{\text{affective}}.
\]

## 5. Agrégation

\[
\mathcal E_{\text{total}}(d,t)=\sum_{i\in I}\alpha_i\mathcal E_i
+\beta\prod_i\mathcal E_i^{\gamma_i}
+\delta\mathcal E_{\text{synergy}},
\]

\[
\frac{d\alpha_i}{dt}=\kappa_i(\operatorname{precision}_i-\operatorname{avg\_precision})
+\lambda_i(\operatorname{confidence}_i-\alpha_i)
+\mu_i\frac{\partial\mathcal J_{\text{system}}}{\partial\alpha_i},
\]

avec $\sum_i\alpha_i=1$, $\alpha_i\ge\alpha_{\min,i}(t)$ et un poids minimal du mentor avant $t_{\text{autonomy}}(d)$.

## 6. Métriques systémiques

\[
\mathcal I_{\text{efficiency}}(t)=
\frac{\|\mathbf X_{\text{real}}-\mathbf X_{\text{ideal}}\|}
{\|\mathbf X_{\text{initial}}-\mathbf X_{\text{ideal}}\|}\frac1t
\exp\!\left(-\frac{\sigma^2_{\mathcal E}+\|\operatorname{bias}\|^2}{2\tau^2}\right),
\]

\[
\mathcal I_{\text{health}}=\alpha\operatorname{Cohesion}
+\beta\operatorname{Diversity}+\gamma\operatorname{Resilience}
+\delta\operatorname{Adaptability}+\epsilon\operatorname{Synergy}.
\]

La métrique procédurale d’équité et la détection de biais sont

\[
\mathcal I_{\text{fairness}}=1-
\frac{\sigma(\mathcal E_{\text{individual}})}{\mu(\mathcal E_{\text{individual}})}
+\alpha\operatorname{corr}(\mathcal E_{\text{individual}},\mathcal M_{\text{real}})
-\beta\|\operatorname{bias}\|+\gamma\mathcal V_{\text{justice}},
\]

\[
\operatorname{bias}(t)=\mathbb E[\mathcal E(d,t)-\mathcal M(d,t)\mid
\operatorname{type}(d)=\tau]
+\operatorname{Var}[\mathcal E(d,t)\mid\operatorname{type}(d)=\tau].
\]

Voir le domaine [Équité](../21-fairness/fairness.md) pour les contraintes et mécanismes propres à la justice distributive.

## 7. Limites et points scientifiques non résolus

- La condition $\dim(\mathcal M)=\dim(\mathcal C)+\dim(\mathcal V)+\dim(\mathcal{Val})+\dim(\mathcal P)$ emploie des espaces dont les dimensions ne sont pas définies et distingue $\mathcal V$ de $\mathcal{Val}$ sans convention explicite.
- $\mathcal M_r$ est inclus dans l’indice intégré mais aucune famille de métriques $m_{r,j}$ n’est construite dans le chapitre.
- $\mathcal E_{\text{community}}$ est annoncée comme quatrième source, mais ne reçoit pas de formule propre.
- $\mathcal E_{\text{truth}}$, les fonctions de normalisation, les références réelles et les méthodes d’estimation des biais ne sont pas définies. L’évaluation par les pairs est indéfinie si $P_d(t)=\varnothing$.
- Les seuils et coefficients restent à calibrer. L’« efficacité » décroît avec la distance à l’idéal, mais la direction d’interprétation de l’indice n’est pas explicitée.
