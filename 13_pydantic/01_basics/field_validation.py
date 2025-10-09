from pydantic import BaseModel , field_validator , model_validator

class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls , v): # cls is the class itself and v is the value of the field
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v # always return the value after validation. If you modify it , return the modified value.
    
class SignUpData(BaseModel):
    password: str
    confirm_password : str

    # model validator is used to validate multiple fields together. Here mode is after means after all the validation of individual fields , this validator will run.
    @model_validator(mode='after')
    def password_match(cls , values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values 