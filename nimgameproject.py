"""
Nim Game

Ely Terrazas

CSC 119

11/14/2021

This program lets the user play the Nim game against the computer

"""
from random import randint


def introducePlayer():
    user=input("Hello whats your name?")
    print("Hello,",user,"!! welcome to the Nim Game today you will be playing against computer")

def howToPlay():
    askHowToPlay=input("Do you know how to play Nim game?(Y/N)")
    if askHowToPlay=="N":
        print("""*****I will gladly explan!!*****
You must remove 1 to 2 marbles from the pile at a time.
If you remove the final marble you lose!
GOOD LUCK!!!""")
    else:
            print("Enjoy the game,GOODLUCK!")


secondPlayer="Computer"
marblePick=0
gameOver=False
marbleAmount=randint(1,50)

if(marbleAmount%4)==1:
    marbleAmount+=1


def takingMarblesComputer():
    takingMarbles=randint(1,2)
    global marbleAmount
    while takingMarbles>marbleAmount:
        takingMarble=randint(1,2)
        marbleAmount-=takingMarble
        return marbleAmount

def takingMarblePlayer():
    global MarbleAmount
    marbleAmount-=marblePick
    return marbleAmount

def validInputs():
    global marblePicks
    validInput=False
    while not validInput:
        print("Your turn,",user)
        marplePick=int(input("How many marbles would you like to take?(1 or 2"))
        if marblePick==1 or marblePick==2:
            print("You took",marblePick,"marbles!")
        else:
            validInput=True
    while marblePick>marbleAmount:
        print("That's too many marbles!")
        marblePick=int(input("How many marbles would you like to take?(1 or 2"))
    return marblePick

def winnerChickenDinner(player):
    if marbleAmount==0:
        print("Congrats",player,"you beat computer!!")
        global gameOver
        gameOver=False
def playAgain():
    global gameOver
    gameOver=False
    return gameOver

def main():
    user=input
    while gameOver==False:
        print("It's Computers turn! There are:",takingMarblesComputer(),"marbles left")
        winnerChickenDinner(user)
        if gameOver==True:
            break
        validInputs()
        print("There are still",takingMarblePlayer,"marbles left")
        winnerChickenDinner(secondPlayer)

def playerPlayAgain():
    playAgain=input(user,"would you like to play again?(Y/N)")
    playagain()
    if answer=="Y":
        game()
    else:
        print("Thank you for playing you did great today!")
main()
playAgain()




















    



















    
        
