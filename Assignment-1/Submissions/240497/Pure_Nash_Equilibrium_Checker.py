# Payoff matrix where payoff[s1][s2] = (player1's payoff, player2's payoff) when player1 chooses s1 and player2 chooses s2

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

def isNash(s1,s2):
    # Player 1
    if s1 == "C":
        if(payoff["D"][s2][0] > payoff[s1][s2][0]):
            return False
    else:
        if(payoff["C"][s2][0] > payoff[s1][s2][0]):
            return False
    
    # Player 2
    if s2 == "C":
        if(payoff[s1]["D"][1] > payoff[s1][s2][1]):
            return False
    else:
        if(payoff[s1]["C"][1] > payoff[s1][s2][1]):
            return False
    
    return True

# Check all combinations of strategies to find Nash equilibria
profiles= [("C","C"),("C","D"),("D","C"),("D","D")]
nash_equilibria = []

for s1, s2 in profiles:
    if isNash(s1, s2):
        nash_equilibria.append((s1, s2))

# Print the Nash equilibria
print("Nash Equilibria:")
for equilibrium in nash_equilibria:
    print(equilibrium)
