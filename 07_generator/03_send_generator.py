def chai_customer():
    print("What type of chai you want?")
    order = yield
    while True:
        print(f"Here is your ordered chai: {order}")
        order = yield

stall = chai_customer()
next(stall) # start of the generator

stall.send(input("enter name of chai: "))
stall.send("Ginger chai")

# how this works : we send the value to the generator using the .send() method and we are storing the sent data in order variable using yield expression.

# if we dont write order = yield in while loop then the loop will become the infinite loop as the control will never come back to the while loop after the first yield. We wrote it so it stops at the yield and waits for the next .send() call to send the new order. 