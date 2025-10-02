class ChaiOrder:
    def __init__(self , chai_type , sweetness , size):
        self.chai_type = chai_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls , order_data):
        return cls(
            order_data["chai_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls , order_string):
        chai_type , sweetness , size = order_string.split("-")
        return cls(chai_type , sweetness , size)
    
# classmethod: class method is used to create alternative constructors. It takes the class as the first argument instead of the instance.
# cls(): cls is a convention to represent the class itself. It is used to create instances of the class. / and passes the data to the default constructor.

order1 = ChaiOrder.from_dict({"chai_type" : "masala" , "sweetness" : "medium" , "size" : "Large"})

order2 = ChaiOrder.from_string("Ginger-Less-Small")

print(order1.__dict__)
print(order2.__dict__)

# difference between class method and static method:
# 1. class method takes cls as the first argument while static method does not take any special first argument.
# 2. class method is used to create alternative constructors while static method is used to group utility functions related to the class.
