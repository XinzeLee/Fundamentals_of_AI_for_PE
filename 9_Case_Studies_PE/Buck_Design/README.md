# Buck_Design

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb">
    <img src="https://img.shields.io/badge/Buck_comprehensive-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open buck_comprehensive_case_study.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Buck_Design/buck_modeling_NN.ipynb">
    <img src="https://img.shields.io/badge/Buck_modeling_NN-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open buck_modeling_NN.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Buck_Design/xgboost_buck_modeling.ipynb">
    <img src="https://img.shields.io/badge/Buck_XGBoost-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open xgboost_buck_modeling.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

**Discussion in the article:** **Sec. VII-A** (EDA); **VII-B** (ML surrogate modeling); **VII-C** (MHA optimization).

These notebooks support the **buck converter** one-stop case study in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). Parent overview: [`../README.md`](../README.md).

---

Synchronous buck design: exploration, surrogate modeling, and metaheuristic optimization on simulation-derived performance tables.

## Contents

- `buck_comprehensive_case_study.ipynb`  
- `buck_modeling_NN.ipynb`  
- `xgboost_buck_modeling.ipynb`  
- `total_100W_12V.csv`, `sync_buck_performances_cleaned.csv`

## Outcomes

- EDA and multi-objective screening before optimization  
- Compare classical ensembles, XGBoost, and FNN surrogates on efficiency / ripple  
- Surrogate-assisted PSO and GA over design objectives  
- Outlier handling and correlation diagnostics on tabular buck data  

---

### `buck_comprehensive_case_study.ipynb`

**Topics:** EDA, objectives, lookup / screening, surrogate training, PSO vs. GA over surrogate objectives.

**Algorithms & data:** FNN surrogates, PSO, GA, classical baselines in analysis. `total_100W_12V.csv` and derived loss/ripple-style targets.

**Notes:** Weighted / scenario multi-objective steps; outlier handling; correlation and distribution diagnostics before optimization.

---

### `buck_modeling_NN.ipynb`

**Topics:** Efficiency modeling — EDA, Random Forest / XGBoost, deeper MLP surrogate with regularization and scheduler, prediction surfaces.

**Algorithms & data:** RandomForestRegressor, XGBoost, FNN, t-SNE. `sync_buck_performances_cleaned.csv`.

**Notes:** Scaled inputs; train/val/test; R², RMSE, MAE, loss curves.

---

### `xgboost_buck_modeling.ipynb`

**Topics:** Efficiency and ripple via XGBoost; training diagnostics; optimization stage driven by trained surrogates.

**Algorithms & data:** `XGBRegressor`, Random Forest baseline, MHA stage. `sync_buck_performances_cleaned.csv` with engineered ripple target.

**Notes:** Outlier filtering; prediction vs. actual and round-wise curves.

---

## Algorithm summary

- Random Forest, XGBoost, FNN/MLP surrogates  
- PSO, GA (surrogate-assisted search)  
- t-SNE, correlation / outlier analysis  

## Data summary

- `total_100W_12V.csv` — comprehensive case study (loss / ripple style targets)  
- `sync_buck_performances_cleaned.csv` — efficiency and ripple modeling notebooks  

## Recommended learning sequence

1. `buck_comprehensive_case_study.ipynb`  
2. `buck_modeling_NN.ipynb`  
3. `xgboost_buck_modeling.ipynb`  
