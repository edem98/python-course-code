def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True

string = 'the quick brown fox jumps over the lazy dog'
if (ispangram(string) == True):
    print("Oui c'est un pangram")
else:
    print("Non ceci n'est pas un pangram")