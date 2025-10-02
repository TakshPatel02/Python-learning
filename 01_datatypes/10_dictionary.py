# in list or tuple we have to use indexing to access the elements , in dictionary we use keys to access the values (i can use my name as a key to access elements)

chai_order = dict(type="Masala chai" , size="large" , sugar = 2)
# print(chai_order) # if we print the dictionary it will print in key value pairs , and order does not matter in the dictionary also . 

chai_recipe = {}
# for adding elements in the dictionary
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# print(f"recipe base is : {chai_recipe['base']}") # it is same as we do in the list or tuple but here we use keys instead of index

# for deleting the elements in the dictionary
del chai_recipe["liquid"]
# print(chai_recipe)

# membership testing
# print("base" in chai_recipe) # it will return true if the key is present in the dictionary

chai_order = dict(type="ginger chai" , size = "medium" , sugar = 1)

# print(f"Order details : {chai_order.keys()}") # it will return all the keys in the dictionary
# print(f"Order details : {chai_order.values()}") # it will return all the values in the dictionary
# print(f"Order details : {chai_order.items()}") # it will return all the key , value pairs in the dictionary as tuples in a list

last_item = chai_order.popitem() # it will remove the last item in the dictionary and return it as a tuple
# print(f"the last item is : {last_item}")

extra_spices = {"cardamom":"crushed" , "ginger":"sliced"}
chai_recipe.update(extra_spices) # it will add the key balue pairs from extra_spices dict to chai_recipe dict 
print(chai_recipe)

chai_size = chai_order["size"] 
print(f" the size of the chai is : {chai_size}")

# if the key-value pair is not present in the dict and we try to access it using the key by above method it will crash our program , there is another method to access the value using the key which is get() method
chai_note = chai_order.get("note" , "no note is given") # if the key is not present in the dict it will return None or the default value we provide instead of crashing the program
print(f"the note for the chai is : {chai_note}")


# we studied in the set are also applicable in the dictionary also , like union , interaction , difference etc