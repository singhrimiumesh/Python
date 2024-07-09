# Snake Water Gun Game


# computer input
# s for Snake, w for Water, g for Gun

import random
computer = random.choice(["s", "w", "g"])

# user input
user = input("Enter your choice (s:Snake, w:Water, g:Gun): ")

l = {"s": "Snake", "w": "Water", "g": "Gun"}

print(f"You chosed : {l[user]} \nComputer chosed: {l[computer]}")

if user == computer:
    print("It's a tie")
elif user == "s" and computer == "w":
    print("You win")
elif user == "w" and computer == "g":
    print("You win")
elif user == "g" and computer == "s":
    print("You win")
else:
    print("You lose")
