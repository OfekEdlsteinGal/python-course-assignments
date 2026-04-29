from gibbs_lib import gibbs_free_energy

assert gibbs_free_energy(10, 300, 0.05) == -5
assert gibbs_free_energy(20, 100, 0.1) == 10

print("Tests passed")
