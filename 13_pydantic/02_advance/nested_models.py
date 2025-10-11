from typing import List , Optional
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    address : Address # I can use address model here as a type hint for address field , User contains reference of an Address model

address1 = Address(
    street="123 something st",
    city="Ahmedabad",
    postal_code="100001"
)

user = User(
    id=1,
    name="Taksh Patel",
    address=address1
)

print(user)

user_data = {
    "id" : 2,
    "name" : "Taksh Patel",
    "address" : {
        "street" : "123 nothing st",
        "city" : "Gandhinagar",
        "postal_code" : "200002"
    }
}
user2 = User(**user_data) # Pydantic will automatically convert the nested dictionary into an Address model
print(user2)