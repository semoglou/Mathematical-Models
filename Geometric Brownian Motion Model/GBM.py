import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
S0 = 100 # initial asset price
r = 0.05 # rate of return
sigma = 0.2 # volatility
T = 1 # time horizon (years)
dt = 0.01 # time step
N = 10 # number of simulations

# Calculate number of steps
n = int(T / dt) + 1

# Initialize price path
P = np.zeros((n, N))
P[0,:] = S0

# Generate price path
for i in range(1, n):
    # Calculate next price using GBM formula
    P[i,:] = P[i-1,:] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.normal(size=N))

# Plot price path for all simulations
plt.plot(P)
plt.xlabel('Steps')
plt.ylabel('Price')
plt.title('Geometric Brownian Motion Model')
plt.show()