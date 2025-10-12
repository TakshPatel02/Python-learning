price = input("Enter the amount: ")
source_currency = input("Enter the source currency (USD/EUR/CAD): ")
target_currency = input("Enter the target currency (USD/EUR/CAD): ")

exchange_rates = {
    "USD": {"EUR": 0.85, "CAD": 1.25, "USD": 1.0},
    "EUR": {"EUR": 1.0, "CAD": 1.47, "USD": 1.18},
    "CAD": {"EUR": 0.68, "CAD": 1.0, "USD": 0.80},
}

if source_currency in exchange_rates and target_currency in exchange_rates[source_currency]:
    rate = exchange_rates[source_currency][target_currency]
    converted_amount = float(price) * rate
    print(f"{price} {source_currency} is approximately {converted_amount:.2f} {target_currency}")
else: 
    print("Invalid currency code. Please use USD, EUR, or CAD.")