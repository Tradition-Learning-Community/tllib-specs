# Rapport IR — TLC-FC-14-LIVED-EXPERIENCE-005

Le contrat `TLC-MC-TLC-FC-14-LIVED-EXPERIENCE-005` au commit `1ff27ea31bae784a64ac3eee534404ce2ce322fa` a été transformé en deux représentations candidates : sémantique et fonctionnelle.

L'IR sémantique préserve l'objet équation, la collection d'expériences, les sept symboles, les quatre unresolved et la postcondition candidate. L'IR fonctionnelle rend explicites seulement les opérations écrites dans l'équation : sommation, division par N, appel opaque à Synergie, multiplication par sigma et addition.

`Synergie` reste opaque. Le domaine de `N`, sa relation avec la cardinalité de la collection, ainsi que les types, formes, dimensions et unités restent non résolus. Les quatre questions du contrat sont propagées et bloquent la planification d'implémentation et la génération de code.

Aucun état ou caractère dynamique n'étant défini, aucune IR dynamique n'est produite. L'absence de signature de `Synergie` et de types interdit de présenter la structure fonctionnelle comme un graphe de calcul, donc aucune IR de calcul n'est produite.

Statut recommandé : `revise`. L'IR est une `engineering_candidate` avec réserves préservées; elle ne constitue pas une validation scientifique.
