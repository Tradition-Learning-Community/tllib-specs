# Sémantique dynamique Dynamics

La source contient 11 objets équation : 6 différentielles, 3 stochastiques et 2 équations de feedback. Elle utilise `t`, `dt` et `tau`, mais ne définit ni domaine temporel global, pas de temps, état initial, état final, condition d'arrêt ou méthode numérique.

Le catalogue regroupe 13 objets comme candidats d'état, mais l'extraction les type principalement `Concept`; aucun espace d'état n'est explicite. Aucune transition avant/après n'est formalisée. Les structures sont représentables, mais aucune fonctionnalité n'est déclarée exécutable.
