

def grid_traveler(m,n,dico={}):
    key = str(m) + ',' + str(n)
    key2 = str(n) + ',' + str(m)
    if key in dico:
        return dico[key]
    if key2 in dico:
        return dico[key2]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    dico[key] = grid_traveler(m-1,n,dico) + grid_traveler(m,n-1,dico)
    return dico[key]

print(grid_traveler(18,18))