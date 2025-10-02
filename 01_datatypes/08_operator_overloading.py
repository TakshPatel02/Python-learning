base_liquid = ["water" , "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor # concatenates two lists
# print(full_liquid_mix)

strong_brew = ["black tea" , "water"] * 3 # repeats the list 3 times / if we have multiple elements in the list , it repeats the entire list in sthe same order
# print(strong_brew)

# new_liquid = full_liquid_mix - extra_flavor # this will give an error as - and /  operator is not defined for lists
# print(new_liquid)

# bytearray : it is a mutable sequence of bytes , typically used to store binary data / and we can also convert string to bytearray
raw_data = bytearray(b"cinnamon")
new_raw_data = raw_data.replace(b"cinna" , b"carda") # replace cinna with carda
print(f"the raw data is : {new_raw_data}")