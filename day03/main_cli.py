import sys
from gibbs_lib import gibbs_free_energy

if len(sys.argv) != 4:
    print("Usage: python main_cli.py ΔH T ΔS")
    sys.exit()

delta_H = float(sys.argv[1])
temperature = float(sys.argv[2])
delta_S = float(sys.argv[3])

delta_G = gibbs_free_energy(delta_H, temperature, delta_S)

print("\nResult:")
print(f"ΔG = {round(delta_G, 3)} kJ/mol")

if delta_G < 0:
    print("The reaction is spontaneous.")
elif delta_G > 0:
    print("The reaction is non-spontaneous.")
else:
    print("The reaction is at equilibrium.")

# delta_h = float(sys.argv[1])
#temperature = float(sys.argv[2])
##delta_s = float(sys.argv[3])

#result = gibbs_free_energy(delta_h, temperature, delta_s)

#print(f"ΔG = {result} kJ/mol")

# if result < 0:
   # print("The reaction is spontaneous.")
#else:
 #   print("The reaction is non-spontaneous.")
    
