# 7_PE_Simulation_Automation

This module shows how to automate power-electronics simulation workflows and extract design/performance data programmatically.

## Notebooks in this folder

- `LTspiceAutomation/LTspiceAtuomate.ipynb`
- `PlecsAutomation/Data acquisition.ipynb`

## Related script in this folder

- `SimulinkAutomation/BuckConverter_Automation.m` (MATLAB/Simulink automation entry)

---

## Learning objectives of this module

After completing this module, learners should be able to:

- run parameter sweeps in circuit simulators automatically (instead of manual GUI sweeps);
- collect waveform and scalar metrics into structured files (CSV) for AI model training;
- design robust simulation loops with timeout/error handling for large batch runs;
- connect PE simulation tools with downstream optimization and data-driven modeling pipelines;
- understand cross-tool automation patterns for LTspice, Plecs, Simulink, and Ansys-style environments.

---

## What this module contains

### 1) `LTspiceAutomation/LTspiceAtuomate.ipynb`

**What this notebook contains**
- Uses **PyLTSpice** automation APIs to:
  - set LTspice executable and schematic paths,
  - enumerate multi-parameter combinations (`itertools.product`),
  - run batch transient simulations via netlist parameter updates,
  - parse `.raw` traces and extract target signals/metrics,
  - export sweep results to CSV.

**Additional code-level notes**
- Includes pre-run file existence checks for executable/schematic.
- Logs failed runs and continues sweep execution.
- Demonstrates post-processing (e.g., waveform plotting, overshoot extraction).

### 2) `PlecsAutomation/Data acquisition.ipynb`

**What this notebook contains**
- Uses **PLECS XML-RPC** interface for automated simulation calls.
- Builds grid-search parameter combinations and indexed parameter retrieval helpers.
- Implements threaded execution (`threading.Thread`) with timeout guards (`func_timeout`).
- Writes:
  - scalar performance records (`Performance.csv`),
  - per-run waveform files (`Waveform/*.csv`).

**Additional code-level notes**
- Includes long-run resilience patterns:
  - timeout decorators,
  - error capture for non-convergent simulations,
  - append-style result writing for incremental progress.
- Matches the data-generation style needed for later ML/PIML pipelines.

### 3) `SimulinkAutomation/BuckConverter_Automation.m` (related)

**What this script contains**
- MATLAB-based automation flow for Simulink buck-converter simulation orchestration.
- Intended as the Simulink counterpart to notebook-based LTspice/Plecs automation.

---

## Algorithm and data coverage

### Automation/algorithm coverage

- **Grid search / exhaustive parameter sweep** over user-defined parameter ranges.
- **Batch simulation orchestration** with programmatic simulator calls.
- **Threaded job execution + timeout handling** (Plecs workflow).
- **Automated metric extraction** from raw traces and structured result persistence.

### Data coverage

- **Waveform time-series data** exported per simulation case.
- **Aggregated performance table data** (CSV rows per operating point/design).
- **Simulator-native trace channels** (currents/voltages/thermal nodes depending on setup).

---

## Important note for Ansys automation

For **Ansys**-based automation (e.g., AEDT ecosystem), a highly practical workflow is:

1. **Use "Record Script to File"** in the Ansys GUI to capture a working baseline script.
2. Refactor the recorded script into parameterized automation blocks.
3. Use **PyAEDT** (or similar Python APIs) to run sweeps, submit solves, and export results.

This "record first, then generalize" approach is usually the fastest way to build reliable Ansys automation for PE workflows.

---

## Suggested usage for learners

1. Start from LTspice notebook to understand local parameter-sweep mechanics.
2. Move to Plecs XML-RPC notebook for remote/API-style simulation control.
3. Connect exported CSV/waveform outputs to your ML/PIML training scripts.
4. Reuse the same automation pattern for Simulink/Ansys toolchains.
