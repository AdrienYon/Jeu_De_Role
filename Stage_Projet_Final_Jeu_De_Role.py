"""
   @title : Programme principale de Jeu de rôle 
   @dev : Ce programme permet de simuler un duel entre le joueur et un ordinateur. Le joeur peut soit attaquer l'ordinateur soit se soigner. Le but du jeu est que l'ordinateur ai 0 points de vie.
"""

# Modules du programme 
import random

# paramètres 
ENNEMY_HEALTH = 50 # L'enemi commence à 50PVs
PLAYER_HEALTH = 50 # Le joueur commence avec 50 PVs
Numer_of_potions = 3 # Le joueur commence avec trois potions  
Skip_turn = False


"""
    @dev :  boucle principale. Si le joeur ou l'ordinateur tombe à 0 PVs, le jeu se termine 
"""
while True:
    # Jeux du joueur
    if Skip_turn:
        print("Vous passer votre tour..")
        Skip_turn = False
    else:

        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("souhaiter vous attaquer (1) ou utiliser une potion (2) ? ")
        
        
        if user_choice == "1":
            your_attack = random.randint(5, 10)
            ENNEMY_HEALTH -= your_attack
            print(f"vous avez infliger {your_attack} points de dégats à l'ennemi")
        elif user_choice == "2":
            if Numer_of_potions > 0:
                potion_health = random.randint(15, 50)
                PLAYER_HEALTH += potion_health
                Numer_of_potions -= 1
                Skip_turn = True
                print(f"Vous récuperer {potion_health} points de vie {Numer_of_potions} restantes")
            else:
                print("vous n'avez plus de potion..")
                continue
    
    # Fin de partie : victoire 
    if ENNEMY_HEALTH <= 0:
           print("Bravo tu as gagner !")
           break
    ennemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= ennemy_attack
    print(f"l'ennemi vous a infliger {ennemy_attack} degats")

    # Fin de partie :  Defaite
    if PLAYER_HEALTH <= 0:
        print("tu as perdu")
        break
    
    print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
    print(f"Il reste {ENNEMY_HEALTH} points de vie à votre ennemie")
    print("-" * 40)


# Fin du jeu
print("fin du jeu") 
