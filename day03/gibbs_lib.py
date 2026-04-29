# Gibbs Free Energy Calculator

print("Gibbs Free Energy Calculator")
print("----------------------------")

# Get input from user
delta_H = float(input("Enter enthalpy change ΔH (in kJ/mol): "))
delta_S = float(input("Enter entropy change ΔS (in J/mol·K): "))
temperature = float(input("Enter temperature (in Kelvin): "))

# Convert entropy from J to kJ
delta_S_kJ = delta_S / 1000

# Calculate Gibbs free energy
delta_G = delta_H - (temperature * delta_S_kJ)

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

def gibbs_free_energy(delta_h, temperature, delta_s):
    return delta_h - temperature * delta_s
