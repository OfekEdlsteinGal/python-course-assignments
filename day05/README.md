# Day 05 Assignment - Excel Electrochemical Nernst Analysis

## Project idea

For this assignment I created a fake Excel file with electrochemical data, because I did not have a real lab file that I could use.

The fake data represents measurements of the ferrocene/ferricenium redox system:

```text
FeCp2 ⇌ FeCp2+ + e-
```

The program reads the Excel file, calculates the concentration of the reduced and oxidized forms using the Nernst equation, creates a graph from all the data, saves the results to a new Excel file, and prints a results summary in the terminal.

## Input file

The input file is:

```text
ferrocene_nernst_input.xlsx
```

The important sheet is:

```text
Nernst_Data
```

The columns are:

- `Sample` - sample name
- `Potential_V_vs_SCE` - measured potential
- `E0_V` - formal potential
- `n` - number of electrons
- `Temperature_K` - temperature in Kelvin
- `Total_mM` - total concentration of ferrocene + ferricenium

## Scientific background

The Nernst equation is:

```text
E = E0 + (RT/nF) ln([Ox]/[Red])
```

For this system:

```text
[Ox] = [FeCp2+]
[Red] = [FeCp2]
```

The program first calculates the ratio:

```text
[Ox]/[Red] = exp((E - E0)nF/RT)
```

Then, because the total concentration is known:

```text
Total = [Ox] + [Red]
```

the program calculates the two concentrations separately.

## Galvanic or electrolytic interpretation

The program also calculates:

```text
Delta E = E - E0
```

Then it gives a simple interpretation:

- if `Delta E > 0`, the situation is written as `galvanic cell / spontaneous`
- if `Delta E < 0`, the situation is written as `electrolytic cell / non-spontaneous`
- if `Delta E = 0`, it is the `equilibrium point`

This is a simplified interpretation for this assignment. In a real electrochemical cell, the full cell potential depends on both half-cells.

## Output files

When the program runs, it creates:

```text
ferrocene_nernst_results.xlsx
ferrocene_nernst_plot.png
```

It also prints a summary of the calculated results in the terminal.

## Files in this folder

- `ferrocene_nernst_input.xlsx` - fake input Excel file
- `nernst_lib.py` - scientific calculation functions
- `analyze_ferrocene_nernst.py` - main program
- `test_nernst.py` - tests
- `requirements.txt` - packages needed
- `README.md` - explanation of the project

## How to run

Install requirements:

```bash
pip3 install -r requirements.txt
```

Run the analysis:

```bash
python3 analyze_ferrocene_nernst.py
```

The terminal should print a summary of the results.

## How to run tests

```bash
pytest
```

## AI usage

AI tools were used to help create the fake Excel data, organize the Python code, add the graph, add the graph and terminal output, write tests, and explain the Nernst equation and the electrochemical interpretation.
