def find_matches(d1,d2):
    for k,v in d1.items():
        if k in d2.keys() and v == d2[k]:
            return True
    return