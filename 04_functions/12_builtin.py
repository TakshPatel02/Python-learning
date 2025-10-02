def chai_type(chai = "masala"):
    """"Returns the type of chai""" #docstring
    return chai

print(chai_type.__doc__) # to get the docstring of the function / docstring must be the first statement in the function if not then it will return None. 
print(chai_type.__name__) # to get the name of the function
print(chai_type()) # docstring will not affect the function execution and does not print anything