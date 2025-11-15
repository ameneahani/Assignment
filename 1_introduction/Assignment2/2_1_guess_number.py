import random

computer_num = random.randint(0,10)
number_of_geuss = 0

while True :
    human_num = input("please enter your number between (0 10) or type exit: ")
    number_of_geuss = number_of_geuss + 1
    if human_num == "exit":
        break
    human_num = int(human_num)
    if human_num < computer_num:
        print("Go Up")
    elif human_num > computer_num :
        print("Go Down")
    else :
        print("You Win after", number_of_geuss, "tryied")
        break
    





