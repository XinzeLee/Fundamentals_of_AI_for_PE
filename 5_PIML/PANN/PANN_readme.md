# 5_PIML / PANN

This section points learners to the external PANN repository and summarizes why it is important for physics-informed AI in power electronics.

## Official repository

- **GitHub**: [XinzeLee/PANN](https://github.com/XinzeLee/PANN)

---

## What PANN is (high-level)

**PANN** stands for **Physics-in-Architecture Neural Network**.  
It is a power-electronics-focused physics-informed modeling approach that embeds circuit/state-space physics into the neural architecture (especially recurrent modeling workflows), aiming for:

- stronger physical consistency,
- lower data demand,
- better interpretability for converter behavior,
- flexibility across operating conditions and topology variants.

---

## Key aspects from the external repo

### 1) Core positioning

- PANN is presented as a next-generation AI approach for PE modeling: explainable, data-light, and lightweight.
- The repo emphasizes recurrent inference with physically meaningful internal structure.

### 2) Practical scope in the repository

The external repo includes:

- code modules (for model/network/training/utilities),
- tutorial and notebooks,
- data folder for examples,
- scripts for training and adaptation workflows.

### 3) Claimed technical strengths

- **Data-light training** via embedded physics priors.
- **Model compactness** (lightweight recurrent architecture style).
- **Physical explainability** (model behavior tied to circuit principles).
- **Flexibility** across modulation, operating points, and converter/topology settings.

### 4) Learning resources and references

The repo provides:

- paper references (IEEE publications listed in README),
- Colab notebook links for quick experimentation,
- local setup instructions (`git clone`, install requirements, run notebooks).

---

## Suggested way to use this with this course repo

1. Finish the local `5_PIML/PINN` notebooks in this repository first.
2. Then open [XinzeLee/PANN](https://github.com/XinzeLee/PANN) and read its `README.md`.
3. Start from the tutorial/notebooks there before modifying model code.
4. Compare PANN ideas with the PINN workflows from this course:
   - PINN: physics in loss/residual constraints,
   - PANN: physics embedded into architecture/inference pipeline.

---

## Direct links for learners

- Main repo: [https://github.com/XinzeLee/PANN](https://github.com/XinzeLee/PANN)
- Repository README: [https://github.com/XinzeLee/PANN/blob/main/README.md](https://github.com/XinzeLee/PANN/blob/main/README.md)
- Notebooks folder: [https://github.com/XinzeLee/PANN/tree/main/notebooks](https://github.com/XinzeLee/PANN/tree/main/notebooks)
- Tutorials folder: [https://github.com/XinzeLee/PANN/tree/main/tutorials](https://github.com/XinzeLee/PANN/tree/main/tutorials)

> Source used for this summary: [XinzeLee/PANN](https://github.com/XinzeLee/PANN)