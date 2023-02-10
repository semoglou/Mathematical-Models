import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as ipw
from scipy import integrate


""" Lotka-Volterra (Predator-Prey)  Mathematical Model 

   x: Prey , y: Predator (Population)

   System of Differential Equations:    

      dx/dt = a*x - b*x*y

      dy/dt = d*x*y - g*y   """

# Constants (Parameters describing the interaction of the two species): 

a = 1       # a*x:   Exponential growth of Prey's population
b = 0.3     # b*x*y: The rate of predation on the prey 
g = 1.5     # g*y:   Loss rate of the predators due to either natural death or emigration
d = 0.8     # d*x*y: The growth of the predator population (Note the similarity to the predation rate; however, a different constant is used, as the rate at which the predator population grows is not necessarily equal to the rate at which it consumes the prey)
x0 = 3      # Initial State of Prey's Population
y0 = 2      # Initial State of Predator's Population

def derivative(X, t, a, b, d, g):
    x,y = X
    dotx = x*( a - b*y )
    doty = y*( d*x - g )
    return np.array([dotx, doty])

"""  Odeint Method:  """

Nt = 1000
tmax = 30
t = np.linspace(0, tmax, Nt)  # Nt:samples, from 0 to tmax   (We need to have many samples in order to have a "good" graph)
X0 = [x0, y0]                                                     # Initial State
res = integrate.odeint(derivative, X0, t, args = (a, b, d, g))    # Solve the O.D.E
x, y = res.T                                                      # .T : reverses the order of the axes
plt.figure()
plt.grid()                                                        # To have grid on the graph
plt.title('Odeint Method')
plt.plot(t, x, '.b', label = 'Prey')                              # x, y: solution of the O.D.E
plt.plot(t, y, '-r', label = 'Predator' )
plt.xlabel('Time t, [Days]')
plt.ylabel('Population')
plt.legend()
plt.show()


"""------------------------------------------------------------"""

"""  Phase - Space Graph:  """

plt.figure()
I = np.linspace(1.0, 6.0, 15)  # (prey's population initial state from 1.0, to 6.0, Number of Samples), generates 15 rational numbers from 1 to 6
for prey in I:
    X0 = [prey, 1.0]
    Xf = integrate.odeint(derivative, X0, t, args = (a, b, d, g))       # Xf: The solutions of the ODE for different X0 each time
    plt.plot(Xf[:, 0], Xf[:, 1], "-", label = "$x_0 = $"+str(X0[0]))   
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.legend()
plt.title('Phase - Space')                                              # Where the center is the saddle point: (g/d, a/b)
plt.show()


"""------------------------------------------------------------"""

"""  Direction Field:  """

x = np.linspace(0, 6, 15)     # Generates 15 numbers from 0 to 6
y = np.linspace(0, 6, 15)
X1, Y1 = np.meshgrid(x, y)    # Making a matrice with dimensions x*y
D = [X1, Y1]
Dx1, Dy1 = derivative(D, t = 0, a = 1, b = 1, d = 0.75, g = 1.5)
plt.figure()
plt.title('Direction Field')
Q = plt.quiver(X1,Y1, Dx1, Dy1, pivot = 'mid', cmap = plt.cm.jet)   # vectors (X1,Dx1), (Y1, Dy1)

# Add the same as the above Graph: (Because we want to see the direction fields inside the phase - space )

I = np.linspace(1.0, 6.0, 15)  
for prey in I:
    X0 = [prey, 1.0]
    Xf = integrate.odeint(derivative, X0, t, args = (a, b, d, g))
    plt.plot(Xf[:, 0], Xf[:, 1], "-", label = "$x_0 = $"+str(X0[0]))   
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.legend()    
plt.show()


"""------------------------------------------------------------"""

"""  Phase - Space Graph with & without harvest:  """

u = 0.5
v = 1

def derivative_2(X, t, a, b, d, g, u, v):
    x, y = X
    dotx = x*( ( a - u ) - b*y)           # change of the function - we add the harvest
    doty = y*( ( d*x - ( g + v ) ) )
    return np.array([dotx, doty])

plt.figure()
I = np.linspace(1.0, 6.0, 1)              # Only 1 Sample to see the difference of the graphs
for prey in I:
    X0 = [prey, 1.0]
    Xf = integrate.odeint(derivative, X0, t, args = (a, b, d, g))
    plt.plot(Xf[:, 0], Xf[:, 1], "-", label = "$x_0 = $"+str(X0[0]))

    Xz = integrate.odeint(derivative_2, X0, t, args = (a, b, d, g, u, v))  # Solution
    plt.plot(Xz[:, 0], Xz[:, 1], "-", label = "$x_0 = $"+str(X0[0]))       # We add the case of harvest into the graph

plt.xlabel('Prey')
plt.ylabel('predator')
plt.title('Phase - Space Graph with and without harvest')                   # Center of the Harvest - Graph is ( (g+v)/d, (a-u)/b )
plt.show()
