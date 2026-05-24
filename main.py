import os
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_electrochemistry_data():
    """
    Simulates fetching standardized electrochemical reduction potentials (E0 in Volts) 
    and parameters from a thermodynamic reference database (like NIST / PubChem) 
    for common battery and galvanic cell couples.
    """
    print("[*] Fetching electrochemical reference data from database parameters...")
    
    # Standard Reduction Potentials (E0) at 298.15 K vs SHE (Standard Hydrogen Electrode)
    database_records = {
        "Lithium (Li+/Li)": {"E0": -3.040, "n": 1, "type": "Anode Material"},
        "Zinc (Zn2+/Zn)": {"E0": -0.763, "n": 2, "type": "Anode Material"},
        "Hydrogen (H+/H2)": {"E0": 0.000, "n": 2, "type": "Reference"},
        "Copper (Cu2+/Cu)": {"E0": 0.337, "n": 2, "type": "Cathode Material"},
        "Oxygen (O2/H2O)": {"E0": 1.229, "n": 4, "type": "Cathode Material"},
        "Fluorine (F2/F-)": {"E0": 2.870, "n": 2, "type": "Cathode Material"}
    }
    
    df = pd.DataFrame.from_dict(database_records, orient='index')
    df.index.name = "Redox Couple"
    return df.reset_index()

def calculate_cell_potential(df, anode_name, cathode_name):
    """
    Calculates the Standard Cell Potential (E0_cell) and models the 
    Nernst Equation behavior across varying concentration ratios.
    """
    anode = df[df["Redox Couple"] == anode_name].iloc[0]
    cathode = df[df["Redox Couple"] == cathode_name].iloc[0]
    
    E0_anode = anode["E0"]
    E0_cathode = cathode["E0"]
    
    # E0_cell = E0_cathode - E0_anode
    E0_cell = E0_cathode - E0_anode
    n = min(anode["n"], cathode["n"]) # Number of transferred electrons
    
    print(f"\n[✓] Selected Cell Setup:")
    print(f"    - Anode: {anode_name} (E0 = {E0_anode} V)")
    print(f"    - Cathode: {cathode_name} (E0 = {E0_cathode} V)")
    print(f"    - Standard Cell Potential (E0_cell): {E0_cell:.3f} V")
    
    # Processing Nernst Equation over a range of Reaction Quotients (Q = [Products]/[Reactants])
    # E_cell = E0_cell - (R*T / n*F) * ln(Q)
    # At 25 C (298.15 K): E_cell = E0_cell - (0.0592 / n) * log10(Q)
    
    q_values = np.logspace(-3, 3, 100) # Q values from 0.001 to 1000
    e_cell_values = E0_cell - (0.0592 / n) * np.log10(q_values)
    
    nernst_df = pd.DataFrame({
        "Reaction_Quotient_Q": q_values,
        "Cell_Potential_V": e_cell_values
    })
    
    return E0_cell, nernst_df, f"{anode_name} || {cathode_name}"

def generate_plots(nernst_df, cell_label, E0_cell):
    """
    Generates an electrochemical cell behavior chart.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(nernst_df["Reaction_Quotient_Q"], nernst_df["Cell_Potential_V"], 
             color='emerald' if 'emerald' in plt.colormaps else 'darkgreen', linewidth=2.5, label='Nernst Curve')
    
    plt.axhline(y=E0_cell, color='red', linestyle='--', alpha=0.7, label=f'Standard Potential (E° = {E0_cell:.3f} V)')
    
    plt.xscale('log')
    plt.title(f'Electrochemical Cell Potential vs Concentration Ratio (Q)\nCell: {cell_label}', fontsize=14)
    plt.xlabel('Reaction Quotient (Q = [Anode Ions] / [Cathode Ions]) - Log Scale', fontsize=11)
    plt.ylabel('Cell Voltage (V)', fontsize=11)
    plt.grid(True, which="both", linestyle='--', alpha=0.5)
    plt.legend()
    
    output_plot = 'nernst_voltage_profile.png'
    plt.savefig(output_plot, dpi=300)
    print(f"\n[✓] Electrochemical analysis plot saved as '{output_plot}'")

if __name__ == "__main__":
    print("=== ELECTROCHEMISTRY DATABASE PARSER & SIMULATOR ===")
    
    # 1. Fetch data
    electro_df = get_electrochemistry_data()
    print("\n[*] Available Electrochemical Couples from Database:")
    print(electro_df.to_string(index=False))
    
    # 2. Process Data (Simulating a classic Zinc-Copper Daniell Cell, or change to Lithium-Oxygen!)
    anode_choice = "Zinc (Zn2+/Zn)"
    cathode_choice = "Copper (Cu2+/Cu)"
    
    E0_cell, nernst_results, cell_name = calculate_cell_potential(electro_df, anode_choice, cathode_choice)
    
    # 3. Analyze and Plot
    generate_plots(nernst_results, cell_name, E0_cell)