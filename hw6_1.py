# START

import random

player_1: str = input("Enter the name of the player 1: ")
player_2: str = input("Enter the name of the player 2: ")
player_3: str = input("Enter the name of the player 3: ")
player_4: str = input("Enter the name of the player 4: ")
winner: str = random.choice([player_1, player_2, player_3, player_4])
print(f"The winner is {winner}")

# STOP
