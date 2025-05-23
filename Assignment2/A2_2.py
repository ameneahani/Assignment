# Rock, Scissors, Paper Game
import random
human_score = 0
computer_score = 0
human_choice = 0
while True:
    computer_choice = random.randint(0,3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "scissors"
    elif computer_choice == 3:
        computer_choice = "paper"
    human_choice = input("enter your choice or type exit \n rock or sissors or paper: ")

    if (human_choice == "rock" and computer_choice == "scissors") or (human_choice == "scissors" and computer_choice == "paper") or (human_choice == "paper" and computer_choice == "rock") :
        human_score = human_score +1
    elif (computer_choice == "rock" and human_choice == "scissors") or (computer_choice == "scissors" and human_choice == "paper") or (computer_choice == "paper" and human_choice == "rock") :
        computer_score =computer_score +1
    if human_choice == "exit":
        break
    print("computer choice:", computer_choice, "\n human choice: ", human_choice)

print("computer score :", computer_score, "human score : ", human_score)
if computer_score > human_score :
    print(" You Faile")
elif computer_score < human_score :
    print("You Win")
else :
    print("You are equal")


