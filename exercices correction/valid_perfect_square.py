def valid_perfect_square(num):
    for x in range(num//2):
        if x*x == num:
            return True
        if x*x > num:
            return False
    return True

print(valid_perfect_square(25))