
def array_is_symetric(array):
    flag_symetric = True
    for i in range(len(array)-1):
        if array[i] != array[len(array)-1-i]:
            flag_symetric = False
            break
    return flag_symetric

print(array_is_symetric([1,2,3,0,3,2,1]))

