class TeaLeaf:
    def __init__(self , age):
        self._age = age

    @property
    def age(self):
        return self._age 
    
    @age.setter
    def age(self , age):
        if 0 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be between 0 and 5")
        
leaf = TeaLeaf(2)
leaf.age = 6
print(leaf.age)