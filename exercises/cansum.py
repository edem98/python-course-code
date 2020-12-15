
def can_sum(target,numbers):
    complement = {}
    for x in numbers:
        if target%x == 0:
            return True
        if target - x in complement:
            return True
        complement[target-x] = True

    return False

# print(can_sum(7,[2,4]))

def can_sum_dynamic(target,numbers,memo={},):
    if target == 0: return True
    if target < 0 : return False
    if target in memo: return memo[target]

    for x in numbers:
        if can_sum_dynamic(target - x, numbers) :
            memo[target] = True
            return True

    memo[target] = False
    return False

print(can_sum_dynamic(300,[7,14]))
