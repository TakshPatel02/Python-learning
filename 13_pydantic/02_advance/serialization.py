from pydantic import BaseModel , ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

# Example usage
user = User(
    id=1,
    name="Taksh",
    email="taksh@gmail.com",
    is_active=True,
    created_at=datetime.now(),
    address=Address(
        street="123 Main St",
        city="Anytown",
        zip_code="12345"
    ),
    tags=["admin" , "user"]
)
print(user.model_dump_json(indent=4))  # Pretty print JSON with indentation