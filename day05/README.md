# Day 05 Assignment - Electrochemical Nernst Analysis & Regression

## Project Overview
This project provides a Python-based tool for analyzing electrochemical data. It specifically focuses on the **Ferrocene/Ferricenium** redox system:
`FeCp2 ⇌ FeCp2+ + e-`

The application processes experimental data from Excel, performs scientific calculations based on the Nernst equation, and executes a **Linear Regression analysis** to verify Nernstian behavior.

## Key Features
- **Data Processing:** Automated reading of multi-sheet Excel files using `pandas`.
- **Scientific Analysis:** Calculates concentrations of oxidized/reduced species and their log-ratios.
- **Linear Regression:** Uses `scipy.stats` to determine the experimental slope and formal potential ($E^0$).
- **Visualization:** Generates a dual-panel plot (`analysis_plot.png`) showing species distribution and the linearized Nernst plot.
- **Validation:** Includes a `pytest` suite to ensure calculation accuracy and robust file handling.

## Scientific Background
The analysis is governed by the Nernst equation:
`E = E0 + (RT/nF) * ln([Ox]/[Red])`

A plot of `E` vs `log10([Ox]/[Red])` should yield a linear relationship with a theoretical slope of approximately **0.0592 V per decade** at 25°C (for n=1).

## Folder Structure
- `analyze_ferrocene_nernst.py`: Main execution script (Regression & Plotting).
- `nernst_lib.py`: Core library containing electrochemical logic and constants.
- `test_nernst.py`: Automated test suite.
- `ferrocene_nernst_input.xlsx`: Input data file.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.


## AI Usage 
AI tools (ChatGPT) were used to help understand Python syntax, debug errors, improve the program structure, and receive explanations about Python libraries, how to create excel file.


## Installation & Usage
Ensure you have Python installed, then run:
```bash
pip3 install -r requirements.txt
