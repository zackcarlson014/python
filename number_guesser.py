import random

print("Welcome to Z's number guesser game!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")

number = random.randint(-5, 11)
print(number)

