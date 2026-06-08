# Time_Domain_Modeling

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/DAB_Design/Time_Domain_Modeling/time_series_modeling.ipynb">
    <img src="https://img.shields.io/badge/DAB_time_series-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open time_series_modeling.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

**Discussion in the article:** **Section VII-B** (time-domain waveform modeling on signal-domain DAB waveforms).

This notebook supports the **DAB time-domain** case study in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). 

---

## Review article excerpt

> <p align="center">
>   <img src="../../../docs/img/dab-waveform-modeling-accuracy.png" alt="Neural network accuracy comparison for DAB time-domain waveform modeling" width="720" />
> </p>
>
> <p align="center"><em>Figure 1. NNs for DAB converter time-domain modeling.</em></p>
>
> <p align="center">
>   <img src="../../../docs/img/dab-waveform-modeling-cases.png" alt="Exemplary DAB test-set waveforms" width="720" />
> </p>
>
> <p align="center"><em>Figure 2. Exemplary waveforms in the test set.</em></p>
>
> This case study covers **time-domain modeling** of DAB converters. Model inputs are voltage waveforms **v<sub>p</sub>** and **v<sub>s</sub>**; the output is the current waveform **i<sub>L</sub>**. As shown in Figure 1, four networks are trained in [`time_series_modeling.ipynb`](time_series_modeling.ipynb): **FNN**, **LSTM**, **BiLSTM**, and **BiLSTM with calibration**. Exemplary test-set waveforms appear in Figure 2.
>
> The large errors of the **FNN** show that a feedforward structure does not capture **temporal causality** in signal-domain data. **LSTM** and **BiLSTM** recurrent models handle waveforms more appropriately. Further gains come from **calibrating** waveforms to the rising edge of **v<sub>p</sub>**, which reduces phase ambiguity—aligned with **Section II-B** (signal-domain data) and [`4_Neural_Network/Signal_Domain/`](../../../4_Neural_Network/Signal_Domain/).

---

## Dataset Description

**DAB dataset** — time-domain modeling of DAB converters

| Item | Description |
|------|-------------|
| **Topology** | DAB converter |
| **Modulation** | Triple phase shift (TPS) |
| **Jupyter Notebook** | [`time_series_modeling.ipynb`](time_series_modeling.ipynb) |
| **Operating range** | Input voltage **V<sub>in</sub>** = 200 V, output voltage **V<sub>out</sub>** ∈ [160 V, 240 V], rated power = 1 kW, load range ∈ [100 W, 1000 W] |
| **Task** | Model the inductor current **i<sub>L</sub>** given the ac voltages **v<sub>p</sub>** and **v<sub>s</sub>** |

**AI solutions — ML for time-domain modeling of DAB converters**

- **ML model inputs:** ac voltage waveforms **v<sub>p</sub>** and **v<sub>s</sub>**  
- **ML model outputs:** inductor current waveform **i<sub>L</sub>**  

---

NNs for DAB waveform modeling: alignment/calibration, recurrent architectures.

## Contents

- `time_series_modeling.ipynb`  
- `Waveform/*.csv` (bundled waveform library)

## Outcomes

- Load and preprocess DAB waveform time series  
- Train RNN / LSTM / BiLSTM-style models with train/val/test splits  
- Compare prediction accuracy (e.g. MAE) against measured waveforms  
- Relate signal-domain modeling to **Section II-B** concepts in [`4_Neural_Network/Signal_Domain/`](../../../4_Neural_Network/Signal_Domain/)  

---

### `time_series_modeling.ipynb`

**Topics:** Waveform CSV loading, alignment/segmentation, recurrent models, accuracy/MAE.

**Algorithms & data:** RNN/LSTM/BiLSTM-style PyTorch models. `Waveform/*.csv`.

**Notes:** Train/val/test; best checkpoint; prediction vs. measured waveforms.

---

## Algorithm summary

- RNN, LSTM, BiLSTM (PyTorch)  
- Windowed sequence preprocessing  

## Data summary

- `Waveform/*.csv` — DAB time-domain waveforms (100 bundled files acquired using PLECS automation)  

## Recommended learning sequence

1. [`Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb`](../Performance_Modeling_and_Design/one_stop_AI_DAB_modulation.ipynb) *(tabular EDA and surrogates first, recommended)*  
2. `time_series_modeling.ipynb`  
