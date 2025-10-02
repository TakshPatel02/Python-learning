# your shop adds a 10% VAT on every order. you want this to be consistent and traceable.
#Task: write add_vat(price , vat_rate) , use it to compute final price for 3 orders.

def add_vat(price , vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100 , 150 , 200]

for price in orders:
    final = add_vat(price , 10)
    print(f"Final price after VAT is : {final}")