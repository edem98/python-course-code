
def best_sum(target,numbers,memo={}):
    if target in memo: return memo[target]
    if target == 0 : return []
    if  target < 0 : return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        remainder_combination = best_sum(remainder,numbers,memo)
        if remainder_combination is not None :
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination

print(best_sum(100,[1,2,3,25]))