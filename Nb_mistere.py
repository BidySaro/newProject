# 11/10/24
import random
randomNb = random.randint(0, 100)
coup = 5
x = int(input("Entrez un nombre 0 et 100. Vous avez " + str(coup) + " coups restants. Entrez : "))
dixieme = (randomNb // 10) * 10
while x != randomNb:
    coup = coup-1
    if (coup == 0):
        print("Vous avez utilisez toutes vos coups! Le nombre mistère est "+str(randomNb))
        break
    if (coup == 1):
        print("Nombre entre "+str(dixieme-10)+" et "+str(dixieme+10))
    x = int(input("Faux ! Coups restants: " + str(coup) + ". Entrez : "))
else:
    print("Vous avez devinez")
