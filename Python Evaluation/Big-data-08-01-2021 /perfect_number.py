def perfect_number(number):
    if number < 0:
        return False
    if number == 1:
        return True
    divider_sum = 0
    for divider in range(1,number):
        if number % divider == 0:
            divider_sum += divider
    return divider_sum == number

number = 28
result = perfect_number(number)
print(result)

number = 10
result = perfect_number(number)
print(result)
