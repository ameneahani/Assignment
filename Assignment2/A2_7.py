#Fibonacci sequence
n = int(input("Welcome to making Fibonacci sequence programm \n Please enter n : "))
a = 1
b = 0
if n<1:
    print("n is invalid")

for i in range(1,n+1):

    c = a+b
    a = b
    b = c
    print(c)

