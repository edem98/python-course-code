nb_article = int(input("Saisissez le nombre d'article\n"))
prix = []
for x in range(nb_article):
    prix.append(int(input("Veillez saisir le prix de l'article numero: " + str(x+1)+ "\n")))
somme = 0
for x in prix:
    somme += x
moyenne = somme/len(prix)
print("le chiffre d affaire est: "+ str(somme))
print("la moyenne des prix est: "+ str(moyenne))