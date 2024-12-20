#
import random

tortue = 0
x = int(input("Entrez le nombre de partie à jouer : "))

gagnerTortue = 0
gagnerLievre = 0

randomNb = random.randint(1, 6)

# for i in range(x):
for i in range(x):
    print(" __ Nouvelle partie n°"+ str(i+1)+ " __ Dé affiché : "+str(randomNb))
    while randomNb != 6:
        tortue += 1
        gagnerTortue += 1
        print("La tortue avance d'un case. Il est à la " + str(tortue) + " eme case !")
        if tortue==6 :
            print("La tortue a gagné ! Fin de la partie.")
            break
        randomNb = random.randint(1, 6)
        print("Nouveau lancé de Dé: "+str(randomNb))
    else:
        gagnerLievre += 1
        print("Le lièvre a gagné ! Fin de la partie.")
        # randomNb = random.randint(1, 6)
    tortue = 0
    randomNb = random.randint(1, 6)

print("Frequence de victoire pour lievre : " + str(gagnerLievre / x))
print("Frequence de victoire pour tortue : " + str(gagnerTortue / x))



    