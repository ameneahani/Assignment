import math
print("Welcome to my calculator")
a =float(input("Enter your first number :"))
print("+   -   *   / \nsin   cos   tan   cot \nfactorial   sqrt")
op =input("Select an operator :")

if op== "+" or op== "-" or op== "*" or op=="/":
    b =float(input("Enter your second number : "))
    if op == "+":
        c = a+ b
    elif op == "-":
        c = a -b
    elif op == "*":
        c = a * b
    elif op == "/":
        if b !=0:
            c = a /b
        else:
            print("Not found")
elif op == "sin" or "cos" or "tan" or "cot":
    a = a *math.pi/180
    if op == "sin":
        c = math.sin(a)
    elif op == "cos":
        c = math.cos(a)
    elif op == "tan":
        if a == 90 or a == 270:
            print("Not found")
        else:
            c = math.tan(a)
    elif op == "cot":
        if a==0 or a==180 or a==360:
            print("Not found")
        else:
            c = 1/math.tan(a)
elif op == "sqrt":
    c = math.sqrt(a)
elif op == "factorial":
    c = math.factorial(a)

print(c)
