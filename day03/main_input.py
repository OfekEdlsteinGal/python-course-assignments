from gibbs_lib import gibbs_free_energy

delta_h = float(input("Enter ΔH: "))
temperature = float(input("Enter T: "))
delta_s = float(input("Enter ΔS: "))

print(gibbs_free_energy(delta_h, temperature, delta_s))
