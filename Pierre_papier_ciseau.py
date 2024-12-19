#18/10/24
import random
choix = {
  1: "PIERRE",
  2: "PAPIER",
  3: "CISEAU"
}

x = int(input("Choissisez "+choix[1]+" :1 ,"+choix[2]+" :2 ,"+choix[3]+" :3 .Votre choix : "))
while x != 1 and x != 2 and x != 3:
    print("Choix indisponible")
    x = int(input(choix[1]+" :1 ,"+choix[2]+" :2 ,"+choix[3]+" :3 .Votre choix :"))
else:
    print("Vous avez choisi "+choix[x])

ordi = random.randint(1, 3)
print("J'ai choisi "+choix[ordi])

if x == ordi:
    print("Nul, pas de vainqueur")
elif x == 1 and ordi == 2 or x == 2 and ordi == 3 or x == 3 and ordi == 1:
    print("'~' J'ai gagné!")
else:
    print("*^_^* Vous avez gagné (^=^)!")







