# 3_Ensemble_Learning

This folder studies ensemble-learning behavior under challenging data conditions, with emphasis on when common methods succeed or fail.

## Notebook in this folder

- `ensemle_learning.ipynb`

---

## Learning objectives of this notebook

After completing this notebook, learners should be able to:

- explain core behavior differences among **Random Forest**, **XGBoost**, and **Decision Tree** baselines;
- design controlled synthetic experiments to stress-test ensemble methods;
- evaluate model robustness across repeated runs using distribution-level metrics;
- interpret class-imbalance and noisy-label effects in both classification and regression;
- apply practical mitigation ideas (PCA, outlier handling, regularization) and reassess performance.

---

## What this notebook contains

The notebook is organized around failure/sensitivity scenarios for ensemble models:

1. **Highly correlated input features**
   - compares Random Forest, XGBoost, and Decision Tree over repeated runs;
   - visualizes accuracy distributions and performs significance testing;
   - adds a mitigation section using **PCA + model retraining**.

2. **Class imbalance (classification)**
   - generates imbalanced data using `make_classification`;
   - compares Random Forest and XGBoost over multiple trials;
   - aggregates confusion-matrix behavior and per-class performance.

3. **Noisy labels / output noise (regression)**
   - creates noisy sinusoidal regression data;
   - compares `XGBRegressor` against `Ridge` under extreme noise;
   - applies outlier cleaning (z-score based) and repeats the comparison.

4. **Statistical and visual analysis patterns**
   - repeated random splits/runs instead of one-shot evaluation;
   - histogram-based distribution comparisons and t-test interpretation;
   - confusion-matrix normalization and average metric reporting.

---

## Algorithm and data coverage

### Algorithms covered

- **RandomForestClassifier**
- **DecisionTreeClassifier**
- **XGBClassifier** (XGBoost)
- **XGBRegressor** (XGBoost)
- **Ridge Regression**
- **PCA** (as dimensionality-reduction mitigation, not a predictor itself)

### Data coverage

- **Synthetic/generated datasets**:
  - correlated-feature classification setups;
  - imbalanced classification via `make_classification`;
  - noisy sinusoidal regression examples.
- **No local repository CSV/MAT files** are required for this notebook.

---

## Additional information from notebook code

- **Robustness-first evaluation style**:
  - the notebook repeatedly runs each model and reports mean ± std, instead of relying on a single split.

- **Comparative framing is scenario-specific**:
  - different algorithms lead under different data pathologies (correlation, imbalance, noise), which is the core educational message.

- **Statistical testing included**:
  - t-tests are used to support whether observed performance gaps are likely meaningful.

- **Mitigation workflow is explicit**:
  - PCA is explored for correlated features;
  - outlier cleaning is explored for noisy-label regression.

- **Interpretability support**:
  - confusion matrices, histograms, and average class-level metrics are used to move beyond raw accuracy.

- **Practical runtime note**:
  - XGBoost may emit pandas compatibility/deprecation warnings depending on environment versions; these are usually non-fatal for the tutorial flow.

---

## Suggested usage for learners

1. Run all sections with fixed seeds to reproduce baseline behavior.
2. Compare not only mean scores but also score distributions and variance.
3. Focus on the reason each method fails/succeeds under each scenario.
4. Modify noise level, class imbalance ratio, and feature correlation to observe regime shifts.
5. Use this notebook as a template for stress-testing models before real PE deployment.

