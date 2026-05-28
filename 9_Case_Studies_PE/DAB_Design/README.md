# DAB_Design

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/DAB_Design/Adaptive_Modulation/TinyML.ipynb">
    <img src="https://img.shields.io/badge/DAB_TinyML-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open TinyML.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb">
    <img src="https://img.shields.io/badge/DAB_one_stop-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open one_stop_AI_DAB_modulation.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb">
    <img src="https://img.shields.io/badge/DAB_time_series-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open time_series_modeling.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

| Subfolder | Article sections |
|-----------|------------------|
| [`Performance_Modeling_and_Design/`](Performance_Modeling_and_Design/) | **VII-A** (EDA); **VII-B** (surrogate modeling); **VII-C** (MHA optimization) |
| [`Time_Domain_Modeling/`](Time_Domain_Modeling/) | **VII-B** (sequence / surrogate modeling) |
| [`Adaptive_Modulation/`](Adaptive_Modulation/) | **VII-D** (TinyML for PE control) |

These notebooks support the **dual-active-bridge (DAB)** case studies in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). Parent overview: [`../README.md`](../README.md).

---

DAB modulation and performance: one-stop EDA-to-optimization pipeline, waveform sequence modeling, and deployment-oriented TinyML.

## Contents

| Subfolder | Notebook | Data (local) |
|-----------|----------|----------------|
| `Performance_Modeling_and_Design/` | `one_stop_AI_DAB_modulation.ipynb` | `DAB_TPS.csv`, `utils.py` |
| `Time_Domain_Modeling/` | `time_series_modeling.ipynb` | `Waveform/*.csv` |
| `Adaptive_Modulation/` | `TinyML.ipynb` | `optimization_results.csv` |

## Outcomes

- Quality control (outliers, validity / ZVS-style filters) before surrogate training  
- Compare XGBoost, Random Forest, SVR, and neural surrogates on modulation performance  
- PSO / GA over trained surrogates; adaptive modulation segment  
- Recurrent models on DAB waveform CSVs  
- Model compression: pruning, ONNX, quantization for edge inference  

---

### `Adaptive_Modulation/TinyML.ipynb`

**Topics:** Modulation-oriented NN; capacity sweep and Pareto-style size vs. loss; L1, pruning, ONNX, timing, quantization.

**Algorithms & data:** FNN mapping, Pareto selection, pruning, ONNX Runtime, dynamic quantization. `optimization_results.csv`.

**Notes:** Speed/accuracy tradeoffs; compression path toward small-footprint inference.

---

### `Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`

**Topics:** Full DAB pipeline — EDA, cleaning, t-SNE/PCA, One-Class SVM and Isolation Forest, surrogate comparisons, PSO/GA, adaptive modulation / TinyML segment.

**Algorithms & data:** XGBoost, Random Forest, SVR, PCA, t-SNE, One-Class SVM, Isolation Forest, FNN-style models, PSO, GA. `DAB_TPS.csv`.

**Notes:** Quality control before optimization (validity, ZVS-style filters, outliers); shared plotting/analysis helpers.

---

### `Time_Domain_Modeling/time_series_modeling.ipynb`

**Topics:** Waveform CSV loading, alignment/segmentation, recurrent models, accuracy/MAE.

**Algorithms & data:** RNN/LSTM/BiLSTM-style PyTorch models. `Waveform/*.csv`.

**Notes:** Train/val/test; best checkpoint; prediction vs. measured waveforms.

---

## Algorithm summary

- XGBoost, Random Forest, SVR, FNN  
- RNN / LSTM / BiLSTM  
- PCA, t-SNE; One-Class SVM, Isolation Forest  
- PSO, GA; pruning, ONNX, quantization  

## Data summary

- `Performance_Modeling_and_Design/DAB_TPS.csv` — tabular modulation / performance table  
- `Adaptive_Modulation/optimization_results.csv` — TinyML capacity / optimization sweep  
- `Time_Domain_Modeling/Waveform/*.csv` — time-series waveforms for sequence models  

## Recommended learning sequence

1. `Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`  
2. `Time_Domain_Modeling/time_series_modeling.ipynb`  
3. `Adaptive_Modulation/TinyML.ipynb`  
