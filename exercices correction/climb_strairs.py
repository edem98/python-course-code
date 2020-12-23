def climbing_stairs(num,memo={}):
    if num < 0 : return 0
    if num == 0 : return 1
    if num in memo: return memo[num]
    memo[num] = climbing_stairs(num-1) + climbing_stairs(num-2)
    return memo[num]

print(climbing_stairs(4))