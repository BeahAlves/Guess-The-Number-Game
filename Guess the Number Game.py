from random import randint

print("Welcome to Guess The Number! ;) ")
print("I'm thinking in a number between 1 and 100. ")

picked_number = randint(1, 100)
chances = 10
hard_chances = 5

level = input("Choose a difficulty. Type 'E' to Easy or 'H' to Hard. ")
if level in 'eE':
    for attempt in range(10):
        print(f"You have {chances} attempts to guess the number. ")
        chances -= 1
        guess = int(input("make a guess: "))
        if guess == picked_number:
            print(f"You got it. The answer was {picked_number}")
            break
        elif guess < picked_number:
            print("Too low. ")
            if chances != 1 and 0:
                print("Guess again. ")
        else:
            print("Too high")
            if chances != 1 and 0:
                print("Guess again")
        if chances == 0:
            print("You've run out of guesses, you lose. ")
elif level in 'hH':
    for attempt in range(5):
        print(f"You have {hard_chances} attempts to guess the number. ")
        hard_chances -= 1
        guess = int(input("make a guess: "))
        if guess == picked_number:
            print(f"You got it. The answer was {picked_number}")
            break
        elif guess < picked_number:
            print("Too low. ")
            if hard_chances != 1 and 0:
                print("Guess again. ")
        else:
            print("Too high")
            if hard_chances != 1 and 0:
                print("Guess again")
        if hard_chances == 0:
            print("You've run out of guesses, you lose. ")
            print(f"The correct answer was {picked_number}")
else:
    print("Difficulty not valid. Please, try again. ")