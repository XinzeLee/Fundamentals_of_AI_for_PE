# 3_Ensemble_Learning

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/3_Ensemble_Learning/ensemle_learning.ipynb">
    <img src="https://img.shields.io/badge/Open_ensemle_learning_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open ensemle_learning.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the tutorial article

**Discussion in the article:** **Section III-E** (tree and ensemble ML architectures).

The ensemble-learning notebook supports the tree/ensemble discussion in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

## Contents

- `ensemle_learning.ipynb`

## Outcomes

- Behavior of **Random Forest**, **XGBoost**, and **Decision Tree** baselines side by side  
- Controlled synthetic setups that stress ensembles  
- Repeated runs and distribution-level metrics  
- Class imbalance and noisy labels in classification and regression  
- Mitigations (PCA, outlier handling, regularization) and their effect on scores  

---

## Notebook outline

1. **Correlated features** — RF vs. XGBoost vs. tree; distribution plots; significance tests; PCA + retrain.  
2. **Class imbalance** — `make_classification`; RF vs. XGBoost; aggregated confusion behavior.  
3. **Noisy regression** — noisy sinusoid; `XGBRegressor` vs. `Ridge`; z-score outlier removal and repeat.  
4. **Analysis style** — many random splits; histograms and t-tests; normalized confusion matrices and averaged metrics.

## Algorithms & data

- **Algorithms:** `RandomForestClassifier`, `DecisionTreeClassifier`, `XGBClassifier`, `XGBRegressor`, `Ridge`, `PCA` (preprocessing).  
- **Data:** Synthetic correlated classification, imbalanced classification, noisy regression. No local CSV/MAT.

## Notes

- The notebook is organized as **stress tests**: correlated features, class imbalance, and noisy regression—each with a different failure mode for tree ensembles.  
- Compare **distributions** of scores over repeated splits, not a single lucky train/test partition.  
- **PCA** and **outlier removal** are shown as explicit mitigations when raw features or labels are pathological.  
- Use the same workflow before trusting ensemble surrogates on real PE tabular data (magnetics, converter tables, etc.).

## Recommended learning sequence

1. Run sections with fixed seeds for reproducibility.  
2. Compare score distributions, not only means.  
3. Tie each failure mode to the data generator settings.  
4. Vary noise, imbalance ratio, and correlation to see regime changes.  
5. Reuse the notebook as a template for pre-deployment stress tests.
