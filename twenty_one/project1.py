import random

values = { 1: 1, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3 }

win = 21

total_score = 0

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return values[roll]

while True:
    players = input("How many players? (2-4 / q) ")

    if players == 'q':
        print("Exiting the game.")
        break

    if players.isdigit():
        players = int(players)
        if 2 > players > 4:
            print("Invalid number of players. Please try again.")
            continue
        else:
            print("Starting game with", players, "players.")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
        

  

