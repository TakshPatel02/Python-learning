class BaseChai:
    def __init__(self , type_):
        self.type = type_

    def prepare(self):
        print(f"preparing {self.type} chai....")

# Inheritance : 
class MasalaChai(BaseChai):
    def add_spices(self):
        print('Adding cardamom , ginger , cloves')

class ChaiShop:
    # composition : one class contains the object of another class
    chai_cls = BaseChai 

    def __init__(self):
        self.chai = self.chai_cls("Regular") # here we are creating the object of BaseChai class. 

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

# inheritance + composition : it inherits the chaishop class and also contains the object of masalachai class.
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

    def __init__(self):
        self.chai = self.chai_cls("Masala")

shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()

# fancy has a masala chai object and inherits chaishop's all the methods and attributes.

# what is composition? : composition is a design principle in which one class contains the object of another class.

