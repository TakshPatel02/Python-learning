# you sell different chai sizes. instead if writing everywher , create a function.
#Task: write calculate_bils (cups , price_per_cup) , return total bills , use this fnction for multiple orders.

def calculate_bills(cups , price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bills(3 , 20)
print(f"My bill is : {my_bill}")

print(f"The bill of table 2 is : {calculate_bills(5 , 50)}")

# This way if the pricing logic changes , you only need to update it in one place (inside the function) rather than everywhere in your code . This improves maintainability and reduces errors.