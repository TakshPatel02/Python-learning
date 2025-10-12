import random

guess = int(input("Guess a number (between 1 to 100): "))

computer_guess = random.randint(1 , 100)

while True:
    if guess < computer_guess:
        print("Too Low!")
    elif guess > computer_guess:
        print("Too High!")
    else:
        print("You guessed it right!" , computer_guess)
        break
    guess = int(input("Guess a number (between 1 to 100): "))

print("Game over!")