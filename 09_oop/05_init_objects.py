class ChaiOrder:
    def __init__(self , type_ , size):
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size} ml of {self.type} chai."
    
order = ChaiOrder("Masala" , 200)
print(order.summary())

order_two = ChaiOrder("Ginger" , 220)
print(order_two.summary())

# here we have to write type_ because type is a reserved keyword in python ao we can't use it as a variable name.
