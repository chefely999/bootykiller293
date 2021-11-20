\"""
Game of Nim from Python for Everyone 3rd edition
"""



"""
main() written by: Joseph Adams
This main function is the game play driver for Game of NIM.
"""
from random import seed, randint
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
            #we call playerTurn function with ballCount argument to continue updating amount
            ballCount= ballCount-(playerTurn(ballCount))
            turn = 1            # switch the turn 1 - for computer turn next
        else:                   # computer turn
            if mode == 0:       # computer smart mode
                print("\n\tCOMPUTER TURN - Mode: Smart")
                #we call computerSmart with ballCount to update the count with what the smart computer takes
                ballCount=ballCount-(computerSmart(ballCount))
            else:               # computer hard mode
                print("\n\tCOMPUTER TURN - Mode: Stupid")
                #computer stupid is called if it is picked and also updates ballCount whenever it picks an amount
                ballCount=ballCount-(computerStupid(ballCount))
            turn = 0            # switch the turn 0 - for player turn next
        # TODO: ballCount needs to be updated for each turn
                
    # -------------------------------------------------------
    # OUTPUT - The player who takes the last ball loses.
    # once the ballCount goes to 0, the turn switches, so it is the other
    # player then that wins
    # -------------------------------------------------------
    print("\t\tBall count:", ballCount)
    if turn == 0 and ballCount == 0:
        print("\n***** GAME of NIM Winner! PLAYER!You beat computer what a beast!!! *****\n\n")
    else:
        print("\n***** Game of NIM Winner! COMPUTER!Better luck next time Player computer is really smart!!*****\n\n")

"""
     this function asks the player wether they want to take 1,2, or 3 balls
     and depending on the amount of balls taking will print if it is an approriate amount to take if not will ask them to pick an amount again.
"""
def playerTurn(ballCount):
    ballsTaken= int(input("How many balls do you wish to take?(1,2, or 3)"))
    if ballsTaken<1:
            ballsTaken=int(input("How many balls do you wish to take?(1,2, or 3)"))
    
    elif ballsTaken> ballCount/2:
        if ballCount==1:
            ballsTaken=1
        #if player tries to take more than half will give prompt to pick again 
        elif ballCount==2:
            print("You must take at least 1 ball.")
            ballsTaken=1
            
        else:
            #game will try to make it fair so player cant take all thats left and force computer to lose
            ballsTaken= int(input("Cannot take more than half!How many balls do you wish to take?(1,2, or 3)"))
    return ballsTaken

"""
if the computer stupid is selected the computer will take predictable amount of balls and return the updated amount of ballCount
"""
def computerStupid(ballCount):
    if ballCount==1:
        ballsTaken=1
    #does not let amount taken to be more than half of available amount
    elif ballCount==2:
         ballsTaken=1
    else:
        ballsTaken= randint(1, ballCount//2)
    return ballsTaken
"""
computer smart function takes the initial amount of balls and figures out the best way to get the ball count down to zero with more complicated math than computer stupid
"""
def computerSmart(ballCount):
    if ballCount>63:
        #smart computer checks amount beginning with
        ballsTaken=ballCount-63
    elif ballCount>31 and ballCount<63:
        ballsTaken= ballCount-31
    elif ballCount>15 and ballCount<31:
        ballsTaken=ballCount-15
    elif ballCount>7 and ballCount <15:
        ballsTaken=ballCount-7
    elif ballCount>3 and ballCount<7:
        ballsTaken=ballCount-3
        #once ballCount has reached a low amount the smart computer function will see how many are left and take just the right amount so the player is forced to be the one with no balls left and lose
    else:
        if ballCount==1:
            ballsTaken=1
        elif ballCount==2:
            ballsTaken=1
        else:
            ballsTaken= randint(1, ballCount//2)
    return ballsTaken
    
    
    

main()    
