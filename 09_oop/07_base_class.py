# ways of accessing base class
class Chai:
    def __init__(self , type_ , strength):
        self.type = type_
        self.strength = strength

# method 1 : direct access (code duplication)
class GingerChai(Chai):
    def __init__(self , type_ , strength , spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level

# method 2 : explicitly calling the base class constructor
class MasalaChai(Chai):
    def _init__(self , type_ , strength , spice_level):
        Chai.__init__(self , type_ , strength)
        self.spice_level = spice_level

# method 3 : using super() function / super() gives access to the immediate base class (parent class)
class RegularChai(Chai):
    def __init__(self, type_, strength , spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

