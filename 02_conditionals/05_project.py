# you run an online tea store . if the order amount is more than 300 rupees , delivery is free; otherwise it costs 30 rupees
# task : 
# input : order_amount
# use ternery operator to decide delivery fee

#converting the input string to the integer using int() function
order_amount = int(input("enter your order amount: "))

delivery_fee = 0 if order_amount > 300 else 30

print(f"your delivery fee is  : {delivery_fee} rupees")