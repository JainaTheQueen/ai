import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock, paper or scissors: ").lower()
print("Computer chose:", computer)

if user == computer:
    print("It's a draw!")

elif user == "rock" and computer == "scissors":
    print("You win!")

elif user == "paper" and computer == "rock":
    print("You win!")

elif user == "scissora" and computer == "paper":
    print("You win!")

elif user in choices:
    print("Computer wins!")

else:
    print("Invalid choice!")