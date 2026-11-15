# Chronologie complète des six contrôles — Régression

**Mesures transcrites directement du JSON original** `originaux/experiment_regression_schemes_results.json`.

Ce tableau présente chaque modèle à chaque instant. Les structures d’arbres complètes, coefficients et sondes cachées supplémentaires sont conservés dans le JSON original.

| t | phase | RLS_area_if_no_road | RLS_area_if_road | RLS_road_at_small | RLS_road_at_large | RLS_proxy_effect | Tree_area_if_no_road | Tree_area_if_road | Tree_road_at_small | Tree_road_at_large | Tree_proxy_effect | TinyMLP_area_if_no_road | TinyMLP_area_if_road | TinyMLP_road_at_small | TinyMLP_road_at_large | TinyMLP_proxy_effect | mlp_hidden_proxy_abs_mean_all_contexts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | ambiguous | 13.526 | 13.526 | 6.706 | 6.706 | 6.706 | 4.688 | 10.466 | 9.38 | 15.158 | 0.0 | 7.979 | 13.398 | 7.783 | 13.203 | 7.686 | 1.104 |
| 100 | ambiguous | 13.31 | 13.31 | 6.35 | 6.35 | 6.35 | 8.532 | 8.532 | 0.0 | 0.0 | 11.373 | 8.55 | 13.454 | 8.476 | 13.38 | 7.11 | 1.11 |
| 300 | ambiguous | 13.532 | 13.532 | 6.282 | 6.282 | 6.282 | 8.965 | 17.862 | 8.249 | 17.146 | 0.0 | 8.932 | 13.312 | 8.833 | 13.213 | 6.628 | 1.11 |
| 500 | disambiguation | 13.564 | 13.564 | 12.244 | 12.244 | 0.239 | 9.077 | 17.796 | 8.268 | 16.987 | 0.0 | 9.051 | 17.36 | 8.384 | 16.693 | 0.226 | 0.959 |
| 900 | disambiguation | 13.402 | 13.402 | 12.44 | 12.44 | 0.047 | 9.121 | 17.815 | 8.297 | 16.991 | 0.0 | 9.099 | 17.679 | 8.367 | 16.947 | 0.224 | 0.945 |
| 1600 | disambiguation | 13.493 | 13.493 | 12.419 | 12.419 | 0.11 | 9.017 | 17.981 | 8.109 | 17.073 | 0.0 | 9.021 | 17.904 | 8.183 | 17.066 | 0.204 | 0.929 |

## Descriptions des branches, paramètres et réponses internes, contrôle par contrôle

### Après 40 observations (ambiguous)

**linear_coeff** :

```json
[
  -0.387,
  4.509,
  6.706,
  6.706
]
```

**tree_splits** :

```json
[
  2,
  1,
  0
]
```

**tree_depth** :

```json
2
```

**tree_leaves** :

```json
4
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50",
  "road > 0.50 & area <= 2.50",
  "road > 0.50 & area > 2.50",
  "road > 0.50 & area > 2.50"
]
```

**mlp_hidden_road_difference** :

```json
1.227
```

**mlp_hidden_proxy_difference** :

```json
1.023
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.125,
  -0.759,
  0.568,
  0.404,
  0.325,
  -0.426,
  0.264,
  -0.546
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 6.706,
  "Tree": 0.0,
  "TinyMLP": 5.443
}
```

### Après 100 observations (ambiguous)

**linear_coeff** :

```json
[
  0.316,
  4.437,
  6.35,
  6.35
]
```

**tree_splits** :

```json
[
  6,
  0,
  1
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "proxy <= 0.50 & area <= 2.50 & area > 1.50",
  "proxy > 0.50 & area <= 2.50 & area > 1.50",
  "proxy <= 0.50 & area > 2.50 & area > 3.50",
  "proxy > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.251
```

**mlp_hidden_proxy_difference** :

```json
1.051
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.097,
  -0.814,
  0.557,
  0.399,
  0.096,
  -0.433,
  0.309,
  -0.524
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 6.35,
  "Tree": 12.818,
  "TinyMLP": 5.004
}
```

### Après 300 observations (ambiguous)

**linear_coeff** :

```json
[
  0.164,
  4.511,
  6.282,
  6.282
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.264
```

**mlp_hidden_proxy_difference** :

```json
1.057
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.072,
  -0.816,
  0.551,
  0.417,
  -0.005,
  -0.414,
  0.343,
  -0.513
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 6.282,
  "Tree": 0.0,
  "TinyMLP": 4.624
}
```

### Après 500 observations (disambiguation)

**linear_coeff** :

```json
[
  0.226,
  4.521,
  12.244,
  0.239
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.438
```

**mlp_hidden_proxy_difference** :

```json
0.996
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.013,
  -0.854,
  0.49,
  0.258,
  0.155,
  -0.507,
  0.539,
  -0.608
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 0.239,
  "Tree": 0.0,
  "TinyMLP": 0.127
}
```

### Après 900 observations (disambiguation)

**linear_coeff** :

```json
[
  0.374,
  4.467,
  12.44,
  0.047
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.501
```

**mlp_hidden_proxy_difference** :

```json
0.966
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.046,
  -0.864,
  0.542,
  0.317,
  0.037,
  -0.512,
  0.565,
  -0.575
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 0.047,
  "Tree": 0.0,
  "TinyMLP": 0.102
}
```

### Après 1600 observations (disambiguation)

**linear_coeff** :

```json
[
  0.289,
  4.498,
  12.419,
  0.11
]
```

**tree_splits** :

```json
[
  6,
  1,
  0
]
```

**tree_depth** :

```json
3
```

**tree_leaves** :

```json
8
```

**tree_paths** :

```json
[
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area <= 2.50 & area > 1.50",
  "road > 0.50 & area > 2.50 & area > 3.50",
  "road > 0.50 & area > 2.50 & area > 3.50"
]
```

**mlp_hidden_road_difference** :

```json
1.55
```

**mlp_hidden_proxy_difference** :

```json
0.948
```

**mlp_hidden_a4_r1_p0** :

```json
[
  0.099,
  -0.87,
  0.578,
  0.289,
  0.013,
  -0.528,
  0.586,
  -0.582
]
```

**proxy_abs_mean_all_contexts** :

```json
{
  "RLS": 0.11,
  "Tree": 0.0,
  "TinyMLP": 0.072
}
```
