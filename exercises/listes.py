"""
# declarer une liste
liste = []
# ajouter un element a la fin de la liste
element1 = 10
element2 = 10
element3 = 10
element4 = 10
liste.append(element1)
liste.append(element2)
liste.append(element3)
liste.append(element4)
# retirer un element a la fin de la liste
liste.pop(liste)
# inserer un element a un index dans la liste
index = 2
valeur = 30
liste.insert(index, valeur)
# retirer un element a un index dans la liste
liste.pop(index)
# retirer tous les elements de la liste
liste.clear()
"""

my_list = [1,2,3,4,5,6,7,8,9]
n = 3
for x in range(3):
    elt = my_list[-1]
    my_list.pop()
    my_list.insert(0,elt)
print(my_list)