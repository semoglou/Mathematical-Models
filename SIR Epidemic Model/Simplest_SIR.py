import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Define the SIR model differential equations
def sir_model(y, t, N, beta, gamma):
    # Unpack the variables
    S, I, R = y
    # Differential equations
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    # Return the derivatives
    return dSdt, dIdt, dRdt

# Main function
if __name__ == '__main__':
    # Set the total population size
    N = 1000000
    # Set the initial number of infected and recovered individuals
    I0, R0 = 10, 0
    # Calculate the initial number of susceptible individuals
    S0 = N - I0 - R0
    # Set the transmission rate (beta) and recovery rate (gamma)
    beta, gamma = 0.5, 0.1
    # Create a time array from 0 to 365 days
    t = np.linspace(0, 365, 365)
    # Set the initial conditions for the model
    y0 = S0, I0, R0
    # Solve the differential equations using odeint
    sol = odeint(sir_model, y0, t, args=(N, beta, gamma))
    # Unpack the solution array into separate arrays for S, I, and R
    S, I, R = sol[:, 0], sol[:, 1], sol[:, 2]
    # Plot the results
    plt.figure(figsize=(12, 4))
    plt.plot(t, S/N, 'b', label='Susceptible')
    plt.plot(t, I/N, 'r', label='Infected')
    plt.plot(t, R/N, 'g', label='Recovered')
    plt.legend()
    plt.xlabel('Time [days]')
    plt.ylabel('Proportion of population')
    plt.title('SIR model')
    plt.show()
    
    # Plot the phase space
    plt.figure(figsize=(12, 4))
    plt.plot(S/N, I/N, 'r')
    plt.xlabel('Susceptible')
    plt.ylabel('Infected')
    plt.title('Phase space')
    plt.show()