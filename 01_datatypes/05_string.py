# String Formatting 

chai_type = "Ginger chai"
customer_name = "Taksh"

# print(f"order for {customer_name} : {chai_type} please !")

# Indexing 

chai_description = "Aromatic and Bold"
# print(f"First word : {chai_description[0:8]}") # if i write [0:7] it will print till index 6
# [0:8:1] [start : end : step]
# [0:8:2] will print alternate characters

# print(f"Last word: {chai_description[12:]}") # if i dont give end it will print till end of string

# print(f"Reversed String : {chai_description[::-1]") # will print string in reverse order :  dloB dna citamorA

label_text = "Chai Spècial"
encoded_text = label_text.encode("utf-8")
print(f" encoded text : {encoded_text}") # Chai Sp\xc3\xa8cial

decoded_text = encoded_text.decode("utf-8")
print(f" decoded text : {decoded_text}") # Chai Spècial
