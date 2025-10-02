class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"This chaicup has a size of {self.size} ml."
    
cup = Chaicup()
print(cup.describe()) # in this we don't have to pass the argument because it sends the reference of the object itself to the method automatically as the first argument
print(Chaicup.describe(cup)) # same as cup.describe() / here we are passing the object cup as an argument to the describe method / we are passing the reference of cup to the Chaicup.describe method 

cup_two = Chaicup()
cup_two.size = 200
print(cup_two.describe()) # way 1 
print(Chaicup.describe(cup_two)) # way 2 # both are same / here we are passing the reference (context) of cup_two to the main class 