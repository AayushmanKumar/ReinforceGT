payoff = {
    "C": {
        "C": (3,3),
        "D": (0,5)
    },
    "D": {
        "C": (5,0),
        "D": (1,1)
    }
}

def isNash(p1,p2):
    if payoff[p1][p2][0] < payoff["C"][p2][0] or payoff[p1][p2][0] < payoff["D"][p2][0]:
        return False
    if payoff[p1][p2][1] < payoff[p1]["C"][1] or payoff[p1][p2][1] < payoff[p1]["D"][1]:
        return False
    
    return True

# Checking all combinations of strategies to find Nash equilibria
comb= [("C","C"),("C","D"),("D","C"),("D","D")]
nash_eqbm = []

for p1, p2 in comb:
    if isNash(p1, p2):
        nash_eqbm.append((p1, p2))

# Print the Nash equilibria
print("Nash Equilibria attained for:", nash_eqbm)


# Output
'''
Nash Equilibria attained for: [('D', 'D')]
'''