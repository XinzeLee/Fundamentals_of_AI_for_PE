# 5_PIML (Physics-Informed Machine Learning)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

Physics priors in neural training: **PINN-style** residual losses in the notebooks here, plus **PANN-style** physics-in-architecture modeling (summary and links in [`PANN/README.md`](PANN/README.md)).

## Contents

| Kind | Path |
|------|------|
| Notebooks | `PINN/pinn_ode.ipynb`, `PINN/prior_integration_example.ipynb`, `PINN/prior_integration_example2.ipynb` |
| PANN bridge | [`PANN/README.md`](PANN/README.md) — external [XinzeLee/PANN](https://github.com/XinzeLee/PANN) |

## Outcomes

- Rationale for physics priors when data are sparse or noisy  
- **Physics-informed losses:** data mismatch + equation residuals  
- Automatic differentiation for ODE/PDE constraints during training  
- PINN setups with known vs. learned physical parameters  
- Small prior-integration experiments and constraint-driven behavior  
- Contrast: physics in the loss (PINN) vs. in architecture / inference (PANN)

---

### `PINN/pinn_ode.ipynb`

**Topics:** Temperature / cooling ODE; baseline FNN without physics; PINN with residual loss; known vs. learned parameters; long training with schedulers, checkpoints, loss and fit plots.

**Algorithms & data:** FNN baseline + PINN (ODE residuals). Synthetic temperature–time trajectories (no external CSV/MAT required).

**Notes:** `torch.autograd.grad` for residuals; total loss `data_loss + alpha * physics_loss`; optimizer/scheduler variants; best checkpoints by validation.

---

### `PINN/prior_integration_example.ipynb`

**Topics:** Toy physical law; feedforward model then physics residual; learnable physical parameters; parameter and loss trajectories.

**Algorithms & data:** FNN + PINN-style loss with learnable physics parameter(s). Noisy synthetic data from a closed-form relation.

**Notes:** Logged coefficient updates; longer training for joint fit and parameter estimates; `alpha` balances data fit vs. physics consistency.

---

### `PINN/prior_integration_example2.ipynb`

**Topics:** Prior integration in a PE-oriented narrative; toy structured synthetic setup; train/val/test under low data; scaled inputs, checkpointing, scheduled learning rate.

**Algorithms & data:** Feedforward NN with prior-informed / constraint-aware training. Synthetic sets with embedded structure.

**Notes:** Small-data regime with validation tracking; scaling, checkpoints, scheduled LR; normalization-style stabilizers for constrained training.

---

## PANN (`PANN/README.md`)

[`PANN/README.md`](PANN/README.md) covers **Physics-in-Architecture Neural Network (PANN)**, highlights of [XinzeLee/PANN](https://github.com/XinzeLee/PANN), and links to that repo’s README, notebooks, and tutorials.

The PINN notebooks here emphasize **residual constraints in the loss**. PANN complements that with **physics inside the network**. Together they sketch two common PE-oriented PIML directions.

## Algorithm summary

- Feedforward NN (data-only baseline)  
- PINN / physics-informed residuals  
- Hybrid training: `data_loss + alpha * physics_loss`  
- Learnable physical parameters (selected notebooks)  
- PANN concepts via [`PANN/README.md`](PANN/README.md)

## Data summary

- Synthetic ODE temperature / cooling trajectories  
- Toy prior-constrained synthetic sets  
- Little reliance on repo CSV/MAT for the core PINN demos  
- External PANN materials for architecture-centric workflows

## Practice notes (from the notebooks)

- Compare a pure data fit to the same model with a physics term before drawing conclusions.  
- `alpha` too large → underfitting data; too small → weak physics enforcement.  
- Validation checkpoints help on sensitive PINN loss surfaces.  
- Track both prediction error (e.g. MSE) and physics side (residuals, parameter plausibility).

## Recommended order

1. `PINN/pinn_ode.ipynb`  
2. `PINN/prior_integration_example.ipynb`  
3. `PINN/prior_integration_example2.ipynb`  
4. [`PANN/README.md`](PANN/README.md)

**External PANN repo:** [github.com/XinzeLee/PANN](https://github.com/XinzeLee/PANN)
