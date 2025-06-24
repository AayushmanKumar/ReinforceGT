Payoff_Mat={('C', 'C'): (3,3), ('C', 'D'): (0,5), ('D', 'C'): (5,0), ('D', 'D'): (1,1)}
strategies=[('C', 'C'), ('C', 'D'), ('D', 'C'), ('D', 'D')]
def correct_dicision(strategies):
    nash_equilibria=[]
    for set in strategies:
        change2=False
        change1=False
        p1,p2=set
        p1_payoff,p2_payoff=Payoff_Mat[(p1, p2)]

        for choice in ['C', 'D']:
            if choice!=p1:
                new_pay_off1=Payoff_Mat[choice, p2][0]
                if new_pay_off1 > p1_payoff:
                    # return False
                    change1=True
                
        for choice in ['C', 'D']:
            if choice!=p2:
                new_pay_off2=Payoff_Mat[p1, choice][1]
                if new_pay_off2 > p2_payoff:
                    # return False
                    change2=True

        if not change1 and not change2:
            nash_equilibria.append(set)
        
    return nash_equilibria
        
print( correct_dicision(strategies)," is a Pure Nash Equilibrium.")

# Payoff_Mat = {
#     ('C', 'C'): (3, 3),
#     ('C', 'D'): (0, 5),
#     ('D', 'C'): (5, 0),
#     ('D', 'D'): (1, 1)
# }

# strategies = [('C', 'C'), ('C', 'D'), ('D', 'C'), ('D', 'D')]

# def correct_decision(strategies):
#     nash_equilibria = []

#     for s in strategies:
#         p1, p2 = s
#         p1_payoff, p2_payoff = Payoff_Mat[(p1, p2)]

#         # Initialize flags
#         p1_can_improve = False
#         p2_can_improve = False

#         # Check if Player 1 can improve by changing strategy
#         for alt_p1 in ['C', 'D']:
#             if alt_p1 != p1:
#                 if Payoff_Mat[(alt_p1, p2)][0] > p1_payoff:
#                     p1_can_improve = True
#                     break

#         # Check if Player 2 can improve by changing strategy
#         for alt_p2 in ['C', 'D']:
#             if alt_p2 != p2:
#                 if Payoff_Mat[(p1, alt_p2)][1] > p2_payoff:
#                     p2_can_improve = True
#                     break

#         # If no one can improve, it's a Nash Equilibrium
#         if not p1_can_improve and not p2_can_improve:
#             nash_equilibria.append(s)

#     return nash_equilibria

# # Output result
# print("Pure Nash Equilibria:", correct_decision(strategies))
