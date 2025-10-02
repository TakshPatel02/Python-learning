class OutOfIngredientsError(Exception):
    pass

def chai_order(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing igredients to prepare chai.")
    print("Preparing your chai...")

chai_order(1 , 0)

# Raising a custom exception OutOfIngredientsError when either milk or sugar is zero. The program will terminate with a traceback showing the OutOfIngredientsError and the custom message.

