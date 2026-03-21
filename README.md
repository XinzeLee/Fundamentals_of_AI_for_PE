# Fundamentals of AI for PE — repository overview

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Navigate this README

| Section | Jump to |
|--------|---------|
| Repository metrics | [Overview](#overview) |
| Module folders & roles | [1. Contents and learning path](#1-contents-and-learning-path) |
| Notebook counts by folder | [2. Notebooks by module](#2-notebooks-by-module) |
| Algorithm & data inventory | [3. Algorithms and data](#3-algorithms-and-data) → [3.1 Algorithms](#31-algorithms) · [3.2 Data](#32-data) |
| File tree & highlighted notebooks | [4. Tree and representative notebooks](#4-tree-and-representative-notebooks) → [4.1 Layout](#41-layout) · [4.2 Representative notebooks](#42-representative-notebooks) |
| Full per-notebook table | [5. Per-notebook reference](#5-per-notebook-reference) |

Structured summary of topics, notebook code volume, data assets, and algorithm coverage across Jupyter notebooks (`.ipynb`). Documentation files are omitted from the metrics below.

## Overview

| Metric | Value |
|---|---:|
| Code lines (notebook cells) | **10,111** |
| Jupyter notebooks | **26** |
| PE-oriented datasets | **6** |
| Algorithm labels (see §3) | **24** |

**Summary:** Teaching-oriented AI-for-power-electronics material, with the most notebook code in case studies, neural networks, and metaheuristic optimization.

## 1. Contents and learning path

| Folder | Role |
|--------|------|
| [`0_To_Get_Started`](0_To_Get_Started/) | Environment setup and package checks |
| [`1_MHA`](1_MHA/) | Single- and multi-objective metaheuristic optimization |
| [`2_Classic_ML`](2_Classic_ML/) | Classical machine learning baselines |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | Tree and ensemble methods |
| [`4_Neural_Network`](4_Neural_Network/) | NN fundamentals, sequences, multimodal / MDN |
| [`5_PIML`](5_PIML/) | Physics-informed modeling (`PINN`); PANN summary in [`PANN/`](5_PIML/PANN/) |
| [`6_Agentic_AI`](6_Agentic_AI/) | Agentic AI and PE-GPT (documentation and external links; no local `.ipynb` here) |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | Curated RL reading and links (no local notebooks in-repo) |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | LTspice, PLECS, Simulink automation |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | Buck, DAB, IGBT, magnetic modeling case studies |

## 2. Notebooks by module

| Module | Notebooks | Code lines | Role |
|---|---:|---:|---|
| [`0_To_Get_Started`](0_To_Get_Started/) | 1 | 293 | Setup |
| [`1_MHA`](1_MHA/) | 5 | 1,656 | Optimization core |
| [`2_Classic_ML`](2_Classic_ML/) | 1 | 151 | Classical baseline |
| [`3_Ensemble_Learning`](3_Ensemble_Learning/) | 1 | 542 | Ensembles |
| [`4_Neural_Network`](4_Neural_Network/) | 4 | 1,775 | Deep learning |
| [`5_PIML`](5_PIML/) | 3 | 1,131 | Physics-informed examples |
| [`7_Reinforcement_Learning`](7_Reinforcement_Learning/) | 0 | 0 | Curated RL reading (no local notebooks) |
| [`8_PE_Simulation_Automation`](8_PE_Simulation_Automation/) | 2 | 245 | Tool automation |
| [`9_Case_Studies_PE`](9_Case_Studies_PE/) | 9 | 4,318 | Applied studies |

Case-study notebooks account for the largest share of code, followed by neural-network and MHA modules.

## 3. Algorithms and data

### 3.1 Algorithms

Labels used in the inventory fall into three groups:

- **Optimization:** Genetic Algorithm, PSO, NSGA-II  
- **Neural models:** FNN/MLP, CNN, RNN, GRU, LSTM, Transformer/Attention, MDN, PINN  
- **Classical / ensemble:** Decision Trees, Random Forests, Ridge, SVR, PCA, TSNE, Isolation Forest, One-Class SVM, XGBoost  

**Full list (24 labels):**

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
| Repository files | CSV/MAT in Buck, DAB, IGBT, magnetic studies; DAB waveform CSVs — external sources for IGBT RUL & MagNet-style magnetic data: [9_Case_Studies_PE — External datasets](9_Case_Studies_PE/#external-datasets) |

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
3_Ensemble_Learning/
  ensemle_learning.ipynb
4_Neural_Network/
  Fundamentals/
    NN_basics.ipynb
  Good_Practices/
    good_practice_NN.ipynb
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
    prior_integration_example.ipynb
    prior_integration_example2.ipynb
6_Agentic_AI/
  README.md
7_Reinforcement_Learning/
  README.md
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
```

### 4.2 Representative notebooks

| Notebook | Code lines | Note |
|---|---:|---|
| `9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb` | 1,213 | Broad applied workflow (optimization, classical ML, NN, anomaly models) |
| `9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb` | 905 | End-to-end buck study |
| `4_Neural_Network/Signal_Domain/rnn_basics.ipynb` | 806 | RNN / LSTM / GRU / CNN / Transformer |
| `1_MHA/Multi_Objective_MHA/multi_obj_MHA_master.ipynb` | 652 | NSGA-II and Pareto analysis |
| `3_Ensemble_Learning/ensemle_learning.ipynb` | 542 | Ensemble benchmarks |
| `5_PIML/PINN/prior_integration_example2.ipynb` | 511 | PINN depth |

## 5. Per-notebook reference

*Code line counts: non-empty lines in code cells, excluding lines that are only `#` comments.*

| Notebook | Code lines | Algorithms | Datasets |
|---|---:|---|---|
| `0_To_Get_Started/package_install.ipynb` | 293 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (classification)<br>sklearn:LinearRegression | sklearn.datasets.load_iris<br>sklearn.datasets.make_regression |
| `1_MHA/Multi_Objective_MHA/multi_obj_MHA_master.ipynb` | 652 | NSGA-II (multi-objective GA)<br>PSO (Particle Swarm Optimization) | synthetic / generated (random) |
| `1_MHA/Single_Objective_MHA/algorithm_stats_compare.ipynb` | 90 | Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization) | — |
| `1_MHA/Single_Objective_MHA/buck_design_PSO.ipynb` | 377 | PSO (Particle Swarm Optimization) | — |
| `1_MHA/Single_Objective_MHA/pso_hyp_tuning.ipynb` | 189 | PSO (Particle Swarm Optimization) | synthetic / generated (random) |
| `1_MHA/Single_Objective_MHA/sing_obj_MHA.ipynb` | 348 | PSO (Particle Swarm Optimization) | synthetic / generated (random) |
| `2_Classic_ML/classic_ML.ipynb` | 151 | sklearn:DecisionTreeClassifier | sklearn.datasets.load_breast_cancer |
| `3_Ensemble_Learning/ensemle_learning.ipynb` | 542 | XGBoost (classification)<br>XGBoost (regression)<br>sklearn:DecisionTreeClassifier<br>sklearn:PCA<br>sklearn:RandomForestClassifier<br>sklearn:Ridge | sklearn.datasets.make_classification |
| `4_Neural_Network/Fundamentals/NN_basics.ipynb` | 449 | FNN/MLP (PyTorch) | sklearn.datasets.fetch_california_housing<br>sklearn.datasets.load_breast_cancer |
| `4_Neural_Network/Good_Practices/good_practice_NN.ipynb` | 207 | FNN/MLP (PyTorch) | sklearn.datasets.fetch_california_housing |
| `4_Neural_Network/Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb` | 313 | FNN/MLP (PyTorch)<br>Mixture Density Network (MDN)<br>sklearn:RandomForestRegressor | — |
| `4_Neural_Network/Signal_Domain/rnn_basics.ipynb` | 806 | CNN (PyTorch)<br>FNN/MLP (PyTorch)<br>GRU (PyTorch)<br>LSTM (PyTorch)<br>RNN (PyTorch)<br>Transformer/Attention<br>Transformer/Attention (PyTorch) | synthetic / generated (random) |
| `5_PIML/PINN/pinn_ode.ipynb` | 233 | FNN/MLP (PyTorch)<br>PINN (Physics-Informed Neural Network) | synthetic / generated (random) |
| `5_PIML/PINN/prior_integration_example.ipynb` | 387 | FNN/MLP (PyTorch)<br>PINN (Physics-Informed Neural Network) | synthetic / generated (random) |
| `5_PIML/PINN/prior_integration_example2.ipynb` | 511 | FNN/MLP (PyTorch)<br>PINN (Physics-Informed Neural Network) | synthetic / generated (random) |
| `8_PE_Simulation_Automation/LTspiceAutomation/LTspiceAtuomate.ipynb` | 140 | — | — |
| `8_PE_Simulation_Automation/PlecsAutomation/Data acquisition.ipynb` | 105 | — | — |
| `9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb` | 905 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (regression)<br>sklearn:RandomForestRegressor<br>sklearn:Ridge<br>sklearn:SVR | synthetic / generated (random) |
| `9_Case_Studies_PE/Buck_Design/buck_modeling_NN.ipynb` | 381 | FNN/MLP (PyTorch)<br>XGBoost (regression)<br>sklearn:RandomForestRegressor<br>sklearn:TSNE | — |
| `9_Case_Studies_PE/Buck_Design/xgboost_buck_modeling.ipynb` | 272 | PSO (Particle Swarm Optimization)<br>XGBoost (regression) | — |
| `9_Case_Studies_PE/DAB_Design/Adaptive_Modulation/TinyML.ipynb` | 533 | FNN/MLP (PyTorch) | — |
| `9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb` | 1213 | FNN/MLP (PyTorch)<br>Genetic Algorithm (GA)<br>PSO (Particle Swarm Optimization)<br>XGBoost (classification)<br>XGBoost (regression)<br>sklearn:IsolationForest<br>sklearn:OneClassSVM<br>sklearn:PCA<br>sklearn:SVR<br>sklearn:TSNE | synthetic / generated (random) |
| `9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb` | 166 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | synthetic / generated (random) |
| `9_Case_Studies_PE/IGBT_Maintenance/rul_prediction.ipynb` | 365 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | synthetic / generated (random) |
| `9_Case_Studies_PE/Magnetic_Modeling/magnet_fnn.ipynb` | 260 | FNN/MLP (PyTorch) | — |
| `9_Case_Studies_PE/Magnetic_Modeling/magnet_lstm.ipynb` | 223 | FNN/MLP (PyTorch)<br>LSTM (PyTorch) | — |
