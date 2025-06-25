def best_response(payoff,player,opponent_action):
    best=float('-inf')
    actions = set()
    if(player==1):
        # Finds the payoff for the best response of player 1
        for action in payoff:
            best=max(best,payoff[action][opponent_action][0])

        # Collects all actions that yield the best response for player 1
        for action in payoff:
            if(payoff[action][opponent_action][0]==best):
                actions.add(action)
    else:
        # Finds the payoff for the best response of player 2
        for action in payoff:
            best=max(best,payoff[opponent_action][action][1])

        # Collects all actions that yield the best response for player 2
        for action in payoff:
            if(payoff[opponent_action][action][1]==best):
                actions.add(action)
    
    return actions

# Example usage
payoff = {
    'Bach': {'Bach':(2, 1), 'Stravinsky': (0, 0)},
    'Stravinsky': {'Bach':(0, 0), 'Stravinsky': (1, 2)}
}

print(best_response(payoff, 1, 'Bach'))