chai_type = "plain"

def order():
    global chai_type
    chai_type= "masala"

order()
print(chai_type)

# global is just like the nonlocal keyword but it modifies the global variable from inside the function . here the global chai_type variable is modified by the function order()>

# be extra cautious while using global keyword as it can lead to code that is hard to debug and maintain. 