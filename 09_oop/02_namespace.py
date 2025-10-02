class Chai:
    origin = "India"

print(Chai.origin) # India / Accessing class attribute using class name
Chai.is_hot = True # Creating class attribute using class name 
print(Chai.is_hot) # True

# Creating object from class Chai
masala = Chai()
print(masala.origin)
masala.is_hot = False
print(masala.is_hot) # changing the value of is_hot attribute for masala object / which will not affect the class attribute

masala.flavor = "spicy"
print(masala.flavor) # this attribute is only for the masala object not for the class Chai or any other object created from the class Chai
print(Chai.is_hot) # this is not affected by the change made to masala object