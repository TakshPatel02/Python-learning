# a tea stall offers different prices for different cup sizes . write a program that calculates the price based on size
# task:
# input: small , medium , large
# small -> 10 rupees , medium -> 15 rupees , large -> 20 rupees
# if invalid show unknown cup size

chai_size = input("Enter your chai cup size (small / medium / large) : ").lower()

if chai_size == "small":
    print(f"your small cup of chai costs 10 rupees")
elif chai_size == "medium":
    print(f"your medium cup of chai costs 15 rupees")    
elif chai_size == "large":
    print(f"your large cup of chai costs 20 rupees")
else:
    print("unknown cup size , enter valid cup size given from given options.")    
