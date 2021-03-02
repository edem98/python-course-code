array = [0,2,3,4,5,2,1,0]

def climbing_montain(arr):

    if len(arr) < 3:
        return False

    maxi = max(arr)
    index = arr.index(maxi)

    if index == 0 or index == len(arr) -1:
        return False

    for x in range(index):
        if arr[x] >= arr[x+1]:
            return False

    for x in range(index,len(arr)-1):
        if arr[x] <= arr[x+1]:
            return False

    return True

print(climbing_montain(array))