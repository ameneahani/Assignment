
a = float(input("Enter the first number :"))
b = float(input("Enter the second number :"))
c = float(input("Enter the third number :"))

if a < b+c or b < a+c or c < a+b :
    print ("your triangle is True")
else :
    print("it is impossible")