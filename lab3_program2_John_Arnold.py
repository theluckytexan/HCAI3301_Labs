import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt

# Parameters
beta = 1.3       # Shape
eta = 1000       # Scale

# Simulate lifetimes
data = weibull_min.rvs(beta, scale=eta, size=50)

# Plot histogram
plt.hist(data, bins=10, edgecolor='black')
plt.title("Simulated Sensor Lifetimes")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
