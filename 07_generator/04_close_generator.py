def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

# here we are using yield from to yield all the values from the local_chai and imported_chai generators . This is useful when we want to yield all the values from another generator without writing a loop to yield each value individually . 

def chai_stall():
    try:
        while True:
            order = yield "serving chai"
    except:
        print("closing stall")

stall = chai_stall()
print(next(stall))
stall.close() # closing the generator using close() method / cleaning up the generator

