# Validateur IR — TLC-FC-14-LIVED-EXPERIENCE-005

Ce validateur structurel contrôle les variantes candidates sémantique et fonctionnelle, leurs nœuds, ports, arêtes, classifications, références, couverture et éléments non résolus. Il vérifie également le commit contractuel, le périmètre Git et l'absence de choix de langage ou de méthode numérique interdite.

Il ne constitue ni une validation scientifique, ni un oracle exécutable.

Depuis la racine du worktree :

```powershell
python tools/ir/TLC-FC-14-LIVED-EXPERIENCE-005/validate_ir.py
python -m py_compile tools/ir/TLC-FC-14-LIVED-EXPERIENCE-005/validate_ir.py
```

Résultat attendu : `VALIDATION PASSED`.
