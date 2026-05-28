# IGBT_Maintenance

## Authorship & status

- **Course / code author:** Xinze Li  
- **Review article:** Xinze Li, Fanfan Lin, Juan J. Rodríguez-Andina, Sergio Vazquez, Homer Alan Mantooth, Leopoldo García Franquelo, “Fundamentals of Artificial Intelligence for Power Electronics,” *IEEE Transactions on Industrial Electronics*, 2026.

*These learning resources are still under active refinement; notebooks, data, and documentation may change.*

---

## Google Colab

<p align="center">
  <a href="https://colab.research.google.com/github/XinzeLee/Fundamentals_of_AI_for_PE/blob/main/9_Case_Studies_PE/IGBT_Maintenance/rul_prediction.ipynb">
    <img src="https://img.shields.io/badge/IGBT_RUL-ffffff?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open rul_prediction.ipynb in Colab" />
  </a>
</p>

---

## Alignment with the review article

**Discussion in the article:** **Sec. VII-F** (probabilistic remaining useful life prediction).

This notebook supports the **IGBT maintenance / RUL** case study in *Fundamentals of Artificial Intelligence for Power Electronics* (*IEEE Trans. Ind. Electron.*, 2026). Parent overview: [`../README.md`](../README.md).

---

Probabilistic remaining useful life (RUL) from accelerated-aging IGBT measurements.

## External dataset

| Source | Link |
|--------|------|
| NASA — Insulated Gate Bipolar Transistor (IGBT) accelerated aging | [data.nasa.gov — IGBT accelerated aging](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging) |

The bundled `april22nd-23rdIgbtIRCG40BC30kd-A17.mat` is aligned with this dataset for tutorial use; refer to NASA for licensing and citation requirements.

## Contents

- `rul_prediction.ipynb`  
- `april22nd-23rdIgbtIRCG40BC30kd-A17.mat`

## Outcomes

- Load and window cycle-based features from `.mat` aging data  
- Train a probabilistic sequence model with uncertainty bands  
- Report point error and interval coverage (e.g. 90% CI) on held-out cycles  

---

### `rul_prediction.ipynb`

**Topics:** RUL from `.mat` data; cycle/minima extraction and windowing; probabilistic BiLSTM; uncertainty bands.

**Algorithms & data:** Probabilistic BiLSTM with Gaussian NLL. `april22nd-23rdIgbtIRCG40BC30kd-A17.mat` (from NASA IGBT accelerated aging data — [dataset page](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging)).

**Notes:** Scaler fit on train; point error plus interval coverage (e.g. 90% CI).

---

## Algorithm summary

- Probabilistic BiLSTM (Gaussian NLL)  
- Cycle / minima feature extraction and windowing  

## Data summary

- `april22nd-23rdIgbtIRCG40BC30kd-A17.mat` — see [NASA IGBT accelerated aging](https://data.nasa.gov/dataset/insulated-gate-bipolar-transistor-igbt-accelerated-aging)  

## Recommended learning sequence

1. `rul_prediction.ipynb`  
