payoff = {
    "C": {
        "C": (2,1),
        "D": (0,5)
    },
    "D": {
        "C": (0,0),
        "D": (1,2)
    }
}

def best_action(payoff_matrix, player, opponent_action):
    if player==1:
        p2=action_encoding[opponent_action]
        if payoff['C'][p2][0]>=payoff['D'][p2][0]:
            return action_encoding['C']
        else:
            return action_encoding['D']
    else:
        p1=action_encoding[opponent_action]
        if payoff[p1]['C'][1]>=payoff[p1]['D'][1]:
            return action_encoding['C']
        else:
            return action_encoding['D']

action_encoding={
    'Bash': 'C',
    'Stravinsky': 'D',
    'C': 'Bash',
    'D': 'Stravinsky'
}

print("Best action for player 1 against opponent's action 'C':", best_action(payoff, 1, 'Bash'))

# Output
'''
Best action for player 1 against opponent's action 'C': Bash
'''