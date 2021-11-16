"""
Nim Game

Ely Terrazas

CSC 119

11/14/2021

This program lets the user play the Nim game against the computer

"""



from random import seed,randint
def main():                     # definition of main program
    seed()                      # initialize the random number generator for the game play

    # -------------------------------------------------------
    # INPUT - to randomize the game play
# -------------------------------------------------------
    ballCount = randint(10, 100)# randomly generate the amount of balls to play
    turn = randint(0,1)         # randomly generate who goes first (0) player (1) computer
    mode = randint(0,1)         # randomly generate mode of computer (0) smart (1) stupid

    # -------------------------------------------------------
    # PROCESS - play the game of NIM taking turns
    # -------------------------------------------------------
    print("***** Game of NIM Starts *****")
    while ballCount > 0:        # if there are still balls left, then keep playing
        print("\t\tBall count:", ballCount)
        if turn == 0:           # player turn
            print("\n\tPLAYER TURN")
            playerTurn(ballCount)# TODO: call the playerTurn function 
            turn = 1            # switch the turn 1 - for computer turn next
        else:                   # computer turn
            if mode == 0:       # computer smart mode
                print("\n\tCOMPUTER TURN - Mode: Smart")
                computerSmart(ballCount) # TODO: call the computerSmart function
            else:               # computer hard mode
                print("\n\tCOMPUTER TURN - Mode: Stupid")
                # TODO: call the computerStupid function
            turn = 0            # switch the turn 0 - for player turn next
        # TODO: ballCount needs to be updated for each turn
                
    # -------------------------------------------------------
    # OUTPUT - The player who takes the last ball loses.
    # once the ballCount goes to 0, the turn switches, so it is the other
    # player then that wins
    # -------------------------------------------------------
    print("\t\tBall count:", ballCount)
    if turn == 0 and ballCount == 0:
        print("\n***** GAME of NIM Winner! PLAYER *****\n\n")
    else:
        print("\n***** Game of NIM Winner! COMPUTER *****\n\n")

def playerTurn():
    playerTake=int(input("How many balls would you like to take?(1,2,or 3)"))
    if playerTake==1:
        ballCount=ballCount-1
        print("Ball Count:",ballCount)
        
    if playerTake==2:
        ballCount=ballCount-2
        print("Ball Count:",ballCount)
       
        
    else:
        ballCount=ballCount-3
        print("Ball Count:",ballCount)
     
    
    

def computerSmart():
    computerTurn=randint(1,3)
    ballCount=ballCount-computerTurn
    return ballCount

def validInput():
    playerTake=int(input("How many balls would you like to take?(1,2,or 3)"))
    if playerTake!=int:
        print("Please enter a valid number 1,2, or 3")
    else:
        computerTakeBall()
def playAgain():
    if ballCount==0:
        print("Would you like to play again?(Y/N)")
    if len.upper=="Y":
        main()
    else:
        print("Have a nice day!Thank You for playing!")
    
        
        

main()          # execution of main program

















    



















    
        
