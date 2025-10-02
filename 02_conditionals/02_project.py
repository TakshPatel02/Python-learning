# a local cafe wants a program that suggests a snack. if a customer asks for cookie or samosa , it confirms the order. otherwise it says it's not available.
# Task : 
# take a snack input
# if it's cookie or samosa , confirm the order
# else show unavailability

# for taking the input from the user we have to use input() function
snack = input("Enter your preffered snack : ").lower()

if snack =="cookie" or snack == "samosa":
    print(f"your order is confirmed for : {snack}")
else:
    print(f"your preffered snack {snack} is not available")    