# Fundamentals of AI for PE — repository overview

## Companion tools

Use the interactive **Algorithm Selector** to narrow AI/ML approaches for your PE task, and the **ChatGPT** tutor for deeper Q&A and resource-rich reports aligned with this course.

<p align="center">
  <a href="https://xinzelee.github.io/AI_for_PE_Algorithm_Selector/">
    <img src="https://img.shields.io/badge/Open_algorithm_selector_(web_app)-2563eb?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open the Algorithm Selector web app" />
  </a>
  &nbsp;&nbsp;
  <a href="https://chatgpt.com/g/g-698618895c2481919e113c49bafe23ee-fundamentals-of-ai-for-pe">
    <img src="https://img.shields.io/badge/Open_ChatGPT_assistant-10a37f?style=for-the-badge&logo=openai&logoColor=white" alt="Open the Fundamentals of AI for PE ChatGPT assistant" />
  </a>
</p>

<p align="center">
  <sub>Source code for the selector: <a href="https://github.com/XinzeLee/AI_for_PE_Algorithm_Selector">XinzeLee/AI_for_PE_Algorithm_Selector</a></sub>
</p>

---

## Alignment with the tutorial article

This repository accompanies the invited tutorial *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). Section numbers below follow the **revised manuscript** structure:

| Article section | Topic (short) |
|-----------------|---------------|
| **I** | Introduction |
| **II** | Basics of PE data (tabular, signal, field, graph, unstructured) |
| **III** | Fundamentals of ML for PE (simulation automation, EDA, preprocessing, learning types, architectures, NNs, good practices) |
| **IV** | Fundamentals of PIML for PE |
| **V** | Fundamentals of MHAs for PE optimization |
| **VI** | Agentic AI (incl. PE-GPT2) |
| **VII** | One-stop AI applications throughout the PE lifecycle |
| **VIII** | Conclusion and outlook |

**Folder ↔ article mapping**

| Folder | Article sections |
|--------|------------------|
| [`0_To_Get_Started`](0_To_Get_Started/) | Prerequisite environment; supports hands-on material across the paper |
| [`1_MHA`](1_MHA/) | **V** — `Single_Objective_MHA/`: V-A, V-C; `Multi_Objective_MHA/`: V-B, V-C |
| [`2_Classic_ML`](2_Classic_ML/) | **III-B–III-E** (EDA, preprocessing, learning types, ML architectures); GP + BO notebook also illustrates hyperparameter search workflows related to **V-C** |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | **III-E** (tree / ensemble architectures) |
| [`4_Neural_Network`](4_Neural_Network/) | **II** (modalities) + **III-F–III-G** — see [4_Neural_Network/README.md](4_Neural_Network/README.md) |
| [`4_Neural_Network/Field_Data`](4_Neural_Network/Field_Data/) | **II-C**; **III-F–III-G** ([`field_temperature_residual_fnn.ipynb`](4_Neural_Network/Field_Data/field_temperature_residual_fnn.ipynb)) |
| [`4_Neural_Network/Graph_NN`](4_Neural_Network/Graph_NN/) | **II-D**; **III-E** |
| [`5_PIML`](5_PIML/) (`PINN/`) | **IV-A–IV-C** |
| [`5_PIML/PANN`](5_PIML/PANN/) | **IV-B**; **VII-E** |
| [`6_Agentic_AI`](6_Agentic_AI/) | **VI** (VI-A–VI-C) |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | **III-D** (reinforcement learning) |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | **III-A** (simulation automation for batch data acquisition) |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | **VII** — see [9_Case_Studies_PE/README.md](9_Case_Studies_PE/README.md) |

Per-folder detail appears in each module’s README under **Alignment with the tutorial article**.

---

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Navigate this README

| Section | Jump to |
|--------|---------|
| Companion tools | [Algorithm selector & ChatGPT](#companion-tools) |
| Article ↔ repo mapping | [Alignment with the tutorial article](#alignment-with-the-tutorial-article) |
| Google Colab | [Colab links for all notebooks](#google-colab) |
| Repository metrics | [Overview](#overview) |
| Module folders & learning path | [1. Contents and learning path](#1-contents-and-learning-path) |
| Algorithm & data inventory | [2. Algorithms and data](#2-algorithms-and-data) → [2.1 Algorithms](#21-algorithms) · [2.2 Data](#22-data) |
| Full per-notebook table | [3. Per-notebook reference](#3-per-notebook-reference) |
| Education article (PDF) | [Companion education article](#companion-education-article-pilot-course) |

Structured summary of topics, notebook code volume, data assets, and algorithm coverage across Jupyter notebooks (`.ipynb`). Documentation files are omitted from the metrics below.

## Google Colab

Each module README includes **Open in Colab** badges for its notebooks. On Colab, the usual first code cell clones this repository to `/content/Fundamentals_of_AI_for_PE`, runs `pip install -r requirements.txt`, and sets the working directory to the notebook’s folder so paths resolve. **Exception:** [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) relies on local simulators (LTspice, PLECS, etc.) and is not intended for Colab.

## Overview

| Metric | Value |
|---|---:|
| Code lines (notebook cells) | **11,950** |
| Jupyter notebooks | **31** |
| PE-oriented dataset families | **7** |
| Algorithm labels (see section 2) | **25** |

**Summary:** Teaching-oriented AI-for-power-electronics material, with the most notebook code in case studies, neural networks, and metaheuristic optimization.

## 1. Contents and algorithm learning path

| Folder | Notebooks | Code lines | Role |
|--------|---:|---:|------|
| [`0_To_Get_Started`](0_To_Get_Started/) | 1 | 306 | Environment setup and package checks |
| [`1_MHA`](1_MHA/) | 5 | 1,721 | Single- and multi-objective metaheuristic optimization (**Sec. V**) |
| [`2_Classic_ML`](2_Classic_ML/) | 3 | 559 | Polynomial Ridge (synthetic), classical classification, GP regression & Bayesian optimization (**Sec. III**) |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | 1 | 555 | Tree and ensemble methods (**Sec. III-E**) |
| [`4_Neural_Network`](4_Neural_Network/) | 5 | 2,283 | NN fundamentals, **3D thermal field** regression (`Field_Data/`), good practices, sequences, MDN / hysteresis; [`Graph_NN/`](4_Neural_Network/Graph_NN/) resources (**Sec. II–III**) |
| [`5_PIML`](5_PIML/) | 3 | 1,000 | Physics-informed modeling (`PINN/`); PANN summary in [`PANN/`](5_PIML/PANN/) (**Sec. IV; VII-E**) |
| [`6_Agentic_AI`](6_Agentic_AI/) | — | — | Agentic AI and PE-GPT (documentation; no local `.ipynb`) (**Sec. VI**) |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | 2 | 846 | Buck regulation tutorials — DQN and DDPG — plus curated RL reading (**Sec. III-D**) |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | 2 | 245 | LTspice, PLECS, Simulink automation (**Sec. III-A**) |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | 9 | 4,435 | Buck, DAB, IGBT, magnetic modeling case studies (**Sec. VII**) |

Case-study notebooks account for the largest share of code, followed by neural-network and MHA modules.

## 2. Algorithms and data

### 2.1 Algorithms

Labels used in the inventory fall into three groups:

- **Optimization:** Genetic Algorithm, PSO, NSGA-II  
- **Neural models:** FNN/MLP, CNN, RNN, GRU, LSTM, Transformer/Attention, MDN, PINN  
- **Classical / ensemble:** Decision Trees, Random Forests, Ridge, SVR, PCA, TSNE, Isolation Forest, One-Class SVM, XGBoost, Gaussian process regression (sklearn)  

**Full list (25 labels):**

- `CNN (PyTorch)`
- `FNN/MLP (PyTorch)`
- `GRU (PyTorch)`
- `Genetic Algorithm (GA)`
- `LSTM (PyTorch)`
- `Mixture Density Network (MDN)`
- `NSGA-II (multi-objective GA)`
- `PINN (Physics-Informed Neural Network)`
- `PSO (Particle Swarm Optimization)`
- `RNN (PyTorch)`
- `Transformer/Attention`
- `Transformer/Attention (PyTorch)`
- `XGBoost (classification)`
- `XGBoost (regression)`
- `sklearn:GaussianProcessRegressor`
- `sklearn:DecisionTreeClassifier`
- `sklearn:IsolationForest`
- `sklearn:LinearRegression`
- `sklearn:OneClassSVM`
- `sklearn:PCA`
- `sklearn:RandomForestClassifier`
- `sklearn:RandomForestRegressor`
- `sklearn:Ridge`
- `sklearn:SVR`
- `sklearn:TSNE`

### 2.2 Data

**Index of PE-oriented dataset families (D1–D7)** — bundled CSV/MAT in the repo or documented external sources used by case-study and field notebooks:

| ID | Family | Modality | Location / source | Primary notebooks |
|----|--------|----------|-------------------|-------------------|
| **D1** | Synchronous buck performance | Tabular | [`9_Case_Studies_PE/Buck_Design/sync_buck_performances_cleaned.csv`](9_Case_Studies_PE/Buck_Design/sync_buck_performances_cleaned.csv), [`total_100W_12V.csv`](9_Case_Studies_PE/Buck_Design/total_100W_12V.csv) | `buck_modeling_NN.ipynb`, `xgboost_buck_modeling.ipynb`, `buck_comprehensive_case_study.ipynb` |
| **D2** | DAB modulation / performance table | Tabular | [`9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/DAB_TPS.csv`](9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/DAB_TPS.csv) | `one_stop_AI_DAB_modulation.ipynb` |
| **D3** | DAB adaptive-modulation sweep | Tabular | [`9_Case_Studies_PE/DAB_Design/Adaptive_Modulation/optimization_results.csv`](9_Case_Studies_PE/DAB_Design/Adaptive_Modulation/optimization_results.csv) | `TinyML.ipynb` |
| **D4** | DAB time-domain waveforms | Signal (time series) | [`9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/Waveform/*.csv`](9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/Waveform/) (100 files) | `time_series_modeling.ipynb`, `rnn_basics.ipynb` |
| **D5** | IGBT accelerated aging (RUL) | Signal / tabular windows | [`9_Case_Studies_PE/IGBT_Maintenance/april22nd-23rdIgbtIRCG40BC30kd-A17.mat`](9_Case_Studies_PE/IGBT_Maintenance/april22nd-23rdIgbtIRCG40BC30kd-A17.mat) — derived from [NASA IGBT dataset](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging) | `rul_prediction.ipynb` |
| **D6** | Magnetic core-loss (MagNet-style) | Tabular + harmonic features | [`9_Case_Studies_PE/Magnetic_Modeling/*_downscaled.csv`](9_Case_Studies_PE/Magnetic_Modeling/) (4 files) — aligned with [Princeton MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html) | `magnet_fnn.ipynb`, `magnet_lstm.ipynb` |
| **D7** | 3-D thermal field samples | Field (spatial) | [`4_Neural_Network/Field_Data/cap_Tfield/Tfield_*_downsampled.csv`](4_Neural_Network/Field_Data/cap_Tfield/) (70 scenarios; `x,y,z,T`; loss & Tamb in filename) | `field_temperature_residual_fnn.ipynb` |

**Built-in / sklearn datasets (no repo file)**

| Dataset | Modality | Notebooks (examples) |
|---------|----------|----------------------|
| `sklearn.datasets.load_iris` | Tabular | `package_install.ipynb` |
| `sklearn.datasets.load_breast_cancer` | Tabular | `classic_ML.ipynb`, `NN_basics.ipynb` |
| `sklearn.datasets.fetch_california_housing` | Tabular | `NN_basics.ipynb`, `good_practice_NN.ipynb`, `gaussian_process_bayesian_optimization.ipynb` |
| `sklearn.datasets.make_regression`, `make_classification`, `make_moons`, etc. | Synthetic tabular | `package_install.ipynb`, `ensemle_learning.ipynb`, `mixture_density_net_ensemble_learning.ipynb`, … |

**Synthetic / generated in-notebook (no external file)**

| Use | Modality | Notebooks (examples) |
|-----|----------|----------------------|
| Optimization benchmarks (Sphere, Rastrigin, ZDT-1, …) | Scalar objectives | `1_MHA/**/*.ipynb` |
| Analytical buck / PE-style surfaces | Tabular design space | `buck_design_PSO.ipynb`, `buck_comprehensive_case_study.ipynb` |
| PINN teaching curves (ODE cooling, Burgers PDE) | Field / time | `5_PIML/PINN/*.ipynb` |
| Sequence / control rollouts | Signal / state trajectories | `rnn_basics.ipynb`, `7_Reinforcement_Learning/*.ipynb` |
| Hysteresis loops, MDN demos | Synthetic nonlinear | `mixture_density_net_ensemble_learning.ipynb` |

External dataset licensing and citations: [9_Case_Studies_PE — External datasets](9_Case_Studies_PE/#external-datasets).

## 3. Per-notebook reference

*Code line counts: non-empty lines in code cells, excluding lines that are only `#` comments.*

| Notebook | Code lines | Algorithms | Datasets |
|---|---:|---|---|
| `0_To_Get_Started/package_install.ipynb` | 306 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (classification)<br>sklearn:LinearRegression | sklearn.datasets.load_iris<br>sklearn.datasets.make_regression |
| `1_MHA/Multi_Objective_MHA/multi_obj_MHA_master.ipynb` | 665 | NSGA-II (multi-objective GA)<br>PSO (Particle Swarm Optimization) | synthetic / generated (random) |
| `1_MHA/Single_Objective_MHA/algorithm_stats_compare.ipynb` | 103 | Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization) | — |
| `1_MHA/Single_Objective_MHA/buck_design_PSO.ipynb` | 390 | PSO (Particle Swarm Optimization) | — |
| `1_MHA/Single_Objective_MHA/pso_hyp_tuning.ipynb` | 202 | PSO (Particle Swarm Optimization) | synthetic / generated (random) |
| `1_MHA/Single_Objective_MHA/sing_obj_MHA.ipynb` | 361 | PSO (Particle Swarm Optimization) | synthetic / generated (random) |
| `2_Classic_ML/ridge_polynomial_regression.ipynb` | 82 | sklearn:Ridge | synthetic / generated (random) |
| `2_Classic_ML/classic_ML.ipynb` | 164 | sklearn:DecisionTreeClassifier | sklearn.datasets.load_breast_cancer |
| `2_Classic_ML/gaussian_process_bayesian_optimization.ipynb` | 313 | sklearn:GaussianProcessRegressor (constant × RBF kernel; marginal-likelihood fit); Bayesian optimization (expected improvement over log-hyperparameters) | sklearn.datasets.fetch_california_housing |
| `3_Ensemble_Learning/ensemle_learning.ipynb` | 555 | XGBoost (classification)<br>XGBoost (regression)<br>sklearn:DecisionTreeClassifier<br>sklearn:PCA<br>sklearn:RandomForestClassifier<br>sklearn:Ridge | sklearn.datasets.make_classification |
| `4_Neural_Network/Fundamentals/NN_basics.ipynb` | 462 | FNN/MLP (PyTorch) | sklearn.datasets.fetch_california_housing<br>sklearn.datasets.load_breast_cancer |
| `4_Neural_Network/Good_Practices/good_practice_NN.ipynb` | 220 | FNN/MLP (PyTorch) | sklearn.datasets.fetch_california_housing |
| `4_Neural_Network/Field_Data/field_temperature_residual_fnn.ipynb` | 341 | FNN/MLP (PyTorch); residual (skip) blocks | **D7** — `Field_Data/cap_Tfield/*.csv` |
| `4_Neural_Network/Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb` | 441 | FNN/MLP (PyTorch)<br>Mixture Density Network (MDN)<br>sklearn:RandomForestRegressor<br>Prandtl–Ishlinskii–style hysteresis (play operators, PyTorch) | synthetic nonlinear regression; synthetic rate-independent hysteresis loop |
| `4_Neural_Network/Signal_Domain/rnn_basics.ipynb` | 819 | CNN (PyTorch)<br>FNN/MLP (PyTorch)<br>GRU (PyTorch)<br>LSTM (PyTorch)<br>RNN (PyTorch)<br>Transformer/Attention<br>Transformer/Attention (PyTorch) | synthetic / generated (random); **D4** waveforms when run with local CSVs |
| `5_PIML/PINN/pinn_ode.ipynb` | 341 | FNN/MLP (PyTorch)<br>PINN (ODE; fixed collocation, soft IC, composite loss, Adam + L-BFGS) | synthetic cooling curve + noisy samples |
| `5_PIML/PINN/pinn_pde.ipynb` | 259 | FNN/MLP (PyTorch)<br>PINN (PDE; fixed grids, soft IC/BC, composite loss, Adam + L-BFGS) | synthetic Burgers reference (MoL) |
| `5_PIML/PINN/prior_integration_example.ipynb` | 400 | FNN/MLP (PyTorch)<br>PINN (Physics-Informed Neural Network) | synthetic / generated (random) |
| `7_Reinforcement_Learning/RL_buck_control.ipynb` | 404 | DQN (PyTorch; toy averaged buck) | synthetic / generated (random) |
| `7_Reinforcement_Learning/DDPG_buck_control.ipynb` | 442 | DDPG (PyTorch; toy averaged buck) | synthetic / generated (random) |
| `8_PE_Simulation_Automation/LTspiceAutomation/LTspiceAtuomate.ipynb` | 140 | — | — |
| `8_PE_Simulation_Automation/PlecsAutomation/Data acquisition.ipynb` | 105 | — | — |
| `9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb` | 918 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (regression)<br>sklearn:RandomForestRegressor<br>sklearn:Ridge<br>sklearn:SVR | synthetic / generated (random); **D1** |
| `9_Case_Studies_PE/Buck_Design/buck_modeling_NN.ipynb` | 394 | FNN/MLP (PyTorch)<br>XGBoost (regression)<br>sklearn:RandomForestRegressor<br>sklearn:TSNE | **D1** |
| `9_Case_Studies_PE/Buck_Design/xgboost_buck_modeling.ipynb` | 285 | PSO (Particle Swarm Optimization)<br>XGBoost (regression) | **D1** |
| `9_Case_Studies_PE/DAB_Design/Adaptive_Modulation/TinyML.ipynb` | 546 | FNN/MLP (PyTorch) | **D3** |
| `9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb` | 1226 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (classification)<br>XGBoost (regression)<br>sklearn:IsolationForest<br>sklearn:OneClassSVM<br>sklearn:PCA<br>sklearn:SVR<br>sklearn:TSNE | synthetic / generated (random); **D2** |
| `9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb` | 179 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | **D4** |
| `9_Case_Studies_PE/IGBT_Maintenance/rul_prediction.ipynb` | 378 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | **D5** |
| `9_Case_Studies_PE/Magnetic_Modeling/magnet_fnn.ipynb` | 273 | FNN/MLP (PyTorch) | **D6** |
| `9_Case_Studies_PE/Magnetic_Modeling/magnet_lstm.ipynb` | 236 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | **D6** |

## Companion education article (pilot course)

**[Reforming Power Electronics Education in the Era of AI: A Pilot Course by the University of Arkansas Power Group](docs/Reforming%20Power%20Electronics%20Education%20in%20the%20Era%20of%20AI.pdf)** — Xinze Li and H. Alan Mantooth ([`docs/`](docs/)). Short education paper on a pilot *Fundamentals of AI for Power Electronics* course.

**Conclusion (in brief):** Effective AI-for-PE education should build **domain-grounded judgment** using open materials—not generic AI training alone. The authors call on **students, educators, industry, and public funders** to advance PE-relevant curricula, workforce training, responsibly shareable data, and supporting policy. The PDF frames this repository and the [companion tools](#companion-tools) at the top of this README as practical pieces of that wider effort; see the PDF for the full argument and references.

## License

This repository uses a dual-license structure:

- **Code**: Apache License 2.0  
- **Educational Content (text, figures, explanations)**: CC BY-NC 4.0  

- Code can be used freely.  
- Educational materials cannot be used commercially without permission.  

See the `LICENSE` and `NOTICE` files for details.
