# number is immutable object but here we are changing the reference of the variable sugar_amount to a new object , so the id will change. if we change the value of the same object then the id remains the same.
sugar_amount = 2
# print(f"Intitial value of sugar is : {sugar_amount}") # 2

sugar_amount = 12
# print(f"New value of sugar is : {sugar_amount}") # 12

# print(f"Id of 2 : {id(2)}")
# print(f"Id of 12 : {id(12)}")

# Mutable object example: set gives the same id when we change the value of the object.
spice_mix = set()
print(f"initial id is : {id(spice_mix)}")

spice_mix.add("salt")
spice_mix.add("pepper")

print(f"initial id is : {id(spice_mix)}")
print(f"the value of set: {spice_mix}")