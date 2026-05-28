# Module 7: Reinforcement Learning (curated resources)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

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

## Alignment with the review article

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

1. Start with `RL_buck_control.ipynb`: explore DQN-style RL for voltage tracking in a buck converter—focus on how reward choices impact tracking and constraint satisfaction.
2. Continue to `DDPG_buck_control.ipynb`: try DDPG (continuous actions) on the same task, and compare its performance to the discrete DQN approach—pay attention to the optional smooth-duty reward modification.
3. Experiment by varying reward weights and plant parameters—observe effects on learned policy behavior and stability in both notebooks.
4. Use provided utilities to reset environment conditions (input voltage, setpoint) for robustness and generalization testing.
5. (Optional) Extend the notebooks: modify the reward, add constraints or new objectives relevant to your PE/control goals, and document changes in agent learning.
   
This hands-on sequence illustrates key RL-for-control concepts in a power electronics context, emphasizing how local notebook experiments guide reward and algorithm choice.

## Local notebooks

- **`RL_buck_control.ipynb`** — DQN (discrete duty steps) with experience replay and a target network on an averaged buck voltage-tracking task (pedagogical; not a switching simulator). Resets vary input voltage, reference, and initial state.
- **`DDPG_buck_control.ipynb`** — DDPG (continuous action in \([-1,1]\), Ornstein–Uhlenbeck exploration, target actor–critic, soft updates) on the same averaged plant and reward framing; compares baseline tracking to a smooth-duty penalty, analogous to the DQN notebook.

---

## References

- [Awesome RL](https://github.com/aikorea/awesome-rl)  
- [Applications → Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)  
