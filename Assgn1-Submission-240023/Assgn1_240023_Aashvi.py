def pureNash(profile):

    #Define payoff matrix
    payoffs = {
        ('C','C'): (3, 3),
        ('C','D'): (0, 5),
        ('D','C'): (5, 0),
        ('D','D'): (1, 1)
    }
    strat = ['C','D']

    # Check input
    if profile not in payoffs:
        print("Invalid input. Use only 'C' or 'D' for each player.")
        return False

    p1_strat, p2_strat = profile
    p1_payoff, p2_payoff = payoffs[profile]

    # Check if Player 1 can benefit by devaiting
    for alt_p1 in strat:
        if alt_p1 != p1_strat:
            alt_profile = (alt_p1, p2_strat)
            if payoffs[alt_profile][0] > p1_payoff:
                return False

    # Check if Player 2 can benefit by devaiting
    for alt_p2 in strat:
        if alt_p2 != p2_strat:
            alt_profile = (p1_strat, alt_p2)
            if payoffs[alt_profile][1] > p2_payoff:
                return False

    return True

# Get input 
input_str = input("Enter strategy profile(eg. C D): ").strip().upper()
profile = tuple(input_str.split())

if len(profile) != 2:
    print("Please enter exactly two strategies(eg. C D)")
else:
    if pureNash(profile):
        print(f"{profile} is a Pure Nash Equilibrium.")
    else:
        print(f"{profile} isn't a Pure Nash Equilibrium.")
