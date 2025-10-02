# you're building a simple app that registers users. You want to separate concerns: getting input , validating it and saving it. 
#task: write register_user() that calls: get_input() , validate_input() , save_to_db()

def get_input():
    print("getting user inpuut...")

def validate_input():
    print("validating user input...")

def save_to_db():
    print("saving user to database...")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("user registered successfully.")

register_user()

# This approach of hiding complexity inside functions makes the main logic (register_user) cleaner and easier to understand . Each helper function has a specific task , making the code more organized and maintainable.
# This is especially useful in larger applications where functions can encapsulate complex logic , allowing you to focus on high-level workflows without getting bogged down by details.