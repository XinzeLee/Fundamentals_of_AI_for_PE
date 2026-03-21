# 3_Ensemble_Learning

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Alignment with the tutorial article

**Discussion in the article:** Section III-A; Section IV-D; Section IV-E.

The ensemble-learning notebook supports the tree/ensemble discussion in *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

Ensemble methods under difficult data conditions: when gains appear and when they break down.

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

- Mean ± std over repeats instead of a single split.  
- Leading method depends on the pathology (correlation, imbalance, noise).  
- t-tests support “meaningful gap” vs. noise.  
- PCA and outlier cleaning appear as explicit mitigation steps.  
- XGBoost may print pandas-related warnings on some stacks; usually non-fatal for the tutorial flow.

## Recommended order

1. Run sections with fixed seeds for reproducibility.  
2. Compare score distributions, not only means.  
3. Tie each failure mode to the data generator settings.  
4. Vary noise, imbalance ratio, and correlation to see regime changes.  
5. Reuse the notebook as a template for pre-deployment stress tests.
