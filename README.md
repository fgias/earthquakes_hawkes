# Hawkes Process Modelling of Earthquakes in Greece

## Overview

This project studies earthquake occurrence in Greece using
temporal point processes.

The main goal is to investigate whether earthquake activity is
better explained by independent events or by self-exciting
aftershock processes.

The project compares:

- Homogeneous Poisson process
- Hawkes self-exciting process
- Marked Hawkes process
- ETAS (Epidemic Type Aftershock Sequence) model

The final model includes:

- earthquake clustering
- magnitude-dependent triggering
- realistic aftershock decay following Omori's law

---

## Environment Setup

Create the conda environment:

```bash
mamba create -n hawkes-earthquakes python=3.12 numpy pandas matplotlib scipy jupyter seaborn
````

Activate the environment:

```bash
mamba activate hawkes-earthquakes
```

Install the project in editable mode:

```bash
pip install -e .
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

Period:

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
├── src/
│   └── hawkes.py
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_poisson.ipynb
│   ├── 03_hawkes.ipynb
│   ├── 04_diagnostics.ipynb
│   ├── 05_hawkes_gof.ipynb
│   ├── 06_marked_hawkes.ipynb
│   └── 07_etas.ipynb
│
└── README.md
```

---

# Notebooks

## 01 - Exploration

Data exploration and preprocessing.

Tasks:

* Load and clean earthquake catalogue
* Analyse earthquake magnitudes
* Visualise earthquake occurrence times
* Study inter-arrival times
* Identify clustering behaviour

---

## 02 - Poisson Process

Build a baseline model:

[
\lambda(t)=\lambda
]

Assumption:

> Earthquakes occur independently with a constant rate.

Tasks:

* Estimate earthquake rate
* Compute Poisson likelihood
* Simulate earthquake sequences
* Compare simulated and observed activity

---

## 03 - Hawkes Process

Introduce self-excitation:

[
\lambda(t)=
\mu+
\sum_{t_i<t}
\alpha e^{-\beta(t-t_i)}
]

Parameters:

* (\mu): background seismic activity
* (\alpha): earthquake triggering strength
* (\beta): decay rate of aftershock influence

Tasks:

* Derive and implement likelihood
* Fit parameters using maximum likelihood
* Estimate branching ratio:

[
n=\frac{\alpha}{\beta}
]

---

## 04 - Model Comparison

Compare Poisson and Hawkes models.

Metrics:

* Log likelihood
* AIC
* BIC
* Simulated earthquake sequences

Conclusion:

Hawkes models explain earthquake clustering much better than
independent Poisson processes.

---

## 05 - Marked Hawkes Process

Extend Hawkes by including earthquake magnitude.

Events become:

[
(t_i,M_i)
]

Model:

[
\lambda(t)=
\mu+
\sum_i
K e^{a(M_i-M_0)}
e^{-\beta(t-t_i)}
]

Parameters:

* (K): base triggering strength
* (a): magnitude influence
* (\beta): temporal decay

Main result:

Large earthquakes create disproportionately more aftershocks.

---

## 06 - Marked Hawkes Diagnostics

Validate the model using the time-rescaling theorem.

For a correct model:

[
z_i=
\int_{t_{i-1}}^{t_i}
\lambda(t)dt
]

should follow:

[
z_i\sim Exp(1)
]

Diagnostics:

* Histogram comparison
* QQ plot
* Kolmogorov-Smirnov test

---

## 07 - ETAS Model

Final earthquake model:

Epidemic Type Aftershock Sequence (ETAS).

The model combines:

* background seismicity
* magnitude-dependent triggering
* realistic aftershock decay

Model:

[
\lambda(t)=
\mu+
\sum_i
K e^{a(M_i-M_0)}
\frac{1}{(t-t_i+c)^p}
]

Parameters:

* (\mu): background earthquake rate
* (K): triggering strength
* (a): magnitude scaling
* (c): short-time cutoff
* (p): Omori decay exponent

---

## Final Model Evaluation

All models are compared using:

### Likelihood

Higher is better.

### AIC / BIC

Lower is better.

### Time-rescaling diagnostics

A good model should produce:

[
z_i\sim Exp(1)
]

Evaluated with:

* mean and variance of transformed intervals
* histogram comparison
* QQ plot
* KS test

---

# Results Summary

Model progression:

```
Poisson
    |
    | adds earthquake clustering
    v
Hawkes
    |
    | adds magnitude effects
    v
Marked Hawkes
    |
    | adds realistic aftershock decay
    v
ETAS
```

Final ETAS model achieved:

* highest likelihood
* lowest AIC/BIC
* best goodness-of-fit among tested models

The project demonstrates how increasingly realistic point-process
models improve earthquake modelling by capturing:

* temporal clustering
* aftershock triggering
* magnitude dependence
* long-memory earthquake sequences

---

## Concepts Covered

* Point processes
* Conditional intensity
* Poisson processes
* Maximum likelihood estimation
* Hawkes processes
* Marked point processes
* ETAS models
* Omori's law
* Model selection (AIC/BIC)
* Time-rescaling theorem
* Goodness-of-fit testing

