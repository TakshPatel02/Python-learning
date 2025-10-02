class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
print(cutting.temperature)

del cutting.temperature
print(cutting.temperature) # after deleting the temperature attribute from cutting object / it will look for the attribute in the class Chai

cutting.cup = "small" 
print(cutting.cup)

del cutting.cup
print(cutting.cup) # AttributeError : 'Chai' object has no attribute 'cup' / because cup attribute is only for cutting object not for the class Chai or any other object created from the class Chai

