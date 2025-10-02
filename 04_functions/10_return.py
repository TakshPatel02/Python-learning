def make_chai():
    return "Here is your masala chai"

return_value = make_chai()

# print(return_value)

# when we call the function make_chai() it will return the string "Here is your masala chai" and we are storing that value in the variable return_value and then we are printing the value of return_value.

#  if we want to return values from a function then we have to store them in a variable so we can use them later in the program. 

# early return:
def chai_status(chai_left):
    if chai_left == 0:
        return "sorry we are out of chai"
    return "chai is ready"

print(chai_status(12))
# in this case if we have 0 chai left then we will return the message "sorry we are out of chai" and if we have chai left then we will return the message "chai is ready" .

# once the function returns a value it will exit the function and will not execute any code after the return statement.

# returning multiple values:
def chai_report():
    return 100 , 20 # sold , remaining

sold , remaining = chai_report()
print("Sold: " , sold)
print("Remaining: " , remaining)