# Chronologie complète des indicateurs — 02_classification

**Tableau directement extrait du CSV expérimental original, sans recalcul ni interpolation.**

- Fichier original : `originaux/experiment_classification_schemes_summary.csv`.
- Lignes expérimentales : **10**.
- Colonnes conservées : **17**.
- Les chiffres sont des mesures ou paramètres du protocole, **pas des dénombrements de schèmes**.
- La totalité des états multidimensionnels, au-delà des indicateurs de ce tableau, est conservée dans le JSON/NPZ originaux.

| t | SGD_logistic_orientation | SGD_logistic_marker | SGD_logistic_accuracy | Bernoulli_NB_orientation | Bernoulli_NB_marker | Bernoulli_NB_accuracy | CART_tree_orientation | CART_tree_marker | CART_tree_accuracy | Tiny_MLP_orientation | Tiny_MLP_marker | Tiny_MLP_accuracy | MLP_hidden_1_orientation | MLP_hidden_1_marker | MLP_hidden_2_orientation | MLP_hidden_2_marker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | — | — | — | — | — | — | — | — | — | 0.01609 | 0.00555 | 0.54333 | 0.60294 | 0.25921 | 0.20025 | 0.07625 |
| 40 | 0.04532 | 0.10437 | 0.57167 | 0.4223 | 0.4744 | 0.77167 | 0.0 | 1.0 | 0.53 | 0.51164 | 0.48435 | 0.85667 | 2.88039 | 1.11743 | 2.94186 | 1.7971 |
| 120 | 0.26233 | 0.2138 | 0.67667 | 0.64433 | 0.35537 | 0.71167 | 0.0 | 1.0 | 0.53 | 0.99852 | 0.00011 | 0.88833 | 5.44446 | 0.81637 | 4.85272 | 0.04532 |
| 300 | 0.37721 | 0.35129 | 0.65667 | 0.51663 | 0.48326 | 0.65667 | 0.0 | 1.0 | 0.53 | 0.99919 | 1e-05 | 0.89 | 6.02943 | 0.69004 | 4.89332 | 0.00423 |
| 400 | 0.36756 | 0.40246 | 0.63833 | 0.38919 | 0.6107 | 0.66 | 0.0 | 1.0 | 0.53 | 0.9995 | 1e-05 | 0.89667 | 5.78922 | 0.9188 | 4.88639 | 0.0114 |
| 550 | 0.50158 | 0.28304 | 0.82833 | 0.87766 | 0.11626 | 0.93 | 0.59217 | 0.38628 | 0.665 | 0.9994 | 1e-05 | 0.96833 | 6.01539 | 0.56318 | 4.89236 | 0.00596 |
| 800 | 0.64653 | 0.15231 | 0.965 | 0.93165 | 0.05599 | 0.97333 | 0.59944 | 0.30379 | 0.82167 | 0.99964 | 0.0 | 0.98333 | 5.86711 | 0.50993 | 4.89357 | 0.00413 |
| 1200 | 0.76589 | 0.06269 | 0.98 | 0.95282 | 0.02858 | 0.98333 | 0.72241 | 0.10703 | 0.82667 | 0.99968 | 0.0 | 0.99167 | 5.70679 | 0.46514 | 4.88637 | 0.00507 |
| 2000 | 0.88115 | 0.01948 | 0.97833 | 0.96221 | 0.01466 | 0.98333 | 0.91429 | 0.0 | 0.90333 | 0.99979 | 0.0 | 0.99167 | 5.61225 | 0.43961 | 4.88053 | 0.00468 |
| 3200 | 0.94019 | 0.00075 | 0.97667 | 0.96511 | 0.0074 | 0.98333 | 0.90797 | 0.0 | 0.91833 | 0.99984 | 0.0 | 0.99167 | 5.56419 | 0.48095 | 4.87789 | 0.0018 |
