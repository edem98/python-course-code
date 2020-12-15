x = (21,-5)
l = [21,4,95,-100]

def somme(x):
    return x[0] + x[1]
    # elif x is list:
    #     som = 0
    #     for elt in x:
    #         som += elt
    #     return som
    # else:
    #     print('Type de variable non prise en charge')
    #     return None
def checkIndex(l, number):
    index = 0
    for x in l:
        if x == number:
            return index
        index += 1


# print(checkIndex(l,95))

# try:
#     print(l.index(95, 0, 1))
# except ValueError as e:
#     print("This value is not in the list")
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)