# you're creating a tea menu board , each item must be numbered. task: use enumerate() to print items with numbers

menu = ["Green" ,"Mint" , "Lemon" , "Spiced"]

# enumerate function adds a counter to an iterable and returns it as an enumerate object

# 1st method with index and item in one variable 
# for name in list(enumerate(menu , start=1)):
#     print(f"The menu  items is :  {name}")

# 2nd method with index and items in separate variables
for idx , item in enumerate(menu , start=1):
    print(f"{idx} : {item}")