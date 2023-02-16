import numpy as np
import matplotlib.pyplot as plt
import random

def coin_flip():
    """Simulate a coin flip by generating a random integer between 0 and 1."""
    return random.randint(0,1)   

def monte_carlo(iterations):
    """Simulate a coin flip a specified number of times using a Monte Carlo simulation.
    
    Args:
        iterations (int): The number of times to simulate a coin flip.
    
    Returns:
        tuple: A tuple of two lists: head_probabilities, tail_probabilities, representing the head and tail probabilities over time.

        Note that: head_probabilities[-1], tail_probabilities[-1] representing the "final"-estimated probability of heads and tails
    """

    head_probabilities, tail_probabilities = [], [] 
    heads_counter, tails_counter = 0, 0     # Counters
    for i in range(iterations):
        # Flip the coin
        result = coin_flip()
        if result == 0:
            heads_counter += 1
        else:
            tails_counter += 1
        prob_head, prob_tail = heads_counter/(i+1), tails_counter/(i+1)
        head_probabilities.append(prob_head)
        tail_probabilities.append(prob_tail)
    return head_probabilities, tail_probabilities

def run_the_simulation(iterations):
    heads, tails = monte_carlo(iterations)
    """ 
    Plot the results : 
    This will plot the head and tail probabilities over time 
    with the x-axis labeled "Number of Flips" and the y-axis labeled "Probability" 
    """
    plt.plot(heads, 'b', label="Heads")
    plt.plot(tails,'r', label="Tails")
    plt.xlabel("Number of Flips")
    plt.ylabel("Probability")
    plt.legend()
    plt.show()
    # Final Values
    headsprob = heads[-1]  # These values are estimates of the true probabilities of getting heads and tails when flipping a fair coin, based on the outcomes of the simulated coin flips.
    tailsprob = tails[-1]
    heads_per = format(headsprob*100, '.2f')+'%'  # Estimated percentage of heads after running the Monte Carlo simulation for the specified number of iterations.
    tails_per = format(tailsprob*100, '.2f')+'%'  # Estimated percentage of tails after running the simulation for the specified number of iterations.
    print('Percentage of Heads: '+heads_per)
    print('\nPercentage of Tails: '+tails_per)

run_the_simulation(iterations = 1000)