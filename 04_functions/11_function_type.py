# types of functions : pure function , impure function , recursive function , Lambda function(anonymous function) 

def pure_chai(cups):
    return cups * 10

total_cups = 0
# print("Before changing" , total_cups)

# not recommended to use global variables inside the functions
def impure_chai(cups):
    global total_cups
    total_cups += cups * 10
    return total_cups

# print(pure_chai(3))
# print(impure_chai(40))
# print("After changing" , total_cups)

# Recursive function : a function that calls itself
def pour(n):
    print("cups remaining: " , n)
    if n == 0:
        return "All cups poured"
    return pour(n-1)

# print(pour(3))

# Lambda function : a function that is defined without a name

chai_type = ["light" , "kadak" , "masala" , "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak" , chai_type))

print(strong_chai)
# we are using the filter function to filter out the kadak chai from the list of chai_type and we are using the lambda function to define the condition for filtering . 