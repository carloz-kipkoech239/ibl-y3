import random

# Prompt the user for a level.
while True:
    level_str = input("Enter a level (a positive integer): ")
    try:
        level = int(level_str)
        if level > 0:
            break
    except ValueError:
        pass

# Generate a random integer.
number = random.randint(1, level)

# Prompt the user to guess the integer.
while True:
    guess_str = input("Guess the number (a positive integer between 1 and {}): ".format(level))
    try:
        guess = int(guess_str)
        if guess <= 0:
            raise ValueError
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
