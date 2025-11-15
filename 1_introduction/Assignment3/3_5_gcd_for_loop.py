# GCD ب م م
num1 = int(input("Plese enter your first number : "))
num2 = int(input("Please enter your second number : "))
divisors_num1 =[]
divisors_num2 =[]
for i in range(1,num1):
    if num1%i == 0:
        divisors_num1.append(i)
for i in range (1,num2):
    if num2%i == 0:
        divisors_num2.append(i)

if num1>num2:
        for i in range(len(divisors_num2)-1,0,-1):
            if divisors_num2[i] in divisors_num1:
                 print("GCD = ", divisors_num2[i])
                 break
else:
     for i in range(len(divisors_num1)-1,0,-1):
            if divisors_num1[i] in divisors_num2:
                 print("GCD : ", divisors_num1[i])
                 break
             





