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

| Subfolder | Article sections | Details |
|-----------|------------------|---------|
| [`Performance_Modeling_and_Design/`](Performance_Modeling_and_Design/) | **VII-A**; **VII-B**; **VII-C** | [`Performance_Modeling_and_Design/README.md`](Performance_Modeling_and_Design/README.md) |
| [`Time_Domain_Modeling/`](Time_Domain_Modeling/) | **VII-B** | [`Time_Domain_Modeling/README.md`](Time_Domain_Modeling/README.md) |
| [`Adaptive_Modulation/`](Adaptive_Modulation/) | **VII-D** | [`Adaptive_Modulation/README.md`](Adaptive_Modulation/README.md) |

These notebooks support the **dual-active-bridge (DAB)** case studies in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). Parent overview: [`../README.md`](../README.md).

---

DAB modulation and performance: one-stop EDA-to-optimization pipeline, waveform sequence modeling, and deployment-oriented TinyML.

## Scope

| Track | README | Notebook |
|-------|--------|----------|
| Performance modeling & design | [`Performance_Modeling_and_Design/README.md`](Performance_Modeling_and_Design/README.md) | `one_stop_AI_DAB_modulation.ipynb` |
| Time-domain waveforms | [`Time_Domain_Modeling/README.md`](Time_Domain_Modeling/README.md) | `time_series_modeling.ipynb` |
| Adaptive modulation (TinyML) | [`Adaptive_Modulation/README.md`](Adaptive_Modulation/README.md) | `TinyML.ipynb` |

Per-notebook **Topics**, **Algorithms & data**, and **Notes** are in each subfolder README.

## Outcomes

- Quality control (outliers, validity / ZVS-style filters) before surrogate training  
- Compare XGBoost, Random Forest, SVR, and neural surrogates on modulation performance  
- PSO / GA over trained surrogates  
- Recurrent models on DAB waveform CSVs  
- Model compression: pruning, ONNX, quantization for edge inference  

## Algorithm summary

- XGBoost, Random Forest, SVR, FNN  
- RNN / LSTM / BiLSTM  
- PCA, t-SNE; One-Class SVM, Isolation Forest  
- PSO, GA; pruning, ONNX, quantization  

## Data summary

See **Data summary** in each subfolder README: [`Performance_Modeling_and_Design/`](Performance_Modeling_and_Design/README.md), [`Time_Domain_Modeling/`](Time_Domain_Modeling/README.md), [`Adaptive_Modulation/`](Adaptive_Modulation/README.md).

## Recommended learning sequence

1. [`Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`](Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb)  
2. [`Time_Domain_Modeling/time_series_modeling.ipynb`](Time_Domain_Modeling/time_series_modeling.ipynb)  
3. [`Adaptive_Modulation/TinyML.ipynb`](Adaptive_Modulation/TinyML.ipynb)  
