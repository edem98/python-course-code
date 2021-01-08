def words_longer_than_n(array,n):
    # result = []
    # for word in array:
    #     if len(word) > n:
    #         result.append(word)
    # return result
    return [ x for x in array if len(x) > n]

words = ["serge","ez","sena","prosper"]
result = words_longer_than_n(words,4)
print(result)