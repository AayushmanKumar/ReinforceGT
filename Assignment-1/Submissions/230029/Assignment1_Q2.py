payoff_matrix = {'Bach': {'Bach': (2, 1),'Stravinsky': (0, 0)},'Stravinsky': {'Bach': (0, 0),'Stravinsky': (1, 2)}}

def best_response(payoff_matrix, player, opponent_action):
    best_resp=set()
    max=-1

    for action in payoff_matrix:
        payoff=payoff_matrix[action][opponent_action][player - 1]
        if payoff > max:
            max=payoff
            best_resp={action}
        elif payoff == max:
            best_resp.add(action)

    return best_resp

print(best_response(payoff_matrix, 1, 'Bach'))