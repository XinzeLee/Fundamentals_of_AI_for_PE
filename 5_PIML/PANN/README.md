# 5_PIML / PANN

Bridge to the external **PANN** project and its role in physics-informed AI for power electronics.

## Official repository

- [XinzeLee/PANN](https://github.com/XinzeLee/PANN)

## What PANN is

**PANN** — **Physics-in-Architecture Neural Network**: PE-oriented modeling that bakes circuit / state-space structure into the network (often recurrent), aiming for:

- stronger physical consistency  
- lower data requirements  
- clearer interpretability of converter behavior  
- flexibility across operating points and topologies  

---

## External repository (summary)

**Positioning:** PE-focused “next step” modeling: explainable, data-light, compact networks; recurrent structure with physical meaning.

**Contents:** Model/training/util code; tutorials and notebooks; example data; training and adaptation scripts.

**Stated strengths:** Data-light training via physics priors; compact recurrent-style models; behavior tied to circuit principles; flexibility across modulation and operating conditions.

**Resources:** IEEE and related paper pointers in the upstream README; Colab links; clone + requirements + notebook workflow.

## Recommended path with this course

1. Work through `5_PIML/PINN/` notebooks in this repo.  
2. Open [XinzeLee/PANN](https://github.com/XinzeLee/PANN) and read its [`README.md`](https://github.com/XinzeLee/PANN/blob/main/README.md).  
3. Tutorials and notebooks there before changing core model code.  
4. Contrast with PINN here: **physics in the loss** vs. **physics in architecture / inference**.

## Links

- Repository: [github.com/XinzeLee/PANN](https://github.com/XinzeLee/PANN)  
- README: [github.com/XinzeLee/PANN/blob/main/README.md](https://github.com/XinzeLee/PANN/blob/main/README.md)  
- Notebooks: [github.com/XinzeLee/PANN/tree/main/notebooks](https://github.com/XinzeLee/PANN/tree/main/notebooks)  
- Tutorials: [github.com/XinzeLee/PANN/tree/main/tutorials](https://github.com/XinzeLee/PANN/tree/main/tutorials)  
