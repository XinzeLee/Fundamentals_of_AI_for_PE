# 4_Neural_Network

## Authorship & status

- **Course / code author:** Xinze Li  
- **Tutorial article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligences for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

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

Neural networks from tabular regression/classification through sequence models and mixture-density (MDN) regression.

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

**Topics:** Deterministic FNN baseline → MDN (`pi`, `mu`, `sigma`) with MDN loss; predictive mean and intervals; `RandomForestRegressor` benchmark.

**Algorithms & data:** FNN, MDN, RandomForestRegressor. Synthetic nonlinear regression from a `make_moons`-style pipeline.

**Notes:** Validation checkpoints and schedulers; emphasis on uncertainty bands, not only point predictions.

---

## Algorithm summary

- FNN / MLP (regression and classification)  
- RNN family: vanilla RNN, LSTM, GRU, BiLSTM  
- Mixture Density Network (MDN)  
- `RandomForestRegressor` as a reference in the MDN notebook  

## Data summary

- Tabular: California Housing, Breast Cancer  
- PE waveforms: DAB CSV time series  
- Synthetic nonlinear regression (`make_moons`-style pipeline)  

## Recommended order

1. `Fundamentals/NN_basics.ipynb`  
2. `Good_Practices/good_practice_NN.ipynb`  
3. `Signal_Domain/rnn_basics.ipynb`  
4. `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb`  
5. *(Optional graph track)* [`Graph_NN/README.md`](Graph_NN/README.md) — external GML2023 course, Awesome GNN list, C2G for converters  
