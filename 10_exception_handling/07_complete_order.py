class InvalidChaiError(Exception): pass

# Billing function with exception handling
def bill(flavor , cups):
    try:
        menu = {"masala" : 20, "ginger" : 30}
        # check for valid flavor and cups
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} is not available.")
        if not isinstance(cups , int):
            raise TypeError("Number of cups must be an integer.")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai is {total}.")
    except Exception as e:
        print(f"Error : {e}")
    finally:
        print("Thank you for visiting chai Point.")

bill("mint" , 5)
bill("masala" , "three")
bill("ginger"  , 2)