# set comprehensions: 
#syntax : {expression for item in iterable if condition}

favourite_chais = [
    "masala chai" , "green tea" , "masala chai" , 
    "green tea" , "Lemon tea" , "ginger chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

receipe = {
    "Masala chai" : ["ginger" , "cardamom" , "clove"],
    "Elaichi chai" : ["cardamom" , "milk"] , 
    "Spicy chai" : ["ginger" , "black pepper" , "clove"]
}

unique_spice = {spice for ingredient in receipe.values() for spice in ingredient}
print(unique_spice)