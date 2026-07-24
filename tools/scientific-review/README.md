# Outils déterministes de revue

Depuis la racine du dépôt :

```powershell
python tools/scientific-review/validate_decisions.py
python tools/scientific-review/summarize_review.py
```

Le validateur contrôle l’unicité et l’exhaustivité par rapport à la file originale, la lisibilité YAML, les options sélectionnées, les métadonnées obligatoires des décisions prises et les comptes du tableau de bord. Le résumé affiche les comptes courants et les paquets terminés. Aucun outil n’applique les décisions aux registres scientifiques.
