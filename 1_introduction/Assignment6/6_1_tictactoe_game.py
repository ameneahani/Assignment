import pyfiglet
import random
import colorama
import time
# title = pyfiglet.figlet_format("Tic Tac Toe", font= "banner")
# print(title)

game_board = [["-","-","-"],["-","-","-"],["-","-","-"]]

def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(colorama.Fore.RED+cell,colorama.Fore.RESET,end="")
            elif cell== "O":
                print(colorama.Fore.BLUE+cell,colorama.Fore.RESET,end="")
            else:
                print (cell,end=" ")
        print()

def vared_kon():
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] != "-":
                print("Dont cheet!! ")
            else:
                break
        else:
            print("Enter correctly! ")
    return(row, col)

def check_game(player):
    check_d1 = 0
    check_d2 = 0
    check_equal = 0
    for i in range(3):
        check_row = 0
        check_col = 0
        for j in range(3):
            if game_board[i][j] == player:
                check_row = check_row +1
            if game_board[j][i] == player:
                check_col = check_col + 1
            if i == j and game_board[i][j] == player:
                check_d1 = check_d1 +1
            if i+j ==2 and game_board[i][j] == player:
                check_d2 = check_d2 +1
            if game_board[i][j] != "-":
                check_equal += 1
        if check_row == 3 or check_col == 3 or check_d1 == 3 or check_d2 == 3:
            return(1)
    if check_equal == 9:
        return("equal")

show()
while True:
    select = int(input("Please enter number: \n 1: 2 player \n 2: with computer"))
    if 1 <= select <= 2:
        break
    else :
        print("Enter correct number") 

while True:
    start=time.time()
    print("player 1")
    input_choice = vared_kon()
    game_board[input_choice[0]][input_choice[1]] = "X"
    show()
    if check_game("X") == 1:
        print("player1 Win!")
        break
    elif check_game("equal") == "equal":
        print("Equal!!")
        break
    if select == 1:
        print("player 2")
        input_choice = vared_kon()
    
    elif select == 2:
        print("computer: ")
        while True:
            input_choice = [random.randint(0,2), random.randint(0,2)]
            if game_board[input_choice[0]][input_choice[1]] == "-":
                break
    game_board[input_choice[0]][input_choice[1]] = "O"

    show()
    if check_game("O") == 1:
        if select == 1:
            print("plarer2 Win!")
        else:
            print("Computer Win!")
        break

print("Game Time:",str(time.time()-start), "second")



