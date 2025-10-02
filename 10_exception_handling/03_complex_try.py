def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We do not serve this flavor of chai.")
    except ValueError as e:
        print("Error : " , e)
    else:
        print(f"{flavor} chai is ready!")
    finally:
        print("Next order please!")

serve_chai("masala")
serve_chai("unknown")

# Preparing masala chai... / printing the try block
# masala chai is ready! / the else block runs because there was no error in try block
# Next order please! / finally block always runs regardless of error or no error
# Preparing unknown chai... / printing the try block
# Error :  We do not serve this flavor of chai. / printing the except block because there was an error in try block , the message from the raised ValueError is printed
# Next order please! / finally block runs.

# The else block is not the part of if in the try block , it is used with the try-except construct. The else block runs if there is no error in the try block. The finally block always runs regardless of whether there was an error or not. It is often used for cleanup actions that must be executed.