# 6_Agentic_AI

This module introduces agentic AI for power-electronics workflows through the external **PE-GPT** project.

## Official repository

- Main repository: [XinzeLee/PE-GPT](https://github.com/XinzeLee/PE-GPT)

---

## Learning objectives of this module

After going through this section, learners should be able to:

- understand what an **agentic AI** workflow means in PE design;
- explain PE-GPT's hybrid architecture (LLM agent + RAG + model zoo + simulation + optimization);
- identify where domain knowledge, physics-based models, and tool automation are integrated;
- recognize how PE-GPT supports practical tasks (component selection, modulation optimization, parameter design);
- set up and run the PE-GPT demo stack locally at a high level.

---

## What this module contains

This folder serves as a directional bridge to PE-GPT, focusing on:

1. **Concept overview**
   - PE-GPT is described as a PE-specific multimodal LLM framework for design tasks.

2. **System-level architecture**
   - Hybrid workflow combining:
     - LLM agent reasoning,
     - retrieval-augmented generation (RAG) with PE knowledge base,
     - model zoo (including PANN),
     - simulation repository/tool connections,
     - metaheuristic optimization components.

3. **Application examples (from PE-GPT)**
   - Flyback converter design with component selection.
   - DAB modulation optimization.
   - Buck converter parameter design.

4. **Deployment pointers**
   - clone repo, install requirements, run Streamlit app;
   - optional Plecs XML-RPC integration path for simulation-in-the-loop workflows.

---

## Algorithm and data coverage

### Algorithm coverage (as summarized from PE-GPT)

- **LLM-agent orchestration** for design-task decomposition and interaction.
- **RAG pipeline** for domain-specific retrieval and grounding.
- **Metaheuristic optimization** for PE design objectives.
- **Physics-in-architecture model integration** (PANN in model zoo).
- **Simulation-coupled decision loop** (tool-assisted verification path).

### Data coverage (as summarized from PE-GPT)

- **Knowledge-base documents** used for retrieval and grounding (simplified in public release).
- **PE-specific multimodal inputs/outputs** across model and simulation workflows.
- **Tutorial/demo assets** for converter design tasks.
- **No standalone notebook in this local folder**; this module points to external implementation resources.

---

## Additional information for learners

- PE-GPT is positioned as a **workflow paradigm**, not just a single model.
- Public repo notes describe this release as a **simplified version** of the full methodology.
- The codebase is Python-dominant and includes both core framework modules and tutorial materials.
- Deployment uses Streamlit front-end flow (`main.py`) with dependency setup from requirements files.
- If you explore this after `5_PIML`, you can map:
  - `PINN`/`PANN` modeling ideas -> model zoo component,
  - `MHA` ideas -> optimization agent/tooling layer,
  - simulation automation -> verification loop.

---

## Suggested learning path from this repo to PE-GPT

1. Finish local foundations:
   - `1_MHA`, `4_Neural_Network`, `5_PIML`.
2. Read PE-GPT README in full:
   - [PE-GPT README](https://github.com/XinzeLee/PE-GPT/blob/main/README.md)
3. Inspect key project areas:
   - [core](https://github.com/XinzeLee/PE-GPT/tree/main/core)
   - [tutorial](https://github.com/XinzeLee/PE-GPT/tree/main/tutorial)
4. Run local deployment in PE-GPT environment (per their instructions).

---

## References

- PE-GPT repository: [https://github.com/XinzeLee/PE-GPT](https://github.com/XinzeLee/PE-GPT)
- PE-GPT README: [https://github.com/XinzeLee/PE-GPT/blob/main/README.md](https://github.com/XinzeLee/PE-GPT/blob/main/README.md)