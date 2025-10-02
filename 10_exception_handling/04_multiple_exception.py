def chai_order(item, quantity):
    try:
        price = {"masala" : 20}[item]
        cost = price * quantity
        print(f"Your order for {quantity} {item} chai costs {cost} rupees.")
    except KeyError :
        print(f"Sorry, we do not serve {item} chai.")
    except TypeError:
        print("Quantity must be a number.")

chai_order("ginger" , 2)

# try:
        # price = {"masala" : 20}[item]
        # cost = price * quantity

# How this works : price = {"masala" : 20}["ginger"] / This line raises a KeyError because "ginger" is not a key in the dictionary. The program control is transferred to the except block that handles keyError. 