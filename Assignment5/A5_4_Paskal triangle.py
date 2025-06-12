# Paskal triangle
from array import *
def Paskal(n):
    arr = []
    for i in range (n):
        arr.insert(i,[])
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i].insert(j,1)
            else:
                element = arr[i-1][j-1] + arr[i-1][j]
                arr[i].insert(j, element)
    for elements in arr:
        for element in elements:
            print(element, end=" ")
        print()

Paskal(int(input("Please enter n: ")))

