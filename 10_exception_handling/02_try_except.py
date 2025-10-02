chai_menu = {"masala" : 30 , "ginger" : 40}

try:
    chai_menu["lemon"]
except KeyError:
    print("The key you are trying to access does not exist in the dictionary.")

print("Program continues...")
# By putting the code that might raise an error inside a try block , we can handle the error gracefully using an except block. It is just like an if-else statement but for errors. If try block runs without error then except block is skipped. If there is an error in try block then except block is executed and the program continues to run without crashing.

