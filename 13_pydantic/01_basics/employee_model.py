from typing import Optional
from pydantic import BaseModel , Field

class Employee(BaseModel):
    id : int
    name : str = Field(
        ..., # ellipsis means this field is required
        min_length=3, # name should be at least 3 characters long
        max_length=50, # name should contains max 50 characters
        description="Employee name", # documentation for the field
        examples="Taksh Patel" # example value for the field
    )
    department : Optional[str] = 'general'
    salary : float = Field(
        ...,
        ge=10000, # salary should be greater than or equal to 10000
        le=20000, # salary should be less than or equal to 20000
        description="Employee salary",
    )

employee_one = Employee(id=1, name="Alice", department="HR", salary=15000)