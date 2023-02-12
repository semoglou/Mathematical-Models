import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

"""
 SEIR (Susceptible-Exposed-Infected-Recovered) model is a mathematical model used to simulate the spread of infectious diseases.
 It describes the evolution of four populations: susceptible (S), exposed (E), infected (I), and recovered (R)
 
 System of Differential Equations:

    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I

 """

 # Parameters" Contact rate, beta, and mean recovery rate, gamma.
beta = 0.3
gamma = 0.1
sigma = 0.05

N = 1000      # Total Population

# Initial Conditions:
E0 = 1
I0 = 0
R0 = 0
S0 = N-E0-R0-I0    # S0 = 999 

X0 = [S0, E0, I0, R0]             # Initial conditions vector

t = np.linspace(0, 365, 366)      # Time points for the simulation

# The SEIR model differential equations:

def derivative(X, t, N, beta, gamma, sigma):
    S,E,I,R = X
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

# Integrate the SEIR equations over the time grid t:

solution = odeint(derivative, X0, t, args=(N, beta, gamma, sigma))

S,E,I,R = solution.T

# Plot the results:

plt.figure()
plt.grid()
plt.plot(t, S, 'blue', label='Susceptible')
plt.plot(t, E, 'red', label='Exposed')
plt.plot(t, I, 'yellow', label='Infected')
plt.plot(t, R, 'purple', label='Recovered')
plt.xlabel('Time [days]')
plt.ylabel('Number of individuals')
plt.title('SEIR Model (Odeint Method)')
plt.legend()
plt.show()


"""-----------------------------------------------------------------"""

# Phase Spaces:

""" we can plot the number of exposed individuals against the number of infected individuals
    This allows us to see the dynamical behavior of the system and understand how it evolves over time (Phase Space Infected vs Exposed)
 """

def plot_seir_phase_space(beta, gamma, sigma, N, E0, t):
    num_scenarios = len(E0)
    I0 = np.zeros(num_scenarios)
    R0 = np.zeros(num_scenarios)
    S0 = N - E0 - I0 - R0

    # Integrate the SEIR equations over the time grid t for each scenario
    solutions = []
    for i in range(num_scenarios):
        y0 = [S0[i], E0[i], I0[i], R0[i]]
        sol = odeint(derivative, y0, t, args=(N, beta, gamma, sigma))
        solutions.append(sol)

    # Plot the phase spaces
    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        plt.plot(S, E, label='E0 = {}'.format(E0[i]))

    plt.xlabel('Susceptible')
    plt.ylabel('Exposed')
    plt.title('SEIR Model Phase Space: Susceptible vs Exposed')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        plt.plot(S, I, label='E0 = {}'.format(E0[i]))

    plt.xlabel('Susceptible')
    plt.ylabel('Infected')
    plt.title('SEIR Model Phase Space: Susceptible vs Infected')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        plt.plot(S, R, label='E0 = {}'.format(E0[i]))

    plt.xlabel('Susceptible')
    plt.ylabel('Recovered')
    plt.title('SEIR Model Phase Space: Susceptible vs Recovered')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S,E, I, R = sol.T
        plt.plot(E, I, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Exposed')
    plt.ylabel('Infected')
    plt.title('SEIR Model Phase Space: Exposed vs Infected')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
       S, E, I, R = sol.T
       plt.plot(E, R, label='E0 = {}'.format(E0[i]))

    plt.xlabel('Exposed')
    plt.ylabel('Recovered')
    plt.title('SEIR Model Phase Space: Exposed vs Recovered')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
       S, E, I, R = sol.T
       plt.plot(I, R, label='E0 = {}'.format(E0[i]))

    plt.xlabel('Infected')
    plt.ylabel('Recovered')
    plt.title('SEIR Model Phase Space: Infected vs Recovered')
    plt.legend()
    plt.show()

beta = 0.3
gamma = 0.1
sigma = 0.05
N = 1000
E0 = np.linspace(0, 100, 5)
t = np.linspace(0, 365, 366)
plot_seir_phase_space(beta, gamma, sigma, N, E0, t)


"""-----------------------------------------------------------------"""

# Direction Fields:

""" direction field represents the direction of change of the system, and can be useful to visualize the stability of the system"""

def plot_seir_direction_field(beta, gamma, sigma, N, E0, t):
    Y0 = (N-E0, E0, 0, 0)
    solutions = [odeint(derivative, Y0, t, args=(N, beta, gamma, sigma)) for Y0 in zip(np.ones(len(E0))*(N-E0), E0, np.zeros(len(E0)), np.zeros(len(E0)))]

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        dSdt, dEdt, dIdt, dRdt = derivative(sol.T, t, N, beta, gamma, sigma)
        plt.quiver(E, I, dEdt, dIdt, label='E0 = {}'.format(E0[i]), color='C{}'.format(i))

    plt.xlabel('Exposed')
    plt.ylabel('Infected')
    plt.title('SEIR Model Phase Space: Direction Field')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        dSdt, dEdt, dIdt, dRdt = derivative(sol.T, t, N, beta, gamma, sigma)
        plt.quiver(E, R, dEdt, dRdt, label='E0 = {}'.format(E0[i]), color='C{}'.format(i))

    plt.xlabel('Exposed')
    plt.ylabel('Recovered')
    plt.title('SEIR Model Phase Space: Direction Field')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        dSdt, dEdt, dIdt, dRdt = derivative(sol.T, t, N, beta, gamma, sigma)
        plt.quiver(I, R, dIdt, dRdt, label='E0 = {}'.format(E0[i]), color='C{}'.format(i))

    plt.xlabel('Infected')
    plt.ylabel('Recovered')
    plt.title('SEIR Model Phase Space: Direction Field')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        dSdt, dEdt, dIdt, dRdt = derivative(sol.T, t, N, beta, gamma, sigma)
        plt.quiver(S, I, -dSdt, dIdt, label='E0 = {}'.format(E0[i]), color='C{}'.format(i))

    plt.xlabel('Susceptible')
    plt.ylabel('Infected')
    plt.title('SEIR Model Phase Space: Direction Field')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, I, R = sol.T
        dSdt, dEdt, dIdt, dRdt = derivative(sol.T, t, N, beta, gamma, sigma)
        plt.quiver(S, R, -dSdt, dRdt, label='E0 = {}'.format(E0[i]), color='C{}'.format(i))

    plt.xlabel('Susceptible')
    plt.ylabel('Recovered')
    plt.title('SEIR Model Phase Space: Direction Field')
    plt.legend()
    plt.show()

E0 = np.linspace(0, 100, 5)
t = np.linspace(0, 365, 366)
plot_seir_direction_field(beta, gamma, sigma, N, E0, t)
