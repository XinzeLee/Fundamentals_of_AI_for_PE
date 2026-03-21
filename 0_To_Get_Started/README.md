# 0_To_Get_Started

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Alignment with the tutorial article

**Role:** Environment setup used before running notebooks referenced throughout the invited tutorial *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). There is no dedicated article section—this folder supports the practical material in all modules.

---

Onboarding for the course repo: Python environment and package checks before the AI-for-PE notebooks.

## Contents

- `package_install.ipynb`

## Outcomes

- Python environment suitable for the course (`conda` + `pip`)  
- Core AI/ML packages installed and importable  
- Short sanity checks for numerics, plotting, classical ML, PyTorch, and optimization libraries  
- Basic reading of metrics, training curves, and optimizer output  
- Typical package warnings and when they are usually safe to ignore  

---

## Notebook outline

**Environment**

- Example environment: `conda create -n ai_pe python=3.10 -y` then `conda activate ai_pe`  
- Packages: `numpy`, `matplotlib`, `scikit-learn`, `seaborn`, `torch`, `pyswarms`, `pygad`, `xgboost`

**Per-library checks**

| Library | Coverage |
|---------|----------|
| NumPy | Arrays, matrix ops, RNG, small linear algebra |
| Matplotlib | Line / scatter / bar / fill, subplots |
| scikit-learn | Synthetic regression, split, linear regression, metrics |
| PyTorch | CPU/CUDA, small FNN, training loop, loss plots |
| PySwarms | PSO with trajectory / landscape-style plots |
| PyGAD | GA setup, evolution, fitness / population plots |
| XGBoost | Iris classification, split, accuracy vs. rounds |

## Algorithms & data

**Algorithms:** Linear regression (`sklearn`), MLP (PyTorch), PSO (PySwarms), GA (PyGAD), XGBoost classifier.

**Data:** `make_regression`, random tensors/arrays, `load_iris`. No local CSV/MAT in this folder.

## Notes

- Each library block runs small runnable examples, not import-only checks.  
- PyTorch block selects CPU or CUDA when available.  
- Plots support qualitative checks (fit, residuals, convergence).  
- **Environment:** PyGAD may print compatibility/deprecation messages; XGBoost may warn about pandas APIs depending on versions — usually non-blocking for these demos.  
- Some sections chain several packages (e.g. sklearn + matplotlib + seaborn).

## Recommended order

1. Open `package_install.ipynb` in a fresh environment.  
2. Resolve any import errors before later modules.  
3. Confirm each section produces the expected plots or metrics.  
4. Continue to `1_MHA` and `2_Classic_ML` after this notebook completes without errors.
