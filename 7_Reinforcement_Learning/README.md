# Module 7: Reinforcement Learning (curated resources)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

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

**Discussion in the article:** **Section III-D** (learning types — reinforcement learning for PE control).

These curated resources support the **RL** thread in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

Curated entry to reinforcement learning (RL) with emphasis on **control** and **how rewards shape what the agent learns**. Main external index: **[Awesome RL](https://github.com/aikorea/awesome-rl)**.

## Contents

| Item | Description |
|------|-------------|
| **Reading (control)** | Classic RL-for-control papers under Awesome RL’s `#control` anchor (summary below). |
| **Rewards & objectives** | Related themes elsewhere on the same Awesome RL page and ties to control / PE. |
| **Local notebooks** | `RL_buck_control.ipynb` — DQN-style discrete duty steps; `DDPG_buck_control.ipynb` — DDPG with continuous normalized actions for the same averaged buck voltage-tracking task (NumPy + PyTorch). Both include an optional smooth-duty reward variant. |

---

## PE-oriented reward sketch

Control as sequential decisions under dynamics; learning from **returns, costs, or surrogates** — hence central role of **reward / objective design**. Design choices for regulation, current limiting, efficiency, and thermal limits often include:

- **Tracking:** negative squared error on \(v\), \(i\), or power; optional derivative terms for damping.  
- **Constraints:** penalties or barriers for over-current, over-voltage, overshoot; shaping before hard limits.  
- **Stability:** sparse penalties for instability; curricula from easy to hard setpoints.  
- **Multi-objective:** weighted sums or scalarizations aligned with deployment goals.

---

## Other Awesome RL material (control-adjacent)

- **Codes** — e.g. pole-cart and Q-learning controller examples (stabilization benchmarks).  
- **Applications → Robotics** — continuous dynamics and policy / model-based RL.  
- **Open-source platforms** — Gymnasium, RLlib, garage, etc., for standard environments and algorithms.

## Recommended learning sequence

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
