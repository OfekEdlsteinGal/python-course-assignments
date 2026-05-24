import pandas as pd
import matplotlib.pyplot as plt
from mp_api.client import MPRester


def material_to_dict(doc):
    return {
        "material_id": str(doc.material_id),
        "formula": doc.formula_pretty,
        "band_gap_eV": doc.band_gap,
        "density_g_cm3": doc.density,
        "energy_above_hull_eV_atom": doc.energy_above_hull,
        "is_stable": doc.is_stable,
    }


def classify_band_gap(band_gap):
    if band_gap is None:
        return "unknown"
    if band_gap < 0.1:
        return "metal/conductor"
    if band_gap < 3.0:
        return "semiconductor"
    return "insulator"


# Paste your Materials Project API key here
API_KEY = "X2ukUPKYyONkbM0bws8FmEcWGpqKD2OJ"


fields = [
    "material_id",
    "formula_pretty",
    "band_gap",
    "density",
    "energy_above_hull",
    "is_stable",
]


with MPRester(API_KEY) as mpr:
    docs = mpr.materials.summary.search(
        elements=["Li", "O"],
        fields=fields,
        num_chunks=1,
        chunk_size=100,
    )


# Convert to DataFrame
materials_data = [material_to_dict(doc) for doc in docs]
df = pd.DataFrame(materials_data)


# Process data
df["band_gap_class"] = df["band_gap_eV"].apply(classify_band_gap)

# Sort by stability
# Lower energy_above_hull means more stable
sorted_df = df.sort_values(by="energy_above_hull_eV_atom")


# Save CSV
sorted_df.to_csv("materials_project_results.csv", index=False)


# Print summary
print("\nMaterials Project Li-O Data Analysis")
print("-----------------------------------")
print(f"Number of materials downloaded: {len(sorted_df)}")
print(f"Number of stable materials: {sorted_df['is_stable'].sum()}")

print("\nBand gap classification:")
print(sorted_df["band_gap_class"].value_counts())

print("\n10 most stable materials:")
print(
    sorted_df[
        [
            "material_id",
            "formula",
            "band_gap_eV",
            "band_gap_class",
            "energy_above_hull_eV_atom",
            "is_stable",
        ]
    ].head(10)
)


# Create plot
plt.figure()
sorted_df["band_gap_eV"].dropna().hist(bins=20)
plt.xlabel("Band gap (eV)")
plt.ylabel("Number of materials")
plt.title("Band gap distribution for Li-O materials")
plt.tight_layout()
plt.savefig("materials_project_bandgap_plot.png", dpi=300)

print("\nSaved:")
print("- materials_project_results.csv")
print("- materials_project_bandgap_plot.png")
