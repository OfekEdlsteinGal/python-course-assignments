from gibbs_lib import gibbs_free_energy, interpret_delta_g

# Get input from user
delta_H = float(input("Enter enthalpy change ΔH (in kJ/mol): "))
temperature = float(input("Enter temperature (in Kelvin): "))
delta_S = float(input("Enter entropy change ΔS (in J/mol·K): "))
unit = input("Enter temperature unit (K for Kelvin, C for Celsius): ")

# Calculate using library
delta_G = gibbs_free_energy(delta_H, temperature,unit, delta_S)

# Print result
print("\nResult:")
print("ΔG =", delta_G, "kJ/mol")
# Interpretation
print(interpret_delta_g(delta_G))













