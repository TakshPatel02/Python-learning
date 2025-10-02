# generator comprehensions:
# syntax : (expression for item in iterable if condition)

daily_sale = [10 , 4 , 5 , 7 , 9 , 15 , 3]

total_cups = sum(sale for sale in daily_sale if sale <= 5)
print(total_cups)

# here we are using generator comprehension inside sum function to calculate total cups sold in a week where daily sale is less than or equal to 5. 
# how it is different from other comprehensions is that it doesn't create a new list or set or dictionary in memory. It generates items on the fly and is more memory efficient. 