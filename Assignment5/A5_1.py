# n*m صفحه ی شطرنجی به ابعاد 

def board(n, m):
    for i in range(n):
        for j in range(m):
            if j%2 == 0 and i%2 == 0 or j%2 !=0 and i%2 !=0:
                print("#", end="")
            else:
                print("*", end="")
        print("")

board(int(input("Please enter n: ")), int(input("please enter m: ")))
