# Day 6 Assignment - Materials Project API

## Project idea

This project uses the **Materials Project** database, which is a web-based scientific database for materials science. It is similar in spirit to databases like NCBI or OpenWeatherMap because it gives programmatic access to real data through an API.

The Materials Project provides calculated and curated information about inorganic materials. Examples of available data include chemical formula, crystal structure, band gap, density, thermodynamic stability, formation energy, phase diagrams, electronic structure, and other properties that are useful in chemistry, physics, materials science, and electrochemistry.

In this assignment, I chose to download data about materials that contain **lithium and oxygen**. This is relevant to my field because lithium-containing oxides are important in batteries, electrochemistry, and energy materials.

## What the program does

The Python program connects to the Materials Project API and downloads summary data for Li-O materials.

For each material, the program downloads:

- Materials Project ID
- Chemical formula
- Band gap
- Density
- Energy above hull
- Whether the material is stable

Then the program processes the data by:

1. Saving the downloaded data into a CSV file.
2. Classifying each material as:
   - metal/conductor
   - semiconductor
   - insulator
3. Sorting materials by thermodynamic stability.
4. Printing the 10 most stable materials.
5. Calculating summary statistics.
6. Creating a histogram plot of the band gap distribution.

## How to run

First install the required packages:

```bash
pip install -r requirements.txt
```

Then create a `.env` file in the same folder:

```bash
MP_API_KEY=your_api_key_here
```

Run the program:

```bash
python materials_project_analysis.py
```

The program will create:

- `materials_project_results.csv`
- `materials_project_bandgap_plot.png`

## Files in this project

- `materials_project_analysis.py` - main Python program
- `requirements.txt` - required Python packages
- `.env.example` - example file showing where to put the API key
- `.gitignore` - prevents private/API/cache files from being uploaded to GitHub
- `README.md` - project explanation

## AI usage

I used Gemini and ChatGPT. AI tools were used to help choose a scientific database, understand how to use the Materials Project API, plan the structure of the Python program, debug the logic, improve the README, and explain the scientific meaning of the downloaded data. AI was also used to help organize the project files in a clear way and make the code easier to understand.
