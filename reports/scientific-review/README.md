# Revue humaine de la consolidation scientifique

Cette revue présente les 147 décisions candidates sans prendre de décision scientifique. Commencer par `review-dashboard.md`, puis traiter les paquets dans l’ordre affiché. Chaque section de `review.md` explique la question, les preuves disponibles, les options et leurs conséquences ; la saisie durable s’effectue dans le bloc `human_decision` du fichier `decisions.yaml` correspondant.

Pour décider, remplacer `status: pending`, choisir uniquement une valeur de `allowed_options`, puis renseigner `decided_by`, `decided_at` et `justification`. Documenter les réserves et suivis si nécessaire. Exécuter ensuite `python tools/scientific-review/validate_decisions.py` et `python tools/scientific-review/summarize_review.py`.

Après validation humaine complète, une étape séparée pourra appliquer les décisions. Pendant cette phase, il est interdit de modifier directement les registres globaux candidats, les sources `maths/`, les extractions individuelles, de créer une IR, une API, du code métier ou un découpage fonctionnel.
