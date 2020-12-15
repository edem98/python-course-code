age = input("Quelle est votre age ?\n")
age = int(age)
if age < 18 :
    print("Vous este mineur")
elif age >= 18 and age <= 45:
    print("Vous etes majeurs et jeune")
else:
    print("vous etes vieux")
