# lists : they are mutable sequences , typically used to store collections of homogeneous items
# lists are defined by having values between square brackets []

ingredients = ["milk" , "water" , "black tea"]
ingredients.append("sugar") # adds sugar to the end of the list
# print(ingredients)

# ingredients.pop() # removes the last item from the list

# ingredients.remove("water") # removes the given item from the list
# print(ingredients)

spice_options = ["ginger" , "cardamom"]
chai_options = ["milk" , "water"] # + spice_options # concatenates two lists

chai_options.extend(spice_options) # adds the items of spice_option to the end 

chai_options.insert(1 , "sugar") # indserts sugar at index 1
# print(chai_options)

# last_added = chai_options.pop() # removes and returns the last item from the list
# print(last_added)

chai_options.reverse() # reverses the list
# print(chai_options)

chai_options.sort() # sorts the list in ascending order
# print(chai_options)

sugar_level = [ 1 , 2 , 3 , 4 , 5]
# print(f"Maximum sugar level : {max(sugar_level)}") # returns the maximum value from the list
# print(f"Minimum sugar level : {min(sugar_level)}") # returns the minimum value from the list

# print(f"The sum of all sugar_level is : {sum(sugar_level)}") # returns the sum of all items in the list