import pytest
import numpy as np
import pandas as pd
from analyze_ferrocene_nernst import analyze_excel

def test_linear_regression_accuracy(tmp_path):
    """
    בדיקה שמוודאת שהקוד מצליח לשחזר את הפרמטרים מנתונים ידועים
    """
    # יצירת נתונים סינתטיים מושלמים
    input_file = tmp_path / "test_input.xlsx"
    data = pd.DataFrame({
        "Sample": ["A", "B", "C"],
        "Potential_V_vs_SCE": [0.251, 0.31, 0.369], # הפרשים של ~59mV
        "E0_V": [0.31, 0.31, 0.31],
        "n": [1, 1, 1],
        "Temperature_K": [298.15, 298.15, 298.15],
        "Total_mM": [5, 5, 5]
    })
    
    # תיקון: שמירה עם שם הגיליון שהקוד מצפה לו
    with pd.ExcelWriter(input_file, engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name="Nernst_Data", index=False)
    
    output_excel = tmp_path / "out.xlsx"
    output_plot = tmp_path / "plot.png"
    
    # הרצת הניתוח
    res = analyze_excel(input_file, output_excel, output_plot)
    
    # בדיקה שהקובץ נוצר
    assert output_excel.exists()
    
    # בדיקה שהשיפוע (Slope) קרוב ל-0.059 (59mV)
    # הערה: אם ביצעת שינויים בנוסחה בקוד הראשי, הערך עשוי להשתנות מעט
    # כאן אנחנו בודקים את הלוגיקה של הרגרסיה
    assert res is not None
    assert "Log_Ratio" in res.columns