def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return  1
    x1 = 0
    x2 = 1
    p = 3
    r = 0
    while p<=n:
        r = x1+x2
        x1 = x2
        x2 = r
        p += 1
    return r

print(fib(5))