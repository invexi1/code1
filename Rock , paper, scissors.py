import random

Player_Turn = input("What do you pick rock, paper, or scissors?")

#Cpu_Number = (random.randint("Rock", "Paper", "Scissors"))
Cpu_Number = (random.randint(1 , 3))

if Cpu_Number == 1:
    Cpu_Turn = "Rock"

elif Cpu_Number == 2:
    Cpu_Turn = "Paper"

elif Cpu_Number == 3:
    Cpu_Turn = "Scissors"

print("Computer Picks " + Cpu_Turn)


if Player_Turn == "rock" and Cpu_Turn == "Rock":
    print("Draw! Play again")

if Player_Turn == "paper" and Cpu_Turn == "Paper":
    print("Draw! Play again")

if Player_Turn == "scissors" and Cpu_Turn == "Scissors":
    print("Draw! Play again")



if Player_Turn == "rock" and Cpu_Turn == "Scissors":
    print("Congratulations, you won! :)")

if Player_Turn == "rock" and Cpu_Turn == "Paper":
    print("Sorry, you lost :(")




if Player_Turn == "paper" and Cpu_Turn == "Rock":
    print("Congratulations, you won! :)")

if Player_Turn == "paper" and Cpu_Turn == "Scissors":
    print("Sorry, you lost :(")



if Player_Turn == "scissors" and Cpu_Turn == "Paper":
    print("Congratulations, you won! :)")

if Player_Turn == "scissors" and Cpu_Turn == "Rock":
    print("Sorry, you lost :(")