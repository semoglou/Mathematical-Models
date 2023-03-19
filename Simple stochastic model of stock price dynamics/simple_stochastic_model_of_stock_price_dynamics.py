import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

""" 
simple stochastic model of stock price dynamics 
continuous-time version of the discrete-time model logistic map
sometimes called the stochastic differential equation (SDE) version of the logistic map

Define the function that describes the dynamical system
t: the current time
y: the state of the system (stock price)
r: the interest rate
a: the growth rate
b: the volatility
"""

def stock_price(t, y, r, a, b):
    # Calculate the change in stock price over time
    # based on the current state and the parameters
    dydt = r*y + a*y*(1-y) + b*y*np.random.normal()
    return dydt

"""
Terms of the Model :
r*y: represents the expected return due to the interest rate
a*y*(1-y): represents the expected growth of the stock price due to market conditions 
b*y*np.random.normal(size=1): adds some randomness to the model using normally distributed random numbers
"""

# Example

# Set up Initial conditions and Time span
y0 = [100]   # initial stock price
t_span = [0, 100]   # time span for simulation
t_eval = np.linspace(t_span[0], t_span[1], 1000)   # time points to evaluate solution

# Set up the parameters
r = 0.05   # interest rate 
a = 0.001    # growth rate
b = 0.01   # volatility

# Solve the ODE system numerically using solve_ivp
sol = solve_ivp(stock_price, t_span=t_span, y0=y0, t_eval=t_eval, args=(r, a, b))

# Plot the results
plt.plot(sol.t, sol.y[0], label='Stock Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Stock Price')
plt.legend()
plt.show()

"""
Similar to the graph of f(x) = 1/x , because the logistic equation dy/dt = r*y*(1-y)
has a stable equilibrium point at y=1,
which means that if the initial value of y is close to 1,
the solution will converge towards 1 over time 
"""

def simulation(y0, t_span, t_eval, r, a, b,):
    sol = solve_ivp(stock_price, t_span=t_span, y0=y0, t_eval=t_eval, args=(r, a, b))
    plt.plot(sol.t, sol.y[0], label='Stock Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Price')
    plt.legend()
    plt.show()