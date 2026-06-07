def classify_band_gap(band_gap):
    if band_gap is None:
        return "unknown"
    if band_gap < 0.1:
        return "metal/conductor"
    if band_gap < 3.0:
        return "semiconductor"
    return "insulator"


def analyze_materials(materials):
    results = []

    for material in materials:
        band_gap = material.get("band_gap_eV")

        results.append({
            "material_id": material.get("material_id"),
            "formula": material.get("formula"),
            "band_gap_eV": band_gap,
            "density_g_cm3": material.get("density_g_cm3"),
            "energy_above_hull_eV_atom": material.get("energy_above_hull_eV_atom"),
            "is_stable": material.get("is_stable"),
            "band_gap_class": classify_band_gap(band_gap),
        })

    return sorted(results, key=lambda x: x["energy_above_hull_eV_atom"])