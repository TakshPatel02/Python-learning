import random

answer = input("Welcome to dice roll game! You want to roll the dice? (y/n) : ")

while True:
    if answer.lower() == "y":
        dice_roll = (random.randint(1, 6) , random.randint(1 , 6))
        print(f"You rolled {dice_roll}")
        answer = input("Do you want to roll again? (y/n): ")
    else:
        break

print('Thank you for playing!')