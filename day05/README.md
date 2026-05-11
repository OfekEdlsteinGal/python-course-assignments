# Day 05 Assignment - Ferrocene Nernst Analysis

## Project idea

For this assignment I did not have a real lab data file that I could use, so I created a fake but reasonable Excel file based on an electrochemistry example.

The system is the ferrocene/ferricenium redox couple:

```text
FeCp2 ⇌ FeCp2+ + e-
```

The goal is to calculate how the equilibrium concentration of the reduced species, FeCp2, and the oxidized species, FeCp2+, changes when the cell potential changes.

This is useful because in electrochemistry we can use the measured potential to understand the ratio between the oxidized and reduced forms of a molecule.

## Input file

The input file is:

```text
ferrocene_nernst_input.xlsx
```

The Excel file contains:

- A `Dashboard` sheet that looks similar to the lecture slide.
- A `Constants` sheet with the values used in the calculation.
- A `Nernst_Data` sheet with potentials and calculated redox concentrations.

The fake experiment is:

- Total ferrocene concentration = 5 mM
- E° of ferrocene = +0.31 V vs SCE
- n = 1 electron
- Temperature = 25 °C = 298.15 K

## Scientific background

The Nernst equation is:

```text
Ecell = E°cell − (RT/nF) ln([Red]/[Ox])
```

For this assignment:

```text
Ecell = E°cell − (RT/nF) ln([FeCp2]/[FeCp2+])
```

I rearranged the equation to calculate the ratio between oxidized and reduced species:

```text
[Ox]/[Red] = exp((E − E°) nF / RT)
```

Because the total concentration is 5 mM:

```text
Total = [Red] + [Ox]
```

So the code calculates:

```text
[Red] = Total / (1 + ratio)
[Ox] = Total * ratio / (1 + ratio)
```

When:

```text
Ecell = E°cell
```

then:

```text
[Red] = [Ox]
```

So for a total concentration of 5 mM:

```text
[FeCp2] = 2.5 mM
[FeCp2+] = 2.5 mM
```

## Files in this folder

- `ferrocene_nernst_input.xlsx` - Excel input file with fake electrochemical data and a dashboard.
- `analyze_ferrocene_nernst.py` - main program that reads the Excel file, calculates results, and creates output.
- `nernst_lib.py` - library file with the Nernst equation functions.
- `test_nernst.py` - tests for the calculation and the Excel analysis.
- `requirements.txt` - Python packages needed.
- `ferrocene_nernst_results.xlsx` - output Excel file created by the program.
- `ferrocene_nernst_plot.png` - output graph created by the program.

## How to run the program

Install requirements:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python3 analyze_ferrocene_nernst.py
```

Run the tests:

```bash
pytest
```

## What the program does

The program reads the potential values from the Excel file.  
For every potential, it calculates the ratio:

```text
[FeCp2+]/[FeCp2]
```

Then it calculates the concentration of both species:

```text
[FeCp2]
[FeCp2+]
```

Finally, it creates:

- an Excel results file
- a graph that shows how the concentration changes with potential

## AI usage

AI tools were used to help create the fake electrochemical Excel dataset, write the Python code, organize the project files, create tests, and write the README. AI was also used to help explain the Nernst equation and to make the Excel file look similar to the lecture slide.
