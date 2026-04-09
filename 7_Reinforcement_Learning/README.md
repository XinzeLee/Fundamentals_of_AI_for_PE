# Module 7: Reinforcement Learning (curated resources)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/7_Reinforcement_Learning/RL_buck_control.ipynb">
    <img src="https://img.shields.io/badge/Open_RL_buck_control_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open RL_buck_control.ipynb in Colab" />
  </a>
</p>

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/7_Reinforcement_Learning/DDPG_buck_control.ipynb">
    <img src="https://img.shields.io/badge/Open_DDPG_buck_control_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open DDPG_buck_control.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the tutorial article

**Discussion in the article:** Section IV-D; Section IV-F (reinforcement learning and learning types / architectures).

These curated resources support the **RL** thread in *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

Curated entry to reinforcement learning (RL) with emphasis on **control** and **how rewards shape what the agent learns**. Main external index: **[Awesome RL](https://github.com/aikorea/awesome-rl)**, especially **[Applications → Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)**.

> **Note:** Awesome RL’s maintainers state the list is **no longer updated**. The links below remain useful references; for current libraries, see [Gymnasium](https://gymnasium.farama.org/), [Ray RLlib](https://github.com/ray-project/ray), [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3), and similar projects also linked from Awesome RL.

## Contents

| Item | Description |
|------|-------------|
| **Reading (control)** | Classic RL-for-control papers under Awesome RL’s `#control` anchor (summary below). |
| **Rewards & objectives** | Related themes elsewhere on the same Awesome RL page and ties to control / PE. |
| **Local notebooks** | `RL_buck_control.ipynb` — DQN-style discrete duty steps; `DDPG_buck_control.ipynb` — DDPG with continuous normalized actions for the same averaged buck voltage-tracking task (NumPy + PyTorch). Both include an optional smooth-duty reward variant. |

---

## Awesome RL → [Applications → Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)

The `#control` subsection lists landmark work on **continuous, high-dimensional control** (physical systems, not board games). Entries include:

1. **Pieter Abbeel, Adam Coates, et al.** — *An Application of Reinforcement Learning to Aerobatic Helicopter Flight* (NIPS 2006) — [Paper] [Video]  
   - **Control relevance:** Closed-loop policies on a real dynamical system; apprenticeship / demonstration ideas combined with policy improvement (full algorithm in the paper).

2. **J. Andrew Bagnell and Jeff Schneider** — *Autonomous helicopter control using Reinforcement Learning Policy Search Methods* (ICRA 2001) — [Paper]  
   - **Control relevance:** Early **policy search** on hardware; background for policy-gradient / policy-search families.

**Theme:** Control as sequential decisions under dynamics; learning from **returns, costs, or surrogates** — hence central role of **reward / objective design**.

**Link:** [Awesome RL — Applications — Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)

---

## Reward design and Awesome RL

`#control` lists **applications**, not a dedicated reward-engineering tutorial. Related ideas appear in other sections of the same README:

| Theme | Location on Awesome RL | Control / PE relevance |
|-------|-------------------------|---------------------------|
| Scalar returns vs. average reward | Theory / papers (e.g. R-learning) | Steady-state regulation and tracking, not only discounted sums |
| Policy search & continuous control | Surveys (e.g. *A Tour of RL: Continuous Control*, Ann. Rev. 2019) | Continuous actions (duty, phase shift, …) |
| Credit assignment | Foundations, TD, policy gradient papers | Multi-step PE dynamics obscure cause and effect |
| Operations / scheduling | Applications → Operations research | Business objectives as analogy to multi-objective PE (efficiency, loss, EMI) |

### PE-oriented reward sketch

Design choices for regulation, current limiting, efficiency, and thermal limits often include:

- **Tracking:** negative squared error on \(v\), \(i\), or power; optional derivative terms for damping.  
- **Constraints:** penalties or barriers for over-current, over-voltage, overshoot; shaping before hard limits.  
- **Stability:** sparse penalties for instability; curricula from easy to hard setpoints.  
- **Multi-objective:** weighted sums or scalarizations aligned with deployment goals.

These bullets are **local PE-oriented notes**, not quotations from `#control`.

---

## Other Awesome RL material (control-adjacent)

- **Codes** — e.g. pole-cart and Q-learning controller examples (stabilization benchmarks).  
- **Applications → Robotics** — continuous dynamics and policy / model-based RL.  
- **Open-source platforms** — Gymnasium, RLlib, garage, etc., for standard environments and algorithms.

---

## Place in this course

- **Module 1 (MHA)** — search over **design parameters**. **RL** — search over a **policy** (state → action) under dynamics and uncertainty.  
- **Module 8** (`8_PE_Simulation_Automation`) — simulation loops as inexpensive **rollouts** for training or evaluation (fidelity and reward design matter).  
- **Module 9** (`9_Case_Studies_PE`) — mostly **supervised** learning on logs; RL matters for **closed-loop** behavior and interactive or simulated training.

## Recommended reading path

1. Skim the **Control** list: [link](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control).  
2. Read one **continuous control** survey (Theory section on Awesome RL).  
3. One platform (e.g. Gymnasium + a baseline library) and a classic **cart-pole** or **pendulum** baseline before custom PE environments.

## Local notebooks

- **`RL_buck_control.ipynb`** — DQN (discrete duty steps) with experience replay and a target network on an averaged buck voltage-tracking task (pedagogical; not a switching simulator). Resets vary input voltage, reference, and initial state.
- **`DDPG_buck_control.ipynb`** — DDPG (continuous action in \([-1,1]\), Ornstein–Uhlenbeck exploration, target actor–critic, soft updates) on the same averaged plant and reward framing; compares baseline tracking to a smooth-duty penalty, analogous to the DQN notebook.

---

## References

- [Awesome RL](https://github.com/aikorea/awesome-rl)  
- [Applications → Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)  
