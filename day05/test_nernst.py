from pathlib import Path

import pytest

from nernst_lib import oxidized_reduced_ratio, redox_concentrations, classify_region
from analyze_ferrocene_nernst import analyze_excel


def test_when_e_equals_e0_concentrations_are_equal():
    reduced, oxidized, ratio = redox_concentrations(
        potential_v=0.31,
        e0_v=0.31,
        n=1,
        temperature_k=298.15,
        total_conc_mm=5
    )

    assert ratio == pytest.approx(1.0)
    assert reduced == pytest.approx(2.5)
    assert oxidized == pytest.approx(2.5)


def test_high_potential_gives_more_oxidized_species():
    reduced, oxidized, ratio = redox_concentrations(
        potential_v=0.60,
        e0_v=0.31,
        n=1,
        temperature_k=298.15,
        total_conc_mm=5
    )

    assert oxidized > reduced
    assert ratio > 1


def test_low_potential_gives_more_reduced_species():
    reduced, oxidized, ratio = redox_concentrations(
        potential_v=0.00,
        e0_v=0.31,
        n=1,
        temperature_k=298.15,
        total_conc_mm=5
    )

    assert reduced > oxidized
    assert ratio < 1


def test_classify_region():
    assert classify_region(0.20, 0.31) == "mostly reduced"
    assert classify_region(0.31, 0.31) == "mixed redox region"
    assert classify_region(0.50, 0.31) == "mostly oxidized"


def test_bad_inputs():
    with pytest.raises(ValueError):
        oxidized_reduced_ratio(0.31, 0.31, 0, 298.15)

    with pytest.raises(ValueError):
        redox_concentrations(0.31, 0.31, 1, 298.15, 0)


def test_analyze_excel_creates_results(tmp_path):
    input_file = Path("ferrocene_nernst_input.xlsx")
    output_excel = tmp_path / "results.xlsx"
    output_plot = tmp_path / "plot.png"

    result_df = analyze_excel(input_file, output_excel, output_plot)

    assert len(result_df) > 0
    assert output_excel.exists()
    assert output_plot.exists()

    closest_index = (result_df["Potential_V_vs_SCE"] - 0.31).abs().idxmin()
    closest_row = result_df.loc[closest_index]
    assert closest_row["FeCp2_reduced_mM"] == pytest.approx(2.5, abs=0.8)
    assert closest_row["FeCp2_plus_oxidized_mM"] == pytest.approx(2.5, abs=0.8)
