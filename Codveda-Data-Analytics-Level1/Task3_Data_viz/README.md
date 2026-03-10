# Level 1 - Task 3: Basic Data Visualization

## Dataset : Boston Housing

### Description
Visualisation des données du dataset Boston Housing (déjà nettoyé a la tache 1) à travers
3 types de graphiques : bar plot, line chart et scatter plot.

---

## Graphiques produits

### 1. Bar Plot — Répartition par tranche de prix
![Bar Plot](Task3_Data_viz\housing_bar.png)

- La majorité des maisons se situe dans la tranche **$15-25k** (239 maisons)
- Les propriétés haut de gamme (>$35k) sont peu représentées (67 au total)

### 2. Line Chart — Tendance du prix médian
![Line Chart](Task3_Data_viz\housing_line.png)

- Distribution croissante du prix médian (MEDV) sur l'ensemble des 506 observations
- La moyenne est de **22.5 ($000s)**
- On observe une forte accélération des prix au-delà du rang 450

### 3. Scatter Plot — Nombre de pièces vs Prix médian
![Scatter Plot](Task3_Data_viz\housing_scatter.png.png)

- Corrélation positive claire entre le nombre de pièces (RM) et le prix (MEDV)
- La couleur indique le % de population défavorisée (LSTAT) :
  - **Rouge** → LSTAT élevé → prix bas
  - **Vert** → LSTAT faible → prix élevés

---

## Colonnes utilisées
| Colonne | Description |
|---------|-------------|
| `MEDV`  | Prix médian des maisons ($000s) |
| `RM`    | Nombre moyen de pièces par logement |
| `LSTAT` | % de population à faible statut socio-économique |

---

## Outils
- Python 3.13
- matplotlib
- seaborn
- pandas

## Exécution
```bash
python data_visualization.py
```