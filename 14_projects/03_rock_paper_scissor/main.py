import random

def play_game():
    user_choice = input("Rock , Paper , Scissor ? (r/p/s): ").lower()

    if user_choice == 'r':
        print("You chose 🪨")
    elif user_choice == 'p':
        print("You chose 📄")
    else:
        print("You chose ✂️")

    computer_choice = random.choice(['r' , 'p' , 's'])

    if computer_choice == 'r':
        print("Computer chose 🪨")
    elif computer_choice == 'p':
        print("Computer chose 📄")
    else:
        print("Computer chose ✂️")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's'):
        print("You win!")
    elif (user_choice == 'p' and computer_choice == 'r'):
        print("You win!")
    elif (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else: 
        print("You lose!")

while True:
    play_game()
    if input("Play again? (y/n): ").lower() != 'y':
        break

print("Thanks for playing!")