def palindrome(word):
    i = 0
    j = len(word) -1
    while i < j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def palindrome_number(n):
    if n < 0:
        return False
    save = n
    result = 0
    while n > 0:
        r = n%10
        n = n//10
        result = result*10 + r
    if save == result:
        return True
    return False


result = palindrome_number(121)
print(result)