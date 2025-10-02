# Generator:

def serve_chai():
    yield "Boil water"
    yield "Steep tea"
    yield "Add milk"
    yield "Add sugar"

stpes = serve_chai()

# for step in stpes:
#     print(step)

# behind the scene: generator object is an iterator it does not hold all the values in memory , but generates them on the fly , yield statement is used to produce a value and pause the function's state until the next value is requested. 

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai)) # for 1st value then it pauses until next is called again
print(next(chai)) # for 2nd value
print(next(chai)) # for 3rd value
# print(next(chai)) #  StopIteration error as no more values to yield