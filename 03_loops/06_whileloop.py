# you want to simulate tea heating , it starts at 40 c and boils at 100 c
# Task: use a while loop. increase temperature by 15 until it reaches or exceed 100 , print each temperature step.

temp = 40

while temp <= 100:
    print(f"Current temperature is : {temp} C")
    temp += 15

print("Tea is boiled and ready to serve!")