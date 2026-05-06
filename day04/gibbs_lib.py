def convert_temperature_to_kelvin(temperature, unit):
    unit = unit.lower()

    if unit == "k":
        return temperature
    elif unit == "c":
        return temperature + 273.15
    else:
        raise ValueError("Temperature unit must be 'K' or 'C'.")


def gibbs_free_energy(delta_H, delta_S, temperature, unit="K"):
    temperature_K = convert_temperature_to_kelvin(temperature, unit)

    delta_S_kJ = delta_S / 1000
    delta_G = delta_H - (temperature_K * delta_S_kJ)

    return delta_G


def interpret_delta_g(delta_G):
    if delta_G < 0:
        return "The reaction is spontaneous."
    elif delta_G > 0:
        return "The reaction is non-spontaneous."
    else:
        return "The reaction is at equilibrium."


def equilibrium_temperature(delta_H, delta_S):
    """
    Calculate equilibrium temperature where ΔG = 0
    ΔH in kJ/mol
    ΔS in J/mol·K
    Returns temperature in Kelvin
    """

    delta_S_kJ = delta_S / 1000

    if delta_S_kJ == 0:
        return None

    return delta_H / delta_S_kJ