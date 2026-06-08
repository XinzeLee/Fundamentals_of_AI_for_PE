# Magnetic_Modeling

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Magnetic_Modeling/magnet_fnn.ipynb">
    <img src="https://img.shields.io/badge/Magnetics_FNN-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open magnet_fnn.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/Magnetic_Modeling/magnet_lstm.ipynb">
    <img src="https://img.shields.io/badge/Magnetics_LSTM-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open magnet_lstm.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

**Discussion in the article:** **Section II-C** (tabular / field-motivated loss data); **VII-B** (surrogate modeling).

These notebooks support the **magnetic core loss** case study in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). 

---

## Dataset Description

**MagNet Challenge dataset (downscaled)** — core loss modeling of 3C90 magnetic material

| Item | Description |
|------|-------------|
| **Jupyter Notebooks** | [`magnet_fnn.ipynb`](magnet_fnn.ipynb); [`magnet_lstm.ipynb`](magnet_lstm.ipynb) |
| **Task** | Model the core loss of 3C90 magnetic material |

**AI solutions**

1. **Solution 1 — Feedforward NN**  
   - **Neural network inputs:** harmonic magnitudes, frequency, temperature  
   - **Neural network outputs:** volumetric core loss  

2. **Solution 2 — LSTM**  
   - **Neural network inputs:** B-field waveform, frequency, temperature  
   - **Neural network outputs:** volumetric core loss  

---

Core-loss surrogate modeling from B-waveforms, frequency, and temperature (MagNet downscaled CSVs).

## External dataset

| Source | Link |
|--------|------|
| Princeton University — MagNet Challenge | [MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html) |

The four `*_downscaled.csv` files in this folder are derived from or aligned with MagNet-style data for tutorial use; refer to [MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html) for citation requirements.

## Contents

- `magnet_fnn.ipynb`  
- `magnet_lstm.ipynb`  
- `B_waveform[T]_downscaled.csv`, `Frequency[Hz]_downscaled.csv`, `Temperature[C]_downscaled.csv`, `Volumetric_losses[Wm-3]_downscaled.csv`

## Outcomes

- FFT / harmonic features from B-waveforms for FNN regression  
- BiLSTM branch fused with frequency and temperature for volumetric loss  
- Log targets, scaling, and MAE / RMSE / MAPE reporting  

---

### `magnet_fnn.ipynb`

**Topics:** Core loss from harmonics + operating conditions; FFT features from B-waveforms; FNN regression.

**Algorithms & data:** FNN for volumetric core loss. `B_waveform[T]_downscaled.csv`, `Frequency[Hz]_downscaled.csv`, `Temperature[C]_downscaled.csv`, `Volumetric_losses[Wm-3]_downscaled.csv` (MagNet data — [Princeton MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html)).

**Notes:** Input and output scaling; waveform sequence conversion; parameter count.

---

### `magnet_lstm.ipynb`

**Topics:** BiLSTM temporal features + frequency/temperature numeric inputs; FC head for volumetric loss.

**Algorithms & data:** BiLSTM + fused numeric branch. Same four CSVs as above (see [MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html)).

**Notes:** Multi-modal data; feature fusion; hybrid tabular and sequential input data.

---

## Algorithm summary

- FNN (harmonic / FFT features)  
- BiLSTM + fused numeric inputs  

## Data summary

- `B_waveform[T]_downscaled.csv`  
- `Frequency[Hz]_downscaled.csv`  
- `Temperature[C]_downscaled.csv`  
- `Volumetric_losses[Wm-3]_downscaled.csv` — see [MagNet Challenge](https://www.princeton.edu/~minjie/magnet.html)  

## Recommended learning sequence

1. `magnet_fnn.ipynb`  
2. `magnet_lstm.ipynb`  
