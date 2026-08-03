import random
choice = input("Choose (Rock/Paper/Scissors): ")
computer = random.choice(["Rock", "Paper", "Scissors"])
if choice == computer:
    print("It's a tie!")
elif (choice == "Rock" and computer == "Scissors") or (choice == "Paper" and computer == "Rock") or (choice == "Scissors" and computer == "Paper"):
    print(computer)
    print("You win!")
else:
    print(computer)
    print("You lose!")