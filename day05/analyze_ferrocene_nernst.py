from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from nernst_lib import (
    redox_concentrations,
    classify_region,
    delta_e,
    classify_cell_type,
)


def analyze_excel(input_file, output_excel, output_plot):
    """
    Read the Excel input file, calculate redox concentrations from the
    Nernst equation, save an Excel results file, and create a graph.
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

        sample_name = row["Sample"] if "Sample" in df.columns else f"sample_{len(results) + 1}"
        de = delta_e(potential, e0)

        results.append({
            "Sample": sample_name,
            "Potential_V_vs_SCE": potential,
            "E0_V": e0,
            "Delta_E_V": de,
            "FeCp2_reduced_mM": reduced,
            "FeCp2_plus_oxidized_mM": oxidized,
            "Ox_Red_ratio": ratio,
            "Redox_Interpretation": classify_region(potential, e0),
            "Cell_Type": classify_cell_type(potential, e0),
        })

    result_df = pd.DataFrame(results)

    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        result_df.to_excel(writer, sheet_name="Calculated_Results", index=False)

    create_graph(result_df, output_plot)

    return result_df


def create_graph(result_df, output_plot):
    """
    Create one graph from all data points in the Excel file.
    """
    plt.figure(figsize=(9, 5.5))

    plt.plot(
        result_df["Potential_V_vs_SCE"],
        result_df["FeCp2_reduced_mM"],
        marker="o",
        label="FeCp2 reduced"
    )

    plt.plot(
        result_df["Potential_V_vs_SCE"],
        result_df["FeCp2_plus_oxidized_mM"],
        marker="o",
        label="FeCp2+ oxidized"
    )

    plt.axvline(
        x=result_df["E0_V"].iloc[0],
        linestyle="--",
        label="E0"
    )

    plt.xlabel("Potential (V vs SCE)")
    plt.ylabel("Concentration (mM)")
    plt.title("Ferrocene/Ferricenium concentrations from the Nernst equation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_plot, dpi=200)
    plt.close()


if __name__ == "__main__":
    input_file = Path("ferrocene_nernst_input.xlsx")
    output_excel = Path("ferrocene_nernst_results.xlsx")
    output_plot = Path("ferrocene_nernst_plot.png")

    result_df = analyze_excel(
        input_file,
        output_excel,
        output_plot
    )

    print("Analysis finished successfully.")
    print("Created:", output_excel)
    print("Created:", output_plot)
    print()
    print("Summary of calculated results:")
    print(result_df.to_string(index=False))
