from gibbs_lib import gibbs_free_energy

# Get input from user
delta_H = float(input("Enter enthalpy change ΔH (in kJ/mol): "))
temperature = float(input("Enter temperature (in Kelvin): "))
delta_S = float(input("Enter entropy change ΔS (in J/mol·K): "))

# Calculate using library
delta_G = gibbs_free_energy(delta_H, temperature, delta_S)

# Print result
print("\nResult:")
print("ΔG =", delta_G, "kJ/mol")

# Interpretation
if delta_G < 0:
    print("The reaction is spontaneous.")
elif delta_G > 0:
    print("The reaction is non-spontaneous.")
else:
    print("The reaction is at equilibrium.")







