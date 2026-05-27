# 0_To_Get_Started

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/0_To_Get_Started/package_install.ipynb">
    <img src="https://img.shields.io/badge/Open_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open package_install.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the tutorial article

**Role:** Environment setup used before running notebooks referenced throughout the invited tutorial *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). There is no dedicated article section—this folder supports the hands-on material in **Section III–VII** and all modules.

---

Onboarding for the course repo: Python environment and package checks before the AI-for-PE notebooks.

## Contents

- `package_install.ipynb`

## Outcomes

- Python environment suitable for the course (`conda` + `pip`)  
- Core AI/ML packages installed and importable  
- Short sanity checks for numerics, plotting, classical ML, PyTorch, and optimization libraries  

---

## Notebook outline

**Environment**

- Example environment: `conda create -n ai_pe python=3.10 -y` then `conda activate ai_pe`  
- Packages: `numpy`, `matplotlib`, `scikit-learn`, `seaborn`, `torch`, `pyswarms`, `pygad`, `xgboost`

## Algorithms & data

**Algorithms:** Linear regression (`sklearn`), MLP (PyTorch), PSO (PySwarms), GA (PyGAD), XGBoost classifier.

**Data:** `make_regression`, random tensors/arrays, `load_iris`. No local CSV/MAT in this folder.

## Notes

- Each library block runs small runnable examples, not import-only checks.

## Recommended learning sequence

1. Open `package_install.ipynb` in a fresh environment.  
2. Resolve any import errors before later modules.  
3. Confirm each section produces the expected plots or metrics.  
4. Continue to `1_MHA` and `2_Classic_ML` after this notebook completes without errors.
