# Outils d'adjudication scientifique automatique

Depuis la racine du dépôt :

```text
python tools/scientific-auto-review/run_auto_review.py
python tools/scientific-auto-review/generate_human_exceptions.py
python tools/scientific-auto-review/sample_automatic_decisions.py
python tools/scientific-auto-review/validate_auto_review.py
```

Les trois premiers scripts sont déterministes et régénèrent les artefacts candidats à partir des sources immuables. Le validateur contrôle l'exhaustivité des 147 décisions, la conformité aux seuils, les deux passes, les divergences, l'absence de décision humaine préremplie, les 496 sections, les 830 termes et l'absence de modification d'un chemin protégé.
