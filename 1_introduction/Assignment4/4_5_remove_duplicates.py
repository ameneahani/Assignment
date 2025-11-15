# Remover a duplicate member from a list

num = print("enter a number or type end: ")
list = []
while num != "end":
    num = input("num or end : ")
    if num != "end":
        list.append(int(num))
print("Input list: ", list)
for i in range(len(list)):
    j = i+1
    while j < len(list):
        if list[i] == list[j]:
            list.pop(j)
            j = j-1
        j = j+1

print(list)
    



