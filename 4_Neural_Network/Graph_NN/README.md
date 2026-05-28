# Graph_NN (Graph Neural Networks)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Alignment with the review article

**Discussion in the article:** **Sec. II-D** (graph data in PE); **Sec. III-E** (GNN architectures).

These resources complement the **graph data** and **GNN architecture** discussion in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026).

---

Graph neural networks (GNNs) for **relational data**: circuit topologies, module layouts, and control graphs where **nodes and edges** carry physical meaning. This folder lists **curated external resources** (no local `.ipynb` yet).

## Contents

- `README.md` (this file) — reading list for GNN foundations and PE-oriented applications

## Outcomes

- Relate **graph representations** to PE design objects (converter graphs, layouts, modules)  
- Understand **message passing** as an inductive bias for locality and multi-hop coupling  
- Connect coursework and surveys to **converter performance modeling** (e.g. Circuit-to-Graph)

---

## Reading list

| Resource | Role |
|----------|------|
| [GML2023](https://github.com/xbresson/GML2023/tree/main) (Xavier Bresson) | Hands-on **Graph Machine Learning** course — notebooks, Colab path, conda envs |
| [Awesome Graph Neural Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks) | Surveys and paper lists (GCN, GAT, GraphSAGE, spatio-temporal GNNs); library pointers |
| [Circuit-to-Graph (C2G)](https://github.com/Weihao-Lei/C2G) | **PE application** — topology → graph → GCN+MLP surrogate; fine-tuning for new operating points ([JESTPE 2026](https://ieeexplore.ieee.org/document/10812345)) |

**Suggested sequence:** skim a GNN survey → work through selected **GML2023** notebooks → study **C2G** for converter graph construction and training.

---

## Algorithm summary (conceptual)

- **GCN** — neighborhood aggregation / message passing  
- **GAT** — attention-weighted neighbors  
- **GraphSAGE** — scalable sampling for large graphs  

## Recommended learning sequence

1. Fix notation with one survey from the Awesome list.  
2. Complete core exercises in **GML2023**.  
3. Reproduce or study **C2G** on converter graphs.  
