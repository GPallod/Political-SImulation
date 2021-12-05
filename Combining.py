from Gerrymandering import display, TallyVote
from Continuing_Election import next_ballot, Tally, run_model, initialize
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# Makes a country filled with voters
def init_nation(num_states, num_voters, props, bounds=[0.5, 1]):
    """takes number of states and voters and proportions, and spits out a list of them"""
    nation = []
    voters_state = num_voters / num_states

    if num_voters % num_states != 0:
        return 'Arey'

    for i in np.arange(num_states):
        state = initialize(props[i], voters_state, bounds)
        nation += [state]
    return nation


def NationalTally(nation):  # Tallies votes at a national level
    senators = []
    for state in nation:
        senator = Tally(state)[0]  # Winner of State
        senators.append(senator)
    return TallyVote(senators)


def next_national_election(nation):  # Figures out the next year's national ballot
    new_nation = []
    for state in nation:
        new_state = [next_ballot(state)]
        new_nation += new_state
    return new_nation


# Runs the full model and plots
def run_full_model(num_states, num_voters, props, num_repitions, bounds=[0.5, 1], plot=True, title=''):
    nation = init_nation(num_states, num_voters, props, bounds)
    tallies = []
    for i in np.arange(num_repitions):
        tally = NationalTally(nation)
        nation = next_national_election(nation)
        election_results = 1 - tally[1]
        if tally[0] == 1:  # Just extracts the percentage of votes for 1, otherwise called the Election Result
            election_results = tally[1]
            # election_results = abs(tally[1] + tally[0] - 1) # same as the above
        tallies.append(election_results)

    if plot:
        fig, ax = plt.subplots(nrows=num_states, sharex=True)
        ax[num_states//2].set_ylabel('Percentage of votes for Party 1')
        ax[0].set_title('Each State Election Results for Years ' + title)
        for i in np.arange(num_states):
            state = nation[i]
            ax[i].plot(run_model(state, 100))
            ax[i].set_xlabel('State ' + str(i+1))
            ax[i].set_ylim(0, 1)
        plt.tight_layout()
        fig1, ax1 = plt.subplots()
        ax1.plot(tallies)
        ax1.set_ylabel('Percentage of votes for Party 1')
        ax1.set_title('National Election Results for Years ' + title)
        ax1.set_xlabel('Election Year Number')
        ax1.set_ylim(0, 1)
        # ax1.plot([0.5]*num_repitions)
        plt.show()
    return tallies


# run_full_model(5, 100, [0.1, 0.2, 0.6, 0.8, 0.9], 100)

# G0 = run_full_model(5, 500, [0.4]*5, 100, title='G0')
# Gf = run_full_model(5, 500, [1, 1, 0, 0, 0], 100, title='Gf')
# G1 = run_full_model(5, 500, [0.8, 0.6, 0.6, 0, 0], 100, title='G1')

ns = 5  # num_states must be multiple of 5
G0 = run_full_model(ns, 500, [0.4]*ns, 100, [0.4, 1])
# Gf = run_full_model(ns, 500, [1]*int(ns*0.4) + [0]*int(ns*0.6), 20, [0.4, 0.7], title='Gfair')
# G1 = run_full_model(ns, 500, [0.9]*int(ns*0.2) + [0.7] *
#                     int(ns*0.4) + [0]*int(ns*0.4), 25, title=' G1')


# Observations -
# Gerrymandering is dampened by the 'Lazy Voter' effect. I think
