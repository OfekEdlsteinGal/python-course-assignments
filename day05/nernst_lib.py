import math

R = 8.314462618  # J/(mol*K)
F = 96485.33212  # C/mol


def oxidized_reduced_ratio(potential_v, e0_v, n, temperature_k):
    """
    Calculate [Ox]/[Red] using the Nernst equation.

    For ferrocene:
        FeCp2 ⇌ FeCp2+ + e-

    E = E0 + (RT/nF) ln([Ox]/[Red])

    Therefore:
        [Ox]/[Red] = exp((E - E0) nF / RT)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if temperature_k <= 0:
        raise ValueError("temperature must be above 0 K")

    exponent = (potential_v - e0_v) * n * F / (R * temperature_k)
    return math.exp(exponent)


def redox_concentrations(potential_v, e0_v, n, temperature_k, total_conc_mm):
    """
    Calculate the equilibrium concentrations of reduced and oxidized species.

    total_conc_mm = [Red] + [Ox]
    ratio = [Ox]/[Red]

    Therefore:
        [Red] = total / (1 + ratio)
        [Ox] = total * ratio / (1 + ratio)
    """
    if total_conc_mm <= 0:
        raise ValueError("total concentration must be positive")

    ratio = oxidized_reduced_ratio(potential_v, e0_v, n, temperature_k)
    reduced = total_conc_mm / (1 + ratio)
    oxidized = total_conc_mm * ratio / (1 + ratio)

    return reduced, oxidized, ratio


def classify_region(potential_v, e0_v):
    """
    Give a simple interpretation of the redox composition.
    """
    if potential_v < e0_v - 0.05:
        return "mostly reduced"
    if potential_v > e0_v + 0.05:
        return "mostly oxidized"
    return "mixed redox region"


def delta_e(potential_v, e0_v):
    """
    Calculate the difference between measured potential and formal potential.
    """
    return potential_v - e0_v


def classify_cell_type(potential_v, e0_v):
    """
    Simple electrochemical interpretation using delta E = E - E0.

    If delta E is positive, the redox direction is thermodynamically favorable,
    so it is described here as galvanic/spontaneous.
    If delta E is negative, the direction is not spontaneous and would require
    external voltage, so it is described as electrolytic.
    """
    de = delta_e(potential_v, e0_v)

    if de > 0:
        return "galvanic cell / spontaneous"
    if de < 0:
        return "electrolytic cell / non-spontaneous"
    return "equilibrium point"
