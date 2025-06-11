# Assignment_1 Adhitya ST 240044


#Question 1:

def purenash(strategyprofile,payoffmatrix):

    for i in range (0,2):
        for j in range (0,2):
            if payoffmatrix[i][j]==strategyprofile:
                x=i
                y=j

    if x==0: 
        a='C'
    elif x==1:
        a='D'

    if y==0: 
        b='C'
    elif y==1:
        b='D'

    

    # Used loops to find the position of the required strategy profile 

    ispne1=0    # flag to check improvement in each player's position
    ispne2=0

    # Checking improvement for Player 1

    if(x==1):
        if payoffmatrix[x][y][0]>=payoffmatrix[x-1][y][0]:
            ispne1=1

    if(x==0):
        if payoffmatrix[x][y][0]>=payoffmatrix[x+1][y][0]:
            ispne1=1

    # Checking improvement for Player 2

    if(y==1):
        if payoffmatrix[x][y][1]>=payoffmatrix[x][y-1][1]:
            ispne2=1

    if(y==0):
        if payoffmatrix[x][y][1]>=payoffmatrix[x][y+1][1]:
            ispne2=1

    if(ispne1 and ispne2): #only if there is no improvement in both player's positions
         print("({}, {}) is a Pure Nash Equilibrium.".format(a, b))
    else:
        print("({}, {}) is NOT a Pure Nash Equilibrium.".format(a, b))



#__main__        

payoffmatrix= [
                [(3,3), (0,5)],         #using same matrix for both questions
                [(5,0), (1,1)]
                ]
                
                # This is a 2D matrix where each element is a strategy profile. Row 1: Player 1 chooses C
                # Column 1: Player 2 chooses C


for i in range (0,2):
        for j in range (0,2):
            purenash(payoffmatrix[i][j],payoffmatrix) 

            # Applying the function for each strategy profile 


#----------------------------------------------------------------------------------------------------

#Question 2:

def best_response(payoffmatrix, player, opponentaction): #best response of the player given

    if player==1: #Checking the move for player one


        if opponentaction=='C' or opponentaction=='c': #move by player 2
            if payoffmatrix[0][0][0]>payoffmatrix[1][0][0]:
                print("Player 1 should Cooperate.")
            else:
                print("Player 1 should Defect.") #checking the strategy profile for greater position


        elif opponentaction=='D' or opponentaction=='d' :
            if payoffmatrix[0][1][0]>payoffmatrix[1][1][0]:
                print("Player 1 should Cooperate.")
            else:
                print("Player 1 should Defect.")


    else:       #Checking the move for player two

        if opponentaction=='C' or opponentaction=='c': #move by player 1
            if payoffmatrix[0][0][1]>payoffmatrix[0][1][1]:
                print("Player 2 should Cooperate.")
            else:
                print("Player 2 should Defect.") #checking the strategy profile for greater position


        elif opponentaction=='D' or opponentaction=='d' :
            if payoffmatrix[1][0][1]>payoffmatrix[1][1][1]:
                print("Player 2 should Cooperate.")
            else:
                print("Player 2 should Defect.")


#__main__

player=int(input("\n\nWhose best response do you want to see? Type 1 or 2:"))
opponentaction=input("\nWhat is the opponent action?\nType C for Cooperate and D for Defect:")

best_response(payoffmatrix, player, opponentaction)
