def contains_duplicate(array,k):
    dict1 = {}
    for p , x in enumerate(array):
        if x in dict1:
            dict1[x][0] += 1
            dict1[x].append(p)
        else:
            dict1[x] = [1,p]

    for x in dict1:
        if dict1[x][0] == 1:
            continue
        else:
            i = len(dict1[x]) - 1
            while i > 1:
                if dict1[x][i] - dict1[x][i-1] <= k:
                    return True
                i -= 1
    return False

a = [1,2,3,1,2,3]
b = [1,2,3,1]
k = 3
print(contains_duplicate(b,k))




