import pybamm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load model and parameter values
#model = pybamm.lithium_ion.SPM()
model = pybamm.lithium_ion.SPM({"thermal": "lumped"})
param = pybamm.ParameterValues("Chen2020")
#param = model.default_parameter_values

# Optionally adjust voltage cutoffs per cell (if needed)
param["Lower voltage cut-off [V]"] = 2.8 # Cell-level cutoff
param["Upper voltage cut-off [V]"] = 4.2
param["Current function [A]"] = 1  # Discharge at 1 A
param["Nominal cell capacity [A.h]"]= 100/4
#param["Nominal cell capacity [A.h]"] = 5  # Change capacity to 5 Ah
# Create and solve the simulation
sim = pybamm.Simulation(model, parameter_values=param)


t_eval = np.linspace(0, 36000, 1000000)  # 1000 points over 10 hours
solution = sim.solve(t_eval=t_eval)

#solution=sim.solve([0, 36000])  # 10-hour simulation
# Number of cells in series for 12V battery pack
n_cells = 3
voltage_single_cell = solution["Terminal voltage [V]"].entries
voltage_pack = voltage_single_cell * n_cells  # 12V pack (4 cells)


time = solution["Time [s]"].entries
# Compute SOC manually for SPM
capacity = param["Nominal cell capacity [A.h]"]
discharge = solution["Discharge capacity [A.h]"].entries
soc = 1 - discharge / capacity
voltage = solution["Terminal voltage [V]"].entries
current = solution["Current [A]"].entries
temperature = solution["X-averaged cell temperature [K]"].entries
#This confirms that it hit the voltage cutoff.


print("End time:", time[-1], "s")
print("End voltage:", voltage_pack[-1], "V")

# Save to CSV
df = pd.DataFrame({
    "Time (s)": time,
    "Terminal voltage [V]": voltage,
    "Pack Voltage (V)": voltage_pack,
    "Current (A)": current,
    "Temperature (C)": temperature - 273.15,
    "State of Charge": soc,
    "Discharge capacity": discharge
})

df.to_csv("battery_simulation_output_12V.csv", index=False)

# Plot results
#sim.plot()

plt.figure(figsize=(10, 5))
plt.plot(time, voltage_pack, label="12V Pack Voltage (V)")
plt.plot(time, soc, label="State of Charge", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("12V Lithium-Ion Battery Pack Simulation (3 Cells)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()