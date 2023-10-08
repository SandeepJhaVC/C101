import random

response = "y"

while response == "y":
    # Generate a random number between 1 and 6 to simulate rolling a dice
    dice_value = random.randint(1, 6)

    # Display the dice representation based on the random value
    if dice_value == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif dice_value == 2:
        print("---------")
        print("| 0     |")
        print("|       |")
        print("|     0 |")
        print("---------")
    elif dice_value == 3:
        print("---------")
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
        print("---------")
    elif dice_value == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif dice_value == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    else:  # dice_value == 6
        print("---------")
        print("| 0 0 0 |")
        print("|       |")
        print("| 0 0 0 |")
        print("---------")

    response = input("Do you want to roll the dice again? (y/n): ").lower()

print("Thanks for playing!")
