# Graph_NN (Graph Neural Networks)

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

Graph neural networks (GNNs) for **relational data**: circuit topologies, module layouts, control graphs, and other PE structures where **nodes and edges** carry physical meaning. This folder currently provides **curated external resources** aligned with the tutorial’s graph-data discussion; local teaching notebooks may be added later.

## Contents

- `README.md` (this file) — external course, survey list, and PE-oriented GNN application  
- *No local `.ipynb` in this subfolder yet*

## Outcomes

- Relate **graph representations** (nodes, edges, features) to PE design objects (converter graphs, PCBs, power modules)  
- Understand **message passing** / convolution on graphs as an inductive bias for **locality and multi-hop coupling**  
- Navigate a full **GNN course** with runnable notebooks and multi-OS environments  
- Use a **paper / resource index** to go deeper (GCN, GAT, GraphSAGE, spatio-temporal GNNs, libraries)  
- Connect theory to **converter performance modeling** via graph-based surrogates (**Circuit-to-Graph**)

---

## External course & code — Graph Machine Learning (2023)

**Repository:** [xbresson/GML2023](https://github.com/xbresson/GML2023/tree/main) (Xavier Bresson)

**What it offers**

- **Graph Machine Learning** course materials: Jupyter-centric `codes/`, figures in `pic/`, and **MIT-licensed** distribution.  
- **Google Colab** path: installation notebook linked from the repo README for GPU-backed runs without a local GPU.  
- **Local installs:** Conda environment files for **Linux**, **macOS** (Apple Silicon and Intel), and **Windows** (`environment_*.yml`).  
- **Slides:** linked from the README (hosted separately) for theory alongside the notebooks.

**Why start here**

- Structured progression from graph learning basics to modern convolutional / attention-style models on graphs.  
- Practical coding patterns that transfer directly to **PyTorch Geometric**-style workflows used in research codebases.

---

## External reading list — Awesome Graph Neural Networks

**Repository:** [TrustAGI-Lab/Awesome-Graph-Neural-Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks)

**What it offers**

- **Survey papers** (e.g. comprehensive GNN reviews, geometric deep learning, graph attention).  
- Extensive **paper lists** by theme: recurrent GNNs, **spectral vs. spatial** graph convolutions, graph autoencoders, **spatio-temporal** GNNs, and **application** threads (CV, NLP, physics, chemistry, etc.).  
- **Library** pointers (e.g. PyTorch Geometric, DGL, graph-net style stacks) for implementation.

**How to use it**

- Read **1–2 surveys** first for vocabulary and taxonomy.  
- Drill into **spatial / message-passing** sections when preparing PE graph models.  
- Check **spatio-temporal** entries if your PE graph **evolves over time** (reconfiguration, switching states, or sequence-labeled graphs).

---

## Power electronics application — Circuit-to-Graph (C2G)

**Repository:** [Weihao-Lei/C2G](https://github.com/Weihao-Lei/C2G)

**Title (from repo):** *Circuit-to-Graph: Power Converters Modeling with Multi-Dimensional Generalization*

**Paper:** W. Lei, F. Lin, X. Zhang, X. Li and H. Ma, "Circuit-to-Graph: Power Converters Modeling With Multidimensional Generalization," *IEEE Journal of Emerging and Selected Topics in Power Electronics*, vol. 14, no. 1, pp. 918-932, Feb. 2026.  

**What it offers**

- A **PE-native** pipeline: map a **power converter topology to a graph**, assign **node features** (e.g. component type encodings and parameters), and train a **GCN + MLP** surrogate for **performance prediction**.  
- **Domain adaptation / fine-tuning** narrative for **out-of-domain** operating scenarios with limited extra data.  
- Materials include **`GCN Training and Fine-tuning.ipynb`** and a **`DATA/`** folder for reproducibility.
- Implements the tutorial’s idea that **graph structure** captures **connectivity and multi-hop effects** better than treating topology as a flat categorical label.  
- Bridges **GNN fundamentals** (GCN, pooling, MLP head) with **converter design and generalization**—a natural capstone after GML2023-style exercises.

---

## Fit with the PE AI tutorial

- **Data modality:** Graph inputs align with “graph data in PE” (topologies, layouts, signal-flow or control diagrams).  
- **Hybrid models:** Combine graph encoders with **tabular** or **sequence** branches (see `4_Neural_Network/` FNN and `Signal_Domain/` notebooks) when both relational and time-series information matter.  
- **Trust & data:** As with other deep models, pair graph surrogates with **validation**, **uncertainty**, and **physics checks** where safety-critical.

---

## Recommended order

1. Skim **Awesome-Graph-Neural-Networks** surveys to fix notation (GCN, GAT, GraphSAGE, pooling).  
2. Work through selected notebooks in **[GML2023](https://github.com/xbresson/GML2023/tree/main)** (`codes/`) with Colab or a local conda env.  
3. Study **[C2G](https://github.com/Weihao-Lei/C2G)** for graph construction from converters and GCN–MLP training / fine-tuning.  
4. Revisit **Awesome** lists for **libraries** and specialized topics (e.g. spatio-temporal GNNs) as your PE problem demands.

---

## Library pointers (implementation)

Commonly used with the above materials (also summarized in the Awesome list):

- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)  
- [Deep Graph Library (DGL)](https://www.dgl.ai/)  

Follow each library’s install guide; versions should match your PyTorch / CUDA stack.

---

## Algorithm summary (conceptual)

- **GCN** — graph convolution / message passing with neighborhood aggregation  
- **GAT** — attention-weighted neighbors  
- **GraphSAGE** — scalable sampling and aggregation for large graphs  
- **Spatio-temporal GNNs** — graphs with time-varying features or dynamics (when applicable)

---

## Local notebooks

*None yet in `Graph_NN/`.* When notebooks are added, list them under **Contents** and mirror the per-notebook sections used elsewhere in `4_Neural_Network/`.
