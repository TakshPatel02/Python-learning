# you receive a list of names for chai orders. the goal is to print out the order queue.
# task: use a list of names . print: order ready for {name}

orders = ["Alice", "Bob", "Charlie", "David"]

# iterate through the list of names and print the order ready message , it starts from the index 0 and goes to the last index 
for name in orders:
    print(f"Order is ready for {name}")