# Invert a list

num = print("enter a number or type end: ")
list = []
while num != "end":
    num = input("num or end : ")
    if num != "end":
        list.append(int(num))
#print(list)
inverse_list =[]
for i in range(len(list)-1,-1,-1):
    inverse_list.append(list[i])
print(inverse_list)




