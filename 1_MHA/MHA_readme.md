# 1_MHA (Meta-Heuristic Algorithms)

This folder covers both **single-objective** and **multi-objective** meta-heuristic optimization, with examples ranging from benchmark functions to power-electronics design problems.

## Notebooks in this folder

- `Single_Objective_MHA/sing_obj_MHA.ipynb`
- `Single_Objective_MHA/pso_hyp_tuning.ipynb`
- `Single_Objective_MHA/algorithm_stats_compare.ipynb`
- `Single_Objective_MHA/buck_design_PSO.ipynb`
- `Multi_Objective_MHA/multi_obj_MHA_master.ipynb`

---

## Learning objectives (overall)

After finishing the notebooks in `1_MHA`, learners should be able to:

- explain core ideas of PSO and NSGA-II in practical optimization workflows;
- formulate objective functions, constraints, and penalties for engineering design;
- tune PSO hyperparameters and compare variant behaviors (e.g., LDIW, TVAC);
- evaluate optimizer robustness statistically across repeated runs;
- interpret Pareto fronts and select designs from multi-objective trade-off surfaces;
- apply MHA methods to power-electronics design examples (especially synchronous buck and DAB-related settings).

---

## What each notebook contains

### 1) `sing_obj_MHA.ipynb`

**What this notebook contains**
- Introduces single-objective PSO on benchmark landscapes (Sphere, Rastrigin).
- Implements PSO with linearly decreasing inertia and visualizes particle trajectories/convergence.
- Compares PSO with deterministic optimization baselines (LP/SLSQP/BFGS/Nelder-Mead) and Differential Evolution.

**Algorithm and data coverage**
- Algorithms: PSO, Differential Evolution, SLSQP (Lagrange-style constrained optimization), BFGS, Nelder-Mead, LP baseline.
- Data: synthetic benchmark functions only (no local dataset files).

**Additional code-level notes**
- Uses custom step-wise PSO loop to dynamically update inertia weight.
- Includes animation blocks for both search trajectory and cost-history evolution.
- Good pedagogical bridge between deterministic and stochastic optimization.

---

### 2) `pso_hyp_tuning.ipynb`

**What this notebook contains**
- Implements and compares PSO variants:
  - PSO-LDIW (linearly decreasing inertia weight),
  - TVAC-PSO (time-varying acceleration coefficients).
- Runs hyperparameter sweeps (notably inertia `w`) with repeated trials.
- Reports convergence iteration and best-cost behavior under different settings.

**Algorithm and data coverage**
- Algorithms: PSO-LDIW, TVAC-PSO.
- Data: synthetic optimization functions (10-D Rastrigin, 50-D One-Max style setup).

**Additional code-level notes**
- Emphasizes parameter schedules (`w`, `c1`, `c2`) rather than fixed values.
- Multi-run outputs make variance and stability effects visible.
- Useful as a practical template for PSO configuration studies.

---

### 3) `algorithm_stats_compare.ipynb`

**What this notebook contains**
- Runs PSO and GA repeatedly on the same benchmark problem (10-D Rastrigin).
- Collects best costs from multiple runs.
- Performs statistical comparison using paired t-test.
- Visualizes result distributions with histograms and fitted normal curves.

**Algorithm and data coverage**
- Algorithms: PSO (`pyswarms`), GA (`pygad`), statistical test (paired t-test).
- Data: synthetic benchmark objective values from repeated optimizer runs.

**Additional code-level notes**
- Focuses on **distribution-level** performance, not only single best run.
- Good example for introducing significance testing in optimizer comparison.
- Includes warning handling context from `pygad` runtime output.

---

### 4) `buck_design_PSO.ipynb`

**What this notebook contains**
- Formulates synchronous buck converter design as single-objective optimization.
- Defines analytical loss/volume-related calculations and objective with penalty terms.
- Uses PSO to optimize design variables (e.g., `L`, `C`) under practical constraints.
- Visualizes objective landscapes and interprets optimal design details.

**Algorithm and data coverage**
- Algorithms: constrained PSO with penalty-based objective.
- Data: model-generated engineering data from analytical equations (no external dataset dependency).

**Additional code-level notes**
- Objective function explicitly handles feasibility via penalty factor.
- Includes domain-oriented visualization (3D/2D surfaces for tradeoff intuition).
- Connects abstract PSO mechanics to real PE design constraints.

---

### 5) `multi_obj_MHA_master.ipynb`

**What this notebook contains**
- Introduces Pareto optimality and non-dominated sorting with toy examples.
- Uses ZDT-1 benchmark for multi-objective analysis.
- Implements NSGA-II using `pymoo`, including version/strategy experiments.
- Extends to multi-objective PE design workflow with Pareto-front filtering and design selection.

**Algorithm and data coverage**
- Algorithms: non-dominated sorting, NSGA-II (including variant behavior), Pareto-set extraction.
- Supporting packages/methods: `paretoset`, `pymoo`.
- Data: primarily synthetic/analytical objective evaluations; engineering objective surfaces generated from formulas.

**Additional code-level notes**
- Includes step-wise progress visualization of Pareto front evolution.
- Demonstrates practical post-optimization design retrieval from Pareto sets using value ranges.
- Strong capstone notebook for transitioning from benchmark MOO to engineering decision-making.

---

## Consolidated algorithm coverage in `1_MHA`

- **Single-objective MHA**: PSO (multiple variants), GA.
- **Multi-objective MHA**: NSGA-II, non-dominated sorting, Pareto-front analysis.
- **Comparative baselines**: Differential Evolution, SLSQP, BFGS, Nelder-Mead, LP baseline.

---

## Consolidated data coverage in `1_MHA`

- **Synthetic benchmark functions**: Sphere, Rastrigin, ZDT-1, One-Max style objective.
- **Engineering model-generated data**: analytical loss/volume/cutoff-frequency surfaces for PE design.
- **External repository dataset files**: generally not the primary dependency in this folder; notebooks rely mostly on generated objective evaluations.

---

## Suggested learning sequence

1. `sing_obj_MHA.ipynb` (PSO fundamentals + visual intuition)
2. `pso_hyp_tuning.ipynb` (variant behavior and hyperparameter effects)
3. `algorithm_stats_compare.ipynb` (robustness and statistical comparison)
4. `buck_design_PSO.ipynb` (single-objective engineering application)
5. `multi_obj_MHA_master.ipynb` (Pareto/NSGA-II and multi-objective engineering design)
