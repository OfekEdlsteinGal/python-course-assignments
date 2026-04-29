import sys
from gibbs_lib import gibbs_free_energy

delta_h = float(sys.argv[1])
temperature = float(sys.argv[2])
delta_s = float(sys.argv[3])

result = gibbs_free_energy(delta_h, temperature, delta_s)

print(f"ΔG = {result} kJ/mol")

if result < 0:
    print("The reaction is spontaneous.")
else:
    print("The reaction is non-spontaneous.")
