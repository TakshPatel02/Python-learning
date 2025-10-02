# set : set is an unordered collection of unique elements , it is mutable (can be changed after creation) , and it does not allow duplicate values , the orders of elements are not gauranteed to be preserved
# sets are defined by having values between curly braces {}
essential_spices = {"cinnamon" ,"ginger" , "cardamom"}
optional_spices = {"cloves" ,"ginger" , "black pepper"}

all_spices = essential_spices | optional_spices # union of two sets
# print(f"the union of the two sets is : {all_spices}")

common_spices = essential_spices & optional_spices # intersection of two spices
# print(f"the common spices are : {common_spices}")

unique_to_essential = essential_spices - optional_spices # spices are in essential but not in optioanl
# print(f"the spices unique to essential are : {unique_to_essential}")

unique_to_optional = optional_spices - essential_spices # spices are in optional but not in essential
# print(f"the spices unique to optional are : {unique_to_optional}")

# membership checking
# print(f"is ginger in essential spices ? : {'ginger' in essential_spices}") # true
# print(f"is cloves in essential spices ? : {'cloves' in essential_spices}") # false

# there is an important set called frozenset which is immutable version of set , once created we cannnot add or remove items from it