import sys
from gibbs_lib import gibbs_free_energy

delta_h = float(sys.argv[1])
temperature = float(sys.argv[2])
delta_s = float(sys.argv[3])

print(gibbs_free_energy(delta_h, temperature, delta_s))
