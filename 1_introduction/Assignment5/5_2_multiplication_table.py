#multiplication table n*m

def multy_table(n: int, m: int):
    for row in range(1,n+1):
        for column in range(1,m+1):
            print(row*column, end="  ")
        print("")

multy_table(int(input("Please enter n: ")), int(input("please enter m: ")))
