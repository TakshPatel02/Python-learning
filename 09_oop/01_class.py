class Chai:
    pass

class ChaiTime:
    pass

ginger_tea = Chai()
print(type(ginger_tea)) # <class '__main__.Chai'> because ginger_tea is an instance of Chai class 
print(type(ginger_tea) is Chai) # True / ginger_tea is an instance of Chai class not the ChaiTime class
print(ginger_tea is ChaiTime)
