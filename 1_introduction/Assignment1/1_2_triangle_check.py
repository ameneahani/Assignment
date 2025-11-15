
a = float(input("Please enter first side of the triangle: "))
b = float(input("Please enter second side of the triangle: "))
c = float(input("Plase enter third sid of the triangle: "))
if a < b+c:
    if b < a+c:
        if c < a+b:
            print("It is possible to draw such a triangle")
else :
    print("It is not posible to draw such a triangle")


