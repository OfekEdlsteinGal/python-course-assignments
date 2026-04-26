# Gibbs Free Energy Calculator

## Description
This program calculates the Gibbs Free Energy (ΔG) of a reaction using the thermodynamic equation:

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

## How to Run
Run the Python file and enter the required values when prompted.

---

## Sample Input

Enter enthalpy change ΔH (in kJ/mol): -50  
Enter entropy change ΔS (in J/mol·K): 100  
Enter temperature (in Kelvin): 298  

---

## Sample Output

ΔG = -79.8 kJ/mol  
The reaction is spontaneous.

---

## AI Usage
This assignment was created using ChatGPT (OpenAI).

Prompt used:
"Create a Python program that calculates Gibbs free energy using user input and include a README file with explanation and sample input/output."
