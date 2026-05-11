from pathlib import Path

import pandas as pd
import pytest

from nernst_lib import (
    oxidized_reduced_ratio,
    redox_concentrations,
    classify_region,
    delta_e,
    classify_cell_type,
)
from analyze_ferrocene_nernst import analyze_excel


def test_ratio_when_e_equals_e0():
    ratio = oxidized_reduced_ratio(0.31, 0.31, 1, 298.15)
    assert ratio == pytest.approx(1.0)


def test_redox_concentrations_when_ratio_is_one():
    reduced, oxidized, ratio = redox_concentrations(0.31, 0.31, 1, 298.15, 2.0)

    assert ratio == pytest.approx(1.0)
    assert reduced == pytest.approx(1.0)
    assert oxidized == pytest.approx(1.0)


def test_ratio_increases_when_potential_increases():
    low_ratio = oxidized_reduced_ratio(0.25, 0.31, 1, 298.15)
    high_ratio = oxidized_reduced_ratio(0.40, 0.31, 1, 298.15)

    assert high_ratio > low_ratio


def test_classify_region():
    assert classify_region(0.20, 0.31) == "mostly reduced"
    assert classify_region(0.31, 0.31) == "mixed redox region"
    assert classify_region(0.40, 0.31) == "mostly oxidized"


def test_delta_e():
    assert delta_e(0.40, 0.31) == pytest.approx(0.09)


def test_cell_type():
    assert classify_cell_type(0.40, 0.31) == "galvanic cell / spontaneous"
    assert classify_cell_type(0.20, 0.31) == "electrolytic cell / non-spontaneous"
    assert classify_cell_type(0.31, 0.31) == "equilibrium point"


def test_bad_inputs():
    with pytest.raises(ValueError):
        oxidized_reduced_ratio(0.31, 0.31, 0, 298.15)

    with pytest.raises(ValueError):
        oxidized_reduced_ratio(0.31, 0.31, 1, -10)

    with pytest.raises(ValueError):
        redox_concentrations(0.31, 0.31, 1, 298.15, 0)


def test_analyze_excel_creates_files(tmp_path):
    input_file = tmp_path / "input.xlsx"
    output_excel = tmp_path / "results.xlsx"
    output_plot = tmp_path / "plot.png"

    data = pd.DataFrame({
        "Sample": ["s1", "s2"],
        "Potential_V_vs_SCE": [0.31, 0.40],
        "E0_V": [0.31, 0.31],
        "n": [1, 1],
        "Temperature_K": [298.15, 298.15],
        "Total_mM": [1.0, 1.0],
    })

    with pd.ExcelWriter(input_file, engine="openpyxl") as writer:
        data.to_excel(writer, sheet_name="Nernst_Data", index=False)

    result_df = analyze_excel(
        input_file,
        output_excel,
        output_plot
    )

    assert output_excel.exists()
    assert output_plot.exists()
    assert len(result_df) == 2
    assert "Cell_Type" in result_df.columns
    assert result_df.loc[0, "Cell_Type"] == "equilibrium point"
    assert result_df.loc[1, "Cell_Type"] == "galvanic cell / spontaneous"
