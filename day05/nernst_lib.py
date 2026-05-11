import math

# קבועים פיזיקליים
R = 8.314462618  # J/(mol*K)
F = 96485.33212  # C/mol

def oxidized_reduced_ratio(potential_v, e0_v, n, temperature_k):
    """חישוב היחס לפי משוואת נרנסט"""
    if n <= 0:
        raise ValueError("n must be positive")
    if temperature_k <= 0:
        raise ValueError("temperature must be above 0 K")

    exponent = (potential_v - e0_v) * n * F / (R * temperature_k)
    return math.exp(exponent)

def redox_concentrations(potential_v, e0_v, n, temperature_k, total_conc_mm):
    """חישוב ריכוזים של הצורות המחוזרת והמחומצנת"""
    if total_conc_mm <= 0:
        raise ValueError("total concentration must be positive")

    ratio = oxidized_reduced_ratio(potential_v, e0_v, n, temperature_k)
    reduced = total_conc_mm / (1 + ratio)
    oxidized = total_conc_mm * ratio / (1 + ratio)

    return reduced, oxidized, ratio

def delta_e(potential_v, e0_v):
    """חישוב ההפרש בין הפוטנציאל הנמדד לפוטנציאל הסטנדרטי"""
    return potential_v - e0_v

def classify_region(potential_v, e0_v):
    """סיווג האזור הכימי לפי הפוטנציאל"""
    if potential_v < e0_v - 0.05:
        return "mostly reduced"
    if potential_v > e0_v + 0.05:
        return "mostly oxidized"
    return "mixed redox region"

def classify_cell_type(potential_v, e0_v):
    """סיווג סוג התא (גלווני או אלקטרוליטי)"""
    de = delta_e(potential_v, e0_v)
    if de > 0:
        return "galvanic cell / spontaneous"
    if de < 0:
        return "electrolytic cell / non-spontaneous"
    return "equilibrium point"
