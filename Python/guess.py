import random
number = random.randint(1, 100)
guess = None
while guess != number:
    guess = int(input("Guess: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    elif guess == number:
        print("You guessed it!")