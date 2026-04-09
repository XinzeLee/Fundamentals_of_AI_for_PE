# 4_Neural_Network

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/4_Neural_Network/Fundamentals/NN_basics.ipynb">
    <img src="https://img.shields.io/badge/Open_NN_basics_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open NN_basics.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/4_Neural_Network/Good_Practices/good_practice_NN.ipynb">
    <img src="https://img.shields.io/badge/Open_good_practice_NN_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open good_practice_NN.ipynb in Colab" />
  </a>
</p>
<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/4_Neural_Network/Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb">
    <img src="https://img.shields.io/badge/Open_MDN_notebook_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open mixture_density_net_ensemble_learning.ipynb in Colab" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/4_Neural_Network/Signal_Domain/rnn_basics.ipynb">
    <img src="https://img.shields.io/badge/Open_rnn_basics_in_Colab-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open rnn_basics.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the tutorial article

Subfolders map to sections of *Fundamentals of Artificial Intelligences for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026) as follows:

| Subfolder | Article sections |
|-----------|------------------|
| [`Fundamentals/`](Fundamentals/) | Section III; Section IV-C; Section IV-D; Section IV-F |
| [`Good_Practices/`](Good_Practices/) | Section IV-G |
| [`Signal_Domain/`](Signal_Domain/) | Section III-C; Section IV-F; Section IV-G |
| [`Multi_Modal_Distribution/`](Multi_Modal_Distribution/) | Section IV-E; Section IV-F |
| [`Graph_NN/`](Graph_NN/) | Section III-E; Section IV-F (see [`Graph_NN/README.md`](Graph_NN/README.md)) |

---

Neural networks from tabular regression/classification through sequence models and mixture-density (MDN) regression, including a **hysteresis** extension (Part 3b in the MDN notebook): rate-independent loops, **Prandtl–Ishlinskii** play-operator superposition vs an **MDN** that targets multimodal **p(y|x)**, with references to **B–H**-style behavior in magnetic components.

## Contents

- `Fundamentals/NN_basics.ipynb`  
- `Good_Practices/good_practice_NN.ipynb`  
- `Signal_Domain/rnn_basics.ipynb`  
- `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb`  
- [`Graph_NN/README.md`](Graph_NN/README.md) — graph neural networks: external course (GML2023), Awesome GNN list, PE application (C2G)  

## Outcomes

- Feedforward networks for regression and classification  
- Train/val/test splits, normalization, minibatches, checkpoints  
- Sequence models for waveforms / time series (RNN, LSTM, GRU, BiLSTM, related variants)  
- Probabilistic regression via MDN and uncertainty in the outputs  
- Model combination on multimodal targets and comparison to ensemble baselines  
- Hysteresis as motivation: single-valued maps fail on loops; PI-style state (play operators) vs mixture models for **p(y|x)** on the same synthetic loop  
- *(Graph track)* Where to learn **GNNs** and how they apply to **converter graphs** — see [`Graph_NN/README.md`](Graph_NN/README.md)

---

### `Fundamentals/NN_basics.ipynb`

**Topics:** FNN on California Housing (regression) and Breast Cancer (classification); heads and losses; softmax + NLL-style classification; optional density / probabilistic section.

**Algorithms & data:** FNN/MLP regression and classification. `fetch_california_housing`, `load_breast_cancer`.

**Notes:** Feature scaling; train/val loss; residuals, confusion, ROC; dropout in the classifier.

---

### `Good_Practices/good_practice_NN.ipynb`

**Topics:** Capacity sanity checks; `BatchNorm1d`; strict train/val/test; `DataLoader` minibatches; best checkpoint by validation loss; `ReduceLROnPlateau`; gradient z-scoring before the optimizer step.

**Algorithms & data:** Feedforward regression with stronger training discipline. Tabular data prepared inside the notebook.

**Notes:** Full-batch vs. minibatch comparison; saved best weights; scaler fit on train only.

---

### `Signal_Domain/rnn_basics.ipynb`

**Topics:** DAB waveform CSV loading and preprocessing; windowed FFN, RNN, LSTM, GRU, BiLSTM; further sequence directions in the notebook text; splits, model size, prediction plots.

**Algorithms & data:** Windowed FFN, RNN, LSTM, GRU, BiLSTM (+ transformer-oriented material as documented). Local PE waveform CSVs.

**Notes:** `AdamW` and weight decay; warmup + cosine-style schedules; best checkpoint before test evaluation.

---

### `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb`

**Topics:** Deterministic FNN baseline → MDN (`pi`, `mu`, `sigma`) with MDN loss; predictive mean and intervals; `RandomForestRegressor` benchmark. **Part 3b** adds the same synthetic **hysteresis** setting as the standalone Prandtl–Ishlinskii notebook: **play operators**, a **Prandtl–Ishlinskii–style NN** trained with MSE, and an **MDN** on the loop—contrasting state-based loop tracing with a multimodal conditional density and tying the story to **B–H** loops in real cores.

**Algorithms & data:** FNN, MDN, RandomForestRegressor; play-operator stack / Prandtl–Ishlinskii–style subnetwork (PyTorch). Synthetic nonlinear regression from a `make_moons`-style pipeline; sinusoidal-input **rate-independent** hysteresis loop (aligned parameters with the PI tutorial notebook).

**Notes:** Validation checkpoints and schedulers; emphasis on uncertainty bands, not only point predictions. Part 3b is inserted before the ensemble section: read MDN definitions earlier in the notebook first.

---

## Algorithm summary

- FNN / MLP (regression and classification)  
- RNN family: vanilla RNN, LSTM, GRU, BiLSTM  
- Mixture Density Network (MDN)  
- `RandomForestRegressor` as a reference in the MDN notebook  
- Prandtl–Ishlinskii-style hysteresis (play operators + superposition NN) in the MDN notebook  

## Data summary

- Tabular: California Housing, Breast Cancer  
- PE waveforms: DAB CSV time series  
- Synthetic nonlinear regression (`make_moons`-style pipeline)  
- Synthetic hysteresis loop (time-ordered input, multimodal **p(y|x)** vs PI state)  

## Recommended order

1. `Fundamentals/NN_basics.ipynb`  
2. `Good_Practices/good_practice_NN.ipynb`  
3. `Signal_Domain/rnn_basics.ipynb`  
4. `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb`  
5. *(Optional graph track)* [`Graph_NN/README.md`](Graph_NN/README.md) — external GML2023 course, Awesome GNN list, C2G for converters  
