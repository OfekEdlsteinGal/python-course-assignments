from gibbs_lib import gibbs_free_energy

delta_h = float(input("Enter ΔH: "))
temperature = float(input("Enter T: "))
delta_s = float(input("Enter ΔS: "))

result = gibbs_free_energy(delta_h, temperature, delta_s)

print(f"ΔG = {result} kJ/mol")

if result < 0:
    print("The reaction is spontaneous.")
else:
    print("The reaction is non-spontaneous.")

