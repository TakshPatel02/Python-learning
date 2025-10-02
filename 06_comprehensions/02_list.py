# List comprehensions
# Syntax : [expression for item in iterable if condition]

menu = [
    "Masala chai",
    "Iced lemon tea",
    "Green tea",
    "Iced peach tea",
    "Ginger chai"
]

# making new list containing iced tea
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

# here expression means what we want to include in the new list , if i write tea.upper() then it will convert all the items in the new list to uppercase. 

iced_tea = [my_tea for my_tea in menu if "iced" in my_tea.lower()]
# we have to use same variable name in expression as well as in for loop. Otherwise it will give error. that your variable is not defined.
