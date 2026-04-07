# Statistical Engineering Project

## Overview
This project builds a pure Python statistical engine (StatEngine) to analyze 1D numerical data and perform statistical calculations. It also includes a Monte Carlo simulation to model server crashes, demonstrating the Law of Large Numbers (LLN).

## Key features:

- Compute central tendency (mean, median, mode)
- Measure dispersion (variance, standard deviation)
- Detect outliers
- Simulate probabilistic events with large datasets

## Mathematical Logic

### Mean
Sum of values divided by number of values.

### Median
- Odd number of elements: middle value
- Even number of elements: average of the two middle values

### Variance
- Population: sum((x - mean)^2) / n
- Sample: sum((x - mean)^2) / (n - 1)

### Standard Deviation
Square root of variance.
## Setup Instructions
Clone the repository:
- git clone <your-repo-link>
Navigate to the project folder:
- cd statistical_engine
Run the main analysis:
- python main.py


## ✅ Acceptance Criteria Checklist

### 🔹 Data Validation & Error Handling
- [x] Passes **empty dataset handling** (raises ValueError)
- [x] Handles **invalid data types** (e.g., strings, None) with clear TypeError
- [x] Prevents **division by zero errors**

### 🔹 Central Tendency
- [x] Correctly calculates **mean**
- [x] Correctly calculates **median for odd-length datasets**
- [x] Correctly calculates **median for even-length datasets**
- [x] Correctly computes **mode**
- [x] Supports **multimodal distributions** (returns multiple modes)
- [x] Returns message when **no mode exists (all values unique)**

### 🔹 Dispersion Measures
- [x] Correctly calculates **population variance (n)**
- [x] Correctly calculates **sample variance (n-1, Bessel’s correction)**
- [x] Correctly computes **standard deviation from variance**

### 🔹 Outlier Detection
- [x] Detects outliers using **standard deviation threshold**
- [x] Handles case where **standard deviation = 0** (no false outliers)

### 🔹 Monte Carlo Simulation
- [x] Simulates probability using **random module**
- [x] Produces results consistent with **Law of Large Numbers**
- [x] Handles **invalid input (e.g., days ≤ 0)**

### 🔹 Code Quality & Structure
- [x] Code is **modular** (separated into src, tests, main)
- [x] Functions are **reusable and well-structured**
- [x] Uses only **Python standard libraries**

### 🔹 Testing
- [x] Unit tests verify **mean, median (odd/even), standard deviation**
- [x] Tests include **error handling cases**
- [x] All tests run successfully using `unittest`