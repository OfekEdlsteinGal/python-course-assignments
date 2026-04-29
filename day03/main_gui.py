import tkinter as tk
from gibbs_lib import gibbs_free_energy

def calculate():
    dh = float(entry_dh.get())
    t = float(entry_t.get())
    ds = float(entry_ds.get())

    result = gibbs_free_energy(dh, t, ds)

    if result < 0:
        message = "The reaction is spontaneous."
    elif result > 0:
        message = "The reaction is non-spontaneous."
    else:
        message = "The reaction is at equilibrium."

    result_label.config(text=f"ΔG = {result} kJ/mol\n{message}")

   # result_label.config(text=str(gibbs_free_energy(dh, t, ds)))

root = tk.Tk()

entry_dh = tk.Entry(root)
entry_dh.pack()

entry_t = tk.Entry(root)
entry_t.pack()

entry_ds = tk.Entry(root)
entry_ds.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
