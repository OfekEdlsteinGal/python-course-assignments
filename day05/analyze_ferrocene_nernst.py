import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import linregress
from nernst_lib import redox_concentrations, delta_e

def analyze_excel(input_file, output_excel, output_plot):
    # קריאת נתוני המעבדה מקובץ האקסל
    df = pd.read_excel(input_file, sheet_name="Nernst_Data")

    results = []
    for _, row in df.iterrows():
        # חילוץ פרמטרים מכל שורה
        potential = float(row["Potential_V_vs_SCE"])
        e0 = float(row["E0_V"])
        n = int(row["n"])
        temp = float(row["Temperature_K"])
        total = float(row["Total_mM"])

        # חישוב ריכוזים על בסיס משוואת נרנסט (מתוך הספרייה)
        red, ox, ratio = redox_concentrations(potential, e0, n, temp, total)
        
        results.append({
            "Sample": row["Sample"] if "Sample" in df.columns else "Unknown",
            "Potential_V": potential,
            "Log_Ratio": np.log10(ratio), # נדרש לרגרסיה ליניארית
            "FeCp2_reduced_mM": red,
            "FeCp2_plus_oxidized_mM": ox,
            "Ox_Red_ratio": ratio
        })

    result_df = pd.DataFrame(results)

    # --- ניתוח מעבדתי: רגרסיה ליניארית ---
    # אנחנו בודקים את הקשר: E = E0 + Slope * log10(Ox/Red)
    # השיפוע התיאורטי עבור n=1 בטמפ' החדר הוא ~0.059V
    slope, intercept, r_value, p_value, std_err = linregress(result_df["Log_Ratio"], result_df["Potential_V"])
    
    print("-" * 30)
    print(f"Laboratory Analysis Results:")
    print(f"Experimental Slope: {slope:.4f} V/decade")
    print(f"Calculated E0: {intercept:.4f} V")
    print(f"R-squared (Fit Quality): {r_value**2:.4f}")
    print("-" * 30)

    # שמירת התוצאות לאקסל חדש
    result_df.to_excel(output_excel, index=False)
    
    # יצירת גרף משולב
    create_combined_plot(result_df, slope, intercept, output_plot)
    
    return result_df

def create_combined_plot(df, slope, intercept, output_plot):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # גרף 1: ריכוזים מול פוטנציאל
    ax1.plot(df["Potential_V"], df["FeCp2_reduced_mM"], 'o-', label="Reduced")
    ax1.plot(df["Potential_V"], df["FeCp2_plus_oxidized_mM"], 's-', label="Oxidized")
    ax1.set_xlabel("Potential (V)")
    ax1.set_ylabel("Concentration (mM)")
    ax1.set_title("Species Distribution")
    ax1.legend()

    # גרף 2: ליניאריזציה של נרנסט 
    ax2.scatter(df["Log_Ratio"], df["Potential_V"], color='black', label="Data Points")
    fit_line = slope * df["Log_Ratio"] + intercept
    ax2.plot(df["Log_Ratio"], fit_line, 'r--', label=f"Fit (Slope={slope:.3f}V)")
    ax2.set_xlabel("log10([Ox]/[Red])")
    ax2.set_ylabel("Potential (V)")
    ax2.set_title("Nernst Plot Linearization")
    ax2.legend()

    plt.tight_layout()
    plt.savefig(output_plot)
    print(f"Analysis plots saved to {output_plot}")

if __name__ == "__main__":
    # מוצא את הנתיב של התיקייה שבה נמצא הסקריפט הנוכחי
    base_path = Path(__file__).parent
    
    # מגדיר את שמות הקבצים יחסית לתיקייה הזו
    input_file = base_path / "ferrocene_nernst_input.xlsx"
    output_excel = base_path / "results.xlsx"
    output_plot = base_path / "analysis_plot.png"
    
    # הרצת הניתוח
    analyze_excel(input_file, output_excel, output_plot)