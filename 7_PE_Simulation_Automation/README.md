# 7_PE_Simulation_Automation

Automation for PE simulation: batch runs, metrics extraction, and CSV-friendly outputs for downstream ML.

## Contents

| Kind | Path |
|------|------|
| Notebooks | `LTspiceAutomation/LTspiceAtuomate.ipynb`, `PlecsAutomation/Data acquisition.ipynb` |
| MATLAB | `SimulinkAutomation/BuckConverter_Automation.m` — Simulink buck automation |

## Outcomes

- Parameter sweeps driven from code instead of manual GUI sweeps  
- Waveforms and scalars in structured files (CSV) for training pipelines  
- Batch loops with timeout / error handling for large sweeps  
- Patterns portable toward optimization and surrogate modeling  
- Cross-tool perspective: LTspice, PLECS, Simulink, and similar Ansys-style flows  

---

### `LTspiceAutomation/LTspiceAtuomate.ipynb`

**Topics:** **PyLTSpice** — simulator binary and schematic paths; Cartesian parameter grids (`itertools.product`); batch transient runs via netlist parameters; `.raw` parsing; CSV export; plots and metrics (e.g. overshoot).

**Notes:** Pre-flight checks for simulator binary and schematic files; failed runs logged while the sweep continues.

---

### `PlecsAutomation/Data acquisition.ipynb`

**Topics:** **PLECS XML-RPC** automation; grid-search parameter grids and indexed helpers; worker threads with `func_timeout` timeouts; `Performance.csv` plus per-run `Waveform/*.csv`.

**Notes:** Timeouts, non-convergent-case handling, append-style result files for long jobs; output shape aligned with later ML/PIML notebooks.

---

### `SimulinkAutomation/BuckConverter_Automation.m`

**Topics:** MATLAB orchestration for the Simulink buck model — parallel to the LTspice/PLECS notebooks.

---

## Automation coverage

- Exhaustive grid search over user-defined ranges  
- Batch invocation of simulators from Python or MATLAB  
- Threaded PLECS jobs with timeouts  
- Automated metrics from raw traces and CSV persistence  

## Data products

- Per-case waveform time series  
- One CSV row per operating point or design  
- Simulator channel names (currents, voltages, thermal nodes) depend on the schematic  

---

## Ansys-style workflows

A practical pattern for AEDT-class tools:

1. **Record Script to File** in the GUI for a working baseline.  
2. Refactor into parameterized functions or modules.  
3. **PyAEDT** (or similar) for sweeps, solves, and exports.

Recording a known-good GUI flow first, then generalizing, is usually the fastest path to reliable automation.

## Recommended order

1. LTspice notebook — local sweep mechanics.  
2. PLECS XML-RPC notebook — API-style remote control.  
3. Connect CSV/waveform outputs to ML or PIML scripts.  
4. Reuse the same ideas for Simulink or Ansys toolchains.
