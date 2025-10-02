staff = [("Amit" , 15) , ("John" , 14) , ("Sara" , 16)]

for name , age in staff:
    if age <= 18:
        print(f"{name} is eligible for managing staff")
        break
else:
    print(f"No one is eligible for managin the staff")

# in this case if the if condition satisfied , the else block and other iterations will be skipped , only 1st iteration will be executed.

# for else is used when you want to run some code only if the loop completes normally ,without hitting a break statement. / this is also called fallback logic.