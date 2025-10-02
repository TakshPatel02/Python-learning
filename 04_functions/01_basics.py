#Reducing the code duplication using functions

# you're managing a busy tea stall , you receive many orders and want to print each customer's name along with the type of chai they ordered.
#Task: write a function print_order(name, chai_type) , call it multipe times for differnet customers.

# def defines a function , print order is the function name , name and chai_type are parameters.
def print_order(name , chai_type):
    print(f"{name} ordered {chai_type} chai")

print_order("Taksh" , "Masala")
print_order("Jay" , "Ginger")
print_order("Aman" , "Tulsi")

# we pass arguments to the function call , and in function definition we receive them as parameters.
# this way we can reuse the same function for different inputs without rewriting the same code. this is reducing the code duplication.