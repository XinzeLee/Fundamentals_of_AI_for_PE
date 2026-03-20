# 2_Classic_ML

This folder introduces classic machine-learning workflows through a practical classification example.

## Notebook in this folder

- `classic_ML.ipynb`

---

## Learning objectives of this notebook

After completing `classic_ML.ipynb`, learners should be able to:

- build a standard classification pipeline using `scikit-learn`;
- train and evaluate a **Decision Tree** classifier on a real benchmark dataset;
- interpret classification quality using **accuracy** and **confusion matrix**;
- visualize model behavior through **decision boundaries** in 2D feature space;
- understand optional fuzzy-logic extensions (fuzzy decision tree) and dependency handling.

---

## What this notebook contains

The notebook focuses on decision-tree-based classification for breast cancer diagnosis:

1. **Dataset loading and preprocessing**
   - loads `sklearn.datasets.load_breast_cancer`;
   - extracts features/labels and selects two features for visualization;
   - performs train/test split with stratification.

2. **Classic Decision Tree baseline**
   - trains `DecisionTreeClassifier(max_depth=4, random_state=42)`;
   - computes predictions and evaluation metrics.

3. **Optional Fuzzy Decision Tree branch**
   - attempts to import `fuzzytree` and run `FuzzyDecisionTreeClassifier`;
   - includes fallback behavior if package import or initialization fails;
   - aligns depth settings with classic tree for fairer comparison.

4. **Visualization and interpretation**
   - plots confusion matrices with `seaborn.heatmap`;
   - plots decision boundaries for classic and (if available) fuzzy models;
   - includes feature-index checks to avoid out-of-bound plotting errors.

---

## Algorithm and data coverage

### Algorithms covered

- **Decision Tree Classifier** (`sklearn.tree.DecisionTreeClassifier`)
- **Fuzzy Decision Tree Classifier** (`fuzzytree.FuzzyDecisionTreeClassifier`, optional dependency)

### Data coverage

- **Primary dataset**: Breast Cancer Wisconsin dataset via `load_breast_cancer()`.
- **Data type**: built-in tabular classification dataset from `scikit-learn`.
- **No local repository CSV/MAT files** are required for this notebook.

---

## Additional information from notebook code

- **Fair comparison intent**:
  - model depth is matched (e.g., `max_depth=4`) between classic and fuzzy trees where possible.

- **Visualization-first teaching design**:
  - confusion matrix heatmaps are used for quantitative interpretation;
  - 2D decision-boundary plots provide geometric intuition for classifier behavior.

- **Defensive programming details**:
  - plotting utility checks feature index bounds before generating decision surfaces.

- **Practical caveat**:
  - fuzzytree API parameters may vary by package version, so some arguments are intentionally handled conservatively in code.

---

## Suggested usage for learners

1. Run the notebook end-to-end with default `scikit-learn` setup.
2. Verify baseline decision-tree performance and confusion matrix interpretation.
3. Optionally install `fuzzytree` and rerun to compare classic vs fuzzy behavior.
4. Modify selected feature pairs and tree depth to observe decision-boundary changes.
