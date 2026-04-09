# 2_Classic_ML

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/2_Classic_ML/ridge_polynomial_regression.ipynb">
    <img src="https://img.shields.io/badge/Open_ridge_polynomial_regression-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open ridge_polynomial_regression.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/2_Classic_ML/classic_ML.ipynb">
    <img src="https://img.shields.io/badge/Open_classic_ML_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open classic_ML.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the tutorial article

**Discussion in the article:** Section III-A; Section IV-D; Section IV-E.

The classical ML baseline here supports the tutorial narrative in *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

Classical machine learning: a **regression** notebook (polynomial features + Ridge on synthetic data) and a **classification** notebook (decision trees on Breast Cancer).

## Contents

- `ridge_polynomial_regression.ipynb` — bias–variance story in 1-D  
- `classic_ML.ipynb` — classification and decision boundaries  

## Outcomes

- **Polynomial Ridge regression** on synthetic 1-D data: **underfitting**, **overfitting**, and regularization (`ridge_polynomial_regression.ipynb`)  
- `scikit-learn` classification pipeline from data to metrics  
- Decision tree training on a standard benchmark  
- Accuracy and confusion matrix  
- Decision boundaries in 2D projected feature space  
- Optional fuzzy decision tree branch and version quirks  

---

## Notebook outline

**Data**

- `sklearn.datasets.load_breast_cancer`  
- Two features selected for 2D visualization; stratified train/test split  

**Models**

- `DecisionTreeClassifier(max_depth=4, random_state=42)`  
- Optional `fuzzytree.FuzzyDecisionTreeClassifier` with fallback if missing or failing  
- Aligned depth settings when both trees run  

**Visualization**

- Confusion matrices (`seaborn.heatmap`)  
- Decision boundaries for classic and optional fuzzy models  
- Index checks before plotting to avoid out-of-range features  

## Algorithms & data

- **Algorithms:** `DecisionTreeClassifier`; optional `FuzzyDecisionTreeClassifier`.  
- **Data:** Breast Cancer Wisconsin (built-in). No repo CSV/MAT required.

## Notes

- Depth matched between classic and fuzzy tree where possible for a fair comparison.  
- Heatmaps and 2D boundaries support both numeric and geometric interpretation.  
- `fuzzytree` APIs differ by release; the notebook uses conservative argument handling.

## Recommended order

1. `ridge_polynomial_regression.ipynb` for the regression / regularization narrative.  
2. `classic_ML.ipynb` with default `scikit-learn` only (decision tree).  
3. Review confusion matrix and boundaries for the classic tree.  
4. Optionally install `fuzzytree` and compare.  
5. Try other feature pairs or `max_depth` to see boundary changes.
