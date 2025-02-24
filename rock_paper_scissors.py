import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue # This will skip the rest of the code in the loop and start from the beginning
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    
