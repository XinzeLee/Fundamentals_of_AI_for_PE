# 5_PIML (Physics-Informed Machine Learning)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/5_PIML/PINN/pinn_ode.ipynb">
    <img src="https://img.shields.io/badge/Open_pinn_ode_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open pinn_ode.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/5_PIML/PINN/prior_integration_example.ipynb">
    <img src="https://img.shields.io/badge/Open_prior_integration_example_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open prior_integration_example.ipynb in Colab" />
  </a>
</p>

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/5_PIML/PINN/pinn_pde.ipynb">
    <img src="https://img.shields.io/badge/Open_pinn_pde_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open pinn_pde.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

**Discussion in the article:** [`PINN/`](PINN/) notebooks — **Section IV-A–IV-C** (PIML motivation, priors, PINN fundamentals). [`prior_integration_example.ipynb`](PINN/prior_integration_example.ipynb) emphasizes **IV-B** (integrating prior knowledge).

For **physics-in-architecture (PANN)** material, see [`PANN/README.md`](PANN/README.md) (**Section IV-B**; **VII-E**).

---

Physics priors in neural training: **PINN-style** residual losses in the notebooks here, plus **PANN-style** physics-in-architecture modeling (summary and links in [`PANN/README.md`](PANN/README.md)).

## Contents

| Kind | Path |
|------|------|
| Physics-informed Neural Network | `PINN/pinn_ode.ipynb`, `PINN/pinn_pde.ipynb`, `PINN/prior_integration_example.ipynb` |
| Physics-in-architecture Neural Network | [`PANN/README.md`](PANN/README.md) — external [XinzeLee/PANN](https://github.com/XinzeLee/PANN) |

## Outcomes

- Rationale for physics priors when data are sparse or noisy  
- **Physics-informed losses:** data mismatch + equation residuals  
- Automatic differentiation for ODE/PDE constraints during training  
- PINN setups with known vs. learned physical parameters  
- Small prior-integration experiments and constraint-driven behavior  
- Contrast: physics in the loss (PINN) vs. in architecture / inference (PANN)

---

### `PINN/pinn_ode.ipynb`

**Topics:** Newton cooling ODE $dT/dt = k(T_\infty - T)$; data-only FNN vs PINN with composite loss (ODE residual + IC + sparse data); known vs learnable $k$.

**Algorithms & data:** FNN + PINN (ODE residuals via autograd). Synthetic cooling trajectories.

**Notes:** Same recipe as `pinn_pde.ipynb` (fixed collocation, soft constraints, Adam + optional L-BFGS).

---

### `PINN/pinn_pde.ipynb`

**Topics:** Burgers PDE PINN; MoL reference solution; fixed collocation grids; weighted PDE + IC + BC loss; contour diagnostics.

**Algorithms & data:** FNN + PINN (PDE residuals via autograd). Synthetic Burgers reference field.

**Notes:** Tune $\lambda$ weights so no single term dominates training.

---

### `PINN/prior_integration_example.ipynb`

**Topics:** Toy physical law; feedforward model then physics residual; learnable physical parameters; parameter and loss trajectories.

**Algorithms & data:** FNN + PINN-style loss with learnable physics parameter(s). Noisy synthetic data from a closed-form relation.

**Notes:** Logged coefficient updates; longer training for joint fit and parameter estimates; `alpha` balances data fit vs. physics consistency.

---

## PANN (`PANN/README.md`)

[`PANN/README.md`](PANN/README.md) covers **Physics-in-Architecture Neural Network (PANN)**, highlights of [XinzeLee/PANN](https://github.com/XinzeLee/PANN), and links to that repo’s README, notebooks, and tutorials.

The PINN notebooks here emphasize **residual constraints in the loss**. PANN complements that with **physics inside the network**. Together they sketch two common PE-oriented PIML directions.

## Algorithm summary

- Feedforward NN (data-only baseline)  
- PINN / physics-informed residuals (ODE or PDE)  
- Hybrid training: **weighted composite** objectives (residual + soft IC/BC or IC + optional data terms), not only `data_loss + alpha * physics_loss`  
- Fixed collocation / boundary / initial grids (Burgers + cooling ODE examples)  
- Learnable physical parameters (selected notebooks; cooling rate $k>0$ via $\exp(\log k)$ in `pinn_ode.ipynb`)  
- PANN concepts via [`PANN/README.md`](PANN/README.md)

## Data summary

- Synthetic ODE temperature / cooling trajectories  
- Toy prior-constrained synthetic sets  
- Little reliance on repo CSV/MAT for the core PINN demos  
- External PANN materials for architecture-centric workflows

## Practice notes (from the notebooks)

- Compare a pure data fit to the same model with a physics term before drawing conclusions.  
- Scalar weights ($\lambda_{\mathrm{pde}}, \lambda_{\mathrm{ic}}$, etc.) mediate data vs. physics vs. constraints; if one term dominates, training can stall or overfit the wrong objective.  
- Validation checkpoints help on sensitive PINN loss surfaces.  
- Track both prediction error (e.g. MSE / relative $L_2$ vs. ground truth) and physics side (residuals, parameter plausibility).

## Recommended learning sequence

1. `PINN/pinn_ode.ipynb`  
2. `PINN/pinn_pde.ipynb`  
3. `PINN/prior_integration_example.ipynb`  
4. [`PANN/README.md`](PANN/README.md)

**External PANN repo:** [github.com/XinzeLee/PANN](https://github.com/XinzeLee/PANN)
