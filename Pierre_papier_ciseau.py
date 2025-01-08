import random

# Dictionary for choices
choices = {
    1: "PIERRE",
    2: "PAPIER",
    3: "CISEAU"
}

def get_user_choice():
    while True:
        try:
            choice = int(input("Choissisez 1: PIERRE, 2: PAPIER, 3: CISEAU. Votre choix: "))
            if choice in choices:
                return choice
            else:
                print("Choix indisponible")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Nul, pas de vainqueur"
    elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):
        return "'~' J'ai gagné!"
    else:
        return "*^_^* Vous avez gagné (^=^)!"

user_choice = get_user_choice()
print(f"Vous avez choisi {choices[user_choice]}")

computer_choice = get_computer_choice()
print(f"J'ai choisi {choices[computer_choice]}")

result = determine_winner(user_choice, computer_choice)
print(result)
