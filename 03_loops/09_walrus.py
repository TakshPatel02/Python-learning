# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible , remainder is {remainder}")

# using walrus operator
value = 13

if (remainder := value % 5):
    print(f"Not divisible , remainder is {remainder}")

# walrus operator allows you to assign values to variables as part of an expression , it is also called assignment expression. and it returns the value assigned.

available_sizes = ["small" ,"medium" ,"large"]

if (requested_size := input("what size do you want?")) in available_sizes:
    print(f"Adding {requested_size} size to your order")
else:
    print(f"Requested size unavailable : {requested_size}")

# in this if our entered size is not available in the list , then whole if block will be skipped and no variable will be created.

flavors = ["masala" ,"ginger" , "lemon" , "mint"]

print(f"available flavors are : {flavors}")

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry , we dont have {flavor}")

print(f"You choose {flavor}")

# here the while loop will keep asking for input until a valid flavor is entered . once a valid flavor is chosen , the loop exits and the chosen flavor is printed.