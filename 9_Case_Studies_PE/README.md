# 9_Case_Studies_PE

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Alignment with the tutorial article

Case-study folders map to **Section VII** (and supporting sections) of *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026):

| Folder | Article sections |
|--------|------------------|
| [`Buck_Design/`](Buck_Design/) | VII-A; VII-B; VII-C |
| [`DAB_Design/Performance_Modeling_and_Design/`](DAB_Design/Performance_Modeling_and_Design/) | IV-B; VII-A; VII-B; VII-C |
| [`DAB_Design/Time_Domain_Modeling/`](DAB_Design/Time_Domain_Modeling/) | VII-B |
| [`DAB_Design/Adaptive_Modulation/`](DAB_Design/Adaptive_Modulation/) | VII-D |
| [`IGBT_Maintenance/`](IGBT_Maintenance/) | VII-F |
| [`Magnetic_Modeling/`](Magnetic_Modeling/) | III-C; IV-F; IV-G |

---

End-to-end AI case studies for power electronics: data preparation, surrogates, optimization, uncertainty, and deployment-oriented acceleration.

## External datasets

Some case studies use **public datasets** in addition to CSV/MAT files shipped in this folder:

| Study | Source | Link |
|--------|--------|------|
| **IGBT maintenance (RUL)** | NASA — Insulated Gate Bipolar Transistor (IGBT) accelerated aging | [data.nasa.gov — IGBT accelerated aging](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging) |
| **Magnetic modeling** | Princeton University — MagNet Challenge | [MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html) |

The bundled `.mat` / `*_downscaled.csv` files in `IGBT_Maintenance` and `Magnetic_Modeling` are derived from or aligned with these sources for tutorial use; refer to the original sites for licensing and citation requirements.

## Scope

**Subfolders:** `Buck_Design`, `DAB_Design/Adaptive_Modulation`, `DAB_Design/Performance_Modeling_and_Design`, `DAB_Design/Time_Domain_Modeling`, `IGBT_Maintenance`, `Magnetic_Modeling`.

**Notebooks**

1. `Buck_Design/buck_comprehensive_case_study.ipynb`  
2. `Buck_Design/buck_modeling_NN.ipynb`  
3. `Buck_Design/xgboost_buck_modeling.ipynb`  
4. `DAB_Design/Adaptive_Modulation/TinyML.ipynb`  
5. `DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`  
6. `DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb`  
7. `IGBT_Maintenance/rul_prediction.ipynb`  
8. `Magnetic_Modeling/magnet_fnn.ipynb`  
9. `Magnetic_Modeling/magnet_lstm.ipynb`  

## Outcomes

- PE modeling pipelines from raw or simulation data to deployable models  
- Comparison of classical ML, ensembles, NNs, and sequences under realistic constraints  
- Objective-driven search with surrogates and metaheuristics  
- Cleaning, outliers, and simple robustness statistics  
- Uncertainty for reliability (e.g. probabilistic RUL)  
- Compression and acceleration (pruning, ONNX, quantization) in a TinyML-oriented thread  

---

## Buck design

### `buck_comprehensive_case_study.ipynb`

**Topics:** EDA, objectives, lookup / screening, surrogate training, PSO vs. GA over surrogate objectives.

**Algorithms & data:** FNN surrogates, PSO, GA, classical baselines in analysis. `total_100W_12V.csv` and derived loss/ripple-style targets.

**Notes:** Weighted / scenario multi-objective steps; outlier handling; correlation and distribution diagnostics before optimization.

### `buck_modeling_NN.ipynb`

**Topics:** Efficiency modeling — EDA, Random Forest / XGBoost, deeper MLP surrogate with regularization and scheduler, prediction surfaces.

**Algorithms & data:** RandomForestRegressor, XGBoost, FNN, t-SNE. `sync_buck_performances_cleaned.csv`.

**Notes:** Scaled inputs; train/val/test; R², RMSE, MAE, loss curves.

### `xgboost_buck_modeling.ipynb`

**Topics:** Efficiency and ripple via XGBoost; training diagnostics; optimization stage driven by trained surrogates.

**Algorithms & data:** `XGBRegressor`, Random Forest baseline, MHA stage. `sync_buck_performances_cleaned.csv` with engineered ripple target.

**Notes:** Outlier filtering; prediction vs. actual and round-wise curves.

---

## DAB design

### `Adaptive_Modulation/TinyML.ipynb`

**Topics:** Modulation-oriented NN; capacity sweep and Pareto-style size vs. loss; L1, pruning, ONNX, timing, quantization.

**Algorithms & data:** FNN mapping, Pareto selection, pruning, ONNX Runtime, dynamic quantization. `optimization_results.csv`.

**Notes:** Speed/accuracy tradeoffs; compression path toward small-footprint inference.

### `Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`

**Topics:** Full DAB pipeline — EDA, cleaning, t-SNE/PCA, One-Class SVM and Isolation Forest, surrogate comparisons, PSO/GA, adaptive modulation / TinyML segment.

**Algorithms & data:** XGBoost, Random Forest, SVR, PCA, t-SNE, One-Class SVM, Isolation Forest, FNN-style models, PSO, GA. `DAB_TPS.csv`.

**Notes:** Quality control before optimization (validity, ZVS-style filters, outliers); shared plotting/analysis helpers.

### `Time_Domain_Modeling/time_series_modeling.ipynb`

**Topics:** Waveform CSV loading, alignment/segmentation, recurrent models, accuracy/MAE.

**Algorithms & data:** RNN/LSTM/BiLSTM-style PyTorch models. `Waveform/*.csv`.

**Notes:** Train/val/test; best checkpoint; prediction vs. measured waveforms.

---

## IGBT maintenance

### `IGBT_Maintenance/rul_prediction.ipynb`

**Topics:** RUL from `.mat` data; cycle/minima extraction and windowing; probabilistic BiLSTM; uncertainty bands.

**Algorithms & data:** Probabilistic BiLSTM with Gaussian NLL. `april22nd-23rdIgbtIRCG40BC30kd-A17.mat` (from NASA IGBT accelerated aging data — [dataset page](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging)).

**Notes:** Scaler fit on train; point error plus interval coverage (e.g. 90% CI).

---

## Magnetic modeling

### `Magnetic_Modeling/magnet_fnn.ipynb`

**Topics:** Core loss from harmonics + operating conditions; FFT features from B-waveforms; FNN regression.

**Algorithms & data:** FNN for volumetric core loss. `B_waveform[T]_downscaled.csv`, `Frequency[Hz]_downscaled.csv`, `Temperature[C]_downscaled.csv`, `Volumetric_losses[Wm-3]_downscaled.csv` (MagNet-style data — [Princeton MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html)).

**Notes:** Log targets and scaling; MAE, RMSE, MAPE; parameter count.

### `Magnetic_Modeling/magnet_lstm.ipynb`

**Topics:** BiLSTM temporal features + frequency/temperature numeric inputs; FC head for volumetric loss.

**Algorithms & data:** BiLSTM + fused numeric branch. Same four CSVs as above (see [MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html)).

**Notes:** Shared split indices across branches; multi-input `Dataset` / `DataLoader` pattern.

---

## Algorithm summary

- Classical / ensembles: Random Forest, XGBoost, SVR  
- Neural: FNN/MLP, RNN/LSTM/BiLSTM, probabilistic BiLSTM  
- Analysis: PCA, t-SNE  
- Quality / anomalies: One-Class SVM, Isolation Forest, z-score filters  
- Optimization: PSO, GA, surrogate-assisted search  
- Deployment: pruning, ONNX, ONNX Runtime, quantization  

## Data summary

- **Buck:** `total_100W_12V.csv`, `sync_buck_performances_cleaned.csv`  
- **DAB:** `DAB_TPS.csv`, `optimization_results.csv`, `Time_Domain_Modeling/Waveform/*.csv`  
- **IGBT:** `april22nd-23rdIgbtIRCG40BC30kd-A17.mat` — see [NASA IGBT accelerated aging](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging)  
- **Magnetic:** the four `*_downscaled.csv` files listed above — see [Princeton MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html)  

## Recommended order

1. `Buck_Design/buck_comprehensive_case_study.ipynb`  
2. `Buck_Design/buck_modeling_NN.ipynb`, `xgboost_buck_modeling.ipynb`  
3. `DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`  
4. `DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb`  
5. `DAB_Design/Adaptive_Modulation/TinyML.ipynb`  
6. `IGBT_Maintenance/rul_prediction.ipynb`  
7. `Magnetic_Modeling/magnet_fnn.ipynb`, `magnet_lstm.ipynb`  
