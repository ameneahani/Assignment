# detect whether the input array is sorted from smallest to largest number

seq =[]
sort = 1

while True:
    a = input("Please enter your number or type end : ")
    if a != "end":
        seq.append(int(a))
    else:
        break
for i in range(0,len(seq)-1):
    if seq[i] > seq[i+1]:
        print("This sequance is not sorted")
        sort = 0
        break
if sort == 1:
    print("This sequance is sorted")

