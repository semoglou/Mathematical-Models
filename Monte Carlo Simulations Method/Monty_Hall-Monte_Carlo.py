import random
import matplotlib.pyplot as plt

""" Solving the Monty Hall Problem with Monte Carlo Simulation """

Doors = ['goat', 'car', 'goat']

def monte_carlo(iterations):
    switchdoor_win_probability = []
    stickdoor_win_probability = []
    switch_win = 0                            # Counters
    stick_win = 0
    for i in range(iterations):
        random.shuffle(Doors)
        door = random.randrange(0,2)
        choice = Doors[door]
        if choice != 'car':                      # Switching would be the right move
            switch_win += 1
        else:                                    # Sticking would be the right move
            stick_win += 1
        win_by_switch_prob = switch_win / (i+1)          
        win_by_stick_prob = stick_win / (i+1)
        switchdoor_win_probability.append(win_by_switch_prob)
        stickdoor_win_probability.append(win_by_stick_prob)
    return switchdoor_win_probability, stickdoor_win_probability           # The Final values of the list are the "strategy"-probabilities

def monty_hall(iterations):
    switchdoor_win_probability, stickdoor_win_probability = monte_carlo(iterations)
    switch, stick = switchdoor_win_probability[-1], stickdoor_win_probability[-1]           
    print('Always switching winning probability: ',format((switch*100),'.2f')+'%\n')
    print('Always sticking winning probability: ',format((stick*100),'.2f')+'%')
    plt.figure()
    plt.grid()
    plt.title('Winning Probability')
    plt.plot(switchdoor_win_probability, 'b', label = 'Switch Door')
    plt.plot(stickdoor_win_probability, 'r', label = 'Stick to Door')
    plt.xlabel('Iterations')
    plt.ylabel('Probability')
    plt.ylim([0,1])
    plt.legend()
    plt.show()

monty_hall(10000)
