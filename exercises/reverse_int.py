def reverse(x: int) -> int :
    res = ''
    x = str(x)
    if x[0] == "-" :
        res += x[0]
        x = x[1::]
    for c in range(0, len(x), -1) :
        if x[c] != '0' :
            res += x[c]

    print(res)
    return res

reverse(-3)