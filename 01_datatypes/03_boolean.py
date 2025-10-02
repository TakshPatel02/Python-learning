# Boolean : True is represented by 1 and False is represented by 0

is_boiled = True
count = 5

total_count = is_boiled + count # upcasting : converting boolean to integer
# print(f"Total count is : {total_count}")

milk_present = 0
# print(f"Is there any milk present? : {bool(milk_present)}") # converting integer to boolean using bool() function

#  Logical operators with boolean values
has_milk = True
has_sugar = False
can_make_tea = has_milk and has_sugar # both conditions need to be true
can_make_tea = has_milk or has_sugar # only one condition needs to be true
can_make_tea = not has_sugar # negation operator : inverts the boolean value
# print(f"Can we make tea? : {can_make_tea}")

