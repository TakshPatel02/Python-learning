# A tea stall owner has a digital token display. for every customer in line , a token number is printed and chai is served,
# task : user s for loop to generate token numbers from 1 to 10 using range() . print : serving chai to token [number]

# range in python generates a sequence of numbers from start (inclusive) to stop (exclusive) means it will not include the stop number 
# in for loop token first value will be 1 and then in next iteration it will be 2 and so on till 10 but bot including the 10
for token in range(1 , 11):
    print(f"Serving the chai to Token number {token}")