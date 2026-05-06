import sys
from gibbs_lib import gibbs_free_energy

if len(sys.argv) != 4:
    print("Usage: python main_cli.py ΔH T ΔS")
    sys.exit()


if len(sys.argv) != 5:
    print("Usage: python3 main_cli.py <delta_H> <temperature> <unit><delta_S>")
    print("Example with Kelvin: python3 main_cli.py 10 50 300 K")
    print("Example with Celsius: python3 main_cli.py 10 50 25 C")
    sys.exit(1)

delta_H = float(sys.argv[1])
delta_S = float(sys.argv[2])
temperature = float(sys.argv[3])
unit = sys.argv[4]

delta_G = gibbs_free_energy(delta_H, delta_S, temperature, unit)

print("\nResult:")
print("ΔG =", delta_G, "kJ/mol")
print(interpret_delta_g(delta_G))
    


# delta_H = float(sys.argv[1])
# temperature = float(sys.argv[2])
# delta_S = float(sys.argv[3])

# delta_G = gibbs_free_energy(delta_H, temperature, delta_S)

# print("\nResult:")
# print(f"ΔG = {round(delta_G, 3)} kJ/mol")

# if delta_G < 0:
#   print("The reaction is spontaneous.")
# elif delta_G > 0:
#    print("The reaction is non-spontaneous.")
#else:
#    print("The reaction is at equilibrium.")





