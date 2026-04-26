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

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Navigate this README

| Section | Jump to |
|--------|---------|
| Companion tools | [Algorithm selector & ChatGPT](#companion-tools) |
| Google Colab | [Colab links for all notebooks](#google-colab) |
| Repository metrics | [Overview](#overview) |
| Module folders & roles | [1. Contents and learning path](#1-contents-and-learning-path) |
| Notebook counts by folder | [2. Notebooks by module](#2-notebooks-by-module) |
| Algorithm & data inventory | [3. Algorithms and data](#3-algorithms-and-data) → [3.1 Algorithms](#31-algorithms) · [3.2 Data](#32-data) |
| File tree & highlighted notebooks | [4. Tree and representative notebooks](#4-tree-and-representative-notebooks) → [4.1 Layout](#41-layout) · [4.2 Representative notebooks](#42-representative-notebooks) |
| Full per-notebook table | [5. Per-notebook reference](#5-per-notebook-reference) |
| Article ↔ repo mapping | [Alignment with the tutorial article](#alignment-with-the-tutorial-article) |
| Education article (PDF) | [Companion education article](#companion-education-article-pilot-course) |

Structured summary of topics, notebook code volume, data assets, and algorithm coverage across Jupyter notebooks (`.ipynb`). Documentation files are omitted from the metrics below.

## Google Colab

Each module README includes **Open in Colab** badges for its notebooks. On Colab, the usual first code cell clones this repository to `/content/Fundamentals_of_AI_for_PE`, runs `pip install -r requirements.txt`, and sets the working directory so paths resolve. **Exception:** [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) relies on local simulators (LTspice, PLECS, etc.) and is not intended for Colab.

## Overview

| Metric | Value |
|---|---:|
| Code lines (notebook cells) | **11,950** |
| Jupyter notebooks | **31** |
| PE-oriented datasets | **7** |
| Algorithm labels (see section 3) | **25** |

**Summary:** Teaching-oriented AI-for-power-electronics material, with the most notebook code in case studies, neural networks, and metaheuristic optimization.

## 1. Contents and learning path

| Folder | Role |
|--------|------|
| [`0_To_Get_Started`](0_To_Get_Started/) | Environment setup and package checks |
| [`1_MHA`](1_MHA/) | Single- and multi-objective metaheuristic optimization |
| [`2_Classic_ML`](2_Classic_ML/) | Classical machine learning baselines |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | Tree and ensemble methods |
| [`4_Neural_Network`](4_Neural_Network/) | NN fundamentals, **3D thermal field** regression (`Field_Data/`), good practices, sequences, multimodal / MDN (incl. synthetic hysteresis: Prandtl–Ishlinskii-style play-operator NN vs MDN, B–H–style motivation); [`Graph_NN/`](4_Neural_Network/Graph_NN/) (GNN resources) |
| [`5_PIML`](5_PIML/) | Physics-informed modeling (`PINN`); PANN summary in [`PANN/`](5_PIML/PANN/) |
| [`6_Agentic_AI`](6_Agentic_AI/) | Agentic AI and PE-GPT (documentation and external links; no local `.ipynb` here) |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | Buck regulation tutorials — DQN (`RL_buck_control.ipynb`) and DDPG (`DDPG_buck_control.ipynb`) — plus curated RL reading |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | LTspice, PLECS, Simulink automation |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | Buck, DAB, IGBT, magnetic modeling case studies |

## 2. Notebooks by module

| Module | Notebooks | Code lines | Role |
|---|---:|---:|---|
| [`0_To_Get_Started`](0_To_Get_Started/) | 1 | 306 | Setup |
| [`1_MHA`](1_MHA/) | 5 | 1,721 | Optimization core |
| [`2_Classic_ML`](2_Classic_ML/) | 3 | 559 | Polynomial Ridge (synthetic) + classical classification + GP regression & Bayesian optimization (California housing) |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | 1 | 555 | Ensembles |
| [`4_Neural_Network`](4_Neural_Network/) | 5 | 2,283 | Deep learning |
| [`5_PIML`](5_PIML/) | 3 | 1,000 | Physics-informed examples (`PINN/`) |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | 2 | 846 | RL tutorials (DQN + DDPG buck) + curated reading |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | 2 | 245 | Tool automation |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | 9 | 4,435 | Applied studies |

Case-study notebooks account for the largest share of code, followed by neural-network and MHA modules.

## 3. Algorithms and data

### 3.1 Algorithms

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

### 3.2 Data

| Kind | Examples |
|------|----------|
| Built-in / sklearn | `Iris`, `Breast Cancer`, `California Housing`, `make_*` generators |
| Synthetic | Optimization, PINN, sequence models |
| Repository files | CSV/MAT in Buck, DAB, IGBT, magnetic studies; **3D thermal field** downsampled CSVs in [`4_Neural_Network/Field_Data`](4_Neural_Network/Field_Data/) (loss/Tamb in filename, `x,y,z,T` in file); DAB waveform CSVs — external sources for IGBT RUL & MagNet-style magnetic data: [9_Case_Studies_PE — External datasets](9_Case_Studies_PE/#external-datasets) |

## 4. Tree and representative notebooks

### 4.1 Layout

```text
0_To_Get_Started/
  package_install.ipynb
1_MHA/
  Multi_Objective_MHA/
    multi_obj_MHA_master.ipynb
  Single_Objective_MHA/
    algorithm_stats_compare.ipynb
    buck_design_PSO.ipynb
    pso_hyp_tuning.ipynb
    sing_obj_MHA.ipynb
2_Classic_ML/
  classic_ML.ipynb
  gaussian_process_bayesian_optimization.ipynb
  ridge_polynomial_regression.ipynb
3_Ensemble_Learning/
  ensemle_learning.ipynb
4_Neural_Network/
  Field_Data/
    field_temperature_residual_fnn.ipynb
    Tfield_*_downsampled.csv
    cap_Tfield/
      (additional T-field CSV scenarios)
  Fundamentals/
    NN_basics.ipynb
  Good_Practices/
    good_practice_NN.ipynb
  Graph_NN/
    README.md
  Multi_Modal_Distribution/
    mixture_density_net_ensemble_learning.ipynb
  Signal_Domain/
    rnn_basics.ipynb
5_PIML/
  README.md
  PANN/
    README.md
  PINN/
    pinn_ode.ipynb
    pinn_pde.ipynb
    prior_integration_example.ipynb
6_Agentic_AI/
  README.md
7_Reinforcement_Learning/
  README.md
  DDPG_buck_control.ipynb
  RL_buck_control.ipynb
8_PE_Simulation_Automation/
  LTspiceAutomation/
    CAB425M12XM3_LTspice.asy
    DPT_Test_Stand_HB_automate.asc
    LTspiceAtuomate.ipynb
  PlecsAutomation/
    C2M0080120D.xml
    C2M0080120D_bodydiode.xml
    DAB_sample1.plecs
    Data acquisition.ipynb
  SimulinkAutomation/
    BuckConverter.slx
    BuckConverter_Automation.m
9_Case_Studies_PE/
  Buck_Design/
    buck_comprehensive_case_study.ipynb
    buck_modeling_NN.ipynb
    sync_buck_performances_cleaned.csv
    total_100W_12V.csv
    xgboost_buck_modeling.ipynb
  DAB_Design/
    Adaptive_Modulation/
      optimization_results.csv
      TinyML.ipynb
    Performance_Modeling_and_Design/
      DAB_TPS.csv
      one_stop_AI_DAB_modulation.ipynb
      utils.py
    Time_Domain_Modeling/
      time_series_modeling.ipynb
      Waveform/
        *.csv
  IGBT_Maintenance/
    april22nd-23rdIgbtIRCG40BC30kd-A17.mat
    rul_prediction.ipynb
  Magnetic_Modeling/
    B_waveform[T]_downscaled.csv
    Frequency[Hz]_downscaled.csv
    magnet_fnn.ipynb
    magnet_lstm.ipynb
    Temperature[C]_downscaled.csv
    Volumetric_losses[Wm-3]_downscaled.csv
docs/
  Reforming Power Electronics Education in the Era of AI.pdf
```

### 4.2 Representative notebooks

| Notebook | Code lines | Note |
|---|---:|---|
| `9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb` | 1,226 | Broad applied workflow (optimization, classical ML, NN, anomaly models) |
| `9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb` | 918 | End-to-end buck study |
| `4_Neural_Network/Signal_Domain/rnn_basics.ipynb` | 819 | RNN / LSTM / GRU / CNN / Transformer |
| `1_MHA/Multi_Objective_MHA/multi_obj_MHA_master.ipynb` | 665 | NSGA-II and Pareto analysis |
| `3_Ensemble_Learning/ensemle_learning.ipynb` | 555 | Ensemble benchmarks |
| `7_Reinforcement_Learning/RL_buck_control.ipynb` | 404 | DQN-style voltage control on an averaged buck (toy) |
| `7_Reinforcement_Learning/DDPG_buck_control.ipynb` | 442 | DDPG continuous-action voltage control on the same averaged buck (toy) |

## 5. Per-notebook reference

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
| `4_Neural_Network/Field_Data/field_temperature_residual_fnn.ipynb` | 341 | FNN/MLP (PyTorch); residual (skip) blocks | `4_Neural_Network/Field_Data/*.csv` (3D samples: `x,y,z`, `T`; loss & Tamb from filename) |
| `4_Neural_Network/Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb` | 441 | FNN/MLP (PyTorch)<br>Mixture Density Network (MDN)<br>sklearn:RandomForestRegressor<br>Prandtl–Ishlinskii–style hysteresis (play operators, PyTorch) | synthetic nonlinear regression; synthetic rate-independent hysteresis loop |
| `4_Neural_Network/Signal_Domain/rnn_basics.ipynb` | 819 | CNN (PyTorch)<br>FNN/MLP (PyTorch)<br>GRU (PyTorch)<br>LSTM (PyTorch)<br>RNN (PyTorch)<br>Transformer/Attention<br>Transformer/Attention (PyTorch) | synthetic / generated (random) |
| `5_PIML/PINN/pinn_ode.ipynb` | 341 | FNN/MLP (PyTorch)<br>PINN (ODE; fixed collocation, soft IC, composite loss, Adam + L-BFGS) | synthetic cooling curve + noisy samples |
| `5_PIML/PINN/pinn_pde.ipynb` | 259 | FNN/MLP (PyTorch)<br>PINN (PDE; fixed grids, soft IC/BC, composite loss, Adam + L-BFGS) | synthetic Burgers reference (MoL) |
| `5_PIML/PINN/prior_integration_example.ipynb` | 400 | FNN/MLP (PyTorch)<br>PINN (Physics-Informed Neural Network) | synthetic / generated (random) |
| `7_Reinforcement_Learning/RL_buck_control.ipynb` | 404 | DQN (PyTorch; toy averaged buck) | synthetic / generated (random) |
| `7_Reinforcement_Learning/DDPG_buck_control.ipynb` | 442 | DDPG (PyTorch; toy averaged buck) | synthetic / generated (random) |
| `8_PE_Simulation_Automation/LTspiceAutomation/LTspiceAtuomate.ipynb` | 140 | — | — |
| `8_PE_Simulation_Automation/PlecsAutomation/Data acquisition.ipynb` | 105 | — | — |
| `9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb` | 918 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (regression)<br>sklearn:RandomForestRegressor<br>sklearn:Ridge<br>sklearn:SVR | synthetic / generated (random) |
| `9_Case_Studies_PE/Buck_Design/buck_modeling_NN.ipynb` | 394 | FNN/MLP (PyTorch)<br>XGBoost (regression)<br>sklearn:RandomForestRegressor<br>sklearn:TSNE | — |
| `9_Case_Studies_PE/Buck_Design/xgboost_buck_modeling.ipynb` | 285 | PSO (Particle Swarm Optimization)<br>XGBoost (regression) | — |
| `9_Case_Studies_PE/DAB_Design/Adaptive_Modulation/TinyML.ipynb` | 546 | FNN/MLP (PyTorch) | — |
| `9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb` | 1226 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (classification)<br>XGBoost (regression)<br>sklearn:IsolationForest<br>sklearn:OneClassSVM<br>sklearn:PCA<br>sklearn:SVR<br>sklearn:TSNE | synthetic / generated (random) |
| `9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb` | 179 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | synthetic / generated (random) |
| `9_Case_Studies_PE/IGBT_Maintenance/rul_prediction.ipynb` | 378 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | synthetic / generated (random) |
| `9_Case_Studies_PE/Magnetic_Modeling/magnet_fnn.ipynb` | 273 | FNN/MLP (PyTorch) | — |
| `9_Case_Studies_PE/Magnetic_Modeling/magnet_lstm.ipynb` | 236 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | — |

## Alignment with the tutorial article

This repository accompanies the invited tutorial *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). The mapping below links **top-level folders** (and selected subfolders) to **article sections** as numbered in the paper.

| Folder | Article sections |
|--------|------------------|
| [`0_To_Get_Started`](0_To_Get_Started/) | Prerequisite environment; supports hands-on material across the paper |
| [`1_MHA`](1_MHA/) | II-A–II-D (`Single_Objective_MHA`: II-A, II-C, II-D; `Multi_Objective_MHA`: II-B, II-C) |
| [`2_Classic_ML`](2_Classic_ML/) | III-A; IV-D; IV-E |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | III-A; IV-D; IV-E |
| [`4_Neural_Network`](4_Neural_Network/) | See subfolders in [4_Neural_Network/README.md](4_Neural_Network/README.md) |
| [`4_Neural_Network/Field_Data`](4_Neural_Network/Field_Data/) | III-C; IV-F; IV-G (3-D thermal samples → **T**; [`field_temperature_residual_fnn.ipynb`](4_Neural_Network/Field_Data/field_temperature_residual_fnn.ipynb)) |
| [`4_Neural_Network/Graph_NN`](4_Neural_Network/Graph_NN/) | III-E; IV-F |
| [`5_PIML`](5_PIML/) (`PINN/`) | V |
| [`5_PIML/PANN`](5_PIML/PANN/) | V-C; VII-E |
| [`6_Agentic_AI`](6_Agentic_AI/) | VI |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | IV-D; IV-F |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | IV-A |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | See [9_Case_Studies_PE/README.md](9_Case_Studies_PE/README.md) (Buck, DAB threads, IGBT, magnetics) |

Per-folder detail appears in each module’s README under **Alignment with the tutorial article**.

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
