from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from nernst_lib import redox_concentrations, classify_region


def analyze_excel(input_file, output_excel, output_plot):
    """
    Read the Excel input file, calculate redox concentrations from the
    Nernst equation, save an Excel results file and a graph.
    """
    df = pd.read_excel(input_file, sheet_name="Nernst_Data")

    results = []
    for _, row in df.iterrows():
        potential = float(row["Potential_V_vs_SCE"])
        e0 = float(row["E0_V"])
        n = int(row["n"])
        temperature = float(row["Temperature_K"])
        total = float(row["Total_mM"])

        reduced, oxidized, ratio = redox_concentrations(
            potential,
            e0,
            n,
            temperature,
            total
        )

        results.append({
            "Potential_V_vs_SCE": potential,
            "FeCp2_reduced_mM": reduced,
            "FeCp2_plus_oxidized_mM": oxidized,
            "Ox_Red_ratio": ratio,
            "Interpretation": classify_region(potential, e0)
        })

    result_df = pd.DataFrame(results)

    with pd.ExcelWriter(output_excel) as writer:
        result_df.to_excel(writer, sheet_name="Calculated_Results", index=False)

    plt.figure(figsize=(8, 5))
    plt.plot(result_df["Potential_V_vs_SCE"], result_df["FeCp2_reduced_mM"], marker="o", label="FeCp2 reduced")
    plt.plot(result_df["Potential_V_vs_SCE"], result_df["FeCp2_plus_oxidized_mM"], marker="o", label="FeCp2+ oxidized")
    plt.axvline(x=0.31, linestyle="--", label="E0 = 0.31 V")
    plt.xlabel("Potential (V vs SCE)")
    plt.ylabel("Concentration (mM)")
    plt.title("Ferrocene/Ferricenium equilibrium from the Nernst equation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_plot)
    plt.close()

    return result_df


if __name__ == "__main__":
    input_file = Path("ferrocene_nernst_input.xlsx")
    output_excel = Path("ferrocene_nernst_results.xlsx")
    output_plot = Path("ferrocene_nernst_plot.png")

    result_df = analyze_excel(input_file, output_excel, output_plot)

    print("Analysis finished.")
    print("Created:", output_excel)
    print("Created:", output_plot)
    print()
    print(result_df.head())
