#LCM ک م م 
num1 = int(input("Please enter first number: "))
num2 = int(input("please enter second number: "))

num1_multiple = []
num2_multiple = []
for i in range(1,num2+1):
    num1_multiple.append(i*num1)
for i in range(1,num1+1):
    num2_multiple.append(i*num2)
    
if num1 > num2:
    for i in range(len(num1_multiple)):
        if num1_multiple[i] in num2_multiple:
            print("LCM: ", num1_multiple[i])
else:
    for i in range(len(num2_multiple)):
        if num2_multiple[i] in num1_multiple:
            print("LCM: ", num2_multiple[i])

