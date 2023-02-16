import numpy as np
import matplotlib.pyplot as plt

def random_walk(num_steps):
    """Simulate a 1D random walk of a specified number of steps."""
    # Define the set of possible steps
    steps = [-1, 1]
    
    # Initialize the position and the list of positions over time/steps
    pos = 0 # Initial Position / Origin
    positions = [pos]
    
    # Take the specified number of steps
    for i in range(num_steps):
        # Randomly select a step
        step = np.random.choice(steps)
        
        # Update the position
        pos += step
        
        # Append the new position to the list of positions
        positions.append(pos)
    
    return positions

def monte_carlo_random_walk(num_walks, num_steps):
    """Simulate a random walk a specified number of times using a Monte Carlo simulation.
    
    Args:
        num_walks (int): The number of times to simulate a random walk.
        num_steps (int): The number of steps to take for each random walk.
    
    Returns:
        list: A list of lists, where each inner list represents the positions over time/steps for a single random walk.
    """
    # Initialize a list to hold the positions over time for each random walk
    positions_over_time = []
    
    for i in range(num_walks):
        # Perform a random walk and add the positions over time to the list
        positions = random_walk(num_steps)
        positions_over_time.append(positions)
        
    return positions_over_time

def monte_carlo_return_to_origin(num_walks, num_steps):
    """Simulate a random walk a specified number of times using a Monte Carlo simulation and calculate the 
        probability of returning to the origin for each step of the walk.
    
    Args:
        num_walks (int): The number of times to simulate a random walk.
        num_steps (int): The number of steps to take for each random walk.
    
    Returns:
        list: A list of floats representing the probability of returning to the origin for each step of the walk.
    """
    # Perform the random walks and get the positions over time
    positions_over_time = monte_carlo_random_walk(num_walks, num_steps)
    
    # Initialize a list to hold the probability of returning to the origin for each step of the walk
    prob_return_to_origin = [0.0] * num_steps
    
    # For each step of the walk, calculate the probability of returning to the origin
    for i in range(1, num_steps):
        num_returned_to_origin = 0
        
        # Count the number of walks that returned to the origin at this step
        for positions in positions_over_time:
            if positions[i] == 0:
                num_returned_to_origin += 1
        
        # Calculate the probability of returning to the origin at this step
        prob_return_to_origin[i] = num_returned_to_origin / num_walks
    
    return prob_return_to_origin # list, which holds the estimated probabilities of returning to the origin for each step of the walk.

def returned(positions_over_time, num_walks):
    # Count the number of walks that returned to the origin
    num_returned_to_origin = 0
    for positions in positions_over_time:
      if positions[-1] == 0:
        num_returned_to_origin += 1
    # Calculate the probability of returning to the origin
    prob_return = num_returned_to_origin / num_walks
    print("Probability of returning to the origin: ", format(prob_return*100, '.2f')+'%')

def Plot(num_walks, num_steps):

    positions_over_time = monte_carlo_random_walk(num_walks, num_steps)
    prob_return_to_origin = monte_carlo_return_to_origin(num_walks, num_steps)

    # Plot the positions over time/steps for a few (5) random walks
    plt.figure()
    for positions in positions_over_time[:5]:
        plt.plot(positions)
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.title("Random Walks")

    # Plot the probability of returning to the origin over time/steps
    plt.figure()
    plt.plot(prob_return_to_origin)
    plt.xlabel("Step")
    plt.ylabel("Probability of returning to origin")
    plt.title("Probability of Returning to the Origin for a Random Walk")
    plt.show()

    returned(positions_over_time, num_walks)

Plot(num_walks = 1000, num_steps = 100)