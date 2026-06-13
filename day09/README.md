# Day 09 – Solubility Prediction Using Machine Learning

## Overview

This project uses the Delaney Solubility Dataset (ESOL) from MoleculeNet to predict aqueous solubility of small molecules using machine learning.

The goal is to build a regression model that predicts:

Measured Log Solubility (mol/L)

from molecular descriptors.

## Dataset

Dataset:

delaney-processed.csv

Source:

https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/delaney-processed.csv

The dataset contains experimental solubility measurements together with molecular descriptors.

## Features Used

* MolWt
* MolLogP
* NumRotatableBonds
* AromaticProportion

Target:

* measured log solubility in mols per litre

## Installation

Create a virtual environment:

python -m venv venv

Activate:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run

Download:

delaney-processed.csv

Place it in the project directory.

Run:

python solubility_prediction.py

## Output

The script generates:

* solubility_predictions.csv
* solubility_plot.png
* solubility_model.pkl

It also prints:

* R²
* MAE
* RMSE

## Machine Learning Model

RandomForestRegressor

Parameters:

* n_estimators = 200
* random_state = 42

## AI Usage

ChatGPT was used to:

* Help select a suitable dataset
* Design the machine learning workflow
* Generate the initial Python implementation
* Explain model evaluation metrics
* Assist with debugging and project documentation

# Prompts Used

Prompt 1:
Create a Python project that predicts molecular solubility using the Delaney ESOL dataset.

Prompt 2:
Help debug Python code and explain the meaning of R², MAE, and RMSE.
