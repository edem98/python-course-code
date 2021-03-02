array = [10,2,5,3]

def n_and_double(array):
    for x in range(len(array)):
        for y in range(x+1,len(array)):
            if array[x]*2 == array[y] or array[y]*2 == array[x]:
                return True
    return False

print(n_and_double(array))