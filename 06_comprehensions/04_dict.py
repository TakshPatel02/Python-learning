# dictionary comprehension:

tea_price_inr = {
    "Masala chai" : 40,
    "Green Tea" : 50,
    "Lemon tea" : 200
}

# tea_price_usd = {tea : price_in_usd for tea , price in tea_price_inr.items() for price_in_usd in [price/80]}

tea_price_usd = {tea : price / 80 for tea , price in tea_price_inr.items()}
print(tea_price_usd)