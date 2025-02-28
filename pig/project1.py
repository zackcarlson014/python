import random

values = { 1: 1, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3 }

win = 21

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return values[roll]
