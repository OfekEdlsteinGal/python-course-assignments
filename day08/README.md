# Day 08 – Materials Project Web Application

## Overview

This project is a web application built with FastAPI based on the Materials Project analysis assignment from Day 06.

The application analyzes material properties and classifies materials according to their band gap values.

The project separates the business logic from the web layer, allowing the same functions to be used both by the application and by the automated tests.

---

## Features

* Analyze material data
* Classify materials as:

  * Metal / Conductor
  * Semiconductor
  * Insulator
* REST API built with FastAPI
* Automated tests using pytest

---

## Project Structure

```text
day08/
│
├── app.py
├── materials_logic.py
├── test_app.py
├── test_logic.py
├── requirements.txt
└── README.md
```

---

## Business Logic

The business logic is implemented in `materials_logic.py`.

Main functions:

* `classify_band_gap()`
* `analyze_materials()`

These functions are used both by the FastAPI application and by the test suite.

---

## Installation

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

```bash
pytest
```

Expected output:

```text
3 passed
```

---

## Running the Web Application

Start the FastAPI server:

```bash
python3 -m uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to access the interactive API documentation.

---

## Example Request

POST `/analyze`

```json
[
  {
    "material_id": "mp-1",
    "formula": "Li2O",
    "band_gap_eV": 4.2,
    "density_g_cm3": 2.1,
    "energy_above_hull_eV_atom": 0.0,
    "is_stable": true
  }
]
```

Example response:

```json
{
  "number_of_materials": 1,
  "results": [
    {
      "material_id": "mp-1",
      "formula": "Li2O",
      "band_gap_eV": 4.2,
      "density_g_cm3": 2.1,
      "energy_above_hull_eV_atom": 0.0,
      "is_stable": true,
      "band_gap_class": "insulator"
    }
  ]
}
```


# AI Prompts Used

ChatGPt help me convert my Materials Project analysis code into a FastAPI web application, separate business logic from web routes.
