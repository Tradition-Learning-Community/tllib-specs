# tllib-specs

Bienvenue dans le dépôt de spécifications mathématiques et algorithmiques pour la bibliothèque **tllib**.

Ce dépôt est le lieu de travail principal du **cercle scientifique** de TLC. Il est organisé en deux pôles complémentaires :

- **Mathématiques** (dossier `math/`) : définitions, axiomes, théorèmes, équations, preuves.
- **Algorithmique** (dossier `algorithms/`) : analyses de complexité, choix numériques, pseudo-code, optimisations.

## Organisation des dossiers

- `math/` : contient les fondements mathématiques. Chaque fichier correspond à un thème (ex: `master-dynamics.md`, `disciple-evolution.md`). Les équations sont écrites en **LaTeX** entre `$$` (pour une bonne lisibilité humaine et par l'IA).
- `algorithms/` : décrit les algorithmes qui implémentent les modèles mathématiques. On y trouve du pseudo-code, une analyse de complexité, et des justifications de choix numériques.
- `notes/` : espace de travail informel pour les brouillons, réflexions en cours, compte‑rendus de réunions internes.
- `references/` : bibliographie (fichier BibTeX, liens vers des articles, etc.).

## Format des fichiers

Tous les fichiers sont en **Markdown** (`.md`) pour une lecture aisée par les humains et par l’IA.  
Les formules mathématiques sont saisies en **LaTeX** encadré par `$$` (bloc) ou `$` (inline) selon la taille.

Exemple :
```markdown
$$
\frac{dK}{dt} = \alpha \nabla_K R(K,\nu) + \beta \mathbb{E}[\delta K_{ped}] + \gamma I_{ext} + \sigma dW
$$
