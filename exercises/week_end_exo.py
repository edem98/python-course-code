def match(w1,w2):
    dic = {}
    for i,v in enumerate(w2):
        for char in w1:
            if v == char:
                if v in dic:
                    if i not in dic[v]:
                        dic[v].append(i)
                else:
                    dic[v] = [i]
    return dic

print(match('javascript','java'))