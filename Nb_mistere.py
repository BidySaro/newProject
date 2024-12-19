# 11/10/24
import random
randomNb = random.randint(0, 100)
coup = 5
x = int(input("Enter a number between 0 and 100. Ypu have " + str(coup) + " guess rest. Your guess : "))
dixieme = (randomNb // 10) * 10
while x != randomNb:
    coup = coup-1
    if (coup == 0):
        print("Too bad, you don't have any guess left. The right number is "+str(randomNb))
        break
    if (coup == 1):
        print("One guess left. Clue : the number is between "+str(dixieme-10)+" and "+str(dixieme+10))
    x = int(input("Not yet ! Guess left : " + str(coup) + ". Your guess : "))
else:
    print("Congrats! You've got it")
