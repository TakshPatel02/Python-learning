from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function.")
        func()
        print("After the function.")
    return wrapper

@my_decorator
def greet():
    print("Hello from taksh patel!")

greet()
print(greet.__name__) #wrapper
# why wrapper? because greet is now reference to wrapper function.

# after using wraps : the metadata of original function is preserved.