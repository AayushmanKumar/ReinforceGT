def bestResponse(payoff_matrix, player, opponent_action):
    #Initializing empty set to store best responses
    best_actions = set()
    #Initializing payoff with negative infinity
    best_payoff = float('-inf')

#Player 1 has index 0, player 2 has index 1
    payoff_index = 0 if player == 1 else 1

    if player == 1:
        for p1_action in payoff_matrix:
            #Loops through its own actions
            if opponent_action in payoff_matrix[p1_action]:
                current_payoff = payoff_matrix[p1_action][opponent_action][payoff_index]

                if current_payoff > best_payoff:
                    best_payoff = current_payoff
                    #Reset best actions set to only have this one
                    best_actions = {p1_action}
                elif current_payoff == best_payoff:
                    best_actions.add(p1_action)

    elif player == 2:
        if opponent_action not in payoff_matrix:
            return set()
#Loops through player 1's matrix as that's how matrix is give in standard form
        for p2_action in payoff_matrix[opponent_action]:
            current_payoff = payoff_matrix[opponent_action][p2_action][payoff_index]

            if current_payoff > best_payoff:
                best_payoff = current_payoff
                best_actions = {p2_action}
            elif current_payoff == best_payoff:
                best_actions.add(p2_action)
    else:
        raise ValueError("Player must be 1 or 2.")

    return best_actions