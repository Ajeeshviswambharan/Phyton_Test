import pybamm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load model and parameter values
model = pybamm.lithium_ion.SPM()
param = model.default_parameter_values

# Create and solve the simulation
sim = pybamm.Simulation(model, parameter_values=param)
solution=sim.solve([0, 3600])  # 1-hour simulation
time = solution["Time [s]"].entries
voltage = solution["Terminal voltage [V]"].entries

# Compute SOC manually for SPM
capacity = param["Nominal cell capacity [A.h]"]
discharge = solution["Discharge capacity [A.h]"].entries
soc = 1 - discharge / capacity


# Save to CSV
df = pd.DataFrame({
    "Time (s)": time,
    "Voltage (V)": voltage,
    "State of Charge": soc
})

df.to_csv("battery_simulation_output.csv", index=False)

# Plot results
#sim.plot()

plt.figure(figsize=(10, 5))
plt.plot(time, voltage, label="Voltage (V)")
plt.plot(time, soc, label="State of Charge", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Battery Simulation: Voltage and SOC vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()