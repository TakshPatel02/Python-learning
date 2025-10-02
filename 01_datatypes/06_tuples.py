# tuples are also immutable like strings but they can hold multiple data types.

masala_spices = ("turmeric" , "cumin" , "coriander")

(spice1 , spice2 , spice3) = masala_spices # unpacking a tuple and assigning to multiple variables

# print(f"all the spice are : {masala_spices}") 
# print(f"the spices one by one : {spice1} , {spice2} , {spice3}")

ginger_ratio , cardemon_ratio = 1 , 3 # mutltiple assignments / this is also tuple behind the scenes.

# print(f"ration of G: {ginger_ratio} and C : {cardemon_ratio}")

ginger_ratio , cardemon_ratio = cardemon_ratio , ginger_ratio
# print(f"after swapping : ration of G: {ginger_ratio} and C : {cardemon_ratio}")

# membership checking

# checking the string is available in tuple or not / in this we have to give exact case matching , if we give 'Cumnin' it will return false 
# print(f"Is ginger in masala spices ? : {'ginger' in masala_spices}") # false

