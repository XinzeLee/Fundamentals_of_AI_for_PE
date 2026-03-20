# 6_Agentic_AI

Agentic AI for power-electronics workflows, with pointers to the external **PE-GPT** project.

## Official repository

- [XinzeLee/PE-GPT](https://github.com/XinzeLee/PE-GPT)

## Outcomes

- Agentic workflow: LLM-led steps, tools, and PE design tasks  
- PE-GPT stack: LLM agent, RAG, model zoo, simulation hooks, optimization  
- Where domain knowledge, physics-based models, and automation meet  
- Example task classes: component selection, modulation optimization, parameter design  
- High-level picture of local deployment (Streamlit, dependencies)  

---

## Module role

Bridge material for PE-GPT, not a local notebook lab.

1. **Concepts** — PE-focused multimodal LLM framework for design.  
2. **Architecture** — LLM reasoning, RAG over a PE knowledge base, model zoo (incl. PANN), simulation links, metaheuristic optimization.  
3. **Examples (from PE-GPT)** — Flyback component selection; DAB modulation; buck parameter design.  
4. **Deployment** — Repository clone, requirements, Streamlit entry; optional PLECS XML-RPC for simulation-in-the-loop.

## Algorithms & assets (from PE-GPT descriptions)

- LLM agent orchestration  
- RAG for retrieval and grounding  
- Metaheuristic optimization for objectives  
- PANN-class models in the zoo  
- Simulation-coupled decision loops  

**Data / assets:** Knowledge-base documents, multimodal PE inputs/outputs, tutorial/demo materials. **This folder has no course `.ipynb` files** — follow the GitHub repo for code.

## Notes

- PE-GPT is a **workflow** (agent + tools + models), not a single static model.  
- Public releases are described as simplified relative to the full research stack.  
- Python-centric codebase with core modules and tutorials.  
- Streamlit front end (`main.py`) and `requirements` files for setup.  
- After `5_PIML`: PINN/PANN ↔ zoo; `1_MHA` ↔ optimization layer; `8_PE_Simulation_Automation` ↔ verification loops.

## Recommended path

1. Local foundations: `1_MHA`, `4_Neural_Network`, `5_PIML`.  
2. Read [PE-GPT README](https://github.com/XinzeLee/PE-GPT/blob/main/README.md).  
3. Browse [core](https://github.com/XinzeLee/PE-GPT/tree/main/core) and [tutorial](https://github.com/XinzeLee/PE-GPT/tree/main/tutorial).  
4. Local stack: follow PE-GPT’s own setup instructions.

## References

- [PE-GPT](https://github.com/XinzeLee/PE-GPT)  
- [PE-GPT README](https://github.com/XinzeLee/PE-GPT/blob/main/README.md)  
