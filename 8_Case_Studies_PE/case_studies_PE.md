# 8_Case_Studies_PE

This module contains end-to-end AI case studies for power electronics, covering data preparation, surrogate modeling, optimization, uncertainty-aware prediction, and deployment-oriented acceleration.

## Folder coverage (all subfolders)

- `Buck_Design`
- `DAB_Design/Adaptive_Modulation`
- `DAB_Design/Performance_Modeling_and_Design`
- `DAB_Design/Time_Domain_Modeling`
- `IGBT_Maintenance`
- `Magnetic_Modeling`

## Notebooks covered in this module

1. `Buck_Design/buck_comprehensive_case_study.ipynb`
2. `Buck_Design/buck_modeling_NN.ipynb`
3. `Buck_Design/xgboost_buck_modeling.ipynb`
4. `DAB_Design/Adaptive_Modulation/TinyML.ipynb`
5. `DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`
6. `DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb`
7. `IGBT_Maintenance/rul_prediction.ipynb`
8. `Magnetic_Modeling/magnet_fnn.ipynb`
9. `Magnetic_Modeling/magnet_lstm.ipynb`

---

## Learning objectives (overall module)

After completing this module, learners should be able to:

- build practical PE modeling pipelines from raw/simulation data to deployable AI models;
- compare classical ML, ensemble methods, neural networks, and sequence models under realistic constraints;
- perform objective-driven optimization using surrogate models + metaheuristics;
- apply data cleaning/outlier handling and evaluate robustness statistically;
- model uncertainty for reliability-related tasks (e.g., probabilistic RUL prediction);
- apply TinyML-oriented compression/acceleration methods (pruning, ONNX export, quantization).

---

## What each case study contains

### A) Buck design

#### 1) `buck_comprehensive_case_study.ipynb`
**What this notebook contains**
- End-to-end buck workflow:
  - exploratory analysis and objective construction,
  - lookup-table/feasible-component screening,
  - surrogate model training for multiple objectives,
  - optimization loop using metaheuristics.
- Compares PSO and GA for design search over surrogate objectives.

**Algorithm and data coverage**
- Algorithms: FNN surrogates, PSO, GA, plus classical baselines used during analysis.
- Data: `total_100W_12V.csv` and processed performance targets (loss/ripple-style objectives).

**Additional code-level notes**
- Multi-objective framing is implemented via weighted/scenario-specific optimization steps.
- Includes outlier handling and distribution/correlation diagnostics before optimization.

#### 2) `buck_modeling_NN.ipynb`
**What this notebook contains**
- Efficiency-modeling pipeline with:
  - EDA,
  - baseline models (Random Forest / XGBoost),
  - deeper NN surrogate (residual-style MLP + regularization/scheduler),
  - prediction-surface visualization.

**Algorithm and data coverage**
- Algorithms: RandomForestRegressor, XGBoost regressor, feedforward NN surrogate, t-SNE for visualization.
- Data: `sync_buck_performances_cleaned.csv`.

**Additional code-level notes**
- Uses standardized inputs and tracked train/val/test split.
- Reports R2/RMSE/MAE-style metrics and loss trajectories.

#### 3) `xgboost_buck_modeling.ipynb`
**What this notebook contains**
- Data-driven modeling of buck efficiency and ripple ratio.
- XGBoost-centric training/evaluation with tracked landscapes during boosting rounds.
- MHA stage that evaluates optimization objective through trained surrogates.

**Algorithm and data coverage**
- Algorithms: XGBRegressor (primary), Random Forest baseline, MHA-based optimization stage.
- Data: `sync_buck_performances_cleaned.csv` with engineered ripple target.

**Additional code-level notes**
- Includes outlier filtering and detailed training diagnostics.
- Uses prediction-vs-actual and training-curve visual checks.

---

### B) DAB design

#### 4) `Adaptive_Modulation/TinyML.ipynb`
**What this notebook contains**
- AI control-oriented modulation modeling workflow for DAB.
- Capacity sweep and Pareto-style size-vs-loss analysis.
- L1 regularization, post-pruning, ONNX export, runtime benchmarking, and quantization.

**Algorithm and data coverage**
- Algorithms: feedforward NN for modulation mapping, Pareto selection, pruning, ONNX Runtime acceleration, dynamic quantization.
- Data: `optimization_results.csv` (phase-shift optimization outcomes).

**Additional code-level notes**
- Includes deployment-minded speed/accuracy tradeoff benchmarking.
- Demonstrates practical model compression path to TinyML-compatible inference.

#### 5) `Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`
**What this notebook contains**
- Comprehensive one-stop DAB workflow:
  - EDA and cleaning,
  - t-SNE/PCA analysis,
  - outlier detection (One-Class SVM, IsolationForest),
  - surrogate training and model comparisons,
  - optimization via PSO/GA,
  - adaptive-modulation/TinyML stage.

**Algorithm and data coverage**
- Algorithms: XGBoost, Random Forest, SVR, PCA, t-SNE, One-Class SVM, Isolation Forest, FNN-type models, PSO, GA.
- Data: `DAB_TPS.csv`.

**Additional code-level notes**
- Strongly emphasizes quality control before optimization (validity/ZVS filtering + outlier screening).
- Uses utility functions for reproducible visualization and analysis.

#### 6) `Time_Domain_Modeling/time_series_modeling.ipynb`
**What this notebook contains**
- Time-domain waveform modeling for DAB with recurrent architectures.
- Loads waveform CSV set, aligns/segments signals, and trains sequence models.
- Compares recurrent variants and evaluates prediction accuracy/MAE.

**Algorithm and data coverage**
- Algorithms: RNN/LSTM/BiLSTM-style sequence modeling with PyTorch.
- Data: `Waveform/*.csv` (time-series data for converter behavior).

**Additional code-level notes**
- Uses train/val/test split and best-model checkpoint tracking.
- Includes detailed waveform visualization against predictions.

---

### C) IGBT maintenance

#### 7) `IGBT_Maintenance/rul_prediction.ipynb`
**What this notebook contains**
- Remaining Useful Life (RUL) workflow for IGBT:
  - `.mat` ingestion,
  - cycle/minima extraction and windowing,
  - probabilistic sequence regression,
  - uncertainty quantification with confidence intervals.

**Algorithm and data coverage**
- Algorithms: probabilistic BiLSTM regressor with Gaussian NLL loss.
- Data: `april22nd-23rdIgbtIRCG40BC30kd-A17.mat`.

**Additional code-level notes**
- Uses train/val/test split with scaler fit-on-train policy.
- Reports both predictive error and calibration-like interval coverage (e.g., 90% CI containment).

---

### D) Magnetic modeling

#### 8) `Magnetic_Modeling/magnet_fnn.ipynb`
**What this notebook contains**
- Core-loss modeling pipeline using waveform-derived harmonic features + operating conditions.
- FFT-based feature extraction from B-waveforms.
- Feedforward NN training/evaluation with preprocessing and model-size tracking.

**Algorithm and data coverage**
- Algorithms: FNN regression surrogate for volumetric core loss.
- Data:
  - `B_waveform[T]_downscaled.csv`
  - `Frequency[Hz]_downscaled.csv`
  - `Temperature[C]_downscaled.csv`
  - `Volumetric_losses[Wm-3]_downscaled.csv`

**Additional code-level notes**
- Uses log-transform on targets + scaling strategy.
- Evaluates MAE/RMSE/MAPE and model parameter size.

#### 9) `Magnetic_Modeling/magnet_lstm.ipynb`
**What this notebook contains**
- Sequence-aware magnetic-loss modeling:
  - BiLSTM extracts waveform-temporal features,
  - concatenates numerical operating features (frequency/temperature),
  - FC head regresses volumetric loss.

**Algorithm and data coverage**
- Algorithms: BiLSTM + numeric-feature fusion regression network.
- Data: same four magnetic-modeling CSV datasets as above.

**Additional code-level notes**
- Maintains consistent split indices across sequence and numeric branches.
- Demonstrates multi-input PyTorch dataset/dataloader pattern.

---

## Consolidated algorithm coverage in `8_Case_Studies_PE`

- **Classical/ensemble ML**: Random Forest, XGBoost, SVR
- **Neural models**: FNN/MLP, recurrent models (RNN/LSTM/BiLSTM), probabilistic BiLSTM
- **Representation/analysis**: PCA, t-SNE
- **Data quality/anomaly filtering**: One-Class SVM, Isolation Forest, z-score filtering
- **Optimization**: PSO, GA, surrogate-assisted search
- **Deployment acceleration**: pruning, ONNX export, ONNX Runtime inference, quantization

---

## Consolidated data coverage in `8_Case_Studies_PE`

- Buck datasets:
  - `total_100W_12V.csv`
  - `sync_buck_performances_cleaned.csv`
- DAB datasets:
  - `DAB_TPS.csv`
  - `optimization_results.csv`
  - `Time_Domain_Modeling/Waveform/*.csv`
- IGBT dataset:
  - `april22nd-23rdIgbtIRCG40BC30kd-A17.mat`
- Magnetic datasets:
  - `B_waveform[T]_downscaled.csv`
  - `Frequency[Hz]_downscaled.csv`
  - `Temperature[C]_downscaled.csv`
  - `Volumetric_losses[Wm-3]_downscaled.csv`

---

## Suggested learning sequence

1. `Buck_Design/buck_comprehensive_case_study.ipynb` (full pipeline view)
2. `Buck_Design/buck_modeling_NN.ipynb` and `xgboost_buck_modeling.ipynb` (surrogate depth/comparison)
3. `DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb` (largest integrated DAB workflow)
4. `DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb` (time-domain sequence modeling)
5. `DAB_Design/Adaptive_Modulation/TinyML.ipynb` (deployment and acceleration)
6. `IGBT_Maintenance/rul_prediction.ipynb` (probabilistic reliability modeling)
7. `Magnetic_Modeling/magnet_fnn.ipynb` and `magnet_lstm.ipynb` (magnetic-loss modeling variants)
