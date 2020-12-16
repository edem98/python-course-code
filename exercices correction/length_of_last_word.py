def length(word):
    count = 0
    find_space = False
    i = len(word)-1
    while not find_space and i >= 0:
        if word[i] == " ":
            find_space = True
        else:
            count += 1
        i -= 1
    return count


print(length(" hello"))