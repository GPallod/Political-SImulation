import numpy as np  # Import

# Initializing
total_votes = []
num_voters = 12
prop = 0.5

for i in range(num_voters):
    if i < prop * num_voters:
        vote = 1
    else:
        vote = 0
    total_votes.append(vote)

# votes = np.append(np.ones(prop * num_voters), np.ones((1 - prop) * num_voters)) # Does the same thing as above
# print(total_votes)

# Defining Functions


def TallyVote(votes):
    winner = np.random.randint(0, 2)
    percent = np.mean(votes)  # Percent votes for 1
    if percent != 0.5:
        winner = round(percent)
    if winner == 0:
        percent = 1 - percent  # If winner is 0, then the percent of winning votes is just 1 minus that
    return [winner, percent]


def display(all_votes):
    final_result = [TallyVote(state)[0] for state in all_votes]
    print('State Votes = ', final_result, 'Winner = ', TallyVote(final_result)[0])


# Gerrymander 1
State1 = [1, 1, 1, 1]
State2 = [0, 0, 0, 0]
State3 = [1, 1, 0, 0]
all_votes = [State1, State2, State3]
# print(all_votes)

# display(all_votes)
