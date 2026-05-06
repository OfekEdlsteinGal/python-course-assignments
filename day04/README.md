# Gibbs Free Energy Calculator

## Overview

This project is a computational tool designed to calculate the Gibbs Free Energy (ΔG) of a system using the thermodynamic equation:

ΔG = ΔH - TΔS

Where:
- ΔG = Gibbs Free Energy (kJ/mol)
- ΔH = Enthalpy change (kJ/mol)
- T = Temperature (K)
- ΔS = Entropy change (J/mol·K)

The program converts entropy from J to kJ and then calculates ΔG.
Since ΔS is typically given in J/mol·K, the program converts it to kJ/mol·K before performing the calculation.

The program also determines whether the reaction is:
- Spontaneous (ΔG < 0)
- Non-spontaneous (ΔG > 0)
- At equilibrium (ΔG = 0)

---

## Structure

* **gibbs_lib.py**: This file contains the main calculation logic (Shared Library).
* **main_input.py**: Interactive terminal version using user input.
* **main_cli.py**: Command-line argument version using `sys.argv`.
* **main_gui.py**: Graphical User Interface (Tkinter).
* **test_gibbs.py**: Verification test cases.
---

## How to Use

### main_input.py

Run:

```
python main_input.py
```

The program will ask:

* Enter enthalpy change ΔH (in kJ/mol)
* Enter temperature (in Kelvin)
* Enter entropy change ΔS (in J/mol·K)

After entering the values, it will calculate and display ΔG and determines whether the reaction is spontaneous or not.


---

### main_cli.py

Run:

```
python main_cli.py 10 300 0.05
```

Where:

* ΔH=10
* T=300
* ΔS=0.05 

The program will output the calculated ΔG.

---

### main_gui.py

Run:

```
python main_gui.py
```

A window will open:

* Enter values in the fields
* Click "Calculate"
* The result (ΔG) will be displayed

---

## Testing

Run:

```
python test_gibbs.py
```

If everything works correctly, you should see:

```
Tests passed
```

---

## AI Interaction

I used ChatGPT to help structure the project and understand how to separate the business logic from the user interface.


ChatGPT helped me:

* Create a shared library file
* Build three versions of the program (input, CLI, GUI)
