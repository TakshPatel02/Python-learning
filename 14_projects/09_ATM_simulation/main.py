from traceback import print_tb


print("Welcome to the ATM: ")
print("1. check balance " \
    "\n2. Deposit" \
    "\n3. Withdraw" \
    "\n4. Exit")

balance = 0

while True:
    option = input("Choose your option: ")
    match option:
        case '1':
            print(f"Your balance is {balance}")
        case '2':
            amount = input('Enter amount to deposit: ')
            balance += int(amount)
            print(f"Your new balance is {balance}")
        case '3':
            amount = input("Enter amount to withdraw: ")
            balance -= int(amount)
            print(f"Your new balance is {balance}")
        case '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        case _:
            print("Invalid option. Please try again.")
