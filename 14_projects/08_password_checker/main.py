# password strength checker 

password = input("Enter your password: ")

if len(password) < 8:
    print("Password is weak.")
elif password.isalpha() or password.isdigit():
    print("Password is moderate.")
else:
    print("Password is strong.")
