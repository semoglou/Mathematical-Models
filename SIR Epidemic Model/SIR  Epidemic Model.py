import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
""" 
        SIR Epidemic Model (A simple mathematical description of the spread of a disease in a population N)
         ( S + I + R = N )
         S(t): Susceptible but not yet infected with the disease
         I(t): Infectious individuals
         R(t): individuals who have Recovered from the disease and now have immunity to it

         (SIR model describes the change in the population of each of these compartments in terms of two parameters, β and γ.
         β describes the effective contact rate of the disease: an infected individual comes into contact with βN
         other individuals per unit of time (of which the fraction that are susceptible to contracting the disease is S/N). 
         γ is the mean recovery rate: that is,
         1/γ is the mean period of time during which an infected individual can pass it on)
         
         System of Differential Equations: (β = beta, γ = gamma)
         
         dS/dt = (-beta * S * I) / N 
         dI/dt = (beta * S * I / N) - (gamma * I)
         dR/dt = gamma * I                               
         

         We Pose X = (S, I, R), (dotX or) X' = ((-beta * S * I) / N , (beta * S * I / N) - (gamma * I) , dR/dt = gamma * I  ) = f(X)

         
         For the code: we initialize beta = 0.4, gamma = 0.1, and N = 350 (population), 
         starting with one infected I(0) = I0 = 1

        """
N = 350                 # Population
I0 = 1                  # Initial State: 1 Infected
R0 = 0
S0 = N - I0 - R0
beta = 0.4              # Contact rate 
gamma = 0.1             # Mean recovery rate
tmax = 160              # A grid of time points / days
Nt = 160
t = np.linspace(0, tmax, Nt + 1)

"""  Odeint Method:  """

def Main_1():
   N = 350                 # Population
   I0 = 1                  # Initial State: 1 Infected
   R0 = 0
   S0 = N - I0 - R0
   beta = 0.4              # Contact rate 
   gamma = 0.1             # Mean recovery rate
   tmax = 160              # A grid of time points / days
   Nt = 160
   t = np.linspace(0, tmax, Nt + 1)

   def derivative(X, t):
       S, I, R = X 
       dotS = (-beta * S * I) / N 
       dotI = (beta * S * I / N) - (gamma * I)
       dotR = gamma * I   
       return np.array([dotS, dotI, dotR])

   X0 = S0, I0, R0          # Initial Conditions Vector

   res = integrate.odeint(derivative, X0, t)
   S, I, R = res.T

   plt.figure()
   plt.grid()
   plt.title('Odeint Method')
   plt.plot(t, S, 'b', label = 'Susceptible')
   plt.plot(t, I, 'r', label = 'Infected')
   plt.plot(t, R, 'g', label = 'Recoverd with immunity')
   plt.xlabel('Time t, [days]')
   plt.ylabel('Number of individuals')
   plt.ylim([0, N])
   plt.legend()
   plt.show()

"""  Comparing the Differences of Rzero:  """

def Main_2():
   
   """ R_0 or Rzero is a parameter describing the average number of new infections due to a sick individual.
       Its commonly called the basic reproduction number. Its a fundamental concept in epidemiology.
       If R_0 > 1 the epidemic will persist otherwise it will die out. R_0 = (beta * N / gamma)
       or Rzero = beta/gamma (as a percentage of N) 
       """

   # We'll compare the different cases of R_0 :

   def der(X, t, beta, gamma):
       S, I, R = X
       dotS = (-beta * S * I) / N 
       dotI = (beta * S * I / N) - (gamma * I)
       dotR = gamma * I
       return np.array([dotS, dotI, dotR])

   X0 = S0, I0, R0          # Initial Conditions Vector

   def Case(beta, gamma):
       Rzero = beta/gamma
       res = integrate.odeint(der, X0, t, args = (beta, gamma))
       S, I, R = res.T
       plt.figure()
       plt.grid()
       if Rzero > 1:
           Rzero = format(Rzero, '.2f')
           title = 'Rzero = '+ str(Rzero)
           plt.title(title)   
       else:
           plt.title('Rzero <= 1 - the epidemic dies out ')                         
       plt.plot(t, S, 'b', label = 'Susceptible')
       plt.plot(t, I, 'r', label = 'Infected')
       plt.plot(t, R, 'g', label = 'Recoverd with immunity')
       plt.xlabel('Time t, [days]')
       plt.ylabel('Percentage of individuals')
       plt.ylim([0, N])
       plt.legend()
       plt.show()

   def Examples():
      L = [ [0.5, 0.1], [0.3, 0.1], [0.2, 0.1], [0.125, 0.1], [0.01, 0.1] ] 
      for [beta, gamma] in L:
        Case(beta, gamma)

   Examples()

""" Phase - Space of SI Model: """

def Main_3():
   
   # We already know that S+I+R = N => R = N - S - R
   # Thus, we simplify the SIR -> SI Model, using only the first two O.D.E's

   def derivative_SI(X, t, beta = 0.4, gamma = 0.1):
       S, I = X 
       dotS = (-beta * S * I) / N 
       dotI = (beta * S * I / N) - (gamma * I)
       return np.array([dotS, dotI])
   plt.figure()
   I = np.linspace(1, 6, 15)
   for i in I:
      X0 = [S0, i]
      Xf = integrate.odeint(derivative_SI, X0, t, args = (0.4, 0.1))
      plt.plot(Xf, "-", label = "$s = $"+str(X0[1]))
   plt.xlabel('Susceptible')
   plt.ylabel('Infected')
   plt.legend()
   plt.title('Phase - Space')                                              
   plt.show()

Main_1()
Main_2()
Main_3()

