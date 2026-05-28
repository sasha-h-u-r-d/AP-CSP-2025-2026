#Sasha Hurd-Groves
#"Rock-Paper-Scissors" Game
#In this programming assignment, you will create a simple Python program that allows the player to play the classic game of "Rock-Paper-Scissors" against the computer. The game involves selecting either rock, paper, or scissors and comparing the choices to determine the winner. The program should also keep track of the score and give the player the option to play again.

#Import
import random
import time
#Function

def rps():
    global score
    global computer
    global move
    score=0
    print("Welcome to Rock-Paper-Scissors")
    play=input("What would you like to do: play, play again, or quit: ")
    while play=="play" or "play again":
        move=input("What's your move: ")
        print("You chose", move)
        if move=="rock":
            rock()   #changes into all of the seperate games
        if move=="paper":
            paper()
        if move=="scissors":
            scissors()
        else:
            print("uh oh I don't think the computer can fight against that. Could you try again?")
        print("Score=",score)
        again=input("Would you like to play again? ")
        if again=="yes":
            play=="play again"
        if again=="no": #changes play to make it false to break the loop
            play=="quit"
            break


def rock():
    global move
    global score
    global computer
    computer=random.randint(1,3)
    if computer==1:
        time.sleep(1)
        print("Computer chose rock")
        print("Tie")
        score=score+0

    if computer==3:
        time.sleep(1)
        print("Computer chose rock")
        print("You lost")
        score=score+0

    if computer==2:
        time.sleep(1)
        print("Computer chose rock")
        print("You won")
        score=score+1



def scissors():
    global move
    global score
    global computer
    computer=random.randint(1,3)
    if computer=="2":
        time.sleep(1)
        print("Computer chose scissors")
        print("Tie")
        score=score+0

    if computer=="1":
        time.sleep(1)
        print("Computer chose scissors")
        print("You lost")
        score=score+0

    if computer=="3":
        time.sleep(1)
        print("Computer chose scissors")
        print("You won")
        score=score+1



def paper():
    global move
    global score
    global computer
    computer=random.randint(1,3)
    if computer=="3":
        time.sleep(1)
        print("Computer chose paper")
        print("Tie")
        score=score+0

    if computer=="2":
        time.sleep(1)
        print("Computer chose paper")
        print("You lost")
        score=score+0

    if computer=="1":
        time.sleep(1)
        print("Computer chose paper")
        print("You won")
        score=score+1
    






#Main
rps()



