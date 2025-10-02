users = [
    {"id": 1 , "total" : 100 , "coupon" : "P20"},
   {"id": 2 , "total" : 150 , "coupon" : "F10"},
    {"id": 3 , "total" : 80 , "coupon" : "P50"},
]

discounts = {
    "P20" : (0.2 , 0),
    "F10" : (0.5 , 0),
    "P50" : (0 , 10)
}

for user in users:
    percent , fixed = discounts.get(user["coupon"] , (0 , 0))
    discount = user["total"] * percent + fixed
    print(f"User {user["id"]} paid {user["total"]} and got discount for next visit : {discount}")

# here we have a list of users with their total purchase amount and coupon codes. we also have a dictionary of discounts associated with each coupon code. for each user, we retrieve the discount details using the coupon code, calculate the total discount, and print out the user's id, total amount paid, and the discount they received for their next visit. and this code is highly scalable , we can easily add more users or discount types without changing the core logic of the code.