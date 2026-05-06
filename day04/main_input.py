from gibbs_lib import gibbs_free_energy, interpret_delta_g,equilibrium_temperature

# Get input from user
delta_H = float(input("Enter enthalpy change ΔH (in kJ/mol): "))
delta_S = float(input("Enter entropy change ΔS (in J/mol·K): "))
temperature = float(input("Enter temperature:" ))
unit = input("Enter temperature unit (K for Kelvin, C for Celsius): ")

# Calculate using library
delta_G = gibbs_free_energy(delta_H, delta_S, temperature, unit)
eq_temp = equilibrium_temperature(delta_H, delta_S)

# Print result
print("\nResult:")
print("ΔG =", delta_G, "kJ/mol")

# Interpretation
print(interpret_delta_g(delta_G))

if eq_temp is not None:
    print("Equilibrium temperature =", round(eq_temp, 2), "K")
else:
    print("Equilibrium temperature cannot be calculated because ΔS = 0")















