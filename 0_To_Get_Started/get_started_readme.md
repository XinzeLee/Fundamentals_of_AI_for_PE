# 0_To_Get_Started

This folder is the onboarding entry point for the course repository.  
It focuses on environment setup and package verification before moving to advanced AI-for-PE notebooks.

## Notebook in this folder

- `package_install.ipynb`

---

## Learning objectives of this notebook

After completing `package_install.ipynb`, learners should be able to:

- set up a clean Python environment for this course (`conda` + `pip`);
- install and verify the core AI/ML packages used in later modules;
- run baseline examples for numerical computing, plotting, ML, neural networks, and optimization;
- interpret basic model outputs and training/optimization curves;
- identify common package/runtime warnings and continue safely when they are non-blocking.

---

## What this notebook contains

The notebook is organized as a package-by-package validation workflow:

1. **Environment and package installation**
   - recommends creating a dedicated environment:
     - `conda create -n ai_pe python=3.10 -y`
     - `conda activate ai_pe`
   - installs all required packages in one command:
     - `numpy`, `matplotlib`, `scikit-learn`, `seaborn`, `torch`, `pyswarms`, `pygad`, `xgboost`

2. **Package test blocks**
   - **NumPy**: array creation, matrix ops, random numbers, simple linear algebra
   - **Matplotlib**: line/scatter/bar/fill plots and subplot layout
   - **scikit-learn**: synthetic regression generation, train/test split, linear regression, metric evaluation
   - **PyTorch**: device check (CPU/CUDA), simple feed-forward NN, training loop, prediction/loss visualization
   - **PySwarms**: particle swarm optimization with trajectory/contour-style visualization
   - **PyGAD**: genetic algorithm setup, evolution run, best-solution inspection, fitness/population visualization
   - **XGBoost**: Iris classification, train/test split, fitting and epoch-level accuracy plotting

---

## Algorithm and data coverage

### Algorithms covered

- **Linear Regression** (`sklearn.linear_model.LinearRegression`)
- **Feed-forward Neural Network / MLP** (PyTorch)
- **Particle Swarm Optimization (PSO)** (PySwarms)
- **Genetic Algorithm (GA)** (PyGAD)
- **XGBoost Classifier** (`xgboost.XGBClassifier`)

### Data coverage

- **Synthetic/generated data**:
  - `make_regression(...)` for regression demo
  - random tensors/arrays for neural-network and optimization examples
- **Built-in benchmark dataset**:
  - Iris (`sklearn.datasets.load_iris`) for XGBoost classification
- **No local repository CSV/MAT files** are required in this notebook.

---

## Additional code-level notes

- **Good onboarding design**: each package is validated with executable examples, not only import checks.
- **GPU awareness**: PyTorch block checks CUDA availability and selects device accordingly.
- **Visualization-first approach**: many sections include plots to verify behavior qualitatively (fit quality, residuals, convergence).
- **Warnings observed**:
  - PyGAD emits compatibility/deprecation warnings in some environments.
  - XGBoost may show pandas deprecation warnings depending on installed versions.
  - These warnings are usually non-fatal for learning execution.
- **Dependency chain note**: some demos rely on multiple packages together (for example, scikit-learn + matplotlib + seaborn).

---

## Suggested usage for learners

1. Run all cells top-to-bottom in a fresh environment.
2. Confirm no import failures occur.
3. Confirm each section produces expected plots/metrics.
4. If a package fails, reinstall in the same active environment and rerun that section.
5. Proceed to `1_MHA` and `2_Classic_ML` only after this notebook runs successfully end-to-end.
