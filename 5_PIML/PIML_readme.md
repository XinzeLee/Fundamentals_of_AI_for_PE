# 5_PIML (Physics-Informed Machine Learning)

This module focuses on integrating physical priors into neural-network training, through both:

- **PINN-style** physics-constrained loss design (inside this repo notebooks), and
- **PANN-style** physics-in-architecture modeling (linked external repo summary in `PANN/PANN_readme.md`).

## Notebooks in this folder

- `PINN/pinn_ode.ipynb`
- `PINN/prior_integration_example.ipynb`
- `PINN/prior_integration_example2.ipynb`

## Related reading in this folder

- `PANN/PANN_readme.md` (summary + direct links to external PANN repository)

---

## Learning objectives (overall module)

After completing this module, learners should be able to:

- explain why pure data-driven NN fitting can fail under sparse/noisy data and how physics priors help;
- construct **physics-informed loss functions** that combine data mismatch and equation residual terms;
- use automatic differentiation to enforce ODE/PDE structure during training;
- train PINN-style models for cases with known and unknown physical parameters;
- design toy prior-integration experiments to understand constraint-driven learning behavior;
- distinguish two mainstream PE-oriented PIML strategies:
  - physics in loss (PINN),
  - physics in architecture/inference (PANN).

---

## What each notebook contains

### 1) `PINN/pinn_ode.ipynb`

**What this notebook contains**
- A PINN case study around a temperature annealing / cooling ODE.
- Baseline feedforward NN fitting **without** physics constraints.
- Physics-informed training with residual loss from governing law.
- A variant where physical parameters are known versus learned.
- Long-horizon training loops with scheduler/checkpoint logic and fit/loss visualization.

**Algorithm and data coverage**
- Algorithms: FNN baseline + PINN (ODE residual-constrained training).
- Data: synthetic or generated temperature-time samples (no external repository dataset dependency required).

**Additional code-level notes**
- Uses `torch.autograd.grad` to compute derivatives for residual terms.
- Defines total loss as `data_loss + alpha * physics_loss` with tunable weighting.
- Includes optimizer/scheduler variants (e.g., Adam + cosine/reduce-on-plateau style control).
- Tracks and reloads best-validation checkpoints for stable comparison.

---

### 2) `PINN/prior_integration_example.ipynb`

**What this notebook contains**
- A prior-integration tutorial using a toy physical relationship.
- Builds classic feedforward model first, then adds physics-informed residual penalty.
- Demonstrates training when unknown physical parameter(s) are part of the model and can be learned.
- Visualizes parameter trajectory and loss evolution under prior-constrained optimization.

**Algorithm and data coverage**
- Algorithms: FNN + PINN-style total-loss integration with learnable physics parameter(s).
- Data: synthetic toy data generated from known formula with noise.

**Additional code-level notes**
- Explicitly records learned physical coefficient updates during training.
- Uses large-epoch training to show convergence of both fit and physically meaningful parameter estimates.
- Highlights practical balancing between data-fit quality and physics consistency (`alpha` weighting).

---

### 3) `PINN/prior_integration_example2.ipynb`

**What this notebook contains**
- Broader prior-integration examples for PE context:
  - toy prior-learning setup (structured synthetic relation),
  - extension narrative toward PE-oriented PIML/PANN use cases.
- Implements train/val/test split strategy with low-data settings to illustrate prior benefit.
- Uses standardized inputs, NN training with checkpointing, and scheduler-controlled optimization.

**Algorithm and data coverage**
- Algorithms: feedforward NN under prior-informed/constraint-aware training setup.
- Data: synthetic generated datasets designed to encode known physical structure.

**Additional code-level notes**
- Demonstrates small-data regime behavior with explicit validation tracking.
- Applies practical training hygiene: scaling, checkpointing, scheduled LR updates.
- Includes weight/parameter normalization-style manipulations to stabilize training in constrained setups.

---

## PANN extension (related summarized information)

The `PANN` subfolder in this module now includes a dedicated external summary:

- `PANN/PANN_readme.md`

### What is added there

- a concise overview of **Physics-in-Architecture Neural Network (PANN)**;
- key repository highlights from [XinzeLee/PANN](https://github.com/XinzeLee/PANN);
- practical usage guidance on how to transition from this module's PINN notebooks to PANN workflows;
- direct links to PANN repo resources (main page, README, notebooks, tutorials).

### Why this matters for `5_PIML`

- The current notebooks teach **PINN** via residual-constrained optimization.
- The added PANN summary introduces a complementary paradigm: embedding physics **inside model architecture**, not only in the loss.
- Together, they provide a fuller PIML picture for power-electronics learners.

---

## Consolidated algorithm coverage in `5_PIML`

- **Feedforward neural network (baseline data-driven model)**
- **PINN / physics-informed residual learning**
- **Hybrid total-loss training** (`data_loss + alpha * physics_loss`)
- **Learnable physics-parameter inference** (in selected examples)
- **PANN concept linkage** via module reading (`PANN/PANN_readme.md`)

---

## Consolidated data coverage in `5_PIML`

- **Synthetic ODE-based temperature/cooling trajectories**
- **Toy prior-constrained synthetic datasets**
- **No heavy dependency on repository CSV/MAT files** for core PIML demonstrations in this folder
- **External PANN resource linkage** for architecture-centric PE PIML workflows

---

## Additional practical guidance from code patterns

- Start from a baseline purely data-driven fit first, then add physics loss and compare.
- Tune `alpha` (physics-loss weight) carefully; too high can underfit data, too low can ignore physics.
- Use validation-based checkpointing because PINN loss landscapes can be sensitive.
- Monitor both:
  - prediction metrics (MSE/fit),
  - physics consistency metrics (residual/parameter plausibility).

---

## Suggested learning sequence

1. `PINN/pinn_ode.ipynb` (core PINN concept and ODE residual mechanics)
2. `PINN/prior_integration_example.ipynb` (explicit unknown-parameter prior learning)
3. `PINN/prior_integration_example2.ipynb` (broader prior integration and PE-oriented extension)
4. `PANN/PANN_readme.md` (bridge to external architecture-centric PIML repository)

---

## Direct link for PANN follow-up

- External repository: [https://github.com/XinzeLee/PANN](https://github.com/XinzeLee/PANN)
