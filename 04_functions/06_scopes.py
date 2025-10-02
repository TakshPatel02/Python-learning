# scopes 
def serve_chai():
    chai_type = "Masala" # local scope
    print(f"serving {chai_type} chai")

chai_type = "Lemon" # global scope
serve_chai()
print(f"Outside function {chai_type}")

# if the variable is not in the function but the same name variable is in the global scope then function refers to the global scope variable , but if the variable is defined in the function then it refers to the local scope variable despite the same name variable in the global scope. We can't use the local scope variable outside the function . 


# nested functions and scopes
def chai_counter():
    chai_order = "lemon"
    def print_order():
        print(f"Your order is {chai_order} chai")
    print_order()

# chai_order = "lemon"
chai_counter()

# in nested function the inner function can refer to the variable in the outer function but the outer function can't refer to the variable in the inner function. inner function can refer global scope also . 

# function first priotize the local scope variable then the outer function variable then the global scope variable . 