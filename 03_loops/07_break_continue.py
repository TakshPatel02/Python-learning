# some chai flavors are out of stock. you want to skip those and stop entirely if someone requests a restircted flavor.
# task : skip if flavor is out of stock , break if flavor is discontinued.

flavors = ["Ginger" , "Out of stock" , "Lemon" , "Discontinued" , "Tulsi"]

for flavor in flavors:
    if flavor == "Out of stock":
        continue
        print("Out of stock flavor find")
    if flavor == "Discontinued":
        break
    print(f"{flavor} item found")
    

print("Out side of the loop")

# continue skips the current iteration and moves to the next one , break stops the entire loop. 
# in this case , "Out of stock" is skipped and "Discontinued" stops the loop.