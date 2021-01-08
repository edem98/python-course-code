def remove_duplicates(array):
    return list(set(array))

test = [1,3,1,5,4,4,5,2]
result = remove_duplicates(test)
print(result)