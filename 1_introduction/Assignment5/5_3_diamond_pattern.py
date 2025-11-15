# Diamon with row of n
def Diamond(n: int):
    
    for row in range(n):
        for empty in range(n-row-1):
            print(" ", end="")
        for star in range(2*row+1):
            print("*", end="")
        print("")
    for row in range(n-1):
        for empty in range(row+1):
            print(" ", end="")
        for star in range((2*n-1)-(2*(row+1))):
            print("*", end="")
        print("")

Diamond(int(input("Please enter n: ")))
    


