# you're preparing an order summary with customer names and their total bill.
# task: use two lists:one for names and one for bills , print:{name} paid {amount}

names = ["Alice", "Bob", "Charlie", "David"]
bills = [40 , 50 , 80 , 20]

# zip function combines two lists into a list of tuples , each tuple contains one item from each list

# 1st method with one variable
# for item in zip(names , bills):
#     print(f"paid {item}")

# 2nd method with two variables
for names , amount in zip(names , bills):
    print(f"{names} paid {amount}")
