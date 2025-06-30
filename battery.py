import pybamm
import pandas as pd
import numpy as np

# Load model and parameter values
model = pybamm.lithium_ion.SPM()
param = model.default_parameter_values

# Create and solve the simulation
sim = pybamm.Simulation(model, parameter_values=param)
solution=sim.solve([0, 3600])  # 1-hour simulation
time = solution["Time [s]"].entries
voltage = solution["Terminal voltage [V]"].entries


# Save to CSV
df = pd.DataFrame({
    "Time (s)": time,
    "Voltage (V)": voltage
})

df.to_csv("battery_simulation_output.csv", index=False)

# Plot results
sim.plot()