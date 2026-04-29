from gibbs_lib import gibbs_free_energy

assert round(gibbs_free_energy(10, 300, 0.05), 3) == 9.985
assert round(gibbs_free_energy(20, 100, 0.1), 3) == 19.99

print("Tests passed")

