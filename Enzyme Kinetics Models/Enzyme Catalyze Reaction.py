import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

"""  
 Enzyme Kinetics - Enzyme Catalyze Reaction

   S → P   S: Substrate, P: Product  

   This is described within the following multi-step mechanism:  
   E+S ⇌(k1a/k1b) C →(k2) E+P 

   Where k1a, k1b, k2 (>0) are rate constants 
   E is the enzyme  
   and C is the enzyme - substrate complex.
   
   Differential Equations Model (of concentrations functions):

     d[S]/dt = -k1a*[S]*[E] + k1b*[C] 
     d[E]/dt = -k1a*[S]*[E] + (k1b + k2)*[C] 
     d[C]/dt = k1a*[S]*[E] - (k1b + k2)*[C] 
     d[P]/dt = k2*[C] .
"""
# Model
def enzyme_model(Y, t, k1a, k1b, k2):
    S, E, C, P = Y
    dSdt = (-k1a) * S * E + k1b * C
    dEdt = (-k1a) * S * E + (k1b + k2) * C
    dCdt = k1a * S * E - (k1b + k2) * C 
    dPdt = k2 * C
    return dSdt, dEdt, dCdt, dPdt

# Plot
def plot_enzyme_model(Y0, t, k1a, k1b, k2):
    solution = odeint(enzyme_model, Y0, t, args = (k1a, k1b, k2)) 
    S, E, C, P = solution.T
    plt.figure()
    plt.grid()
    plt.plot(t, S, 'b', label = 'Substrate')
    plt.plot(t, E, 'r', label = 'Enzyme')
    plt.plot(t, C, 'g', label = 'Enzyme-Substrate Complex')
    plt.plot(t, P, 'black', label = 'Product')
    plt.xlabel('Time [seconds]')
    plt.ylabel('Concentration')
    plt.title('Enzyme - Catalyzed Reaction')
    plt.legend()
    plt.show()
    
# Initial Conditions and Parameters
S0 = 100  # Initial Substrate Concentration
E0 = 20  # Initial Enzyme Concentration
C0 = 0  # Initial Enzyme-Substrate Complex Concentration
P0 = 0  # Initial Product Concentration
Y0 = [S0, E0, C0, P0]  # Initial Conditions Vector
k1a = 3
k1b = 2
k2 = 4
t = np.linspace(0, 10, 11)

# Example
plot_enzyme_model(Y0, t, k1a, k1b, k2)

# Phase - Space
def plot_enzyme_model_phase_space(E0, t, k1a, k1b, k2):
    num_scenarios = len(E0)
    S0 = [100]*len(E0)
    C0, P0 = np.zeros(len(E0)), np.zeros(len(E0))
    solutions = []

    for i in range(num_scenarios):
        Y0 = [S0[i], E0[i], C0[i], P0[i]]
        sol = odeint(enzyme_model, Y0, t, args = (k1a, k1b, k2))
        solutions.append(sol)

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, C, P = sol.T
        plt.plot(S, E, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Substrate Concentration')
    plt.ylabel('Enzyme Concentration')
    plt.title('Enzyme - Catalyzed Reaction: Phase Space [S] vs [E]')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, C, P = sol.T
        plt.plot(S, C, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Substrate Concentration')
    plt.ylabel('Enzyme-Substrate Complex Concentration')
    plt.title('Enzyme - Catalyzed Reaction: Phase Space [S] vs [C]')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, C, P = sol.T
        plt.plot(E, C, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Enzyme Concentration')
    plt.ylabel('Enzyme-Substrate Complex Concentration')
    plt.title('Enzyme - Catalyzed Reaction: Phase Space [E] vs [C]')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, C, P = sol.T
        plt.plot(E, P, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Enzyme Concentration')
    plt.ylabel('Product Concentration')
    plt.title('Enzyme - Catalyzed Reaction: Phase Space [E] vs [P]')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, C, P = sol.T
        plt.plot(C, P, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Enzyme-Substrate Complex Concentration')
    plt.ylabel('Product Concentration')
    plt.title('Enzyme - Catalyzed Reaction: Phase Space [C] vs [P]')
    plt.legend()
    plt.show()

    plt.figure()
    for i, sol in enumerate(solutions):
        S, E, C, P = sol.T
        plt.plot(S, P, label='E0 = {}'.format(E0[i]))
    plt.xlabel('Substrate Concentration')
    plt.ylabel('Product Concentration')
    plt.title('Enzyme - Catalyzed Reaction: Phase Space [S] vs [P]')
    plt.legend()
    plt.show()

E0 = np.linspace(0, 40, 5)
t = np.linspace(0, 10, 11)
k1a = 3
k1b = 2
k2 = 4

# Example
plot_enzyme_model_phase_space(E0, t, k1a, k1b, k2)
