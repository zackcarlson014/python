import random

values = { 1: 1, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3 }

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return values[roll]

while True:
    players = input("How many players? (2 - 4 / q) ")

    if players == 'q':
        print("Exiting the game.")
        break

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print(f"Starting game with", players, "players.")
            break
        else:
            print("Invalid input. Please enter a number between 2 and 4.")
            continue
            
    else:
        print("Invalid input. Please enter a number between 2 and 4.")
        continue
    
max_score = 21
player_scores = [0] * players

while max(player_scores) < max_score:
    
    for i in range(players):
      print(f"\nPlayer {i + 1}'s turn.\n")
      current_score = player_scores[i]
      
      while True:
        should_continue = input("Do you want to roll the dice? (y/n) ")
  
        if should_continue.lower() != 'y':
            break
        
        else:
            roll = roll_dice()

            if roll == 1:
                print(f"Player {i + 1} rolled a 1. Total score: {player_scores[i]}")
                break
            
            current_score = player_scores[i] + roll

            if current_score > max_score:
                print(f"Player {i + 1} rolled a {roll}. Total score: {player_scores[i]} - Busted!")
                continue

            elif current_score == max_score:
                player_scores[i] = current_score
                print(f"Player {i + 1} rolled a {roll}. Total score: {player_scores[i]} - Winner!")
                break
        
            else:
                player_scores[i] = current_score
                print(f"Player {i + 1} rolled a {roll}. Total score: {player_scores[i]}")
                continue
        

  

