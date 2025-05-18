# calculator
import math

a =float (input("please enter first number:"))
print("what do you want to do?")
op =input("+  -  *  /  \n sin  cos tan cot \n log  sqrt  factorial: ")
if op =="sin" or op =="cos" or op =="tan" or op =="cot":
    a =a* math.pi /180 # convert degree to radian
    if op =="sin":
        res =math.sin(a)
    elif op =="cos":
        res =math.cos(a)
    elif op =="tan":
        res = math.tan(a)
    elif op =="cot":
        if math.tan(a) != 0:
            res=1/math.tan(a)
        else :
            res ="Infinity"
elif op == "sqrt":
    res =math.sqrt(a)
elif op =="log":
    res =math.log(a)
elif op =="factorial":
    res =math.factorail(a)

elif op == "+" or op=="-" or op=="*" or op=="/" :
    b =float(input("enter second number: "))
    if op =="+":
        res =a+b
    elif op =="-":
        res =a-b
    elif op =="*":
        res =a*b
    elif op =="/":
        if b==0:
            res ="Infinity"
        else :
            res =a/b
print (res)

