from tarfile import StreamError
from pydantic import BaseModel
from typing import Optional , List, Union

# Optional Nested Models
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None # Company can optionally have an address

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None # Employee can optionally have a company

user = Employee(
    name="Taksh Patel",
    company=Company(
        name="Tech Corp",
        address=Address(
            street="456 Tech Ave",
            city="Innovation City",
            postal_code="300003"
        )
    )
)

# Mixed Nested Models
class TextContent(BaseModel):
    type: str = "text" # default value is text
    content: str

class ImageContent(BaseModel):
    type: str = "image" # default value is image
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent , ImageContent]] # sections can contain list of Textcontent or ImageContent

# Deeply Nested Structures
class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    address: Address
    branches: List[Address] = [] # list of addresses for branches
