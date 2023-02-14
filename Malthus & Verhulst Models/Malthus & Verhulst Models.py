import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""   Malthus Growth Model / Simple Exponential Growth Model   """

# Malthusian growth model
def malthus_model(Y, t, r):
    P = Y
    dPdt = r * P
    return dPdt

# Plot
def plot_malthus_model(P0, r, t):
   
   """
   Parameters:
    - P0 (int): Initial Population.
    - r (float): Population growth rate.
    - t : Time points for the simulation.

    """
   solution = odeint(malthus_model, P0, t, args = (r,))
   P = solution
   # Plot the results:
   plt.figure()
   plt.grid()
   plt.plot(t, P, 'b', label = 'Population with growth rate r = '+str(r)+' and initial population number = '+ str(P0))
   plt.xlabel('Time [days]')
   plt.ylabel('Number of individuals')
   plt.title('Malthusian growth Model')
   plt.legend()
   plt.show()

# Initial Population:
P0 = 100

# Population growth rate:
r = 0.2

# Time points for the simulation
t = np.linspace(0, 10, 11)     

plot_malthus_model(P0, r, t)

# Compare different cases of growth rate r
def compare_r_cases(r_1, r_2, r_3, P0, t):
    solution_1 = odeint(malthus_model, P0, t, args = (r_1,))
    solution_2 = odeint(malthus_model, P0, t, args = (r_2,))
    solution_3 = odeint(malthus_model, P0, t, args = (r_3,))
    P1, P2, P3 = solution_1, solution_2, solution_3
    plt.figure()
    plt.grid()
    plt.plot(t, P1, 'b', label = 'Population with growth rate r = '+str(r_1))
    plt.plot(t, P2, 'orange', label = 'Population with growth rate r = '+str(r_2))
    plt.plot(t, P3, 'r', label = 'Population with growth rate r = '+str(r_3))
    plt.xlabel('Time [days]')
    plt.ylabel('Number of individuals')
    plt.ylim([0, 400])  # Optional
    plt.title('Malthusian Model - Comparison of r rate ')
    plt.legend()
    plt.show()

compare_r_cases(0.2, 0, -0.2, P0 = 100, t = np.linspace(0, 10, 11))

"---------------------------------------------------------------------------------------"

"""   Verhulst Logistic Growth Model   """

def logistic_model(Y, t, k, K):
    P = Y
    dPdt = k * P * (1 - (P / K))
    return dPdt

# Plot
def plot_logistic_model(P0, k, K, t):

    """
   Parameters:
    - P0 (int): Initial Population.
    - k (float): Relative Growth Rate Coefficient
    - K (int): Carrying Capacity.
    - t : Time points for the simulation.

    """
    solution = odeint(logistic_model, P0, t, args = (k, K) )
    P = solution
   # Plot the results:
    plt.figure()
    plt.grid()
    plt.plot(t, P, 'b', label = 'Population with Carrying Capacity K  = '+str(K)+'\nRelative Growth Rate Coefficient k = '+str(k)+'\n and initial population number = '+ str(P0))
    plt.xlabel('Time [days]')
    plt.ylabel('Number of individuals')
    plt.title('Verhulst Logistic Growth Model')
    plt.legend()
    plt.show()

# Initial Population:
P0 = 100

# Carrying Capacity:
K = 1000

# Relative Growth Rate Coefficient:
k = 0.3

# Time points for the simulation
t = np.linspace(0, 50, 51)

plot_logistic_model(P0, k, K, t)

# Compare different cases of relative growth rate coefficient k
def compare_k_cases(k_1, k_2, k_3, P0, K, t):
    solution_1 = odeint(logistic_model, P0, t, args = (k_1, K))
    solution_2 = odeint(logistic_model, P0, t, args = (k_2, K))
    solution_3 = odeint(logistic_model, P0, t, args = (k_3, K))
    P1, P2, P3 = solution_1, solution_2, solution_3
    plt.figure()
    plt.grid()
    plt.plot(t, P1, 'b', label = 'Population with relative growth rate coefficient k = '+str(k_1))
    plt.plot(t, P2, 'orange', label = 'Population with relative growth rate coefficient k = '+str(k_2))
    plt.plot(t, P3, 'r', label = 'Population with relative growth rate coefficient k = '+str(k_3))
    plt.xlabel('Time [days]')
    plt.ylabel('Number of individuals')
    plt.ylim([0, 1000])  # Optional
    plt.title('Verhulst Logistic Growth Model - Comparison of k rate ')
    plt.legend()
    plt.show()

compare_k_cases(0.3, 0, -0.3, P0 = 100, K = 1000, t = np.linspace(0, 50, 51))
