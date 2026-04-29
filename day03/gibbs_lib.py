def gibbs_free_energy(delta_h, temperature, delta_s):
    delta_s_kj = delta_s / 1000
    return delta_h - temperature * delta_s_kj
