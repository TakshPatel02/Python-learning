# chai = "Ginger chai"

# def prepare_chai(order):
#     print(f"preparing {order}")

# prepare_chai(chai)

# we only passing the a copy of the variable chai to the function , if we change the value of chai inside the function it will not affect the original variable chai , becasue the string is immutable in python . 

chai = [1 , 2 , 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai) 

# we are passing the reference of the list chai to the function , if we are changing the value of the list inside the function it will affect the original list chai , because the list is mutable in python . 

# in simple words , if we pass a mutable objewct to a function and change it inside the function , it will affect the original object , but if we pass an immutable object to a function and change it inside the function , it will not affect the original object . 

def make_chai(tea , milk , sugar):
    print(tea , milk , sugar)

make_chai("Darjeeling" , "Yes" , "Low") # positional arguments
make_chai(tea="Ginger" , milk="No" , sugar="High") # keyword arguments 

def special_chai(*ingredient , **extras):
    print("Ingredients: " , ingredient)
    print("Extras: " , extras)

special_chai("Cinnamon" , "Cardamom" , sweetener = "Honey" , foam="Yes")

# *args does not have to be named args , we can name it anything we want , but the convention is to use args  , if we pass the postional arguments to the function it will be stored in the args as a tuple . by using *args.

# **kwargs makes a dictionary of the keyword arguments we pass to the function and returns it . 

# defalut parameters:
def custom_chai(tea = "masala" , milk = "yes"):
    print(tea , milk)

custom_chai("ginger") # if we dont pass the second argument it will take the default value of milk as "yes" . 
