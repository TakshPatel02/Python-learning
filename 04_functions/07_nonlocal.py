def update_order():
    chai_type = "Elaichi"
    print(f"before update your order is {chai_type} chai") # Elaichi
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"Your order is {chai_type} chai") # kesar

update_order()

# nonlocal keyword is used to modify the variables in the outer function scope from the inner function. the outer chai_type variable is modified by the inner function kitchen() . variable is the same but the value is overwritten . nonlocal only change the immediate outer function variable not the global variables.