def panagram(word):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for char in chars:
        if char not in word.lower():
            return False
    return True

word = "The quick brown fox jumps over the lazy dog"
result = panagram(word)
print(result)

word = "Not a panagram"
result = panagram(word)
print(result)