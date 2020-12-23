def extract_result(n):
    if n < 0:
        return False
    result = 0
    while n > 0:
        r = n%10
        r = r*r
        n = n//10
        result += r
    return result


def happy_number(num):
    found = {}
    while num not in found:
        found[num] = True
        num = extract_result(num)
        if num == 1:
            return True

    return False

print(happy_number(19))