# 2_Classic_ML

Classical machine learning via a single classification workflow.

## Contents

- `classic_ML.ipynb`

## Outcomes

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

1. Baseline path with default `scikit-learn` only.  
2. Review confusion matrix and boundaries for the classic tree.  
3. Optionally install `fuzzytree` and compare.  
4. Try other feature pairs or `max_depth` to see boundary changes.
