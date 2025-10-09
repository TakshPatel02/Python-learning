from math import prod
from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True # default value

product_one = Product(id = 1 , name="Laptop" , price=999.99 , in_stock=True)

product_two = Product(id = 2 , name="Mouse" , price=49.99)

product_three = Product(name="keyboard")

# Always use type annotations in pydantic models.
# Set sensible default values for optional fields.

