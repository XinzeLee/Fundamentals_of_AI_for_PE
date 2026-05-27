# 6_Agentic_AI

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Alignment with the tutorial article

**Discussion in the article:** **Section VI** (VI-A generative AI basics; VI-B reactive → agentic leap; VI-C PE-GPT2 process automation).

This documentation folder supports the **agentic AI** discussion in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

Agentic AI for power-electronics workflows, with pointers to the external **PE-GPT** project.

## Official repository

- [XinzeLee/PE-GPT](https://github.com/XinzeLee/PE-GPT)

## Outcomes

- Agentic workflow: LLM-led steps, tools, and PE design tasks  
- PE-GPT stack: LLM, RAG, model zoo, simulation hooks, optimization  
- Where domain knowledge, physics-based models, and automation meet  
- Example task classes: component selection, modulation optimization, parameter design  
- High-level picture of local deployment (Streamlit, dependencies)  

## Notes

- PE-GPT is an **agentic-AI framework** (agent + tools + models), not a single foundational model.  
- Public releases are described as simplified relative to the full research stack.  
- Python-centric codebase with core modules and tutorials.  
- Streamlit front end (`main.py`) and `requirements` files for setup.  
- After `5_PIML`: PINN/PANN ↔ zoo; `1_MHA` ↔ optimization layer; `8_PE_Simulation_Automation` ↔ verification loops.

## Recommended learning sequence

1. Local foundations: `1_MHA`, `4_Neural_Network`, `5_PIML`.  
2. Read [PE-GPT README](https://github.com/XinzeLee/PE-GPT/blob/main/README.md).  
3. Browse [core](https://github.com/XinzeLee/PE-GPT/tree/main/core) and [tutorial](https://github.com/XinzeLee/PE-GPT/tree/main/tutorial).  
4. Local stack: follow PE-GPT’s own setup instructions.

## References

- [PE-GPT](https://github.com/XinzeLee/PE-GPT)  
- [PE-GPT README](https://github.com/XinzeLee/PE-GPT/blob/main/README.md)  
