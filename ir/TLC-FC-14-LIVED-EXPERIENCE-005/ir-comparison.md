# Comparaison des variantes IR — TLC-FC-14-LIVED-EXPERIENCE-005

## IR sémantique

- **Objectif** : préserver les symboles, l'équation, la collection et les unresolved du contrat actuel.
- **Justification** : le contrat contient un objet, sept symboles, une équation et quatre unresolved explicites.
- **Avantages** : proximité maximale avec le contrat; incertitudes localisées; aucune hypothèse calculatoire.
- **Limites** : ne définit ni évaluation exécutable, ni types, ni `Synergie`.
- **Sémantique préservée** : expression complète, postcondition candidate et absence d'état, sans résoudre le domaine de N ni l'additionnabilité.
- **Structure explicite** : symboles, ensemble opaque, opérateur opaque et validations.
- **Informations opaques** : appartenance et cardinalité de `{ell_i}`, signature de `Synergie`, types, formes, dimensions et unités.
- **Unresolved propagés** : les quatre questions contractuelles.
- **Décisions nécessaires** : les deux décisions contractuelles et la politique d'échec.
- **Planification d'implémentation** : non prête.
- **Génération de code** : interdite.
- **Conformité** : conforme sous réserves explicitement préservées.

## IR fonctionnelle

- **Objectif** : expliciter uniquement la composition opératoire visible dans l'équation.
- **Justification** : la somme, la division, l'appel à `Synergie`, la multiplication et l'addition figurent explicitement dans la source.
- **Avantages** : rend les dépendances symboliques visibles sans choisir d'algorithme ou de type.
- **Limites** : ce n'est pas un graphe calculable; l'ordre d'évaluation et les règles d'erreur restent absents.
- **Sémantique préservée** : expression complète et unresolved contractuels.
- **Structure explicite** : opérateurs et ports symboliques, validation séparée de `N`.
- **Informations opaques** : `Synergie`, toutes les signatures et compatibilités de types.
- **Unresolved propagés** : les quatre questions contractuelles.
- **Décisions nécessaires** : définition scientifique, types, représentation finie et politique d'échec.
- **Planification d'implémentation** : non prête.
- **Génération de code** : interdite.
- **Conformité** : conforme comme encodage structurel candidat.

## Variantes non produites

- **IR de calcul** : rejetée; aucun flux calculable complet ne peut être construit sans définir `Synergie`, les types, la cardinalité et les règles d'échec.
- **IR dynamique** : rejetée; le contrat ne contient aucun état, transition, invariant d'état ou caractère temporel défini.
