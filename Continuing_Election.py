""" This program checks the threshold of each voter.
And if his/her party gets more votes than their threshold, then the voter doesn't vote in the next election"""

import numpy as np
import matplotlib.pyplot as plt
from Gerrymandering import TallyVote

# Initializing


def initialize(prop, num_voters, bounds=[0.5, 1]):
    agents = []
    for i in np.arange(num_voters):
        if i < prop * num_voters:
            preference = 1
        else:
            preference = 0
        actually = True
        # if result > threshold, then voter will not vote next election
        threshold = np.round(np.random.uniform(bounds[0], bounds[1]), 3)  # uniform distribution
        # threshold = np.round(np.random.uniform(0.75, 0.125), 3)  # normal distribution
        agents.append([preference, actually, threshold])
    return agents

# Defining Functions


def Tally(agents):  # Tallying with agents
    # First, check if anybody is voting at all
    # if nobody is voting, then everybody is voting the same way (not true, but okay)
    check = False
    for agent in agents:
        check = check or agent[1]
    if not check:
        return [agents[0][0], 1]

    votes = [agent[0] for agent in agents if agent[1]]
    return TallyVote(votes)


def next_ballot(agents):  # If win margin > threshold, then voter too lazy to vote next time
    local_result = Tally(agents)
    local_winner = local_result[0]
    margin_win = local_result[1]

    if margin_win == 0.5:
        return agents

    next_voters = []
    for agent in agents:
        preference = agent[0]
        threshold = agent[2]

        if local_winner == preference and margin_win > threshold:
            next_actually = False
        else:
            next_actually = True
        # next_actually = not ((local_winner == preference) and (margin_win > threshold)) # Same as above
        next_voters.append([preference, next_actually, threshold])
    return next_voters


statey = [[1, True, 0.546], [0, True, 0.85], [0, True, 0.55]]
# print(next_ballot(statey))


def run_model(agents, num_repitions, plot=False, limits=True):  # Running the Model many times
    tallies = []

    for i in range(num_repitions):
        tally = Tally(agents)
        agents = next_ballot(agents)
        if tally[0] == 1:  # Just extracts the percentage of votes for 1, otherwise called the Election Result
            election_results = tally[1]
        else:
            election_results = 1 - tally[1]
        # election_results = abs(tally[1] + tally[0] - 1) # same as the above
        tallies.append(election_results)

    if plot:
        plt.plot(tallies)
        plt.title('State Elections over Numerous Years')
        plt.ylabel('Percentage of votes for Party 1')
        plt.xlabel('Election Year Number')
        if limits:
            plt.ylim(0, 1)
        plt.show()

    return tallies


def varying_prop():
    for r in np.arange(0.1, 1.1, 0.1):
        agents = initialize(r, 100)
        run_model(agents, 100)


# print(agents)
# for i in range(5):
#     agents = initialize(0.8, 100)
#     run_model(agents, 20, True)

# varying_prop()
# run_model(initialize(100, 0.4), 100, True)


# Observations -
# Sometimes it just dies out, sometimes its stuck in a 2 cycle, sometimes it is just a flat line (when prop = 0.5)
