# 4_Neural_Network

This module covers practical neural-network development from tabular baselines to sequence modeling and probabilistic regression.

## Notebooks in this folder

- `Fundamentals/NN_basics.ipynb`
- `Good_Practices/good_practice_NN.ipynb`
- `Signal_Domain/rnn_basics.ipynb`
- `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb`

---

## Learning objectives (overall module)

After finishing this module, learners should be able to:

- build and train feedforward neural networks for regression and classification;
- apply robust training workflow patterns (train/val/test split, normalization, mini-batch training, checkpointing);
- implement and compare sequence models for waveform/time-series prediction (RNN/LSTM/GRU/BiLSTM and related variants);
- understand probabilistic regression via Mixture Density Networks (MDN) and uncertainty-aware outputs;
- implement model combination on the multi-modal distribution problems
- compare NN-based models with ensemble baselines under the same data setup.

---

## What each notebook contains

### 1) `Fundamentals/NN_basics.ipynb`

**What this notebook contains**
- Introduces basic FNN modeling on tabular tasks:
  - numerical regression (California Housing);
  - categorical/binary classification (Breast Cancer).
- Covers model-head/loss alignment (regression vs classification).
- Includes a reconfigured classification setup using softmax-style output + NLL-oriented training.
- Adds an advanced section on density/probabilistic ideas.

**Algorithm and data coverage**
- Algorithms: FNN/MLP regression, FNN/MLP classification.
- Data: `fetch_california_housing`, `load_breast_cancer` (scikit-learn built-ins).

**Additional code-level notes**
- Uses feature standardization before NN training.
- Tracks train/validation losses and visualizes residuals/confusion/ROC behavior.
- Includes dropout in classification architecture to reduce overfitting risk.

---

### 2) `Good_Practices/good_practice_NN.ipynb`

**What this notebook contains**
- Demonstrates engineering best practices for NN training:
  - overfit-capacity sanity check mindset;
  - normalization layers (`BatchNorm1d`);
  - strict train/val/test split usage;
  - mini-batch training with `DataLoader`;
  - best-checkpoint selection by validation loss.
- Adds advanced optimization workflow:
  - learning-rate annealing (`ReduceLROnPlateau`);
  - gradient z-scoring before optimizer step.

**Algorithm and data coverage**
- Algorithms: feedforward NN for regression with improved training strategy.
- Data: preprocessed tabular regression-style setup (split and scaled in notebook).

**Additional code-level notes**
- Includes both full-batch and mini-batch variants for comparison.
- Explicitly saves and reloads best model weights.
- Emphasizes reproducible preprocessing (fit scaler on train only).

---

### 3) `Signal_Domain/rnn_basics.ipynb`

**What this notebook contains**
- Loads and processes DAB converter waveform CSV data for time-series learning.
- Implements multiple sequence/backbone models:
  - feedforward model with sliding window,
  - vanilla RNN,
  - LSTM,
  - GRU,
  - BiLSTM,
  - additional advanced sequence-model directions (as documented in notebook narrative).
- Uses train/val/test splitting, model-size reporting, and prediction-vs-ground-truth plotting.

**Algorithm and data coverage**
- Algorithms: FFN (windowed), RNN, LSTM, GRU, BiLSTM (and documented transformer-oriented direction).
- Data: local waveform CSV files from PE case-study waveform directory.

**Additional code-level notes**
- Uses `AdamW` with weight decay for several models.
- Applies warmup + cosine-style LR scheduling logic in training loops.
- Maintains best-validation checkpoints before test evaluation.

---

### 4) `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb`

**What this notebook contains**
- Builds a probabilistic regression workflow:
  - starts with deterministic FNN regression baseline;
  - upgrades to **MDN** (mixture components with `pi`, `mu`, `sigma`);
  - trains with custom MDN likelihood-style loss;
  - visualizes predictive mean and confidence intervals.
- Adds ensemble benchmark comparison using `RandomForestRegressor`.

**Algorithm and data coverage**
- Algorithms: FNN regression, Mixture Density Network (MDN), RandomForestRegressor baseline.
- Data: synthetic/nonlinear regression data derived from `make_moons` transformation workflow.

**Additional code-level notes**
- Uses validation-based checkpointing and scheduler updates during training.
- Demonstrates uncertainty visualization rather than point-prediction only.
- Useful bridge between deep learning and uncertainty-aware modeling.

---

## Consolidated algorithm coverage in `4_Neural_Network`

- **Feedforward neural networks (MLP/FNN)** for regression and classification
- **RNN-family sequence models**: vanilla RNN, LSTM, GRU, BiLSTM
- **Probabilistic neural model**: Mixture Density Network (MDN)
- **Reference baseline**: RandomForestRegressor (for comparison in probabilistic-regression notebook)

---

## Consolidated data coverage in `4_Neural_Network`

- Built-in tabular datasets:
  - California Housing
  - Breast Cancer
- Local PE waveform sequence data:
  - DAB waveform CSV-based time-series samples
- Synthetic nonlinear regression data:
  - transformed setup based on `make_moons`-style generation

---

## Suggested learning sequence

1. `Fundamentals/NN_basics.ipynb` (core MLP concepts and task-dependent heads/losses)
2. `Good_Practices/good_practice_NN.ipynb` (training discipline and optimization hygiene)
3. `Signal_Domain/rnn_basics.ipynb` (time-series/waveform modeling for PE)
4. `Multi_Modal_Distribution/mixture_density_net_ensemble_learning.ipynb` (probabilistic regression and uncertainty)

