# Array with lenth of n with non-reapiting random numbers
import random

array = []
n = int(input("Please enter n: "))
for i in range(n):
    
    random_num = random.randint(0, 100)
    #print(random_num)
    if random_num in array:
        i -= 1
    else:        
        array.append(random_num)

print(array)

