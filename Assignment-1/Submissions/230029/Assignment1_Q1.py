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