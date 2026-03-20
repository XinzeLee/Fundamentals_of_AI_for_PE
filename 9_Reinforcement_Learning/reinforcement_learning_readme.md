# Module 9: Reinforcement Learning (curated resources)

This module provides a **curated entry point** to reinforcement learning (RL), with emphasis on **control-oriented applications** and **how rewards define what the agent learns**. The primary external reference summarized here is the community-maintained list **[Awesome RL](https://github.com/aikorea/awesome-rl)**—in particular the **[Applications → Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)** subsection.

> **Note:** The Awesome RL README states that **the page is no longer maintained**. The links and paper pointers below remain useful as historical pointers; for up-to-date libraries, also consult current docs for [OpenAI Gym](https://github.com/openai/gym), [Ray RLlib](https://github.com/ray-project/ray), [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3), etc., which are listed elsewhere in the same Awesome RL document.

---

## What this module contains

| Item | Description |
|------|-------------|
| **Curated reading (Control)** | Short list of **classic RL-for-control** references under the `#control` anchor of Awesome RL (see summary below). |
| **Reward & objective design (highlighted)** | Pointers to **reward-related ideas** on the same Awesome RL page (not only the `#control` bullet list) and how they connect to control. |
| **Hands-on notebooks** | *Not present in this repository snapshot.* When you add notebooks here, treat this file as the module map and extend the “Local notebooks” section. |

---

## Summary: Awesome RL → [Applications → Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)

The **`#control`** subsection is a **compact reading list** of landmark work applying RL to **continuous, high-dimensional control** (not abstract games). As indexed in Awesome RL, it highlights:

1. **Pieter Abbeel, Adam Coates, et al.** — *An Application of Reinforcement Learning to Aerobatic Helicopter Flight* (NIPS 2006) — [Paper] [Video]  
   - **Why it matters for control:** Learns **closed-loop policies** for a **real dynamical system** (helicopter) under realistic dynamics and safety-critical constraints; illustrates **learning from demonstrations / apprenticeship-style ideas** in combination with RL-style improvement (see the original paper for the full method).

2. **J. Andrew Bagnell and Jeff G. Schneider** — *Autonomous helicopter control using Reinforcement Learning Policy Search Methods* (ICRA 2001) — [Paper]  
   - **Why it matters for control:** Early **policy search** on a physical platform; useful baseline for understanding **policy gradient / policy search** families before deep RL.

**Takeaway:** Both entries stress **control as sequential decision-making** under dynamics: the agent chooses actions over time, and **learning** is driven by **evaluation of behavior** (returns, costs, or surrogate objectives)—which is where **reward / objective design** becomes central.

**Direct link:** [Awesome RL — Applications — Control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)

---

## Highlight: reward function design (why it matters for control)

The `#control` subsection itself lists **applications**, not a dedicated “reward engineering” tutorial. On the **same Awesome RL README**, reward-related concepts appear in other sections:

| Theme | Where it shows up on Awesome RL (same repo) | Relevance to control / PE |
|------|-----------------------------------------------|----------------------------|
| **Scalar returns vs. average reward** | Theory / Papers — e.g. **R-Learning** (*maximizing undiscounted / relative values*). | Control tasks often care about **steady-state** performance (regulation, tracking error), not only a discounted sum. |
| **Policy search & continuous control** | Surveys — e.g. *A Tour of Reinforcement Learning: The View from Continuous Control* (Ann. Rev. 2019). | Connects **policy optimization** to **continuous action spaces** typical in power electronics (duty cycle, phase shift, etc.). |
| **Credit assignment** | Foundational papers (e.g. Minsky 1961) and TD / policy gradient papers. | Multi-step dynamics (inductor current, temperature) make **which action caused which outcome** non-obvious—good reward design reduces ambiguity. |
| **Operations / scheduling** | Applications → **Operations Research** | Shows RL with **business objectives** (throughput, tardiness)—analogous to **multi-objective** PE metrics (efficiency, loss, EMI). |

### Practical angles (especially for power electronics)

When you design **rewards** for **control** tasks (voltage regulation, current limiting, efficiency, thermal limits), consider:

- **Regulation / tracking:** negative squared error on \(v\), \(i\), or power; often add **derivative terms** for damping.
- **Constraints:** **penalty** or **barrier** terms for over-current, over-voltage, overshoot; or **reward shaping** that guides the agent before hard constraints bite.
- **Safety / stability:** sparse penalties for instability indicators; curriculum learning (easier setpoints first).
- **Multi-objective:** weighted sum of efficiency, loss, and stress metrics—or **scalarization** consistent with your deployment goal.

These are **not** quoted from the `#control` anchor; they are **additional guidance** to connect RL theory to PE-style control problems.

---

## Highlight: control-related tasks (beyond the two helicopter papers)

Still within **Awesome RL**, useful **control-adjacent** material includes:

- **Codes →** *Simulation code for Reinforcement Learning Control Problems* — *Pole-Cart Problem*, *Q-learning Controller* (classic **stabilization** benchmarks).
- **Applications → Robotics** — many **policy search / model-based** RL works for **continuous dynamics** (related mindset to PE plants).
- **Open Source Reinforcement Learning Platforms** — e.g. **OpenAI Gym**, **Ray RLlib**, **garage**, etc., for **standardized control environments** and reproducible algorithms.

Use these when you want **environments** and **baselines** beyond the short `#control` reading list.

---

## Additional information

### How this fits the `Fundamentals_of_AI_for_PE` learning path

- **Modules 1 (MHA)** and classical optimization **search for a point** (design variables). **RL** searches for a **policy** (mapping states → actions) under **uncertainty and dynamics**.
- **Module 7 (PE Simulation Automation)** can supply **cheap rollouts** (simulation loops) for RL training or evaluation—subject to **simulation fidelity** and **reward design**.
- **Module 8 (Case Studies)** often uses **supervised learning** on logged data; RL is relevant when you need **closed-loop** behavior and **online** or **simulated** interaction.

### Suggested follow-up reading order

1. Skim **Control** entries: [link](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control).  
2. Read **continuous control** perspective (survey linked under Theory).  
3. Pick **one** platform (e.g. Gymnasium + a stable baseline library) and reproduce a **cart-pole** or **pendulum** agent before attempting a PE-inspired custom environment.

### Local notebooks (placeholder)

If you add notebooks under `9_Reinforcement_Learning/`, list them here, for example:

- `*.ipynb` — environment definition, reward specification, training loop, evaluation plots.

---

## References (external)

- **Awesome RL (curated list):** [https://github.com/aikorea/awesome-rl](https://github.com/aikorea/awesome-rl)  
- **Control subsection:** [https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control](https://github.com/aikorea/awesome-rl?tab=readme-ov-file#control)
