# Gibbs Free Energy Calculator

## Overview

This project is a computational tool designed to calculate the Gibbs Free Energy (ΔG) of a system using the thermodynamic equation:

ΔG = ΔH - TΔS

This calculation helps determine whether a process is spontaneous or not.

---

## Structure

* **gibbs_lib.py**: This file contains the main calculation logic (Shared Library).
* **main_input.py**: Interactive terminal version using user input.
* **main_cli.py**: Command-line argument version using `sys.argv`.
* **main_gui.py**: Graphical User Interface (Tkinter).
* **test_gibbs.py**: Verification test cases.
* *(Optional)* initial version of the script (if you had one in day02).

---

## How to Use

### main_input.py

Run:

```
python main_input.py
```

The program will ask:

* Enter ΔH
* Enter T
* Enter ΔS

After entering the values, it will calculate and display ΔG.

---

### main_cli.py

Run:

```
python main_cli.py 10 300 0.05
```

Where:

* 10 = ΔH
* 300 = T
* 0.05 = ΔS

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
* Design test cases
* Organize the project structure
