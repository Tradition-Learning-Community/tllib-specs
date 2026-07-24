# Rapport de validation IR — TLC-FC-14-LIVED-EXPERIENCE-005

## Résultat

Les variantes sémantique et fonctionnelle couvrent le contrat candidat sans altération. Elles portent `source_contract_ready_for_ir: false` et `progression_mode: candidate_with_preserved_reservations`. Elles ne sont prêtes ni pour la planification d'implémentation ni pour la génération de code.

## Contrôles de couverture

- Objet et relation : couverts; la relation reste contextuelle et non normative.
- Six symboles : couverts, dont `Synergie` comme `OpaqueOperator`.
- Espaces et états : absents du contrat; aucun n'a été inventé.
- Trois entrées et une sortie : couvertes.
- Équation : expression préservée; normalisation non altérée.
- Contraintes : `N != 0` et additionnabilité représentées.
- Postcondition : représentée.
- Préconditions, invariants, hypothèses et propriétés : absents du contrat.
- Oracle : base symbolique conservée; aucun oracle exécutable inventé.
- Unresolved : 3/3 propagés dans les deux variantes et dans `ir-open-questions.yaml`.
- Décisions d'implémentation : 2/2 propagées; politique d'échec ajoutée comme décision d'ingénierie différée.
- Couverture : 21 éléments, aucun manquant.

## Contrôles de non-invention

- Aucun C++, Python applicatif, binding ou type de langage cible.
- Aucun solveur, schéma numérique, discrétisation, approximation ou optimisation.
- Aucun type scalaire, domaine, unité, dimension, forme ou valeur par défaut ajouté.
- Aucune définition de `Synergie`.
- Aucun ordre d'évaluation ni politique d'erreur imposé.
- Aucun état ou effet temporel ajouté.
- Aucun fichier d'une autre fonctionnalité consulté ou incorporé.

## Aptitude

- Sémantique : candidate conforme avec réserves.
- Fonctionnelle : candidate conforme comme structure symbolique non exécutable.
- Calcul : non produite.
- Dynamique : non produite.
- Planification d'implémentation : `false`.
- Génération de code : `false`.
