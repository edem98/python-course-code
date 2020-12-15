import random


again = True
resp = ""
while again:
    number = random.randint(0, 1000)
    trial = 1
    while trial <= 10:
        guess = int(input("Quelle nombre l'ordinateur a t'il choisi ?: \n"))
        if guess < number:
            print("Votre nombre est trop bas")
        elif guess > number:
            print("Votre nombre est trop haut")
        else:
            print("Vous avez gagnez le jeu en " + str(trial) + " coups")
            break
        trial += 1

    if trial == 10:
        print("Desole ... Vous avez perdu")
    resp = input("Voulez-vous continuez ? (Y/N): \n")
    if resp.lower() == "y":
        continue
    else:
        again = False
print("merci d'avoir jouer notre jeu.")