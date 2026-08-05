# Culture comme milieu structurant de la transmission

## 1. Définition

La culture n’est pas un arrière-plan passif. Elle constitue un milieu actif qui déforme et oriente la transmission, et dans lequel une tradition doit pouvoir prendre forme sans perdre son noyau identitaire.

Dans l’espace [contextuel](../24-context/context.md), deux composantes portent directement cette structure :

\[
\mathcal C_{\text{cultural}}	imes\mathcal C_{\text{symbolic}}
\subset\mathcal C.
\]

$\mathcal C_{\text{cultural}}$ regroupe Valeurs, croyances, normes, langues et représentations partagées. $\mathcal C_{\text{symbolic}}$ regroupe mythes, récits fondateurs, figures emblématiques et objets sacrés. La source réserve un espace métrique $\mathcal M$, non nécessairement vectoriel, aux aspects symboliques non quantifiables.

## 2. Fonction structurante

La culture agit sur :

- la réception du Message ;
- l’application des Principes ;
- l’incarnation des Valeurs ;
- la pratique des Compétences.

Elle participe aux poids $w_i(\mathbf X,t)$ et aux couplages $\gamma_{ij}(\mathbf X,t)$ de la métrique contextuelle

\[
g_c=\sum_iw_i(\mathbf X,t)dx_i\otimes dx_i
+\sum_{i<j}\gamma_{ij}(\mathbf X,t)dx_i\otimes dx_j.
\]

Le poids culturel varie avec les événements, crises, innovations et transformations sociales ; sa loi n’est pas séparée de la dynamique générale

\[
\frac{dw_i}{dt}=\alpha_i(\mathcal E_{\text{contexte}}-w_i)
+\beta_iw_i(1-w_i)
+\gamma_i\nabla_{\mathbf X}w_i\cdot\frac{d\mathbf X}{dt}.
\]

## 3. Plasticité culturelle et noyau identitaire

La source distingue :

- les éléments robustes de faible sensibilité contextuelle, principalement Principes et Valeurs fondamentales ;
- les formes culturellement plastiques de plus forte sensibilité, principalement Pratiques et certaines Compétences.

Cette distinction est mesurée au niveau du système par

\[
\mathcal S_{\text{contexte}}=
\|\nabla_{\mathbf c}\mathbf H\|
+\|\nabla_{\mathbf c}^2\mathbf H\|
+\left\|\frac{\partial\mathbf H}{\partial(\nabla\mathbf c)}\right\|.
\]

L’adaptation culturelle légitime agit sur les formes sensibles et laisse intacts les éléments robustes. Elle est un cas de l’opérateur $\mathcal A_{\text{contexte}}$ défini dans [Contexte](../24-context/context.md), non un opérateur autonome supplémentaire.

## 4. Conditions de fidélité culturelle

Une transmission culturellement située doit simultanément :

1. employer les langues, formes, rites et méthodes recevables dans le milieu ;
2. conserver la connexion à la source commune ;
3. maintenir l’état adapté $\mathbf X^*$ dans un voisinage du noyau invariant lorsque la fonction $\mathcal J$ pénalise l’écart aux Valeurs fondamentales ;
4. éviter deux échecs opposés explicités par la source : l’ignorance du milieu, qui rend la tradition inopérante, et la dissolution dans le milieu, qui vide la tradition de son identité.

## 5. Limites et points scientifiques non résolus

- Le chapitre ne donne pas d’espace d’état, d’opérateur ni de métrique exclusivement culturels au-delà des facteurs $\mathcal C_{\text{cultural}}$ et $\mathcal C_{\text{symbolic}}$ du contexte.
- Les Valeurs, croyances, normes, langues, représentations, mythes et objets symboliques ne sont pas coordonnés ni mesurés.
- La frontière entre forme culturellement adaptable et noyau robuste est décrite par une sensibilité relative, mais aucun seuil de séparation n’est fourni.
- La préservation du noyau est affirmée sous forte pénalisation dans $\mathcal J$ sans borne quantitative sur le voisinage ni coefficient minimal de pénalisation.
