def brew_chai(flavor):
    if flavor not in ["masala" , "ginger" , "elaichi"]:
        raise ValueError(f"{flavor} chai is not available.")
    print(f"Brewing your {flavor} chai...")

brew_chai("mint")

# Raising a ValueError with a custom message when an unsupported flavor is requested . The program will terminate with a traceback showing the ValueError and the custom message.