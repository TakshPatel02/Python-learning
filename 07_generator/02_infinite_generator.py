def infinite_chai():
    cup = 1
    while True:
        yield f"Cup #{cup}"
        cup += 1

chai = infinite_chai()

for _ in range(int(input("How many cups of chai? "))):
    print(next(chai))