from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data = {'id' : "12" , 'name' : "TakshPatel" , 'is_active' : True}

# we only have to pass unpacked dictionary to the model.
user = User(**input_data)
print(user)

# if i will change the type of is_active to str it will give error called validation error.
# All pydantic models are inherited from BaseModel class.
# Pydantic models provide data validation and settings management using Python type annotations.
# Pydantic tries to change the input data to the specified type , if it is not possible it will give validation error. like i passed id as str it converted it to int.

