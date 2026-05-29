# 9_Case_Studies_PE

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Buck_Design/buck_comprehensive_case_study.ipynb">
    <img src="https://img.shields.io/badge/Buck_comprehensive-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open buck_comprehensive_case_study.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Buck_Design/buck_modeling_NN.ipynb">
    <img src="https://img.shields.io/badge/Buck_modeling_NN-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open buck_modeling_NN.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Buck_Design/xgboost_buck_modeling.ipynb">
    <img src="https://img.shields.io/badge/Buck_XGBoost-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open xgboost_buck_modeling.ipynb in Colab" />
  </a>
</p>
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
<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Magnetic_Modeling/magnet_fnn.ipynb">
    <img src="https://img.shields.io/badge/Magnetics_FNN-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open magnet_fnn.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Magnetic_Modeling/magnet_lstm.ipynb">
    <img src="https://img.shields.io/badge/Magnetics_LSTM-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open magnet_lstm.ipynb in Colab" />
  </a>
</p>
<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/IGBT_Maintenance/rul_prediction.ipynb">
    <img src="https://img.shields.io/badge/IGBT_RUL-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open rul_prediction.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

Case-study folders map to **Section VII** (*One-stop AI applications throughout the PE lifecycle*) of *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026):

| Folder | Article sections | Details |
|--------|------------------|---------|
| [`Buck_Design/`](Buck_Design/) | **VII-A**; **VII-B**; **VII-C** | [`Buck_Design/README.md`](Buck_Design/README.md) |
| [`DAB_Design/`](DAB_Design/) | **VII-A** – **VII-D** (by subfolder) | [`DAB_Design/README.md`](DAB_Design/README.md) |
| [`IGBT_Maintenance/`](IGBT_Maintenance/) | **VII-F** | [`IGBT_Maintenance/README.md`](IGBT_Maintenance/README.md) |
| [`Magnetic_Modeling/`](Magnetic_Modeling/) | **II-C**; **VII-B** | [`Magnetic_Modeling/README.md`](Magnetic_Modeling/README.md) |

---

End-to-end AI case studies for power electronics: data preparation, surrogates, optimization, uncertainty, and deployment-oriented acceleration.

## Scope

| Case study | README |
|------------|--------|
| Buck converter design | [`Buck_Design/README.md`](Buck_Design/README.md) |
| DAB modulation & performance | [`DAB_Design/README.md`](DAB_Design/README.md) |
| IGBT maintenance (RUL) | [`IGBT_Maintenance/README.md`](IGBT_Maintenance/README.md) |
| Magnetic core loss | [`Magnetic_Modeling/README.md`](Magnetic_Modeling/README.md) |

**DAB subfolders:** [`Performance_Modeling_and_Design/`](DAB_Design/Performance_Modeling_and_Design/README.md), [`Time_Domain_Modeling/`](DAB_Design/Time_Domain_Modeling/README.md), [`Adaptive_Modulation/`](DAB_Design/Adaptive_Modulation/README.md) (overview: [`DAB_Design/README.md`](DAB_Design/README.md)).

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
- Comparison of classical ML, ensemble learning, and NNs under realistic constraints  
- Objective-driven search with surrogates and metaheuristics  
- Cleaning, outliers, and simple robustness statistics  
- Uncertainty for reliability (e.g. probabilistic RUL)  
- Compression and acceleration (pruning, ONNX, quantization) in a TinyML-oriented thread  
- Controller-oriented NN structure design

---

## Algorithm summary

- Classical / ensemble learning: SVR, Random Forest, XGBoost  
- Neural: FNN/MLP, RNN/LSTM/BiLSTM, probabilistic BiLSTM  
- Analysis: PCA, t-SNE  
- Quality / anomalies: One-Class SVM, Isolation Forest, z-score filters  
- Optimization: PSO, GA, surrogate-assisted search  
- Deployment: pruning, ONNX, ONNX Runtime, quantization  

## Data summary

See **Data summary** (and **External dataset** where applicable) in each subfolder README: [`Buck_Design/`](Buck_Design/README.md), [`DAB_Design/`](DAB_Design/README.md), [`IGBT_Maintenance/`](IGBT_Maintenance/README.md), [`Magnetic_Modeling/`](Magnetic_Modeling/README.md).

## Recommended learning sequence

1. `Buck_Design/buck_comprehensive_case_study.ipynb`  
2. `Buck_Design/buck_modeling_NN.ipynb`, `xgboost_buck_modeling.ipynb`  
3. `DAB_Design/Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`  
4. `DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb`  
5. `DAB_Design/Adaptive_Modulation/TinyML.ipynb`  
6. `IGBT_Maintenance/rul_prediction.ipynb`  
7. `Magnetic_Modeling/magnet_fnn.ipynb`, `magnet_lstm.ipynb`  
