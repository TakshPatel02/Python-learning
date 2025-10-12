# Improved Dice roll game with user-defined number of dice and replay option

import random

dice_num = input("Welcome to dice roll game! How many dice you want to roll : ")
answer = input("You want to roll the dice? (y/n) : ")

while True:
    if answer.lower() == "y":
        dice_roll = tuple(random.randint(1 , 6) for _ in range(int(dice_num)))
        print(f"You rolled {dice_roll}")
        answer = input("Do you want to roll again? (y/n): ")
    else:
        break

print('Thank you for playing!')