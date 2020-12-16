def valid_anagram(word1,word2):
    d1 = {}
    d2 = {}
    for x in word1:
        if x in d1:
            d1[x] += 1
        else:
            d1[x] = 1

    for x in word2:
        if x in d2:
            d2[x] += 1
        else:
            d2[x] = 1

    for x in word1:
        if d1[x] != d2[x]:
            return False

    return True

print(valid_anagram("anagram","instagram"))