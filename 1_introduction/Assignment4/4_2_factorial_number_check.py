# Detect whether number is Factirial ro not
import math
num = int(input("Please enter the number: "))
n=0
while True:# از 1 شروع میکند و اعداد پشت هم را بررسی میکند تا زمانی که به یک عدد بخشپذیر نباشد 
    n += 1
    if num%n != 0:
        break
factorial =[]
for i in range(1,n):
    a = math.factorial(i)
    factorial.append(a)
#print(factorial)
if num in factorial: 
    print("The number is a fictorial ")
else: 
    print("The number is not a factorial")

