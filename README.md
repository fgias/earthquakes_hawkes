# Hawkes Process Modelling of Earthquakes in Greece

## Overview

This project studies earthquake occurrence times in Greece using
point processes.

The main goal is to compare:

- Homogeneous Poisson process
- Hawkes self-exciting process

and investigate whether earthquake clustering is better explained by aftershock triggering.

---

## Environment Setup

Create the conda environment:

```bash
mamba create -n hawkes-earthquakes python=3.12 numpy pandas matplotlib scipy jupyter seaborn
````

Activate:

```bash
mamba activate hawkes-earthquakes
```

Launch Jupyter:

```bash
jupyter notebook
```

---

## Dataset

Earthquake data are obtained from the USGS Earthquake Catalog.

The dataset contains:

* time of occurrence
* latitude
* longitude
* depth
* magnitude
* location

Region:

* Greece
* 2016-2026

File:

```
data/earthquakes_greece_2016_2026.csv
```

---

## Project Structure

```
hawkes-earthquakes/

├── data/
│   └── earthquakes_greece_2016_2026.csv
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_poisson.ipynb
│   ├── 03_hawkes.ipynb
│   └── 04_diagnostics.ipynb
│
└── README.md
```

---

## Notebooks

### 01 - Exploration

* Load and clean earthquake data
* Visualise earthquake occurrence times
* Analyse inter-arrival times
* Identify temporal clustering

---

### 02 - Poisson Process

Build a baseline model:

[
\lambda(t)=\lambda
]

Tasks:

* Estimate earthquake rate
* Simulate Poisson earthquake sequences
* Compare simulated and observed activity

---

### 03 - Hawkes Process

Introduce the self-exciting model:

[
\lambda(t)=\mu+\sum_{t_i<t}\alpha e^{-\beta(t-t_i)}
]

where:

* (\mu): background earthquake rate
* (\alpha): excitation strength
* (\beta): decay rate of aftershock influence

Tasks:

* Implement the likelihood
* Estimate parameters using maximum likelihood
* Analyse earthquake triggering

---

### 04 - Diagnostics

Evaluate the fitted model:

* Compare Poisson vs Hawkes
* Plot fitted intensity
* Perform goodness-of-fit checks
* Compute branching ratio:

[
n=\frac{\alpha}{\beta}
]

---

## Concepts Covered

* Point processes
* Poisson processes
* Conditional intensity
* Maximum likelihood estimation
* Hawkes processes
* Self-excitation
* Model validation
