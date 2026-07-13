import random
while True:
    print("Roll the dice? (y/n): ")
    user_input = input().lower()
    if user_input == 'y':
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
    elif user_input == 'n':
        print("Thanks for playing!")
        break
        