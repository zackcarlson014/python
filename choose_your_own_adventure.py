name = input("What is your name? ")
print("Hello, " + name + "!")
print("Welcome to Z's choose your own adventure game!")
print("You are on a deserted island.")
print("You see a treasure chest.")
print("Do you want to open it?")
choice = input("Yes/No: ").lower()

if choice == "yes":
    print("You found a map inside the chest.")
    print("The map leads to a hidden cave.")
    print("Do you want to follow the map?")
    choice = input("Yes/No: ").lower()
    if choice == "yes":
        print("You follow the map and find the hidden cave.")
        print("Inside the cave, you find a pile of gold.")
        print("Congratulations! You win!")
    else:
        print("You decide not to follow the map.")
        print("You wander around the island and get lost.")
        print("You are never found.")
        print("Game over.")
else:
    print("You decide not to open the chest.")
    print("You wander around the island and get lost.")
    print("You are never found.")
    print("Game over.")
print("Goodbye, " + name + "!")

