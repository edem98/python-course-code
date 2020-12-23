def is_vowel(char):
    if char in "aeuioAEUIO":
        return True
    return False

def reverse_vowels(word):
    s = list(word)
    i = 0
    j = len(word) - 1
    while i < j:
        if is_vowel(s[i]):
            if is_vowel(s[j]):
                a = s[i]
                s[i] = s[j]
                s[j] = a
                i = i + 1
                j = j - 1
            else:
                j = j -1
        else:
            i = i + 1

    return "".join(s)

print(reverse_vowels("leetcode"))
