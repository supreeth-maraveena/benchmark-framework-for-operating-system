# 📘 OS Benchmark Framework

## 🚀 Overview
A benchmarking framework for evaluating operating system policies.

This project analyzes combinations of **CPU scheduling**, **disk scheduling**, and **page replacement algorithms** to determine the most efficient policy for a given workload. It allows users to simulate different workload types, generate realistic system parameters, and identify the best-performing policy using normalized performance metrics.

---

## 🎯 Objectives
* **Compare** multiple OS policy combinations systematically.
* **Understand** how performance varies with workload characteristics.
* **Identify** the most efficient policy for a given scenario.
* **Provide** clear, visual insights using data-driven evaluation.

---

## ⚙️ Features

### ✅ Supports multiple workload types:
* CPU-bound
* I/O-bound
* Memory-bound
* Mixed

### ✅ Implements core OS algorithms:
* **CPU Scheduling:** FCFS, SJF, Priority, Round Robin
* **Page Replacement:** FIFO, LRU, Optimal
* **Disk Scheduling:** FCFS, SSTF, SCAN

### ✅ Custom input support:
* Number of processes
* Burst time range
* Page reference length
* Disk requests
* Number of frames

### ✅ Automated benchmarking:
* Evaluates all possible combinations
* Computes performance metrics
* Normalizes scores (0 to 1 scale)

### ✅ Insight generation:
* Explains why a policy performs best

### ✅ Visualization using R:
* Clean horizontal bar chart
* Top 5 policies highlighted
* Best policy emphasized

---

## 🧠 How It Works

1.  **Step 1: Select Workload** – Choose a workload type (CPU-bound, I/O-bound, etc.).
2.  **Step 2: Provide Parameters** – Enter system parameters or use default values.
3.  **Step 3: Simulation** – Workload is generated randomly based on inputs and all policy combinations are executed.
4.  **Step 4: Evaluation** – Metrics computed include Average Waiting Time (WT), Page Faults (PF), and Seek Time (ST).
    * **Normalization:** $Final Score = \frac{Best Score}{Current Score}$
    * Produces values between 0 and 1 (higher is better).
5.  **Step 5: Output** – Best policies displayed, insights generated, and results exported to `results.csv`.
6.  **Step 6: Visualization (R)** – Top 5 policies plotted and the best policy is highlighted.

---

## 📊 Sample Output

### Console Output
* Best policy combination
* Performance metrics
* Explanation of results

### Visualization
* Horizontal bar chart
* Ranked policy combinations
* Normalized scores

---

## 🗂️ Project Structure
```text
os_benchmark/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── workloads/
│   ├── cpu_bound.py
│   ├── io_bound.py
│   ├── memory_bound.py
│   └── mixed.py
│
├── algorithms/
│   ├── cpu/
│   ├── memory/
│   └── disk/
│
├── engine/
│   ├── runner.py
│   ├── evaluator.py
│   └── normalizer.py
│
├── analysis/
│   ├── decision.py
│   └── insights.py
│
├── models/
│   └── result.py
│
├── utils/
│   └── helpers.py
│
├── plots.R
└── results.csv
```
---

## 🛠️ Technologies Used
* **Python** – Core simulation and benchmarking
* **R (ggplot2)** – Data visualization
* **VS Code** – Development environment

---

## ▶️ How to Run

1.  **Run the Python Program**
    ```bash
    python main.py
    ```
2.  **Follow the Prompts**
    * Choose workload
    * Enter parameters
3.  **Generate Results**
    * Results saved in: `results.csv`
4.  **Visualize in R**
    * Open `plots.R` in RStudio and run the file

---

## 📈 Interpretation of Results
* Scores range from **0 to 1**.
* **1.0** indicates the best policy.
* Values closer to 1 indicate better performance.

---

## 🧪 Use Cases
* Academic OS analysis.
* Algorithm comparison studies.
* Understanding workload-dependent behavior.
* Performance tuning experiments.

---

## 💡 Key Insight
> **There is no universally best scheduling policy.** Performance depends heavily on workload characteristics.

---

## 🔮 Future Enhancements
* Adaptive / AI-based policy selection.
* Real-time workload classification.
* Advanced visualization dashboards.
* Integration with real system traces.

---
