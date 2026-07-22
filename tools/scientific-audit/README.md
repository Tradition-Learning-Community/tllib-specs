# Audit de consolidation scientifique

`audit_scientific_extractions.py` audite les paquets d'extraction liés aux
sources Markdown de `maths/` et génère les livrables candidats de consolidation.
Il ne modifie ni les sources, ni les registres et rapports individuels.

Exécution depuis la racine du dépôt :

```powershell
python tools/scientific-audit/audit_scientific_extractions.py
```

Le script est déterministe : il trie les entrées, n'utilise ni réseau ni date
courante, et réécrit uniquement les sorties de consolidation prévues.
