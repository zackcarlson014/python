print("Welcome to Z's quiz game!")

playing = input("Do you want to play? (yes/no) ")

print(playing)
print("Okay! Let's play!")

if playing.lower() != "yes":
    quit()

print("I will ask you a series of questions.")
print("You will answer them.")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")