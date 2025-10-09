from pydantic import BaseModel
from typing import List , Dict , Optional

class Cart(BaseModel):
    user_id : int
    items : List[str] # list of item names which are strings.
    quantities : Dict[str , int] # dictionary in which key is string and value is integer.

class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None # optional field wth default value None. if has value then it should be string.

cart_data = {
    "user_id" : 1,
    "items" : ["Laptop" , "Mouse" , "Keyboard"],
    "quantities" : {
        "Laptop" : 1,
        "Mouse" : 2,
        "Keyboard" : 2
    }
}

cart = Cart(**cart_data)
print(cart)